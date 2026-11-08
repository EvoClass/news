"""Validate the deliberately small Markdown publishing format; no network or secrets."""
import datetime
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit

FIELDS = set("title slug excerpt category tags language translation_key source_language author_name cover_url cover_alt date draft".split())
REQUIRED = FIELDS - {"tags", "cover_url", "cover_alt"}
LANGUAGES = set("en es fr id it ja ko pt ru th vi zh_CN zh_HK".split())
CATEGORIES = {"news", "release", "guide", "practice", "research"}
SECRET = re.compile(r"(?:sk-[A-Za-z0-9_-]{20,}|gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----)")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def safe_url(value):
    if re.search(r"[\s\\\x00-\x1f]", value):
        return False
    if value.startswith(("#", "/")):
        return not value.startswith("//")
    parts = urlsplit(value)
    return parts.scheme == "https" and bool(parts.netloc) and not parts.username


def parse(text):
    text = text.replace("\r\n", "\n")
    require(len(text.encode("utf-8")) <= 1_048_576, "file exceeds 1 MiB")
    require("\x00" not in text and not SECRET.search(text), "NUL or possible credential found (value redacted)")
    require(text.startswith("---\n") and "\n---\n" in text[4:], "front matter is required")
    header, body = text[4:].split("\n---\n", 1)
    require(len(header.encode("utf-8")) <= 16_384, "front matter exceeds 16 KiB")
    meta = {}
    for line in header.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        key, sep, value = line.partition(":")
        require(sep and key in FIELDS and key not in meta, "unknown or duplicate metadata field")
        value = value.strip()
        require(bool(value), f"empty {key}")
        if key == "draft":
            require(value in {"true", "false"}, "draft must be true or false")
            value = value == "true"
        elif key == "tags" or value.startswith('"'):
            value = json.loads(value)
        elif value.startswith("'"):
            require(value.endswith("'") and len(value) >= 2, "unterminated quoted value")
            value = value[1:-1].replace("''", "'")
        else:
            require(value[0] not in "|>&*!{[", "only flat, single-line metadata is supported")
        if key not in {"tags", "draft"}:
            require(isinstance(value, str) and value.strip(), f"{key} must be a nonempty string")
        meta[key] = value
    require(REQUIRED <= meta.keys(), "missing required fields: " + ", ".join(sorted(REQUIRED - meta.keys())))
    for key, limit in {"title": 200, "excerpt": 500, "author_name": 100, "cover_alt": 300, "cover_url": 2048}.items():
        require(len(meta.get(key, "")) <= limit, f"{key} exceeds {limit} characters")
    for key in ["slug", "translation_key"]:
        require(len(meta[key]) <= 120 and re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", meta[key]), f"invalid {key}")
    require(re.search("[a-z]", meta["slug"]), "slug must contain a letter")
    require(meta["category"] in CATEGORIES, "invalid category")
    require(meta["language"] in LANGUAGES and meta["source_language"] in LANGUAGES, "unsupported language")
    date = meta["date"]
    require(re.fullmatch(r"\d{4}-\d{2}(?:-\d{2})?", date), "date must be YYYY-MM or YYYY-MM-DD")
    datetime.date.fromisoformat(date + "-01" if len(date) == 7 else date)
    tags = meta.get("tags", [])
    require(isinstance(tags, list) and len(tags) <= 10 and all(isinstance(t, str) and len(t) <= 40 for t in tags), "invalid tags")
    if meta.get("cover_url"):
        require(safe_url(meta["cover_url"]) and not meta["cover_url"].startswith("#"), "unsafe cover URL")
        require(bool(meta.get("cover_alt")), "cover_alt is required with cover_url")
    require(bool(body.strip()) and len(body.encode("utf-8")) <= 1_000_000, "body is empty or too large")
    prose = re.sub(r"(?ms)^(```|~~~).*?^\1[^\n]*$", "", body)
    require(not re.search(r"(?m)^#\s", prose), "body must not repeat the page H1 title")
    require(re.search(r"(?m)^##\s", prose), "body needs at least one H2 section")
    require(not re.search(r"(?i)(?:javascript|data|file|vbscript)\s*:", prose), "unsafe URL scheme")
    # Check inline and reference-style Markdown destinations; not a full Markdown parser.
    urls = re.findall(r"!?\[[^\]\n]*\]\(<?([^\s)>]+)", prose)
    urls += re.findall(r"(?m)^\s{0,3}\[[^\]\n]+\]:\s*<?([^\s>]+)", prose)
    for url in urls:
        require(safe_url(url), "links must use HTTPS, a site-root path or an anchor")
    if not meta["draft"]:
        require("replace-with" not in text and "example.com" not in text and "<!--" not in body, "remove template placeholders/comments before publication")
    return meta


def validate(root):
    errors, records = [], []
    for path in sorted((root / "content/news").rglob("*")):
        if path.is_file() and path.suffix.lower() in {".md", ".markdown"}:
            try:
                records.append((path, parse(path.read_text(encoding="utf-8"))))
            except (ValueError, UnicodeError) as error:
                # Do not print input values, including JSON parser documents.
                message = "invalid UTF-8 or JSON value" if isinstance(error, (UnicodeError, json.JSONDecodeError)) else str(error)
                errors.append(f"{path.relative_to(root)}: {message}")
    pairs, slugs, groups = set(), set(), {}
    for path, meta in records:
        pair = (meta["translation_key"], meta["language"])
        if pair in pairs or meta["slug"] in slugs:
            errors.append(f"{path.relative_to(root)}: duplicate translation/language or slug")
        pairs.add(pair)
        slugs.add(meta["slug"])
        groups.setdefault(meta["translation_key"], []).append(meta)
    for key, group in groups.items():
        sources = {m["source_language"] for m in group}
        if len(sources) != 1 or not any(m["language"] == m["source_language"] for m in group):
            errors.append(f"translation group {key}: missing original or inconsistent source language")
        if len({m["date"] for m in group}) != 1:
            errors.append(f"translation group {key}: translations must retain the original date and precision")
    return errors


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    errors = validate(root)
    for error in errors:
        print(error, file=sys.stderr)
    print("News validation failed." if errors else "News validation passed.")
    sys.exit(bool(errors))

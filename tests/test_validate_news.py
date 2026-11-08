import tempfile
from pathlib import Path
import unittest

from scripts.validate_news import parse, validate

ARTICLE = """---
title: EvoClass news
slug: sample-news
date: 2025-11
category: news
language: en
translation_key: sample-news
source_language: en
author_name: EvoClass
excerpt: A verified update.
draft: false
---

A concise introduction.

## Background

Read the [official source](https://evoclass.ai/news).
"""


class NewsValidationTest(unittest.TestCase):
    def test_editorial_sections_include_course_guides(self):
        for category in ["course", "practice", "guide", "release", "research", "news"]:
            with self.subTest(category=category):
                self.assertEqual(parse(ARTICLE.replace("category: news", "category: " + category))["category"], category)

    def test_month_and_exact_date(self):
        self.assertEqual(parse(ARTICLE)["date"], "2025-11")
        self.assertEqual(parse(ARTICLE.replace("2025-11", "2024-02-29"))["date"], "2024-02-29")

    def test_invalid_calendar_dates(self):
        for date in ["2025-13", "2025-00", "2025-2", "2025-02-29", "2025-11-31"]:
            with self.subTest(date=date), self.assertRaises(ValueError):
                parse(ARTICLE.replace("2025-11", date))

    def test_bad_metadata_and_placeholders(self):
        for old, new in [("title: EvoClass news", "title: One\ntitle: Two"), ("category: news", "category: awards"), ("language: en", "language: xx"), ("draft: false", "draft: yes"), ("date: 2025-11\n", ""), ("sample-news", "replace-with-news-slug"), ("title: EvoClass news", "title: |"), ("author_name: EvoClass", "author_name: \"unterminated")]:
            with self.subTest(new=new), self.assertRaises(ValueError):
                parse(ARTICLE.replace(old, new))

    def test_unsafe_links_and_credentials(self):
        for target in ["javascript:alert(1)", "http://example.org", "//example.org", "file:///tmp/x", "../asset.png"]:
            with self.subTest(target=target), self.assertRaises(ValueError):
                parse(ARTICLE.replace("https://evoclass.ai/news", target))
        with self.assertRaisesRegex(ValueError, "redacted"):
            parse(ARTICLE + "sk-" + "x" * 32)

    def test_structure_and_cover(self):
        with self.assertRaises(ValueError):
            parse(ARTICLE.replace("## Background", "# Duplicate title"))
        with self.assertRaises(ValueError):
            parse(ARTICLE.replace("draft: false", "cover_url: https://evoclass.ai/logo.png\ndraft: false"))

    def test_group_identity_and_original(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            directory = root / "content/news"
            directory.mkdir(parents=True)
            (directory / "original.md").write_text(ARTICLE, encoding="utf-8")
            self.assertEqual(validate(root), [])
            translation = ARTICLE.replace("slug: sample-news", "slug: sample-news-zh-cn").replace("\nlanguage: en", "\nlanguage: zh_CN")
            (directory / "translation.md").write_text(translation, encoding="utf-8")
            self.assertEqual(validate(root), [])
            (directory / "duplicate.md").write_text(translation, encoding="utf-8")
            self.assertTrue(any("duplicate" in e for e in validate(root)))
            (directory / "duplicate.md").unlink()
            (directory / "original.md").unlink()
            self.assertTrue(any("missing original" in e for e in validate(root)))

    def test_translation_date_and_utf8(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            directory = root / "content/news"
            directory.mkdir(parents=True)
            (directory / "original.md").write_text(ARTICLE, encoding="utf-8")
            translation = ARTICLE.replace("slug: sample-news", "slug: sample-news-ja").replace("\nlanguage: en", "\nlanguage: ja").replace("2025-11", "2025-11-01")
            (directory / "translation.md").write_text(translation, encoding="utf-8")
            self.assertTrue(any("precision" in e for e in validate(root)))
            (directory / "broken.md").write_bytes(b"\xff")
            self.assertTrue(any("UTF-8" in e for e in validate(root)))


if __name__ == "__main__":
    unittest.main()

# EvoClass News

<img src="assets/evoclass-logo.png" width="96" alt="EvoClass Logo">

EvoClass 官方新闻与动态的公开 Markdown 内容仓库。
Official Markdown source for EvoClass news and updates.

- 官网：[evoclass.ai](https://evoclass.ai)
- 新闻：[evoclass.ai/news](https://evoclass.ai/news)
- 发布分支：`main`
- 文章目录：[`content/news/`](content/news/)
- 文章模板：[`docs/news-template.md`](docs/news-template.md)

## 发布新闻

1. 复制模板，填写标题、摘要、原始发布日期、分类和语言。
2. 将 `.md` 文件上传到 `content/news/`，或通过 Pull Request 合并到 `main`。
3. 设置 `draft: false`；原文的 `language` 与 `source_language` 应一致。
4. 应用同步开启后，约每 5 分钟读取更新，自动补齐主站支持的 13 种语言，校验通过后整批发布。

译文准备需要额外时间，失败时保留上一版公开内容并在后续同步重试。
译文及翻译缓存存储在应用数据库，不回写本仓库。
主站菜单负责语言切换，缺少译本时回退到可用版本。
原文的首次发布日期不会因翻译生成而改变。

修改原文会触发译文更新；删除原文或设为草稿会撤回原文及其自动译本。
人工上传的译本优先，独立遵循自己的发布状态。
首次发布后保留 `slug`、`translation_key`、`language` 和 `source_language`，避免改变文章身份和永久链接。

本仓库为公开仓库，只提交可公开的文章和素材，不要提交 API 密钥、服务器环境文件、个人信息或未获准公开的材料。
说明文档和模板放在 `docs/`，不要放进会被自动发布的 `content/news/`。
不需要在本仓库配置 GitHub Actions 翻译，也不需要仓库写入令牌。

## 应用配置

部署同事在 EvoClass 应用进程中配置以下变量，重启应用后在新闻管理页执行首次同步：

```dotenv
NEWS_GITHUB_SYNC=true
NEWS_GITHUB_REPOSITORY=EvoClass/news
NEWS_GITHUB_BRANCH=main
NEWS_GITHUB_PATH=content/news
NEWS_AUTO_TRANSLATE=true
NEWS_TRANSLATION_MODEL=deepseek:deepseek-v4-flash
# DEEPSEEK_API_KEY 通过服务器的私有环境文件配置，不要写入本仓库。
```

公开仓库可匿名读取；为提高 GitHub API 配额，可在服务器另设具有本仓库 Contents 只读权限的 `NEWS_GITHUB_TOKEN`。
详细迁移、同步、翻译、语言切换和 SEO 验收步骤，见应用仓库的 [中文部署指南](https://github.com/EvoClass/evoclass/blob/main/docs/news-deployment.md)（需要应用仓库访问权限）。
若应用环境仍显式配置旧来源 `EvoClass/evoclass`，须改为 `EvoClass/news`；仅更新应用默认值不会覆盖已有环境变量。

可选 Webhook：在本仓库设置 `push` 事件，目标为 `https://evoclass.ai/api/news/github/webhook`，Content type 为 `application/json`。
Secret 与应用的 `NEWS_GITHUB_WEBHOOK_SECRET` 一致，至少 16 字节，并保持 SSL 验证开启。
Webhook 仅触发同步，发布是否完成以应用后台“同步正常”和线上正文为准。

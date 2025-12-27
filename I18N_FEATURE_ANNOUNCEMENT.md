# 🌍 Browser Use WebUI - 现已支持中文！

## 新功能：国际化支持

Browser Use WebUI 现已完全支持国际化（i18n），提供简体中文界面！

### 🚀 快速使用中文界面

```bash
# 设置中文
export WEBUI_LANGUAGE=zh  # Linux/Mac
$env:WEBUI_LANGUAGE="zh"  # Windows PowerShell

# 启动应用
python webui.py
```

### 📖 文档

- [快速开始指南](QUICKSTART_I18N.md) - 立即使用中文界面
- [详细使用文档](I18N_README.md) - 完整的 i18n 功能说明
- [更新说明](I18N_UPDATE.md) - 新功能介绍
- [实现总结](IMPLEMENTATION_SUMMARY.md) - 技术细节

### 🌟 特性

- ✅ **双语支持**: 英语和简体中文
- ✅ **完整翻译**: 所有界面元素已翻译
- ✅ **保持主题**: Ocean、Default 等主题名保持英文
- ✅ **专业术语**: LLM、API 等技术术语保持英文
- ✅ **易于扩展**: 可轻松添加更多语言

### 🎯 支持的语言

| 语言 | 代码 | 状态 |
|------|------|------|
| English | `en` | ✅ 完整 |
| 简体中文 | `zh` | ✅ 完整 |

### 📸 界面预览

**中文界面示例**:

```
🌐 Browser Use WebUI
使用 AI 助手控制您的浏览器

⚙️ Agent Settings（智能体设置）
  ├─ LLM 提供商
  ├─ LLM 模型名称
  ├─ 使用视觉
  └─ 最大运行步数

🤖 Run Agent（运行智能体）
  ├─ ▶️ 提交任务
  ├─ ⏸️ 暂停
  └─ ⏹️ 停止
```

---

**查看完整 README**: [README.md](README.md)

---

### 📝 添加到主 README

建议在主 README.md 的开头添加以下徽章：

```markdown
[![i18n](https://img.shields.io/badge/i18n-English%20%7C%20%E4%B8%AD%E6%96%87-blue)](I18N_README.md)
```

并在 Installation Guide 之前添加：

```markdown
## 🌍 Internationalization (i18n)

Browser Use WebUI now supports multiple languages!

**Supported Languages:**
- 🇺🇸 English (en) - Default
- 🇨🇳 简体中文 (zh)

**Quick Start with Chinese:**
```bash
export WEBUI_LANGUAGE=zh
python webui.py
```

**Learn More:** [i18n Documentation](I18N_README.md) | [Quick Start Guide](QUICKSTART_I18N.md)
```

### 🎉 现在就试试！

```bash
# 克隆仓库
git clone https://github.com/browser-use/web-ui.git
cd web-ui

# 设置中文环境
export WEBUI_LANGUAGE=zh

# 安装依赖
pip install -r requirements.txt

# 启动应用
python webui.py
```

访问 http://localhost:7788 即可看到中文界面！

# 国际化更新说明

## ✨ 新增功能

已为 Browser Use WebUI 添加完整的国际化（i18n）支持！

### 🎯 主要特性

1. **双语支持**：英语 (en) 和简体中文 (zh)
2. **保持主题关键词**：所有主题名称（Ocean, Default, Soft 等）保持英文
3. **完整翻译**：界面所有文本已翻译
4. **易于扩展**：可轻松添加更多语言

### 📁 新增文件

- `src/utils/i18n.py` - 国际化核心模块
- `I18N_README.md` - 详细的 i18n 使用文档
- `demo_i18n.py` - i18n 功能演示脚本

### 🔄 更新文件

以下文件已更新以支持 i18n：

- `src/webui/interface.py`
- `src/webui/components/agent_settings_tab.py`
- `src/webui/components/browser_settings_tab.py`
- `src/webui/components/browser_use_agent_tab.py`
- `src/webui/components/deep_research_agent_tab.py`
- `src/webui/components/load_save_config_tab.py`

## 🚀 快速开始

### 设置语言

**方法 1: 环境变量**
```bash
# 使用中文
export WEBUI_LANGUAGE=zh
python webui.py

# 使用英文（默认）
export WEBUI_LANGUAGE=en
python webui.py
```

**方法 2: .env 文件**
```bash
echo "WEBUI_LANGUAGE=zh" >> .env
python webui.py
```

### 测试 i18n 功能

运行演示脚本：
```bash
python demo_i18n.py
```

## 📸 翻译示例

### 英语界面
```
🌐 Browser Use WebUI
Control your browser with AI assistance

⚙️ Agent Settings
  - LLM Provider
  - LLM Model Name
  - Use Vision
  
🤖 Run Agent
  - ▶️ Submit Task
  - ⏸️ Pause
  - ⏹️ Stop
```

### 中文界面
```
🌐 Browser Use WebUI
使用 AI 助手控制您的浏览器

⚙️ Agent Settings（智能体设置）
  - LLM 提供商
  - LLM 模型名称
  - 使用视觉
  
🤖 Run Agent（运行智能体）
  - ▶️ 提交任务
  - ⏸️ 暂停
  - ⏹️ 停止
```

## 💡 设计原则

1. **保留技术术语**：LLM、API、CDP 等专业术语保持英文
2. **表情符号不变**：所有表情符号在翻译后保留
3. **主题名称英文**：Ocean、Default、Soft 等主题名称保持英文
4. **中英混排**：标签页采用"English（中文说明）"格式，兼顾两种语言用户

## 📚 更多信息

详细文档请参阅 [`I18N_README.md`](I18N_README.md)

## 🛠️ 开发者注意事项

添加新的 UI 组件时：

```python
from src.utils.i18n import t

# ✅ 使用 i18n
label = t("my_new_label")

# ❌ 不要硬编码文本
label = "My New Label"
```

## 🌍 支持的语言

- 🇺🇸 English (en) - Default
- 🇨🇳 简体中文 (zh)

欢迎贡献更多语言翻译！

## 🔗 相关文件

- [详细使用文档](I18N_README.md)
- [i18n 模块源码](src/utils/i18n.py)
- [演示脚本](demo_i18n.py)

---

**注意**：所有现有功能保持不变，只是添加了多语言支持。

# 国际化 (i18n) 功能说明

## 概述

本项目已添加国际化支持，目前支持英语（en）和中文（zh）两种语言。所有界面文本都已实现翻译，同时保持了主题关键词（如 "Ocean", "Default" 等）为英文。

## 使用方法

### 1. 设置语言

通过环境变量设置界面语言：

```bash
# 设置为中文
export WEBUI_LANGUAGE=zh

# 设置为英文（默认）
export WEBUI_LANGUAGE=en
```

或者在 `.env` 文件中添加：

```
WEBUI_LANGUAGE=zh
```

### 2. 在代码中使用翻译

```python
from src.utils.i18n import t

# 使用翻译函数
label_text = t("llm_provider")  # 根据当前语言返回 "LLM Provider" 或 "LLM 提供商"

# 在 Gradio 组件中使用
import gradio as gr
textbox = gr.Textbox(
    label=t("task_input"),
    placeholder=t("task_input_placeholder")
)
```

### 3. 添加新的翻译

如需添加新的翻译键值，请编辑 `src/utils/i18n.py` 文件：

```python
TRANSLATIONS = {
    "en": {
        "your_new_key": "English Text",
        # ... 其他翻译
    },
    "zh": {
        "your_new_key": "中文文本",
        # ... 其他翻译
    }
}
```

## 已翻译的界面元素

### 主界面
- 应用标题和副标题
- 所有标签页标题（保留表情符号和英文主题名）

### Agent Settings（智能体设置）
- LLM 提供商和模型设置
- 温度和上下文长度设置
- API 密钥和基础 URL
- 规划器 LLM 设置
- 最大步数和操作数设置

### Browser Settings（浏览器设置）
- 浏览器路径和用户数据目录
- 无头模式和安全设置
- 窗口尺寸设置
- CDP/WSS URL 设置
- 录制和跟踪路径设置

### Run Agent（运行智能体）
- 任务输入和交互界面
- 开始、暂停、停止按钮
- 浏览器实时视图
- 任务输出和历史

### Deep Research（深度研究）
- 研究任务设置
- 并行智能体数量
- 研究结果显示和下载

### Load & Save Config（加载和保存配置）
- 配置文件加载和保存
- 状态显示

## 翻译原则

1. **保持主题关键词为英文**：如 "Ocean"、"Default"、"Soft" 等主题名称保持英文
2. **保留表情符号**：所有按钮和标签页的表情符号都保留
3. **技术术语处理**：
   - 专有名词保留英文：LLM、API、CDP、WSS、MCP 等
   - 中文翻译添加英文括号说明：如 "⚙️ Agent Settings（智能体设置）"
4. **一致性**：相同概念在不同位置使用相同翻译

## 支持的语言

- 🇺🇸 English (en) - 默认语言
- 🇨🇳 简体中文 (zh)

## 扩展支持更多语言

要添加新语言支持，请在 `src/utils/i18n.py` 的 `TRANSLATIONS` 字典中添加新的语言代码和翻译：

```python
TRANSLATIONS = {
    "en": { ... },
    "zh": { ... },
    "ja": {  # 日语示例
        "app_title": "Browser Use WebUI",
        "app_subtitle": "AIアシスタントでブラウザを制御",
        # ... 更多翻译
    }
}
```

## API 参考

### `set_language(lang: str)`
设置当前语言。

```python
from src.utils.i18n import set_language
set_language("zh")  # 切换到中文
```

### `get_text(key: str, lang: str = None) -> str`
获取指定键的翻译文本。

```python
from src.utils.i18n import get_text
text = get_text("app_title")  # 使用当前语言
text_zh = get_text("app_title", "zh")  # 指定语言
```

### `t(key: str, lang: str = None) -> str`
`get_text` 的简写形式。

```python
from src.utils.i18n import t
text = t("app_title")
```

## 注意事项

1. 翻译键必须在所有支持的语言中都存在
2. 如果翻译键不存在，函数会返回键本身作为后备
3. 如果指定的语言不存在，会自动回退到英语
4. 建议在添加新UI组件时同时添加翻译

## 贡献

欢迎贡献新的语言翻译或改进现有翻译！请确保：
- 翻译准确、自然
- 遵循项目的翻译原则
- 所有翻译键在新语言中都有对应翻译

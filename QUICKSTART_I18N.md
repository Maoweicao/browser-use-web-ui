# 🚀 快速开始 - 国际化功能

## 立即使用中文界面

### 方法 1: 命令行 (推荐)

**Windows (PowerShell):**
```powershell
$env:WEBUI_LANGUAGE="zh"
python webui.py
```

**Windows (CMD):**
```cmd
set WEBUI_LANGUAGE=zh
python webui.py
```

**Linux/Mac:**
```bash
export WEBUI_LANGUAGE=zh
python webui.py
```

### 方法 2: .env 文件 (持久化)

编辑或创建 `.env` 文件：
```bash
WEBUI_LANGUAGE=zh
```

然后正常启动：
```bash
python webui.py
```

### 方法 3: 在代码中设置

在 `webui.py` 开头添加：
```python
from src.utils.i18n import set_language
set_language('zh')
```

## 🎯 支持的语言

- `en` - English（英语）- 默认
- `zh` - 简体中文

## 📸 效果预览

### 英语界面 (WEBUI_LANGUAGE=en)
```
🌐 Browser Use WebUI
Control your browser with AI assistance

Tabs:
├─ ⚙️ Agent Settings
├─ 🌐 Browser Settings
├─ 🤖 Run Agent
├─ 🎁 Agent Marketplace
│  └─ Deep Research
└─ 📁 Load & Save Config
```

### 中文界面 (WEBUI_LANGUAGE=zh)
```
🌐 Browser Use WebUI
使用 AI 助手控制您的浏览器

标签页:
├─ ⚙️ Agent Settings（智能体设置）
├─ 🌐 Browser Settings（浏览器设置）
├─ 🤖 Run Agent（运行智能体）
├─ 🎁 Agent Marketplace（智能体市场）
│  └─ Deep Research（深度研究）
└─ 📁 Load & Save Config（加载和保存配置）
```

## 🧪 测试 i18n 功能

运行演示脚本查看所有翻译：
```bash
python demo_i18n.py
```

你会看到：
- 支持的语言列表
- 英语翻译示例
- 中文翻译示例
- 代码使用示例

## 💡 小提示

### 保持英文主题名
无论选择哪种语言，主题名称保持英文：
- Ocean
- Default
- Soft
- Monochrome
- Glass
- Origin
- Citrus
- Base

### 技术术语
专业术语保持英文以避免歧义：
- LLM (Large Language Model)
- API (Application Programming Interface)
- CDP (Chrome DevTools Protocol)
- WSS (WebSocket Secure)
- MCP (Model Context Protocol)

## 🔧 故障排除

### 界面仍显示英文？

1. 检查环境变量是否设置：
   ```bash
   echo $WEBUI_LANGUAGE  # Linux/Mac
   echo %WEBUI_LANGUAGE%  # Windows CMD
   $env:WEBUI_LANGUAGE   # Windows PowerShell
   ```

2. 确保值为 `zh` 不是 `ZH` 或 `zh-CN`

3. 重启应用

### 部分文字未翻译？

这可能是新增的功能，请查看 `src/utils/i18n.py` 确认翻译键是否存在。

## 📚 更多信息

- **详细文档**: [I18N_README.md](I18N_README.md)
- **更新说明**: [I18N_UPDATE.md](I18N_UPDATE.md)
- **实现总结**: [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md)

## 🌟 示例截图说明

当你设置 `WEBUI_LANGUAGE=zh` 后，界面会显示：

**标签页标题**:
- ⚙️ Agent Settings（智能体设置）
- 🌐 Browser Settings（浏览器设置）
- 🤖 Run Agent（运行智能体）

**设置项**:
- LLM Provider → LLM 提供商
- LLM Model Name → LLM 模型名称
- Temperature → 温度
- Use Vision → 使用视觉

**按钮**:
- ▶️ Submit Task → ▶️ 提交任务
- ⏸️ Pause → ⏸️ 暂停
- ⏹️ Stop → ⏹️ 停止
- 🗑️ Clear → 🗑️ 清除

**提示信息**:
- "Enter your task here..." → "在此输入您的任务..."
- "Controls randomness in model outputs" → "控制模型输出的随机性"

## 🎉 开始使用！

现在就试试中文界面：
```bash
export WEBUI_LANGUAGE=zh
python webui.py --port 7788
```

访问: http://localhost:7788

享受全中文的 Browser Use WebUI 体验！🚀

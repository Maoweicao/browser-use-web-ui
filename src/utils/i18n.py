"""
Internationalization (i18n) support for Browser Use WebUI.
"""
import os
from typing import Dict, Any, Optional

# Current language (can be set via environment variable or config)
CURRENT_LANGUAGE = os.getenv("WEBUI_LANGUAGE", "en")

# Translation dictionaries
TRANSLATIONS: Dict[str, Dict[str, str]] = {
    "en": {
        # Main interface
        "app_title": "Browser Use WebUI",
        "app_subtitle": "Control your browser with AI assistance",
        
        # Tab titles (keeping emojis and English theme names)
        "tab_agent_settings": "⚙️ Agent Settings",
        "tab_browser_settings": "🌐 Browser Settings",
        "tab_run_agent": "🤖 Run Agent",
        "tab_agent_marketplace": "🎁 Agent Marketplace",
        "tab_load_save_config": "📁 Load & Save Config",
        "tab_deep_research": "Deep Research",
        
        # Agent Marketplace
        "marketplace_subtitle": "Agents built on Browser-Use",
        
        # Agent Settings
        "override_system_prompt": "Override system prompt",
        "extend_system_prompt": "Extend system prompt",
        "mcp_server_json": "MCP server json",
        "mcp_server": "MCP server",
        "llm_provider": "LLM Provider",
        "llm_provider_info": "Select LLM provider for LLM",
        "llm_model_name": "LLM Model Name",
        "llm_model_name_info": "Select a model in the dropdown options or directly type a custom model name",
        "llm_temperature": "LLM Temperature",
        "llm_temperature_info": "Controls randomness in model outputs",
        "use_vision": "Use Vision",
        "use_vision_info": "Enable Vision(Input highlighted screenshot into LLM)",
        "ollama_context_length": "Ollama Context Length",
        "ollama_context_length_info": "Controls max context length model needs to handle (less = faster)",
        "base_url": "Base URL",
        "base_url_info": "API endpoint URL (if required)",
        "api_key": "API Key",
        "api_key_info": "Your API key (leave blank to use .env)",
        "planner_llm_provider": "Planner LLM Provider",
        "planner_llm_model_name": "Planner LLM Model Name",
        "planner_llm_temperature": "Planner LLM Temperature",
        "planner_use_vision": "Use Vision(Planner LLM)",
        "max_run_steps": "Max Run Steps",
        "max_run_steps_info": "Maximum number of steps the agent will take",
        "max_actions": "Max Number of Actions",
        "max_actions_info": "Maximum number of actions the agent will take per step",
        "max_input_tokens": "Max Input Tokens",
        "tool_calling_method": "Tool Calling Method",
        
        # Browser Settings
        "browser_binary_path": "Browser Binary Path",
        "browser_binary_path_placeholder": "e.g. '/Applications/Google\\ Chrome.app/Contents/MacOS/Google\\ Chrome'",
        "browser_user_data_dir": "Browser User Data Dir",
        "browser_user_data_dir_placeholder": "Leave it empty if you use your default user data",
        "use_own_browser": "Use Own Browser",
        "use_own_browser_info": "Use your existing browser instance",
        "keep_browser_open": "Keep Browser Open",
        "keep_browser_open_info": "Keep Browser Open between Tasks",
        "headless_mode": "Headless Mode",
        "headless_mode_info": "Run browser without GUI",
        "disable_security": "Disable Security",
        "disable_security_info": "Disable browser security",
        "window_width": "Window Width",
        "window_width_info": "Browser window width",
        "window_height": "Window Height",
        "window_height_info": "Browser window height",
        "cdp_url": "CDP URL",
        "cdp_url_info": "CDP URL for browser remote debugging",
        "wss_url": "WSS URL",
        "wss_url_info": "WSS URL for browser remote debugging",
        "save_recording_path": "Save Recording Path",
        "save_recording_path_info": "Save recording path",
        "save_recording_path_placeholder": "Save recording path",
        "save_trace_path": "Save Trace Path",
        "save_trace_path_info": "Save trace path",
        "save_trace_path_placeholder": "Save trace path",
        "recording_path": "Recording Path",
        "recording_path_placeholder": "e.g. ./tmp/record_videos",
        "recording_path_info": "Path to save browser recordings",
        "trace_path": "Trace Path",
        "trace_path_placeholder": "e.g. ./tmp/traces",
        "trace_path_info": "Path to save Agent traces",
        "agent_history_save_path": "Agent History Save Path",
        "agent_history_save_path_info": "Specify the directory where agent history should be saved.",
        "save_download_path": "Save Directory for browser downloads",
        "save_download_path_info": "Specify the directory where downloaded files should be saved.",
        "proxy_address": "Proxy Address",
        "proxy_address_info": "Proxy address",
        "proxy_address_placeholder": "Proxy address",
        "chrome_instance_path": "Chrome Instance Path",
        "chrome_instance_path_info": "Chrome instance path",
        "chrome_instance_path_placeholder": "Chrome instance path",
        "minimum_wait_page_load_time": "Minimum Wait Page Load Time",
        "minimum_wait_page_load_time_info": "Minimum wait page load time",
        "wait_for_network_idle_page_load_time": "Wait For Network Idle Page Load Time",
        "wait_for_network_idle_page_load_time_info": "Wait for network idle page load time",
        
        # Run Agent
        "task_input": "Task",
        "task_input_placeholder": "Enter your task here...",
        "add_info": "Additional Information",
        "add_info_placeholder": "Add any additional context or instructions...",
        "start_button": "Start",
        "pause_resume_button": "Pause",
        "stop_button": "Stop",
        "save_session_button": "Save Session",
        "output_display": "Output",
        "download_output": "Download Output",
        "agent_history": "Agent History",
        "browser_state": "Browser State",
        "agent_interaction": "Agent Interaction",
        "your_task_or_response": "Your Task or Response",
        "your_task_placeholder": "Enter your task here or provide assistance when asked.",
        "submit_task": "▶️ Submit Task",
        "pause": "⏸️ Pause",
        "stop": "⏹️ Stop",
        "clear": "🗑️ Clear",
        "browser_live_view": "Browser Live View",
        "task_outputs": "Task Outputs",
        "agent_history_json": "Agent History JSON",
        "task_recording_gif": "Task Recording GIF",
        
        # Load & Save Config
        "load_ui_settings": "Load UI Settings from json",
        "load_config": "Load Config",
        "save_ui_settings": "Save UI Settings",
        "status": "Status",
        
        # Deep Research Agent
        "research_task": "Research Task",
        "research_task_placeholder": "Enter the research topic or question...",
        "resume_task_id": "Resume Task ID",
        "resume_task_id_placeholder": "Leave empty for new task, or enter task ID to resume",
        "parallel_num": "Parallel Agents",
        "parallel_num_info": "Number of parallel agents for research",
        "max_query": "Save Directory",
        "max_query_info": "Directory to save research results",
        "markdown_display": "Research Results",
        "markdown_download": "Download Research",
        "deep_research_start": "Start Research",
        "deep_research_stop": "Stop Research",
    },
    "zh": {
        # 主界面
        "app_title": "Browser Use WebUI",
        "app_subtitle": "使用 AI 助手控制您的浏览器",
        
        # 标签页标题（保留表情符号和英文主题名）
        "tab_agent_settings": "⚙️ Agent Settings（智能体设置）",
        "tab_browser_settings": "🌐 Browser Settings（浏览器设置）",
        "tab_run_agent": "🤖 Run Agent（运行智能体）",
        "tab_agent_marketplace": "🎁 Agent Marketplace（智能体市场）",
        "tab_load_save_config": "📁 Load & Save Config（加载和保存配置）",
        "tab_deep_research": "Deep Research（深度研究）",
        
        # Agent Marketplace
        "marketplace_subtitle": "基于 Browser-Use 构建的智能体",
        
        # Agent Settings
        "override_system_prompt": "覆盖系统提示词",
        "extend_system_prompt": "扩展系统提示词",
        "mcp_server_json": "MCP 服务器 JSON",
        "mcp_server": "MCP 服务器",
        "llm_provider": "LLM 提供商",
        "llm_provider_info": "选择 LLM 提供商",
        "llm_model_name": "LLM 模型名称",
        "llm_model_name_info": "从下拉选项中选择模型或直接输入自定义模型名称",
        "llm_temperature": "LLM 温度",
        "llm_temperature_info": "控制模型输出的随机性",
        "use_vision": "使用视觉",
        "use_vision_info": "启用视觉功能（将高亮截图输入 LLM）",
        "ollama_context_length": "Ollama 上下文长度",
        "ollama_context_length_info": "控制模型需要处理的最大上下文长度（越小越快）",
        "base_url": "基础 URL",
        "base_url_info": "API 端点 URL（如需要）",
        "api_key": "API 密钥",
        "api_key_info": "您的 API 密钥（留空则使用 .env 文件中的配置）",
        "planner_llm_provider": "规划器 LLM 提供商",
        "planner_llm_model_name": "规划器 LLM 模型名称",
        "planner_llm_temperature": "规划器 LLM 温度",
        "planner_use_vision": "使用视觉（规划器 LLM）",
        "max_run_steps": "最大运行步数",
        "max_run_steps_info": "智能体将执行的最大步数",
        "max_actions": "最大操作数",
        "max_actions_info": "智能体每步将执行的最大操作数",
        "max_input_tokens": "最大输入令牌数",
        "tool_calling_method": "工具调用方法",
        
        # Browser Settings
        "browser_binary_path": "浏览器二进制路径",
        "browser_binary_path_placeholder": "例如：'/Applications/Google\\ Chrome.app/Contents/MacOS/Google\\ Chrome'",
        "browser_user_data_dir": "浏览器用户数据目录",
        "browser_user_data_dir_placeholder": "如果使用默认用户数据，请留空",
        "use_own_browser": "使用自己的浏览器",
        "use_own_browser_info": "使用您现有的浏览器实例",
        "keep_browser_open": "保持浏览器打开",
        "keep_browser_open_info": "在任务之间保持浏览器打开",
        "headless_mode": "无头模式",
        "headless_mode_info": "在无 GUI 模式下运行浏览器",
        "disable_security": "禁用安全性",
        "disable_security_info": "禁用浏览器安全性",
        "window_width": "窗口宽度",
        "window_width_info": "浏览器窗口宽度",
        "window_height": "窗口高度",
        "window_height_info": "浏览器窗口高度",
        "cdp_url": "CDP URL",
        "cdp_url_info": "用于浏览器远程调试的 CDP URL",
        "wss_url": "WSS URL",
        "wss_url_info": "用于浏览器远程调试的 WSS URL",
        "save_recording_path": "保存录制路径",
        "save_recording_path_info": "保存录制路径",
        "save_recording_path_placeholder": "保存录制路径",
        "save_trace_path": "保存跟踪路径",
        "save_trace_path_info": "保存跟踪路径",
        "save_trace_path_placeholder": "保存跟踪路径",
        "recording_path": "录制路径",
        "recording_path_placeholder": "例如：./tmp/record_videos",
        "recording_path_info": "保存浏览器录制的路径",
        "trace_path": "跟踪路径",
        "trace_path_placeholder": "例如：./tmp/traces",
        "trace_path_info": "保存智能体跟踪的路径",
        "agent_history_save_path": "智能体历史保存路径",
        "agent_history_save_path_info": "指定保存智能体历史的目录",
        "save_download_path": "浏览器下载保存目录",
        "save_download_path_info": "指定保存下载文件的目录",
        "proxy_address": "代理地址",
        "proxy_address_info": "代理地址",
        "proxy_address_placeholder": "代理地址",
        "chrome_instance_path": "Chrome 实例路径",
        "chrome_instance_path_info": "Chrome 实例路径",
        "chrome_instance_path_placeholder": "Chrome 实例路径",
        "minimum_wait_page_load_time": "最小页面加载等待时间",
        "minimum_wait_page_load_time_info": "最小页面加载等待时间",
        "wait_for_network_idle_page_load_time": "网络空闲页面加载等待时间",
        "wait_for_network_idle_page_load_time_info": "网络空闲页面加载等待时间",
        
        # Run Agent
        "task_input": "任务",
        "task_input_placeholder": "在此输入您的任务...",
        "add_info": "附加信息",
        "add_info_placeholder": "添加任何附加的上下文或说明...",
        "start_button": "开始",
        "pause_resume_button": "暂停",
        "stop_button": "停止",
        "save_session_button": "保存会话",
        "output_display": "输出",
        "download_output": "下载输出",
        "agent_history": "智能体历史",
        "browser_state": "浏览器状态",
        "agent_interaction": "智能体交互",
        "your_task_or_response": "您的任务或回复",
        "your_task_placeholder": "在此输入您的任务或在请求时提供帮助",
        "submit_task": "▶️ 提交任务",
        "pause": "⏸️ 暂停",
        "stop": "⏹️ 停止",
        "clear": "🗑️ 清除",
        "browser_live_view": "浏览器实时视图",
        "task_outputs": "任务输出",
        "agent_history_json": "智能体历史 JSON",
        "task_recording_gif": "任务录制 GIF",
        
        # Load & Save Config
        "load_ui_settings": "从 JSON 加载 UI 设置",
        "load_config": "加载配置",
        "save_ui_settings": "保存 UI 设置",
        "status": "状态",
        
        # Deep Research Agent
        "research_task": "研究任务",
        "research_task_placeholder": "输入研究主题或问题...",
        "resume_task_id": "恢复任务 ID",
        "resume_task_id_placeholder": "新任务请留空，或输入任务 ID 以恢复",
        "parallel_num": "并行智能体数",
        "parallel_num_info": "用于研究的并行智能体数量",
        "max_query": "保存目录",
        "max_query_info": "保存研究结果的目录",
        "markdown_display": "研究结果",
        "markdown_download": "下载研究结果",
        "deep_research_start": "开始研究",
        "deep_research_stop": "停止研究",
    }
}


def set_language(lang: str):
    """Set the current language."""
    global CURRENT_LANGUAGE
    if lang in TRANSLATIONS:
        CURRENT_LANGUAGE = lang
    else:
        raise ValueError(f"Language '{lang}' is not supported. Available languages: {list(TRANSLATIONS.keys())}")


def get_text(key: str, lang: Optional[str] = None) -> str:
    """Get translated text for a given key."""
    language = lang or CURRENT_LANGUAGE
    if language not in TRANSLATIONS:
        language = "en"  # Fallback to English
    
    return TRANSLATIONS[language].get(key, key)


def t(key: str, lang: Optional[str] = None) -> str:
    """Shorthand for get_text."""
    return get_text(key, lang)

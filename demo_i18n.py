"""
演示国际化功能的示例脚本
"""
from src.utils.i18n import t, set_language, TRANSLATIONS

def demo_i18n():
    """演示 i18n 功能"""
    
    print("=" * 80)
    print("Browser Use WebUI 国际化 (i18n) 演示")
    print("=" * 80)
    print()
    
    # 显示支持的语言
    print("支持的语言 / Supported Languages:")
    for lang in TRANSLATIONS.keys():
        print(f"  - {lang}")
    print()
    
    # 演示一些常用翻译键
    demo_keys = [
        "app_title",
        "app_subtitle",
        "tab_agent_settings",
        "tab_browser_settings",
        "tab_run_agent",
        "llm_provider",
        "llm_model_name",
        "use_vision",
        "submit_task",
        "agent_interaction"
    ]
    
    # 英语演示
    print("-" * 80)
    print("English (en):")
    print("-" * 80)
    set_language("en")
    for key in demo_keys:
        print(f"  {key:30s} => {t(key)}")
    print()
    
    # 中文演示
    print("-" * 80)
    print("简体中文 (zh):")
    print("-" * 80)
    set_language("zh")
    for key in demo_keys:
        print(f"  {key:30s} => {t(key)}")
    print()
    
    # 演示代码用法
    print("=" * 80)
    print("代码使用示例 / Code Usage Examples:")
    print("=" * 80)
    print()
    
    print("1. 设置语言 / Set Language:")
    print("   from src.utils.i18n import set_language")
    print("   set_language('zh')  # 切换到中文")
    print()
    
    print("2. 获取翻译文本 / Get Translated Text:")
    print("   from src.utils.i18n import t")
    print("   text = t('app_title')")
    print()
    
    print("3. 在 Gradio 组件中使用 / Use in Gradio Components:")
    print("   import gradio as gr")
    print("   textbox = gr.Textbox(")
    print("       label=t('task_input'),")
    print("       placeholder=t('task_input_placeholder')")
    print("   )")
    print()
    
    print("=" * 80)
    print("使用环境变量设置默认语言 / Set Default Language via Environment Variable:")
    print("=" * 80)
    print()
    print("在命令行中:")
    print("  export WEBUI_LANGUAGE=zh")
    print("  python webui.py")
    print()
    print("或在 .env 文件中:")
    print("  WEBUI_LANGUAGE=zh")
    print()
    
    print("=" * 80)
    print("完成！/ Done!")
    print("=" * 80)


if __name__ == "__main__":
    demo_i18n()

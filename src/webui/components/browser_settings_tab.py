import os
from distutils.util import strtobool
import gradio as gr
import logging
from gradio.components import Component

from src.webui.webui_manager import WebuiManager
from src.utils import config
from src.utils.i18n import t

logger = logging.getLogger(__name__)

async def close_browser(webui_manager: WebuiManager):
    """
    Close browser
    """
    if webui_manager.bu_current_task and not webui_manager.bu_current_task.done():
        webui_manager.bu_current_task.cancel()
        webui_manager.bu_current_task = None

    if webui_manager.bu_browser_context:
        logger.info("⚠️ Closing browser context when changing browser config.")
        await webui_manager.bu_browser_context.close()
        webui_manager.bu_browser_context = None

    if webui_manager.bu_browser:
        logger.info("⚠️ Closing browser when changing browser config.")
        await webui_manager.bu_browser.close()
        webui_manager.bu_browser = None

def create_browser_settings_tab(webui_manager: WebuiManager):
    """
    Creates a browser settings tab.
    """
    input_components = set(webui_manager.get_components())
    tab_components = {}

    with gr.Group():
        with gr.Row():
            browser_binary_path = gr.Textbox(
                label=t("browser_binary_path"),
                lines=1,
                interactive=True,
                placeholder=t("browser_binary_path_placeholder")
            )
            browser_user_data_dir = gr.Textbox(
                label=t("browser_user_data_dir"),
                lines=1,
                interactive=True,
                placeholder=t("browser_user_data_dir_placeholder"),
            )
    with gr.Group():
        with gr.Row():
            use_own_browser = gr.Checkbox(
                label=t("use_own_browser"),
                value=bool(strtobool(os.getenv("USE_OWN_BROWSER", "false"))),
                info=t("use_own_browser_info"),
                interactive=True
            )
            keep_browser_open = gr.Checkbox(
                label=t("keep_browser_open"),
                value=bool(strtobool(os.getenv("KEEP_BROWSER_OPEN", "true"))),
                info=t("keep_browser_open_info"),
                interactive=True
            )
            headless = gr.Checkbox(
                label=t("headless_mode"),
                value=False,
                info=t("headless_mode_info"),
                interactive=True
            )
            disable_security = gr.Checkbox(
                label=t("disable_security"),
                value=False,
                info=t("disable_security_info"),
                interactive=True
            )

    with gr.Group():
        with gr.Row():
            window_w = gr.Number(
                label=t("window_width"),
                value=1280,
                info=t("window_width_info"),
                interactive=True
            )
            window_h = gr.Number(
                label=t("window_height"),
                value=1100,
                info=t("window_height_info"),
                interactive=True
            )
    with gr.Group():
        with gr.Row():
            cdp_url = gr.Textbox(
                label=t("cdp_url"),
                value=os.getenv("BROWSER_CDP", None),
                info=t("cdp_url_info"),
                interactive=True,
            )
            wss_url = gr.Textbox(
                label=t("wss_url"),
                info=t("wss_url_info"),
                interactive=True,
            )
    with gr.Group():
        with gr.Row():
            save_recording_path = gr.Textbox(
                label=t("recording_path"),
                placeholder=t("recording_path_placeholder"),
                info=t("recording_path_info"),
                interactive=True,
            )

            save_trace_path = gr.Textbox(
                label=t("trace_path"),
                placeholder=t("trace_path_placeholder"),
                info=t("trace_path_info"),
                interactive=True,
            )

        with gr.Row():
            save_agent_history_path = gr.Textbox(
                label=t("agent_history_save_path"),
                value="./tmp/agent_history",
                info=t("agent_history_save_path_info"),
                interactive=True,
            )
            save_download_path = gr.Textbox(
                label=t("save_download_path"),
                value="./tmp/downloads",
                info=t("save_download_path_info"),
                interactive=True,
            )
    tab_components.update(
        dict(
            browser_binary_path=browser_binary_path,
            browser_user_data_dir=browser_user_data_dir,
            use_own_browser=use_own_browser,
            keep_browser_open=keep_browser_open,
            headless=headless,
            disable_security=disable_security,
            save_recording_path=save_recording_path,
            save_trace_path=save_trace_path,
            save_agent_history_path=save_agent_history_path,
            save_download_path=save_download_path,
            cdp_url=cdp_url,
            wss_url=wss_url,
            window_h=window_h,
            window_w=window_w,
        )
    )
    webui_manager.add_components("browser_settings", tab_components)

    async def close_wrapper():
        """Wrapper for handle_clear."""
        await close_browser(webui_manager)

    headless.change(close_wrapper)
    keep_browser_open.change(close_wrapper)
    disable_security.change(close_wrapper)
    use_own_browser.change(close_wrapper)

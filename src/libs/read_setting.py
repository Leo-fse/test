
from src.const.graph_setting import figure_setting, renderer_settings, sources
from src.utils import log_decorator, logger


@log_decorator(logger)
def main():
    logger.debug("設定ファイルを読み込みます！")

    setting_info = dict(
        figure_setting=figure_setting, sources=sources, renderer_settings=renderer_settings
    )
    return setting_info


main()

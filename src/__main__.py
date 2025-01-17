import subprocess

from src.libs import drawing_graph, read_setting
from src.settings import BASE_DIR, config, debug
from src.utils.logger import log_decorator, logger


@log_decorator(logger)
def main():
    # 設定ファイルの読み込み
    setting_info = read_setting.main()
    # グラフ化
    graph = drawing_graph.main(setting_info)
    logger.debug(f"setting_info: {setting_info}")
    return graph


if __name__ == "__main__":
    main()

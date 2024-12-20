from settings import BASE_DIR, CONFIG_DIR
from utils import logger, logger_setup, log_decorator

@log_decorator(logger_setup)
def main():
    logger.debug("設定ファイルを読み込みます！")
    logger.info(str(BASE_DIR))
    logger.info(str(CONFIG_DIR))
    logger.info("hello, this is read_setting.py")


main()
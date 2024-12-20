import subprocess

from libs import read_setting
from settings import BASE_DIR, config, debug
from utils.logger import log_decorator, logger, logger_setup


@log_decorator(logger_setup)
def main():
    read_setting.main()
    logger.debug("ツールを起動します！")
    logger.info("ツールを起動します！")
    logger.warning("ツールを起動します！")
    logger.error("ツールを起動します！")
    logger.critical("ツールを起動します！")


if __name__ == "__main__":
    main()

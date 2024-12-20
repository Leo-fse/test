from settings import BASE_DIR, config
from libs import read_setting
from utils.logger import log_decorator, logger_setup, logger

@log_decorator(logger_setup)
def main():
    read_setting.main()
    print(BASE_DIR)
    print(config.sections())


if __name__ == "__main__":
    logger.debug("ツールを起動します！")
    logger.info("ツールを起動します！")
    logger.warning("ツールを起動します！")
    logger.error("ツールを起動します！")
    logger.critical("ツールを起動します！")
    main()
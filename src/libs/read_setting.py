from utils import log_decorator, logger, logger_setup


@log_decorator(logger_setup)
def main():
    logger.debug("設定ファイルを読み込みます！")


main()

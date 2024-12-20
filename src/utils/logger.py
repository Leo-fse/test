import functools
import logging
import os
import re
import time
import traceback

from colorama import Fore, Style, init
from pathlib import Path
from settings import LOGS_DIR

init(autoreset=True)

class ColoredFormatter(logging.Formatter):
    def format(self, record):
        log_colors = {
            "DEBUG": Fore.CYAN,
            "INFO": Fore.GREEN,
            "WARNING": Fore.YELLOW,
            "ERROR": Fore.RED,
            "CRITICAL": Fore.RED,
        }
        log_color = log_colors.get(record.levelname, Fore.RESET)
        record.levelname = f"{log_color}{record.levelname}{Style.RESET_ALL}"
        return super().format(record)

class LoggerSetup:
    def __init__(self, log_dir: Path):
        self.log_dir = log_dir
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self._setup_console_handler()
        self._setup_file_handler()

    def _setup_console_handler(self):
        # コンソール用のハンドラーを設定
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(ColoredFormatter("%(asctime)s - %(levelname)s - %(message)s"))
        self.logger.addHandler(console_handler)

    def _setup_file_handler(self):
        # ログファイルのパスを設定
        log_file_path = self.log_dir / f"log_{time.strftime('%Y%m%d_%H%M%S')}.log"
        
        # ログファイルの履歴を10回分残すために、古いログを削除する
        log_files = sorted(self.log_dir.glob("log_*.log"), key=os.path.getctime, reverse=True)
        if len(log_files) > 10:
            for file_to_delete in log_files[10:]:
                os.remove(file_to_delete)

        file_handler = logging.FileHandler(log_file_path)
        file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
        self.logger.addHandler(file_handler)
        self.file_handler = file_handler
        self.log_file_path = log_file_path

    def get_logger(self):
        return self.logger

    def get_file_handler(self):
        return self.file_handler

def log_decorator(logger_setup):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                logger_setup.logger.info(f"START   {func.__module__}.{func.__name__} args: {args}, kwargs: {kwargs}")
                start_time = time.time()
                result = func(*args, **kwargs)
                end_time = time.time()
                logger_setup.logger.info(f"FINISHED {func.__name__} executed_time: {end_time - start_time:.2f} seconds")
                return result
            except Exception as e:
                logger_setup.logger.error(f"ERROR in {func.__name__} : {traceback.format_exc()}")
                raise
            finally:
                # カラーコードを削除
                remove_color_codes(logger_setup.get_file_handler().stream.name)
        return wrapper
    return decorator

def remove_color_codes(log_file_path):
    with open(log_file_path, "r") as file:
        log_content = file.read()

    # カラーコードを削除する正規表現パターン
    color_code_pattern = re.compile(r"\x1b\[\d+m")
    # カラーコードを削除
    log_content = re.sub(color_code_pattern, "", log_content)

    with open(log_file_path, "w") as file:
        file.write(log_content)

# ログの設定と初期化
# LOGS_DIR = Path('./logs')
logger_setup = LoggerSetup(LOGS_DIR)
logger = logger_setup.get_logger()



if __name__ == "__main__":
    @log_decorator(logger_setup)
    def example_function(a, b):
        logger.info("This is an example function.")
        result = a + b
        logger.debug(f"Result of adding {a} and {b}: {result}")
        return result
    
    example_function(5, 3)

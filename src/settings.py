from pathlib import Path
from configparser import ConfigParser



def ensure_dir_exists(directory: Path) -> Path:
    """指定されたディレクトリを作成し、Pathオブジェクトを返す"""
    directory.mkdir(parents=True, exist_ok=True)
    return directory

def read_config(config_file: Path) -> ConfigParser:
    """指定された設定ファイルを読み込んでConfigParserオブジェクトを返す"""
    config = ConfigParser()
    config.read(config_file)
    return config

BASE_DIR = Path(__file__).resolve().parent.parent

CONFIG_DIR = ensure_dir_exists(BASE_DIR / "config")
DATA_DIR = ensure_dir_exists(BASE_DIR / "data")
INPUT_DIR = ensure_dir_exists(DATA_DIR / "input")
OUTPUT_DIR = ensure_dir_exists(DATA_DIR / "output")
NOTEBOOKS_DIR = ensure_dir_exists(BASE_DIR / "notebooks")
DOCS_DIR = ensure_dir_exists(BASE_DIR / "docs")
TESTS_DIR = ensure_dir_exists(BASE_DIR / "tests")
LOGS_DIR = ensure_dir_exists(BASE_DIR / "logs")


config_file = CONFIG_DIR / "settings.ini"
if not config_file.exists():
    raise FileNotFoundError(f"設定ファイルが見つかりません: {config_file}")

config = read_config(config_file)
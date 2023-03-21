# *_*coding:utf-8 *_*
# @Author : Reggie
# @Time : 2023/2/17 13:50
import platform
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.absolute().as_posix()
Path(BASE_DIR).mkdir(parents=True, exist_ok=True)

# 调试模式
DEBUG = False

# api config
HOST = '0.0.0.0'
PORT = 7600

STATIC_DIR = Path(BASE_DIR).joinpath("static")
if getattr(sys, 'frozen', False) and getattr(sys, '_MEIPASS', None):
    STATIC_DIR = Path(sys._MEIPASS).joinpath("static")

LOG_PATH = Path(BASE_DIR).joinpath("logs")
if getattr(sys, 'frozen', False) and getattr(sys, '_MEIPASS', None):
    LOG_PATH = Path("/chemical_data/websocket_data").joinpath("logs")
LOG_PATH.mkdir(parents=True, exist_ok=True)
LOG_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s -- %(levelname)s -- %(message)s"
        },
        "short": {
            "format": "%(levelname)s -- %(message)s"
        },
        "long": {
            "format": "%(asctime)s -- %(levelname)s -- %(message)s (%(funcName)s in %(filename)s:%(lineno)d])"
        },
        "free": {
            "format": "%(message)s"
        }
    },
    'root': {
        "handlers": ["console", "root_file"],
        'level': "DEBUG" if DEBUG else "INFO",
    },
    "handlers": {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            "formatter": "long"
        },
        "root_file": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "maxBytes": 1000000,
            "backupCount": 3,
            "formatter": "long",
            "filename": Path(LOG_PATH).joinpath("datatables_backend.log"),
            "encoding": "utf-8"
        },
        "access_file": {
            "class": "logging.FileHandler",
            "filename": Path(LOG_PATH).joinpath("fastapi_access.log"),
            "formatter": "long",
            "encoding": "utf-8"
        },
        "error_file": {
            "class": "logging.FileHandler",
            "filename": Path(LOG_PATH).joinpath("fastapi_error.log"),
            "formatter": "long",
            "encoding": "utf-8"
        }
    },
    "loggers": {
        "uvicorn.access": {
            "level": "DEBUG" if DEBUG else "INFO",
            "handlers": ["access_file"],
            "propagate": True
        },
        "uvicorn.error": {
            "level": "DEBUG" if DEBUG else "INFO",
            "handlers": ["error_file"],
            "propagate": True
        }
    },
}

# 指定api启动线程数量
if "win32" == sys.platform or platform.system() == "Windows":
    WORKERS = 1
else:
    WORKERS = 10

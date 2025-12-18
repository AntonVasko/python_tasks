from flask import Flask
import logging
from logging.config import dictConfig
import pythonjsonlogger

dictConfig({
    "version": 1,
    "formatters": {
        "default": {
            "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
        },
        "json": {
            "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "format": "%(asctime)s %(levelname)s %(name)s %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "level": "DEBUG",
            "stream": "ext://sys.stdout",
        },
        "error_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "default",
            "filename": "logs/errors.log",
            "maxBytes": 10485760,
            "backupCount": 5,
            "level": "ERROR"
        },
        "info_file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "formatter": "json",
            "filename": "logs/app.log",
            "when": "midnight",
            "interval": 1,
            "backupCount": 30,
            "level": "INFO"
        }
    },

    "loggers": {
        "werkzeug": {
            "level": "INFO",
            "handlers": ["console"],
            "propagate": False
        },
        "my_app": {
            "level": "DEBUG",
            "handlers": ["console", "info_file", "error_file"],
            "propagate": False
        },
        "sqalchemy": {
            "level": "WARNING",
            "handlers": ["console"],
            "propagate": False
        }
    },

    "root": {
        "level": "INFO",
        "handlers": ["console", "error_file"]
    }
})

app = Flask(__name__)

@app.route('/')
def hello():
    app.logger.info("Обработка запроса")
    app.logger.error("Тестовая ошибка")
    return "Hello World!"

if __name__ == "__main__":
    app.run()
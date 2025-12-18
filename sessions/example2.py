from flask import Flask
import logging
from logging.config import dictConfig

dictConfig({
    "version": 1,
    "formatters": {
        "default": {
            "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
        }
    },
    "handlers": {
        "wsgi": {
            "class": "logging.StreamHandler",
            "stream": "ext://flask.logging.wsgi_errors_stream",
            "formatter": "default"
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": "app.log",
            "formatter": "default",
            "level": "ERROR"
        }
    },
    "root": {
        "level": "INFO",
        "handlers": ["wsgi", "file"]
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
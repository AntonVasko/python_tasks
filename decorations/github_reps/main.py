import requests
from flask import Flask, render_template, session, request, redirect, url_for
import secrets
import sqlite3
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(levelname)s | %(funcName)s | %(message)s',
        },
        'everything': {
          "format": """ ___________________________________________
                        asctime: %(asctime)s\n
                        created: %(created)f\n
                        filename: %(filename)s\n
                        funcName: %(funcName)s\n
                        levelname: %(levelname)s\n
                        levelno: %(levelno)s\n
                        lineno: %(lineno)d\n
                        message: %(message)s\n
                        module: %(module)s\n
                        msecs: %(msecs)d\n
                        name: %(name)s\n
                        pathname: %(pathname)s\n
                        process: %(process)d\n
                        processName: %(processName)s\n
                        relativeCreated: %(relativeCreated)d\n
                        thread: %(thread)d\n
                        threadName: %(threadName)s\n
                        _____________________________________________
                        """

        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'level': 'DEBUG',
            'stream': 'ext://sys.stdout'
        },
        'info_file': {
            'class': 'logging.FileHandler',
            "formatter": "everything",
            'filename': 'logs/app.log',
            'level': 'WARNING'
        }
    },
    'loggers': {
        'my_app': {
            'level': 'DEBUG',
            'handlers': ['info_file'],
            'propagate': False
        }
    },
    'root': {
        'level': 'WARNING',
        'handlers': ['info_file', "console"]
    }
})


url_js = f"https://api.github.com/search/repositories?q=language:js+sort:stars+stars:%3E10000"
url_py = f"https://api.github.com/search/repositories?q=language:python+sort:stars+stars:%3E10000"
url_cpp = f"https://api.github.com/search/repositories?q=language:cpp+sort:stars+stars:%3E10000"

def data(language):
    with sqlite3.connect("languages.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM mid_data WHERE language = (?)", [language])
        ammount = cursor.fetchall()
    return ammount

def data_to_db(url, language, headers = {"Accept": "application/vnd.github.v3+json"}):
    lang = requests.request("GET", url, headers=headers)
    data = lang.json()
    reps = data["items"]
    for el in reps:
        with sqlite3.connect("languages.db") as conn:
            cursor = conn.cursor()
            if el["license"] == None:
                license = "No license"
            else: 
                license = el["license"]["name"]
            cursor.execute(f"INSERT INTO {language} (name, author, stars, forks, license) VALUES(?, ?, ?, ?, ?)", [el["name"], el["owner"]["login"], el["stargazers_count"], el["forks"], license])


app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = secrets.token_hex()

@app.route('/cpp', methods = ["POST", "GET"])
def cpp():
    if session["cpp"] == False:
        session["cpp"] = True
        with sqlite3.connect("languages.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT clicked FROM mid_data WHERE language = 'Cpp'")
            clckd = int(cursor.fetchone()[0])
            cursor.execute("UPDATE mid_data SET clicked = (?) WHERE language = 'Cpp'", [clckd+1])
    app.logger.info("C++")
    statistic = data("Cpp")[0]
    return render_template("cpp.html", reps=statistic[1], stars=statistic[2], forks=statistic[3], licenses=[statistic[4], statistic[5], statistic[6]])

@app.route('/js', methods = ["POST", "GET"])
def js():
    if session["js"] == False:
        session["js"] = True
        with sqlite3.connect("languages.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT clicked FROM mid_data WHERE language = 'JavaScript'")
            clckd = int(cursor.fetchone()[0])
            cursor.execute("UPDATE mid_data SET clicked = (?) WHERE language = 'JavaScript'", [clckd+1])
    app.logger.info("JavaScript")
    statistic = data("JavaScript")[0]
    return render_template("js.html", reps=statistic[1], stars=statistic[2], forks=statistic[3], licenses=[statistic[4], statistic[5], statistic[6]])

@app.route('/py', methods = ["POST", "GET"])
def py():
    if session["py"] == False:
        session["py"] = True
        with sqlite3.connect("languages.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT clicked FROM mid_data WHERE language = 'Python'")
            clckd = int(cursor.fetchone()[0])
            cursor.execute("UPDATE mid_data SET clicked = (?) WHERE language = 'Python'", [clckd+1])
    app.logger.info("Python")
    statistic = data("Python")[0]
    return render_template("py.html", reps=statistic[1], stars=statistic[2], forks=statistic[3], licenses=[statistic[4], statistic[5], statistic[6]])   

@app.route("/logged", methods = ["POST", "GET"])
def index():
    return render_template("index.html")

@app.route('/', methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
        session["username"] = request.form["username"]
        if session["username"] != '':
            session["cpp"] = False
            session["py"] = False
            session["js"] = False
            return redirect(url_for('index'))
    return """
        <form method="POST">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    """

@app.errorhandler(500)
def error_page(error):
    return "Ошибка"

if __name__ == "__main__":
    app.run()

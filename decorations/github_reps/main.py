import requests
from flask import Flask, render_template
import sqlite3

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

@app.route('/cpp', methods = ["POST", "GET"])
def cpp():
    statistic = data("Cpp")[0]
    return render_template("cpp.html", reps=statistic[1], stars=statistic[2], forks=statistic[3], licenses=[statistic[4], statistic[5], statistic[6]])

@app.route('/js', methods = ["POST", "GET"])
def js():
    statistic = data("JavaScript")[0]
    return render_template("js.html", reps=statistic[1], stars=statistic[2], forks=statistic[3], licenses=[statistic[4], statistic[5], statistic[6]])

@app.route('/py', methods = ["POST", "GET"])
def py():
    statistic = data("Python")[0]
    return render_template("py.html", reps=statistic[1], stars=statistic[2], forks=statistic[3], licenses=[statistic[4], statistic[5], statistic[6]])   

@app.route("/", methods = ["POST", "GET"])
def index():
    return render_template("index.html")

@app.errorhandler(500)
def error_page(error):
    return "Ошибка"

if __name__ == "__main__":
    app.run()

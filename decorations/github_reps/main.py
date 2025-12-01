import requests
from flask import Flask, render_template

url_js = f"https://api.github.com/search/repositories?q=language:js+sort:stars+stars:%3E10000"
url_py = f"https://api.github.com/search/repositories?q=language:python+sort:stars+stars:%3E10000"
url_cpp = f"https://api.github.com/search/repositories?q=language:cpp+sort:stars+stars:%3E10000"

def data(url, headers = {"Accept": "application/vnd.github.v3+json"}):
    lang = requests.request("GET", url, headers=headers)
    data = lang.json()
    ammount = {"reps": data["total_count"], "stars": 0, "forks": 0}
    licenses = {"No":0}
    reps = data["items"]
    for el in reps:
        if el["license"] == None:
            licenses["No"]+=1
        else:
            if el["license"]["name"] in licenses:
                licenses[el["license"]["name"]] += 1
            else:
                licenses[el["license"]["name"]] = 1
        ammount["stars"] += el["stargazers_count"]
        ammount["forks"] += el["forks"]
    ammount["stars"] //= ammount["reps"]
    ammount["forks"] //= ammount["reps"]
    rating_licenses = dict()
    for el in licenses:
        rating_licenses[licenses[el]] = el
    keys = sorted(list(rating_licenses.keys()))
    ammount["license1"] = rating_licenses[keys[0]]
    ammount["license2"] = rating_licenses[keys[1]]
    ammount["license3"] = rating_licenses[keys[2]]
    return ammount

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route('/cpp', methods = ["POST", "GET"])
def cpp():
    statistic = data(url_cpp)
    return render_template("cpp.html", reps=statistic["reps"], stars=statistic["stars"], forks=statistic["forks"], licenses=[statistic["license1"], statistic["license2"], statistic["license3"]])

@app.route('/js', methods = ["POST", "GET"])
def js():
    statistic = data(url_js)
    return render_template("js.html", reps=statistic["reps"], stars=statistic["stars"], forks=statistic["forks"], licenses=[statistic["license1"], statistic["license2"], statistic["license3"]])

@app.route('/py', methods = ["POST", "GET"])
def py():
    statistic = data(url_py)
    return render_template("py.html", reps=statistic["reps"], stars=statistic["stars"], forks=statistic["forks"], licenses=[statistic["license1"], statistic["license2"], statistic["license3"]])

@app.route("/", methods = ["POST", "GET"])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()

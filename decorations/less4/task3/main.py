from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<name>")
def main(name):
    return render_template("text.html", name=name)

if __name__ == "__main__":
    app.run()
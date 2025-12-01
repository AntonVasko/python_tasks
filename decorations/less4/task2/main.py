from flask import Flask, render_template

app = Flask(__name__)

todo = ["Покушать",
        "Поспать",
        "Сделать уроки"]

@app.route('/')
def main():
    return render_template("text.html", todo=todo)

if __name__ == "__main__":
    app.run()

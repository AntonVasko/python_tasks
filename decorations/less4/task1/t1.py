from flask import render_template, Flask, request

app = Flask(__name__)

@app.route("/Pushkin")
def stih():
    title = request.args.get("title")
    color = request.args.get("color", "зелёный")
    animal = request.args.get("animal", "кот")
    object = request.args.get("object", "леший")
    return render_template("text.html", title=title, color=color, animal=animal, object=object)

if __name__ == "__main__":
    app.run()
import sys
import os
from flask import Flask, render_template, session, request, redirect, url_for
import secrets
import json
import sqlite3

try:
    conn = sqlite3.connect("cassa.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    data = list(cursor.fetchall())
    for i in range(len(data)):
        data[i] = tuple(list(data[i])[1:])
except:
    with open('cassa.json') as f:
        file = json.load(f)
        data = []
        for el in file:
            pr = file[el]
            data.append((el, pr['Цена'], pr['Скидка'], pr['Цена со скидкой']))

#cassa = Cassa(data, obj, purchases, canc, sum_label, tobuy)

app = Flask(__name__, template_folder="templates")
app.secret_key = secrets.token_hex()

@app.route('/', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session['username'] = request.form["phone_number"]
        if session["username"] != "":
            session["cart"] = dict()
            for el in data:
                session["cart"][el[0]] = 0
            return redirect(url_for("shop"))
    return """
    <form method="post">
        <p><input type=text name=phone_number>
        <p><input type=submit value = login>
    </form>
    """

@app.route("/shop", methods=["POST", "GET"])
def shop():
    if request.method == "POST":
        print(request.form["product"])
        print(session["cart"][request.form["product"]])
        session["cart"][request.form["product"]] += 1
        session.modified = True
    return render_template("products.html", products=data)

@app.route("/cart", methods=["POST", "GET"])
def cart():
    if request.method == "POST":
        if request.form["product"]:
            session["cart"][request.form["product"]] -= 1
        elif request.form["clear"]:
            print("clear")
        session.modified = True
    return render_template("cart.html", cart=session["cart"])

@app.errorhandler(500)
def not_registrated(error):
    return """<h3>Вы не зарегестрированы!
    <form method="GET" action="/"><input type="submit" value="Регистрация">"""

if __name__ == "__main__":
    app.run()
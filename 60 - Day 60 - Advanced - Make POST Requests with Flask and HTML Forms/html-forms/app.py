import requests
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def get_login():
    name = request.form.get('name')
    pwd = request.form.get('password')
    return f"Name: {name} & Pwd: {pwd}"


if __name__ == "__main__":
    app.run(debug=True)

# Clone of this website: https://startbootstrap.com/previews/clean-blog
from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get(url="https://api.npoint.io/11d4e811eacf47e14ead")
response.raise_for_status()
data = response.json()


@app.route("/")
def index():

    return render_template("index.html", data=data)


@app.route("/about")
def get_about():
    return render_template("about.html")


@app.route("/post/<int:number>")
def get_post(number):
    print(number)
    return render_template("post.html", data=data[number - 1])


@app.route("/contact")
def get_contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)

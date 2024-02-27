from datetime import datetime
from flask import Flask, render_template
import random
import requests

app = Flask(__name__)


@app.route("/")
def index():
    random_number = random.randint(1, 10)
    year = datetime.now().year
    return render_template("index.html", msg="Hello World", num=random_number, year=year)


@app.route("/guess/<name>")
def guess(name):
    # Gender Api https://genderize.io/
    response1 = requests.get(url=f"https://api.genderize.io?name={name}")
    response1.raise_for_status()
    gender = response1.json()["gender"]

    # Age Api https://agify.io/
    response2 = requests.get(url=f"https://api.agify.io?name={name}")
    response2.raise_for_status()
    age = response2.json()["age"]
    return render_template("guess.html", name=name, gender=gender, age=age)


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    # https://www.npoint.io You can create your own api using this
    # From the course resource, she made it already for us : https://www.npoint.io/docs/c790b4d5cab58020d391
    response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    response.raise_for_status()
    all_posts = response.json()
    # print(all_posts)
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)

















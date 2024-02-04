from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
response.raise_for_status()
DATABASE = response.json()


@app.route('/')
def home():
    return render_template("index.html", database=DATABASE)


@app.route("/post/<int:blog_id>")
def get_post(blog_id):
    data = DATABASE[blog_id - 1]
    # print(data)
    return render_template("post.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)

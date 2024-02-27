from flask import Flask, render_template, request, redirect

app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    return render_template("index.html", library=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form.get("title")
        author = request.form.get("author")
        rating = request.form.get("rating")
        all_books.append({
            "title": title,
            "author": author,
            "rating": rating
        })
        # print(all_books)
        return redirect("/")
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

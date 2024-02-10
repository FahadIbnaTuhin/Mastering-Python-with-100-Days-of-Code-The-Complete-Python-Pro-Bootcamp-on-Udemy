from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
db = SQLAlchemy(app)

all_books = []


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float(250), nullable=False)


# with app.app_context():
#     # used to create the initial database, no need to execute more than once
#     db.create_all()
#
# with app.app_context():
#     new_book = Book(id=1, title="Fahad", author="Fahad", rating=7.5)
#     db.session.add(new_book)
#
# with app.app_context():
#     db.session.commit()
#     print(Book.query.all())


def check_rating(rating):
    try:
        rating = float(rating)
    except ValueError:
        return None
    else:
        return round(rating, 1)


@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    # something.query.all(), which returns a list of movie objects
    return render_template("index.html", library=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"]
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect("/")
    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        book_id = request.form.get('id')
        book = Book.query.get(book_id)
        book.rating = check_rating(request.form.get('new_rating'))
        db.session.commit()
        return redirect("/")
    book_id = request.args.get('id')
    book = Book.query.get(book_id)
    print(book.title, book.rating)
    return render_template("edit.html", book=book)


@app.route("/delete")
def delete():
    book_id = request.args.get('id')
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField, validators
# import requests

app = Flask(__name__)
app.secret_key = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies-database.db"
db = SQLAlchemy(app)


# class Movie(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(250), unique=True, nullable=False)
#     year = db.Column(db.Integer, nullable=False)
#     description = db.Column(db.String(1000), nullable=False)
#     rating = db.Column(db.Float, nullable=False)
#     ranking = db.Column(db.Integer, nullable=False)
#     review = db.Column(db.String(250), nullable=False)
#     img_url = db.Column(db.String(500), nullable=False)


# with app.app_context():
#     db.create_all()

with app.app_context():
    db.reflect()

# From the default bind key
class Movie(db.Model):
    __table__ = db.metadata.tables["movie"]

with app.app_context():
    new_moive = Movie(
        id=1,
        title="Aladin",
        year=2019,
        description="Aladdin, a kind thief, woos Jasmine, the princess of Agrabah, with the help of Genie. When Jafar, the grand vizier, tries to usurp the king, Jasmine, Aladdin and Genie must stop him from succeeding.",
        rating=6.9,
        ranking=9,
        review="My Favourite Movie",
        img_url="https://www.mamachitchat.com/wp-content/uploads/2019/05/Aladdin-2019-banner.jpg"
    )
    db.session.add(new_moive)

with app.app_context():
    db.session.commit()


@app.route("/")
def home():
    # movies = Movie.query.all()
    # Movie.query.all(), which returns a list of movie objects
    # print(movies[0].title)
    # return render_template("index.html", movies=movies)
    return render_template("select.html")


if __name__ == '__main__':
    app.run(debug=True)

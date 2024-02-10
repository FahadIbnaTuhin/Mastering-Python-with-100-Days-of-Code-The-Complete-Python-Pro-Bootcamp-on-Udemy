from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators
import requests

app = Flask(__name__)
app.secret_key = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies-database.db"
db = SQLAlchemy(app)

# tmdb get api key
MOVIE_DB_API_KEY = "asfasdf"
# https://developers.themoviedb.org/3/search/search-movies
SEARCH_MOVIE_URL = "https://api.themoviedb.org/3/search/movie"
# https://developer.themoviedb.org/reference/movie-details
SEARCH_MOVIE_DETAILS_BY_MOVIE_ID = "https://api.themoviedb.org/3/movie"
PIC_URL = "https://image.tmdb.org/t/p/w500"


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)

# with app.app_context():
#     db.create_all()


class EditForm(FlaskForm):
    rating = StringField("Your rating out of 10 e.g. 7.5", validators=[validators.DataRequired()])
    review = StringField("Your review", validators=[validators.DataRequired()])
    submit = SubmitField("Done")


class AddPageForm(FlaskForm):
    title = StringField("Movie Title", validators=[validators.DataRequired()])
    submit = SubmitField("Add Movie")


# To insert something directly use Sqlite Browser Software because using flask_sqlalchemy it is horrible
# https://www.youtube.com/watch?v=b0Dplx4M5zg
# Don't use this, it sometimes works and sometimes not.
# with app.app_context():
#     new_moive = Movie(
#         id=1,
#         title="Aladin",
#         year=2019,
#         description="Aladdin, a kind thief, woos Jasmine, the princess of Agrabah, with the help of Genie. When Jafar, the grand vizier, tries to usurp the king, Jasmine, Aladdin and Genie must stop him from succeeding.",
#         rating=6.9,
#         ranking=9,
#         review="My Favourite Movie",
#         img_url="https://www.mamachitchat.com/wp-content/uploads/2019/05/Aladdin-2019-banner.jpg"
#     )
#     db.session.add(new_moive)
#
# with app.app_context():
#     db.session.commit()

@app.route("/")
def home():
    # movies = Movie.query.all()
    # Movie.query.all(), which returns a list of movie objects
    # print(movies[0].title)

    movies = Movie.query.order_by(Movie.rating).all()
    print(movies)
    for i in range(len(movies)):
        movies[i].ranking = len(movies) - i
    db.session.commit()
    return render_template("index.html", movies=movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    form = EditForm()
    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        return redirect("/")
    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect("/")


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddPageForm()
    if form.validate_on_submit():
        movie_title = form.title.data

        response = requests.get(SEARCH_MOVIE_URL, params={"api_key": MOVIE_DB_API_KEY, "query": movie_title})
        search_result = response.json()["results"]
        # print(search_result)

        return render_template("select.html", search_result=search_result)
    return render_template("add.html", form=form)


@app.route("/find")
def find_movie():
    movie_id = request.args.get("movie_id")
    if movie_id:
        movie_info = f"{SEARCH_MOVIE_DETAILS_BY_MOVIE_ID}/{movie_id}"

        response = requests.get(url=movie_info, params={"api_key": MOVIE_DB_API_KEY})
        data = response.json()
        print(data)
        pic_url = f"{PIC_URL}{data["poster_path"]}"
        year = data["release_date"].split("-")[0]
        # print(data["original_title"], year, data["overview"], pic_url)


        # Saving data to Database
        new_movie = Movie(
            title=data["original_title"],
            year=year,
            description=data["overview"],
            rating=0,
            ranking=0,
            review="",
            img_url=pic_url
        )
        db.session.add(new_movie)
        db.session.commit()

        # movies = Movie.query.filter_by(title=data["original_title"])
        # return render_template("index.html", movies=movies)

        return redirect(url_for("edit", id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)

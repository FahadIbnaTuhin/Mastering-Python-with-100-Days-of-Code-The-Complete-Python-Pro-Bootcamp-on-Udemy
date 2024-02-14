from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.secret_key = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
# Line below only required once, when creating DB.


# with app.app_context():
#     db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        new_user = User()
        new_user.name = request.form.get("name").title()
        new_user.email = request.form.get("email")
        new_user.password = request.form.get("password")

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("secrets", user_id=new_user.id))

    return render_template("register.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/secrets/<user_id>')
def secrets(user_id):
    user = User.query.get(user_id)
    return render_template("secrets.html", user=user)


@app.route("/download_files")
def download_files():
    # send_from_directory() to download the cheat_sheet.pdf file when the user clicks on the "Download Your File" button
    return send_from_directory("static", path="files/cheat_sheet.pdf")


@app.route('/logout')
def logout():
    print("Hello")
    pass


@app.route('/download')
def download():
    pass


if __name__ == "__main__":
    app.run(debug=True)

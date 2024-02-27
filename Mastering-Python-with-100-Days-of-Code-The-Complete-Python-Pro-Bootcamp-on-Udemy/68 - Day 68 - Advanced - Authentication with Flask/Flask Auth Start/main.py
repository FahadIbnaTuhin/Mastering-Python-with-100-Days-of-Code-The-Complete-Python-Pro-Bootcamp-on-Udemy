from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.secret_key = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Documentation: https://flask-login.readthedocs.io/en/latest/
login_manager = LoginManager()
login_manager.init_app(app)


#  This callback is used to reload the user object from the user ID stored in the session
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


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
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check if the email is associated with another account or not
        if User.query.filter_by(email=request.form.get("email")).first():
            error = "An account is associated with this account. Please Login instead."
            return render_template("register.html", error=error)

        new_user = User()
        new_user.name = request.form.get("name").title()
        new_user.email = request.form.get("email")
        # "pbkdf2:sha256" this is one kind of hash method. Random character won't work
        new_user.password = generate_password_hash(request.form.get("password"), method="pbkdf2:sha256", salt_length=8)

        db.session.add(new_user)
        db.session.commit()

        # Log in and authenticate user after adding details to database.
        login_user(new_user)

        return redirect(url_for("secrets", user_id=new_user.id))

    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if not user:
            error = "That email doesn't exist, please try again."
            return render_template("login.html", error=error)
        elif not check_password_hash(user.password, password):
            error = "Incorrect password. Please try again."
            return render_template("login.html", error=error)
        else:
            login_user(user)
            return redirect(url_for("secrets"))

    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)
    return render_template("secrets.html", name=current_user.name, logged_in=True)


@app.route("/download_files")
@login_required
def download_files():
    # send_from_directory() to download the cheat_sheet.pdf file when the user clicks on the "Download Your File" button
    return send_from_directory("static", path="files/cheat_sheet.pdf")


@app.route('/logout')
def logout():
    logout_user()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

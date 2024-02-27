from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from flask_bootstrap import Bootstrap
# If you use bootstrap library, you don't need to make "base.html". It is from the bootstrap automatically
# https://pythonhosted.org/Flask-Bootstrap/basic-usage.html


app = Flask(__name__)
app.secret_key = "a98sdf6"
Bootstrap(app)


class LoginForm(FlaskForm):
    # Get all field: https://wtforms.readthedocs.io/en/3.1.x/fields/
    email = StringField(label="Email", validators=[validators.DataRequired(message="Please give your email.")])
    password = PasswordField(label="Password", validators=[validators.DataRequired(message="Field Must be atleast 8 characters long.")])
    submit = SubmitField(label="Submit")


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)

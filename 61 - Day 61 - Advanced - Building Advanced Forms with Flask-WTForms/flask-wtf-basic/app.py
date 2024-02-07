# https://www.youtube.com/watch?v=fCAXB9Fz0vI

from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, validators

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"


class ContactForm(FlaskForm):
    name3 = StringField('name', [validators.Length(min=5, max=15,
                                                   message="Please give a input between 5 and 15 characters"),
                                 validators.DataRequired(message="Please enter your name")])
    email = StringField("Email", [validators.DataRequired(message="Please enter your email"),
                                  validators.Email(message="Please enter your email correctly")])
    message = StringField("Message", [validators.DataRequired(message="Please enter a message")])


@app.route("/", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if request.method == "POST" and form.validate():
        return "form submitted successfully"
    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)

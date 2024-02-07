from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.config["SECRET_KEY"] = "secret"


class LOGIN_FORM(FlaskForm):
    # Get all field: https://wtforms.readthedocs.io/en/3.1.x/fields/
    email = StringField(label="Email", validators=[validators.DataRequired()])
    password = PasswordField(label="Password", validators=[validators.DataRequired()])

    submit = SubmitField(label="Log In")


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def get_login():
    login_form = LOGIN_FORM()
    # print(login_form.email.data)
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "123":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)

# Creating or using requirements.txt
# Source: Virtual Environments, in The Hitchhiker’s Guide to Python
# How do you know which Python libraries to install in order to run someone else’s Python project, repo or app? The
# requirements.txt file is the key!

# How to create a requirements.txt file
# If you’re looking to share a project, it’s a good idea to have a record of all the packages used in the project and
# their versions. That way you and anyone else know what packages they need to install to run your project. To do this,
# you’ll want to use a package called pipreqs:
# $ pip install pipreqs

# Afterwards you can generate the requirements.txt file like so:
# $ pipreqs path_to_your_project_folder
# FIT: to install in any directory, just use "pipreqs ./" ./ -> means currect directory
# if you find UnicodeError: use this:  pipreqs --encoding=utf-8 ./

# In Windows Powershell the command you’ll need to run will look like this:
# $python -m  pipreqs.pipreqs path_to_your_project_folder

# “This will create a requirements.txt file, which contains a simple list of all the packages in the current environment
#  and their respective versions. The list is based on the import statements in the project.

# You can see the list of installed packages without the requirements format using pip list. …”

# How to use a requirements.txt file
# “Later it will be easier for a different developer (or you, if you need to re-create the environment) to install the
# same packages using the same versions:

# On Mac
# $ pip3 install -r requirements.txt

# On Windows:
# $ python -m pip install -r requirements.txt

# “This can help ensure consistency across installations, across deployments, and across developers.” You will see a
# requirements.txt file in many GitHub repos. If you want to run the code in such a repo:

# Set up a new virtual environment inside the cloned or downloaded repo’s master folder. (See “Create a new virtual
# environment with Python3” in this document if you forgot how to do this.)
# Activate that virtualenv.
# Then run the pip3 install command shown above. It will install everything listed in the requirements.txt file — using
# the correct version number for each package. That’s very important! And handy!

# Bitlink: http://bit.ly/python-reqs

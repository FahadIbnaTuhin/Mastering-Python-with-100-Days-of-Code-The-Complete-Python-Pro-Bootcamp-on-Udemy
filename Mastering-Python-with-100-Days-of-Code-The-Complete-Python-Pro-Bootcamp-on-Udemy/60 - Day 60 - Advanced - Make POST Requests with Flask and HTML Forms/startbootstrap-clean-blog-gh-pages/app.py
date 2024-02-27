# Clone of this website: https://startbootstrap.com/previews/clean-blog
from flask import Flask, render_template, request
import requests
import smtplib

MY_EMAIL = "asdf@gmail.com"
MY_PASSWORD = "asdf"

app = Flask(__name__)

response = requests.get(url="https://api.npoint.io/11d4e811eacf47e14ead")
response.raise_for_status()
data = response.json()


@app.route("/")
def index():

    return render_template("index.html", data=data)


@app.route("/about")
def get_about():
    return render_template("about.html")


@app.route("/post/<int:number>")
def get_post(number):
    print(number)
    return render_template("post.html", data=data[number - 1])


@app.route("/contact", methods=["GET", "POST"])
def get_contact():
    if request.method == "POST":
        user_details = {
            "name": request.form.get("name"),
            "email": request.form.get("email"),
            "phone": request.form.get("phone", "Not Provided"),
            "message": request.form.get("message")
        }
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="asdf@gmail.com",
                msg=f"Subject: Message from Fahad's Blog!\n\nName: {user_details['name']}\nEmail: {user_details['email']}\n"
                    f"Phone: {user_details['phone']}\nMessage: {user_details["message"]}"
            )
        return render_template("contact.html", msg=True)
    return render_template("contact.html", msg=False)


# @app.route("/form-entry", methods=["GET", "POST"])
# def get_form_entry():
#     if request.method == "POST":
#         name, email, phone, msg = (request.form.get("name"), request.form.get("email"), request.form.get("phone"),
#                                    request.form.get("msg"))
#         # print(name, email, phone, msg)
#
#         return f"<h1>Successfully sent your message.</h1>"
#     return f"HI"


if __name__ == "__main__":
    app.run(debug=True)

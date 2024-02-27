from flask import Flask, jsonify, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


# with app.app_context():
#     db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# http://127.0.0.1:5000/random
@app.route("/random")
def route():
    cafes = db.session.query(Cafe).all()
    # print(cafes)
    random_cafe = random.choice(cafes)
    # https://www.kite.com/python/docs/flask.jsonify

    return jsonify(cafe={
        "id": random_cafe.id,
        "name": random_cafe.name,
        "map_url": random_cafe.map_url,
        "img_url": random_cafe.img_url,
        "location": random_cafe.location,
        "amenities":  {
            "seats": random_cafe.seats,
            "has_toilet": random_cafe.has_toilet,
            "has_wifi": random_cafe.has_wifi,
            "has_sockets": random_cafe.has_sockets,
            "can_take_calls": random_cafe.can_take_calls,
            "coffee_price": random_cafe.coffee_price
        }
    })
    # return redirect("/")


# # http://127.0.0.1:5000/all
@app.route("/all")
def get_all():
    cafes = Cafe.query.all()
    # print(cafes)

    cafes_list = []
    for i in cafes:
        cafes_list.append({
            "id": i.id,
            "name": i.name,
            "map_url": i.map_url,
            "img_url": i.img_url,
            "location": i.location,
            "amenities": {
                "seats": i.seats,
                "has_toilet": i.has_toilet,
                "has_wifi": i.has_wifi,
                "has_sockets": i.has_sockets,
                "can_take_calls": i.can_take_calls,
                "coffee_price": i.coffee_price
            }
        })
    # print(cafes_list)
    # return redirect("/")
    return jsonify(cafes=cafes_list)


# http://127.0.0.1:5000/search?loc=Peckham
# As you can imagine, if you need to test your API with a bunch of parameters, it can quickly get tiring typing them
# all out in the URL bar of your browser. It's also super error-prone. So how do developers test their APIs? One of the
# best tools is Postman. Download Postman: https://www.postman.com/downloads/
@app.route("/search")
def search():
    loc = request.args.get("loc")
    cafes = Cafe.query.filter_by(location=loc).all()
    # print(cafes)

    if len(cafes) != 0:
        cafes_list = []
        for i in cafes:
            cafes_list.append({
                "id": i.id,
                "name": i.name,
                "map_url": i.map_url,
                "img_url": i.img_url,
                "location": i.location,
                "amenities": {
                    "seats": i.seats,
                    "has_toilet": i.has_toilet,
                    "has_wifi": i.has_wifi,
                    "has_sockets": i.has_sockets,
                    "can_take_calls": i.can_take_calls,
                    "coffee_price": i.coffee_price
                }
            })
        return jsonify(cafes=cafes_list)
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})
    # print(cafes_list)
    # return redirect("/")


# http://127.0.0.1:5000/add
@app.route("/add", methods=["POST"])
def add():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        seats=request.form.get("seats"),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        has_sockets=bool(request.form.get("has_sockets")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        coffee_price=request.form.get("coffee_price")
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe"})


# If they knew the id of the cafe (which they can get by making a GET request to fetch data on all the cafes), then they
# can update the coffee_price field of the cafe. In this situation, a PATCH request is probably more efficient, as we
# don't need to change any of the rest of the cafe's data. Create a PATCH request route in target.py to handle PATCH
# requests to our API. In order for our API to be RESTful, ideally, the route should be something like this:
# /update-price/<cafe_id>
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    if cafe is not None:
        cafe.coffee_price = request.args.get("new_price")
        db.session.commit()
        # print(cafe.coffee_price)
        return jsonify(response={"success": "Successfully Updated the price."}), 200
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


@app.route("/report-closed/<int:cafe_id>", methods=["GET", "POST"])
def delete(cafe_id):
    api_key = "BOOM"

    if request.args.get("api_key") == api_key:
        cafe = Cafe.query.get(cafe_id)
        print(cafe)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"Success": "Successfully removed the cafe."}), 200
        else:
            return jsonify(error={"Not Found": "There is no cafe with the provided id."}), 404
    return jsonify(error={"Unauthorized": "You are not authorized to perform this operation."}), 403
    # return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)

# https://documenter.getpostman.com/view/32800275/2sA2r3YkX1

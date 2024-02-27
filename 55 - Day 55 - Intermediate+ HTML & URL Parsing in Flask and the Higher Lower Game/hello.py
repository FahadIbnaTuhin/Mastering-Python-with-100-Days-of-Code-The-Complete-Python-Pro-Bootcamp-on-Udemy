from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello"


@app.route("/bye")
def bye():
    return "Bye"


# @app.route("/username/<name>/10")
# def great(name):
#     return f"Hello there {name + '12'}!"


# If you want to take slash("/") as input in the url, then use "path" in route
# use this as a input "http://127.0.0.1:5000/fahad/10/dhaka/bangladesh"
# @app.route("/<path:name>")
# def great(name):
#     return f"Hello there {name}!"


# at the end must be this number
# http://127.0.0.1:5000/username/fahad/sima/bangladesh/20.30
@app.route("/username/<path:name>/<float:number>")
def great(name, number):
    return f"Hello there {name}, you are {number} years old!"


if __name__ == "__main__":
    app.run(debug=True)


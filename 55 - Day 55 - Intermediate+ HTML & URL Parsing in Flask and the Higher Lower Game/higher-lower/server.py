from flask import Flask
import random

random_num = random.randint(0, 9)

app = Flask(__name__)


@app.route("/")
def index():
    return (f'<h1>Guess a number between 0 and 9</h1>'
            f'<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="Guess" width=300px>'
            f'<br>Answer: {random_num}')


@app.route("/<int:number>")
def guess(number):
    if number > random_num:
        return (f'<h1 style="color: blue">Too High</h1>'
                f'<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" alt="Guess" width=300px>')
    elif number < random_num:
        return (f'<h1 style="color: red">Too Low</h1>'
                f'<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" alt="Guess" width=300px>')
    else:
        return (f"<h1 style='color: green'>You're right</h1>"
                f'<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" alt="Correct Guess" width=300px>')


if __name__ == "__main__":
    app.run(debug=True)

# Get free templates from here: https://html5up.net/
# To change anything from the browser live, write this down to console inside browser develooper tool
# document.body.contentEditable=true
# To use that edit as parmanent, download that page using CTRL+S, then copy that code from there
# and replace that code here in index.html. Then, you have to change src, href again

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, TimeField, SelectField
import csv

app = Flask(__name__)
app.secret_key = '8BYkEfBA6O6donWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[validators.DataRequired()])
    location = StringField('Cafe Location on Google Maps (URL)', validators=[validators.DataRequired(),
                                                                             validators.URL()])
    opening_time = TimeField("Opening Time e.g. 8AM", validators=[validators.DataRequired()])
    closing_time = TimeField("Closing Time e.g. 5:30PM", validators=[validators.DataRequired()])
    coffee_rating = SelectField("Coffee Rating", choices=["☕️", "☕️☕️", "☕️☕️☕️", "☕️☕️☕️☕️", "☕️☕️☕️☕️☕️"],
                                validators=[validators.DataRequired()])
    wifi_rating = SelectField("Wifi Strength Rating", choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪",
                                            "💪💪💪💪💪"], validators=[validators.DataRequired()])
    power_rating = SelectField("Power Socket Availiability", choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌",
                                    "🔌🔌🔌🔌🔌"], validators=[validators.DataRequired()])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open("./cafe-data.csv", "a", encoding="utf-8") as csv_file:
            csv_file.write(f"\n{form.cafe.data},"
                           f"{form.location.data},"
                           f"{form.opening_time.data},"
                           f"{form.closing_time.data},"
                           f"{form.coffee_rating.data},"
                           f"{form.wifi_rating.data},"
                           f"{form.power_rating.data}")
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding="utf-8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
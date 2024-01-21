from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "x@gmail.com"
MY_PASSWORD = "asdfasdf"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(row["month"], row["day"]): row for (index, row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person_row = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person_row["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person_row["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )

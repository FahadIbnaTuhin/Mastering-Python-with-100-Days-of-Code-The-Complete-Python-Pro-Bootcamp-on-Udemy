import datetime as dt
import pandas
import random
import smtplib

my_email = "x@gmail.com"
password = "asdfasdfasd"

# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")
container = data.to_dict(orient="records")
# print(container)

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
for row in container:
    if row["day"] == now.day and row["month"] == now.month:
        # print("Yes")

        # Choose Random Letter
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter_file:
            letter = letter_file.read().replace("[NAME]", row["name"])
            # print(letter)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()

            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=row["email"],
                msg=f"Subject: Happy Birthday {row["name"]}\n\n{letter}"
            )

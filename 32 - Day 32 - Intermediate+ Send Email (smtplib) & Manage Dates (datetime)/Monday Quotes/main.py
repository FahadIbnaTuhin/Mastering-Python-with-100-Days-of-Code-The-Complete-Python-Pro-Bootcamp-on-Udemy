import datetime as dt
import random
import smtplib

# For testing first make sure which date it is then try with this and at the end change it
# If it is Monday, send random quote
if dt.datetime.now().weekday() == 6:
    my_email = "x@gmail.com"
    password = "mcjasdfasdf"

    with open("quotes.txt", "r") as quote_file:
        quote = quote_file.readlines()
        # quote = [row for row in quote_file]

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()

        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="y@yahoo.com",
            msg=f"Subject:Monday Motivation\n\n{random.choice(quote)}"
        )

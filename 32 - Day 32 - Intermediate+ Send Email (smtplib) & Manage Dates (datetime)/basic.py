# import smtplib
#
# my_email = "x@gmail.com"
# # Get your mail app password and paste it here
# password = "fwrasdfsdfsdfasfsdf"
#
# # SMTP: Simple Mail Transfer Protocol. Search on google for your mail provider to get their smtp
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     # TLS:Transport Layer Security
#     # It's way of securing our connection to our email server. This line makes the connection secure.
#     # No middleman can see this if you use this
#
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="x@yahoo.com",
#         msg="Subject:Hello\n\nThis is the body of the email"
#     )
#
# # Google: smtp.gmail.com
# # Yahoo: smtp.mail.yahoo.com
import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
print(year, month, day)

time = now.time()
print(time)

day_of_week = now.weekday()
print(day_of_week)
# Tuesday = 1, ....... Monday = 7


birth = dt.datetime(2003, 12, 30, 5)
print(birth)
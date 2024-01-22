from datetime import datetime

today = datetime.now()

# formatted_time = today.strftime("%d/%m/%Y, %H:%M:%S %p")
# print(formatted_time)
# %Y = 2024, %y = 24
# %H represents the hour in 24-hour format and %I represents the hour in 12-hour format

formatted_time = today.strftime("Date/Month/Year: %d/%m/%y\n\nHour:Minute:Second: %I:%M:%S %p")
# %M represents the minute, %S represents the sec
# and %p represents either AM or PM.
print(formatted_time)

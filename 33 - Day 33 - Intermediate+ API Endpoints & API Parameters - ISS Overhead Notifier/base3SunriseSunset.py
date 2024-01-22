from datetime import datetime
import requests

MY_LAT = 24.070032
MY_LONG = 89.113419

# Webpage: https://sunrise-sunset.org/api
# 1st way:
# data = requests.get(url=f"https://api.sunrise-sunset.org/json?lat={MY_LAT}&lng={MY_LONG}")

# 2nd Way:
# Know the parameter from the api documentation. Here lat and lng is required. Others are optional, so if you want you
# can use those also but not mandatory
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}
# "formatted" is optional and by default it's value is 1 which is 12 hours format. But for 24-hour format we selected 0
data = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)


data.raise_for_status()

data_json = data.json()
print(data_json)
sunrise = data_json["results"]["sunrise"]
sunset = data_json["results"]["sunset"]

print(sunrise)
# print(sunset)

# We did this one by one, getting and applying
sunrise_hour = sunrise.split("T")[1].split(":")[0]
sunset_hour = sunset.split("T")[1].split(":")[0]

print(sunrise_hour, sunset_hour)

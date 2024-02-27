# WEBPAGE: https://openweathermap.org/price
# On the free plan, you can see what things you can use. Right now, these two links are showing and working
# Current Weather, 3-hour Forecast 5 days on first row
# In the api section, at the end of every feature, you can see whether it supports free or not

import requests

MY_API_KEY = "asdfasdf"

weather_params = {
    "lat": 4.882950,
    "lon": 101.965691,
    "appid": MY_API_KEY,
    "units": "metric"
}
# For temperature in Celsius use units=metric

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data)

# print(weather_data["list"][0]["weather"][0]["id"])
# From the api documentation, if the weather id number is less than 700, it means there will be snow or rain.
# For both, you think you should take your umbrella

weather_slice = weather_data["list"][:5]
# print(weather_slice)

will_rain = False
for hour_after3 in weather_slice:
    if hour_after3["weather"][0]["id"] < 700:
        will_rain = True
        break

if will_rain:
    print("Bring an Umbrella")

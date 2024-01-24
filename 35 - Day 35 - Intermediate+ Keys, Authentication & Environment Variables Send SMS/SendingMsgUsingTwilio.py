import requests
import os
from twilio.rest import Client

account_sid = os.environ['asdfasdfasdf']
auth_token = os.environ['asdfasdfasdfsdf']

MY_API_KEY = "asdfasdfadsfasdf"

weather_params = {
    "lat": 55.676098,
    "lon": 12.568337,
    "appid": MY_API_KEY,
    "units": "metric"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data)

weather_slice = weather_data["list"][:5]
# print(weather_slice)

will_rain = False
for hour_after3 in weather_slice:
    if hour_after3["weather"][0]["id"] < 700:
        will_rain = True
        break

if will_rain:
    client = Client(account_sid, auth_token)

    client.api.account.messages.create(
        to="asdfasdf",
        from_="asdf",
        body="It's going to rain today. Remember to take an umbrella."
    )

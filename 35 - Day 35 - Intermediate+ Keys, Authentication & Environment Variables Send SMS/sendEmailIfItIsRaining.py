import os
import requests
import smtplib
import html

# MY_API_KEY = "asdfasdfasdf"
# USER_EMAIL = "asdfasdf"
# USER_PASSWORD = "asdfasdfasdf"

MY_API_KEY = os.environ.get("MY_API_KEY")
USER_EMAIL = "fahadibnatuhin4471@gmail.com"
USER_PASSWORD = os.environ.get("USER_PASS")

weather_params = {
    "lat": 55.676098,
    "lon": 12.568337,
    "appid": MY_API_KEY
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
    # print("Raining")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=USER_EMAIL, password=USER_PASSWORD)
        connection.sendmail(
            from_addr=USER_EMAIL,
            to_addrs="fahadtuhin2@gmail.com",
            msg="Subject: It's going to rain today. FAHAD\n\nRemember to take an umbrella ."
        )

import html

import requests
import smtplib

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

STOCK_API_KEY = "Wasdfasdf"
NEWS_API_KEY = "asfasdfasdf"

USER_EMAIL = "fahadibnatuhin4471@gmail.com"
USER_PASSWORD = "asdfasdf"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}
response_stock = requests.get(url=STOCK_ENDPOINT, params=stock_params)
response_stock.raise_for_status()
stock_data = response_stock.json()["Time Series (Daily)"]
# print(stock_data)
data_list = [value for (key, value) in stock_data.items()]
# print(data_list)

yesterday_closing_price, the_day_before_yesterday_closing_price = data_list[0]["4. close"], data_list[1]["4. close"]
# print(yesterday_closing_price, the_day_before_yesterday_closing_price)

difference = float(yesterday_closing_price) - float(the_day_before_yesterday_closing_price)
print(difference)

upDown = None
if difference > 0:
    upDown = "⬆️"
else:
    upDown = "⬇️"

diff_percent = (difference / float(the_day_before_yesterday_closing_price)) * 100
print(diff_percent)

if abs(diff_percent) > 0.5:
    news_params = {
        "q": STOCK_NAME,
        "apiKey": NEWS_API_KEY
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_data = news_response.json()["articles"]
    # print(news_data)
    three_articles = news_data[:3]
    # print(three_articles)
    for item in three_articles:
        headline = html.unescape(item["title"])
        description = html.unescape(item["description"])
        print(f"Headline: {headline} & Description: {description}")

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()

            connection.login(user=USER_EMAIL, password=USER_PASSWORD)
            connection.sendmail(
                from_addr=USER_EMAIL,
                to_addrs="fahadtuhin2@gmail.com",
                msg=f"Subject: {headline}\n\n{description}"
            )

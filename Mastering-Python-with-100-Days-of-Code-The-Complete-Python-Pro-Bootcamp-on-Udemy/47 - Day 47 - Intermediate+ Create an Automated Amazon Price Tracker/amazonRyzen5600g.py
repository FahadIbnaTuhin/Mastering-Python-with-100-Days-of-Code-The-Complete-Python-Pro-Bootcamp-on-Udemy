from bs4 import BeautifulSoup
import requests
import smtplib

USER_EMAIL = "fahadibnatuhin4471@gmail.com"
USER_PASSWORD = "asdfasdfasdf"

response = requests.get(url="https://www.amazon.com/AMD-Ryzen-5600G-12-Thread-Processor/dp/B092L9GF5N?th=1")
contents = response.text

soup = BeautifulSoup(contents, "html.parser")

price = int(soup.find("span", class_="a-price-whole").getText().replace(".", ""))

if price < 116:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=USER_EMAIL, password=USER_PASSWORD)
        connection.sendmail(
            from_addr=USER_EMAIL,
            to_addrs="fahadtuhin2@gmail.com",
            msg=f"Subject: Ryzen 5 5600G Price Alert\n\n"
                f"The product price is now ${price}, below your target price. Buy now!"
        )

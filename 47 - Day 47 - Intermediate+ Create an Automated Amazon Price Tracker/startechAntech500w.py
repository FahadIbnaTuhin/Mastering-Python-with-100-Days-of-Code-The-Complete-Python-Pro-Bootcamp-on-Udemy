from bs4 import BeautifulSoup
import requests
import smtplib

USER_EMAIL = "fahadibnatuhin4471@gmail.com"
USER_PASSWORD = "asdfasdfasfd"

response = requests.get(url="https://www.startech.com.bd/antec-meta-v550-power-supply")
contents = response.text

soup = BeautifulSoup(contents, "html.parser")

price = int(soup.find("td", class_="product-info-data product-price").getText().replace(",", "").replace("৳", ""))

if price <= 3000:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=USER_EMAIL, password=USER_PASSWORD)
        connection.sendmail(
            from_addr=USER_EMAIL,
            to_addrs="fahadtuhin2@gmail.com",
            msg=f"Subject: Antec META V550 550W PSU Alert\n\n"
                f"The product price is now ${price}, below your target price. Buy now!"
        )

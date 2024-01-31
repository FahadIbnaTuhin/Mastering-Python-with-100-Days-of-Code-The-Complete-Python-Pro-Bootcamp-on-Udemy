# https://chromedriver.chromium.org/downloads
# webdriver will drive the chrome browser and do the automatic task
# just go to pypi->webdriver_manager and download code for chrome from there phrase 4

# This webdriver_manager library will automatically check which chrome you are using and based on that,
# download the perfect webdriver automatically for you. But required internet connection everytime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# driver.get("https://www.google.com")
driver.get("file:///F:/FIT%20Programming/W3Schools%20Latest%20Version/W3Schools%20Latest%20Version/index.html")


time.sleep(5)

# close() just close the active particular tab
driver.close()
# quit() close the entire browser
# driver.quit()



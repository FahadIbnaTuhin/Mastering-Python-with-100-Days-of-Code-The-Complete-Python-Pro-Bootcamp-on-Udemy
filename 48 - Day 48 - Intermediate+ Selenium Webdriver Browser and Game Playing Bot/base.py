# https://chromedriver.chromium.org/downloads
# webdriver will drive the chrome browser and do the automatic task
# just go to pypi->webdriver_manager and download code for chrome from there phrase 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.google.com")


# close() just close the active particular tab
driver.close()
# quit() close the entire browser
# driver.quit()



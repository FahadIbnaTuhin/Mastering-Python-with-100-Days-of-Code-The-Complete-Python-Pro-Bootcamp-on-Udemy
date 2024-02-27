from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

articles_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# print(articles_count.text)
# articles_count.click()

view_sources = driver.find_element(By.LINK_TEXT, "View source")
# view_sources.click()

search = driver.find_element(By.NAME, "search")
search.clear()
search.send_keys("Fahd of Saudi Arabia", Keys.ENTER)


time.sleep(5)
driver.quit()

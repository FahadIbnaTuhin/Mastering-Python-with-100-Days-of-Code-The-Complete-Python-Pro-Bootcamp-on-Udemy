from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(By.NAME, "fName")
fname.send_keys("MD. Fahad")

lname = driver.find_element(By.NAME, "lName")
lname.send_keys("Islam")

email = driver.find_element(By.NAME, "email")
email.send_keys("fahad@gmail.com")

submit = driver.find_element(By.CSS_SELECTOR, ".form-signin button")
submit.click()

time.sleep(5)
driver.quit()

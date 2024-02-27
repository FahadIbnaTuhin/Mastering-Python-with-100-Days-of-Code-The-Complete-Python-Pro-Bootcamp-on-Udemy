# https://chromedriver.chromium.org/downloads from this download you chromedriver based on your current chrome version

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://google.com")
# driver.get("file:///F:/FIT%20Programming/W3Schools%20Latest%20Version/W3Schools%20Latest%20Version/index.html")


# This will allow us again to wait for the presence of the element before we go forward we don't run any issue if what
# we're looking for it doesn't yet exist. Shortcut: after 5 secs, if the element doesn't exist, go ahead and crash the
# program
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
# Clear is good, because there can be text sometimes
input_element.clear()
# Below just do appending
input_element.send_keys("Fahad Ibna Tuhin Official", Keys.ENTER)


WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Fahad Ibna Tuhin Official"))
)
link = driver.find_element(By.PARTIAL_LINK_TEXT, "Fahad Ibna Tuhin Official")
link.click()

time.sleep(5)
driver.quit()

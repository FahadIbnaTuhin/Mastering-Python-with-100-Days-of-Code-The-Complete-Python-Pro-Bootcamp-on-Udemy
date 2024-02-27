from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

USER_EMAIL = "fasdfasdf@gmail.com"
USER_PASSWORD = "asdfasdfasdf"

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3784512795&geoId=106215326&keywords=Executive%20%E2%80%93%20Digital%20Marketing%20(SP%20%26%20IELTS%20Bangladesh)&location=Bangladesh&origin=JOBS_HOME_LOCATION_HISTORY&refresh=true")
driver.maximize_window()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/section/div[2]/section/div/div[1]/div/div/button[1]"))
)
apply = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/div[2]/section/div/div[1]/div/div/button[1]")
apply.click()

agree = driver.find_element(By.CLASS_NAME, 'main__sign-in-link')
agree.click()

email = driver.find_element(By.ID, "username")
email.send_keys(USER_EMAIL)

password = driver.find_element(By.ID, "password")
password.send_keys(USER_PASSWORD)

signIn = driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in")
signIn.click()


time.sleep(10000000)
driver.quit()

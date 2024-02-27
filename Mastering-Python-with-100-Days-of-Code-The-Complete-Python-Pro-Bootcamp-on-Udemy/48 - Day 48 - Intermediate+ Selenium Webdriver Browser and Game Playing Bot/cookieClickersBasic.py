from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")

end_time = time.time() + 5 * 60

# amount full xpath: '/html/body/div[3]/div[5]/div/div[i]/b'
# div full xpath: '/html/body/div[3]/div[5]/div/div[i]'
path = '/html/body/div[3]/div[5]/div/div['
while time.time() < end_time:
    cookie.click()
    money = int(driver.find_element(By.ID, "money").text)
    # print(money)

    for i in range(1, 9):
        amount = driver.find_element(By.XPATH, path + str(i) + ']/b').text.split(" ")[2].replace(",", "")
        # print(str(amount))

        if not amount.isdigit():
            continue

        if money >= int(amount):
            item = driver.find_element(By.XPATH, path + str(i) + ']')
            item.click()
            break

cps = driver.find_element(By.ID, "cps").text.split(" ")[2]
driver.quit()
print(cps)

# 5 mins - 13.6

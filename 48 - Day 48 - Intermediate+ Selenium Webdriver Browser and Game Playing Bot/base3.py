from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# driver.get("https://www.amazon.com/AMD-Ryzen-5600G-12-Thread-Processor/dp/B092L9GF5N")
driver.get("https://python.org")

# price = driver.find_element(By.CLASS_NAME, "a-price-whole").text
# print(price)

# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)

# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)

# xpath is unique for everyone. Go to Inspect, Select the tag then right-click on the tag, then copy -> then xpath.
# before and after use '' because inside is "" here
# bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)


# ------------------------------------------- Upcoming Events Start ---------------------------------------------------
# 1st way -- Not efficient because every loop searching for something
xpath = '//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li'
data = {}
for i in range(1, 6):
    time = driver.find_element(By.XPATH, xpath + str([i]) + '/time').text
    name = driver.find_element(By.XPATH, xpath + str([i]) + '/a').text
    data[i] = {'time': time, 'name': name}
print(data)

# 2nd way - Efficient because stored allthing in 2 times and using the exact xpath
# '//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[1]/time' here we cut the [1],so it can collect all li/time now
# times = [time.text for time in driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li/time')]
# names = [name.text for name in driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li/a')]
# # print(times)
# # print(names)
#
# events = {}
# for i in range(len(times)):
#     events[i] = {
#     "time": times[i],
#     "name": names[i]
#     }
# print(events)

# 3rd way from the video solution - Efficient also
# times = [time.get_attribute("datetime") for time in driver.find_elements(By.CSS_SELECTOR, ".event-widget time")]
# names = [name.text for name in driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")]
# # print(times)
# # print(names)
#
# events = {}
# for i in range(len(times)):
#     events[i] = {
#         "time": times[i],
#         "name": names[i]
#     }
# print(events)
# ------------------------------------------- Upcoming Events End ---------------------------------------------------


driver.quit()

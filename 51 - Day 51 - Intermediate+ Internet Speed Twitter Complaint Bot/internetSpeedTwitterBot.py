from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class InternetSpeedTwitterBot:
    def __init__(self, data):
        service = Service(executable_path="chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        self.user_speeds = data
        self.current_speeds = self.get_internet_speed()

    def tweet_at_provider(self):
        msg = (f"Hey @comcast why is my internet speed {self.user_speeds['down']}down'\'{self.user_speeds['up']}up when"
               f" I pay for {self.current_speeds["down"]}down'\'{self.current_speeds["up"]}up in Washington DC?"
               f" @comcastbusiness  @Xfinity #comcast #speedtest")

        import os
        from dotenv import load_dotenv
        load_dotenv()
        from selenium.webdriver.common.keys import Keys

        self.driver.get("https://twitter.com/i/flow/login")
        self.driver.maximize_window()

        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.NAME, "text"))
        )
        user_email = self.driver.find_element(By.NAME, "text")
        user_email.send_keys(os.getenv("USER_EMAIL"))
        # time.sleep(2)
        user_email.send_keys(Keys.ENTER)

        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.NAME, "text"))
        )
        user_name = self.driver.find_element(By.NAME, "text")
        user_name.clear()
        user_name.send_keys(os.getenv("USER_NAME"))
        # time.sleep(2)
        user_name.send_keys(Keys.ENTER)

        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        user_name = self.driver.find_element(By.NAME, "password")
        user_name.clear()
        user_name.send_keys(os.getenv("USER_PASS"))
        # time.sleep(2)
        user_name.send_keys(Keys.ENTER)

        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "public-DraftStyleDefault-ltr"))
        )
        post_content = self.driver.find_element(By.CLASS_NAME, "public-DraftStyleDefault-ltr")
        post_content.send_keys(msg)
        time.sleep(2)

        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH,
                                            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/'
                                            'div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]'))
        )
        final_post = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/'
                            'div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]')
        final_post.click()

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        go = self.driver.find_element(By.CLASS_NAME, "js-start-test")
        go.click()

        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.CLASS_NAME, "download-speed"))
        )
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.CLASS_NAME, "upload-speed"))
        )
        while (not self.driver.find_element(By.CLASS_NAME, "download-speed").text.replace(".", "")
                .isdigit() or not self.driver.find_element(By.CLASS_NAME, "upload-speed").text.
                replace(".", "").isdigit()):
            continue
        dspeed = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        uspeed = self.driver.find_element(By.CLASS_NAME, "upload-speed").text
        result = {"down": float(dspeed), "up": float(uspeed)}
        return result

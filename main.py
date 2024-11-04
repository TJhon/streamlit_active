from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from tqdm import tqdm
from datetime import datetime

fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
button_active = '//*[@id="root"]/div[1]/div/div/div/div/button'

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.binary_location = "/usr/bin/chromium-browser"


class KeepActive:
    def __init__(self, url_file="./projects_url.txt", logs="./logs_actives/log.txt"):
        self.url_file = url_file
        self.log = logs
        self.driver = webdriver.Chrome(options=options)
        self.read_urls()

    def read_urls(self):
        with open(self.url_file, "r") as archivo:
            urls = [linea.strip() for linea in archivo]
        self.urls = urls
        return self

    @staticmethod
    def active_app(driver, url: str, time_exists=2):
        driver.get(url)
        time.sleep(time_exists)
        try:
            driver.find_element(By.XPATH, button_active).click()
            time.sleep(100)
        except:
            time.sleep(time_exists)

    def keep_actives(self):
        driver = self.driver
        urls = self.urls
        for url in tqdm(urls):
            self.active_app(driver, url)
        print("Done")
        driver.quit()
        with open(self.log, "a") as f:
            f.write(f"{fecha_actual} - done\n")
        return self.url_file


urls = KeepActive().keep_actives()

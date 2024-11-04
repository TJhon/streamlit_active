from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Inicializar el navegador Edge
driver = webdriver.Edge()

driver.get("https://perusismosdata.streamlit.app/Sismos_Reporte_Detallado")

time.sleep(10)

button = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div/div/div/button')
button.click()


time.sleep(100)

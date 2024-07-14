from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://google.com")

    input_element = driver.find_element(By.NAME, "q")
    input_element.clear()
    input_element.send_keys("FC Barcelona")
    input_element.send_keys(Keys.RETURN)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "FC Barcelona")))

    link = driver.find_element(By.PARTIAL_LINK_TEXT, "FC Barcelona")
    link.click()

    time.sleep(5)

finally:
    driver.quit()

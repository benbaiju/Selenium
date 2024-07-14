from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    driver.get("https://orteil.dashnet.org/cookieclicker/")

    english_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "langSelect-EN"))
    )
    english_button.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "bigCookie"))
    )

    cookie_button = driver.find_element(By.ID, "bigCookie")

    for _ in range(10):
        cookie_button.click()
        time.sleep(0.2)

    while True:
        cookie_button.click()
        cookies_count = driver.find_element(By.ID, "cookies").text.split(" ")[0]
        cookies_count = int(cookies_count.replace(",", ""))

        for i in range(4):
            product_price_element = driver.find_element(By.ID, "productPrice" + str(i))
            product_price = int(product_price_element.text.replace(",", "").split(" ")[0])

            if cookies_count >= product_price:
                product = driver.find_element(By.ID, "product" + str(i))
                product.click()
                break

        time.sleep(1)

finally:
    driver.quit()

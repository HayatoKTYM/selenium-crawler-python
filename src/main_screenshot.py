import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

time.sleep(10)

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument('--disable-gpu')
options.add_argument('--disable-extensions')
options.add_argument("--disable-infobars")
options.add_argument("--no-sandbox")
options.add_argument('--start-maximized')
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Remote("http://selenium:4444/wd/hub", options=options)

driver.get('https://hayatoktym.github.io/sample-github-pages/#/dashboard')

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "card"))
    )
    element.screenshot('element_screenshot.png')
finally:
    driver.quit()



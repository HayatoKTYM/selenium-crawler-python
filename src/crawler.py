from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from io import BytesIO


class Crawler:
    def __init__(self, url, target_class_name):
        self.url = url
        self.target_class_name = target_class_name
        self.driver = self._setup_driver()

    @staticmethod
    def _setup_driver():
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-extensions')
        options.add_argument("--disable-infobars")
        options.add_argument("--no-sandbox")
        options.add_argument('--start-maximized')
        options.add_argument("--disable-dev-shm-usage")
        return webdriver.Chrome(options=options)

    def crawl(self, screenshot_name=None):
        self.driver.get(self.url)
        byte_data = None

        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, self.target_class_name))
            )
            if screenshot_name:
                element.screenshot(screenshot_name)
            else:
                png = element.screenshot_as_png
                byte_data = BytesIO(png)
        finally:
            self.driver.quit()
        return byte_data

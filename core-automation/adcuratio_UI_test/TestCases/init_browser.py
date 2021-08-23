import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

class Browser:

    def chrome_browser(self):
        self.web_driver = webdriver.Chrome(executable_path='../../Utils/chromedriver')
        return self.web_driver

    def get_ele_by_xpath(self, locators):
        wait = WebDriverWait(self.web_driver, 20)
        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, locators)))
            return element
        except Exception as ex:
            print("Exception has been thrown. " + str(ex))

    def get_page_title(self):
        return self.web_driver.title


class SERVER:
    TEST_SERVER_URL = ""
    LOCAL_SERVER_URL = "http://localhost:8080/"








import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    FFdriverloc = 'E:\\Python\\lib\\geckodriver'
    driver = webdriver.Firefox(executable_path=FFdriverloc)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
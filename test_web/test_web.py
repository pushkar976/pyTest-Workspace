import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture
def browser():
    FFdriverloc = 'E:\\Python\\lib\\geckodriver'
    driver = webdriver.Firefox(executable_path=FFdriverloc)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_basic_duckduckgo_search(browser):
    URL = 'https://www.duckduckgo.com'
    PHRASE = 'panda'

    browser.get(URL)

    search_input = browser.find_element_by_id('search_form_input_homepage')
    search_input.send_keys(PHRASE + Keys.RETURN)

    link_divs = browser.find_elements_by_css_selector('#links > div')
    print("Link : ",str(link_divs))
    assert len(link_divs) > 0

    xpath = f"//div[@id='links']//*[contains(text(), '{PHRASE}')]"
    results = browser.find_elements_by_xpath(xpath)
    assert len(results) > 0

    search_input = browser.find_element_by_id('search_form_input')
    assert search_input.get_attribute('value') == PHRASE


def test_flipkart(browser):

    myDataFile = open("C:/Users/admin/Desktop/loginData.txt","r")
    contents = myDataFile.readline().split()
    print(contents)

    userID = contents[0]
    pass_word = contents[1]

    url = "https://www.flipkart.com"

    browser.get(url)
    flipLogin = browser.find_element_by_css_selector('input[class="_2zrpKA _1dBPDZ"]')
    flipLogin.send_keys(userID)
    assert flipLogin.get_attribute('value') == '8147070507'
    time.sleep(1)

    flipPass = browser.find_element_by_css_selector('input[type=password]')
    flipPass.send_keys(pass_word)
    assert flipPass.get_attribute('value') == 'flipkart'
    time.sleep(2)

    flipClickLogin = browser.find_element_by_css_selector('button[class="_2AkmmA _1LctnI _7UHT_c"]')
    assert flipClickLogin.is_displayed() == True
    flipClickLogin.click()
    time.sleep(1)


    flipSearchtext = browser.find_element_by_css_selector('input[class="LM6RPg"]')
    flipSearchtext.send_keys("RealMe" + Keys.RETURN)
    time.sleep(5)






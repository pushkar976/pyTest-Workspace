import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
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

def test_search(browser):
    test_flipkart(browser)
    flipSearchtext = browser.find_element_by_css_selector('input[class="LM6RPg"]')
    flipSearchtext.send_keys("realme" + Keys.RETURN)
    time.sleep(5)

def test_dropDown(browser):
    test_search(browser)
    time.sleep(2)
    browser.find_element_by_css_selector('a[class="_2SvCnW"]').click()
    time.sleep(3)
    dropdown_element = browser.find_element_by_css_selector('select[class="fPjUPw"]')
    flipDropDown = Select(dropdown_element)

    numOfOptions = len(flipDropDown.options)
    print(numOfOptions)
    assert numOfOptions == 11

    flipDropDown.select_by_index(8)
    
    allOptions = flipDropDown.options
    print(allOptions)

    for option in allOptions:
        print(option.text)

    time.sleep(3)
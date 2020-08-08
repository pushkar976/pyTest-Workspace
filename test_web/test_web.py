import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
import time
import logging

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

def test_flipkart_login(browser):

    myDataFile = open("C:/Users/admin/Desktop/loginData.txt","r")
    contents = myDataFile.readline().split()
    print(contents)

    userID = contents[0]
    pass_word = contents[1]

    url = "https://www.flipkart.com"
    # browser.set_page_load_timeout(2)
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
    time.sleep(4)

def test_search(browser):
    test_flipkart_login(browser)
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

    priceList = []
    i = 0
    for option in allOptions:
        priceList.append(option.text)
        assert priceList[i] == option.text
        i = i+1

    time.sleep(3)
    print(priceList)


def test_selectCheckbox(browser):
    # try:
        test_dropDown(browser)
        #Explicit Wait
        wait = WebDriverWait(browser, 20)

        try:
            checkBoxElement = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'section._1gjf4c:nth-child(5) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > div:nth-child(2)')))
            checkBoxElement.click()
            print(checkBoxElement.is_selected())
        except TimeoutException as ex:
            print("Exception has been thrown. " + str(ex))

        time.sleep(3)

        sortPrice = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div._1xHtJz:nth-child(4)')))
        sortPrice.click()
        time.sleep(4)


def test_alertWindow(browser):
    url = 'https://testautomationpractice.blogspot.com/'
    browser.get(url)

    wait = WebDriverWait(browser,10)

    alertButton = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#HTML9 > div:nth-child(2) > button:nth-child(1)')))
    alertButton.click()
    time.sleep(5)
    browser.switch_to_alert().accept() # Returns OK
    # browser.switch_to_alert().dismiss() # Returns Cancle

def test_frames(browser):
    url = 'https://www.selenium.dev/selenium/docs/api/java/index.html'
    browser.get(url)

    browser.switch_to.frame('packageListFrame')
    browser.find_element_by_link_text('org.openqa.selenium.firefox').click()

    print('IS ENABLED  : ',browser.find_element_by_link_text('org.openqa.selenium.firefox').is_enabled())
    assert browser.find_element_by_link_text('org.openqa.selenium.firefox').is_enabled() == True

    time.sleep(2)
    browser.switch_to_default_content()

    browser.switch_to.frame('packageFrame')
    browser.find_element_by_link_text('FirefoxOptions').click()
    assert  browser.find_element_by_link_text('FirefoxOptions').is_enabled() == True

    time.sleep(2)
    browser.switch_to_default_content()

    browser.switch_to.frame('classFrame')
    print("Switched to class Frame")
    browser.find_element_by_css_selector('.topNav > ul:nth-child(4) > li:nth-child(2)').click()
    print('IS PAKAGE SELECTED : ',browser.find_element_by_css_selector('.topNav > ul:nth-child(4) > li:nth-child(2)').is_enabled())
    assert browser.find_element_by_css_selector('.topNav > ul:nth-child(4) > li:nth-child(2)').is_enabled() == True
    time.sleep(2)
    browser.switch_to_default_content()

def test_WindowHandle(browser):
    url = 'http://demo.automationtesting.in/Windows.html'
    browser.get(url)
    wait = WebDriverWait(browser,10)
    browser.find_element_by_link_text('Open Seperate Multiple Windows').click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button[onclick="multiwindow()"]'))).click()
    time.sleep(2)
    print(browser.current_window_handle)
    handleWindow = browser.window_handles

    for handle in handleWindow:
        browser.switch_to_window(handle)
        print(browser.title)
        if browser.title is "":
            browser.close()

    time.sleep(5)

def test_WebTables(browser):
    url = 'https://testautomationpractice.blogspot.com/'
    browser.get(url)
    rows = len(browser.find_elements_by_xpath('/html/body/div[4]/div[2]/div[2]/div[2]/footer/div/div[2]/div[2]/div[1]/div/div[1]/table/tbody/tr'))
    cols = len(browser.find_elements_by_xpath('/html/body/div[4]/div[2]/div[2]/div[2]/footer/div/div[2]/div[2]/div[1]/div/div[1]/table/tbody/tr/th'))
    print("No of rows : ",rows)
    print("No of columns : ",cols)

    for r in range(2,rows+1):
        for c in range(1,cols+1):
            tableValues = browser.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[2]/footer/div/div[2]/div[2]/div[1]/div/div[1]/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
            print(tableValues , end='       ')
        print()

def test_scrollPage(browser):
    url = 'https://testautomationpractice.blogspot.com/'
    browser.get(url)

    #1. Scroll down page by pixel
    browser.execute_script("window.scrollBy(0,300)","")
    time.sleep(5)

    #2. Scroll down page using web element visibility
    table = browser.find_element_by_css_selector('#HTML1 > h2:nth-child(1)')
    browser.execute_script("arguments[0].scrollIntoView();",table)
    time.sleep(5)

    #3. Scroll till the end of webpage
    browser.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    time.sleep(10)

'''--------------MOUSE ACTIONS-------------'''

def test_mouseAction(browser):
    url = 'https://opensource-demo.orangehrmlive.com'
    browser.get(url)
    browser.find_element_by_css_selector('input[id="txtUsername"]').send_keys('Admin')
    browser.find_element_by_css_selector('input[id="txtPassword"]').send_keys('admin123')
    browser.find_element_by_css_selector('input[id="btnLogin"]').click()

    admin = browser.find_element_by_css_selector('#menu_admin_viewAdminModule > b:nth-child(1)')
    usrMgnt = browser.find_element_by_css_selector('#menu_admin_UserManagement')
    user = browser.find_element_by_css_selector('#menu_admin_viewSystemUsers')
    time.sleep(5)

    #1. To hover the mouse on desired element and performing the click action
    mouseAction = ActionChains(browser)
    mouseAction.move_to_element(admin).move_to_element(usrMgnt).move_to_element(user).click().perform()
    time.sleep(5)

def test_doubleClick(browser):
    #2. Performing the double click action
    url = 'https://testautomationpractice.blogspot.com/'
    browser.get(url)
    mouseAction = ActionChains(browser)
    webEle = browser.find_element_by_css_selector('#HTML10 > div:nth-child(2) > button:nth-child(6)')
    mouseAction.double_click(webEle).perform()
    time.sleep(5)

def test_rightClick(browser):
    url = 'https://testautomationpractice.blogspot.com/'
    browser.get(url)
    wait = WebDriverWait(browser,10)
    alertButton = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#HTML9 > div:nth-child(2) > button:nth-child(1)')))
    mouseAction = ActionChains(browser)

    # Below command will perform right click action
    mouseAction.context_click(alertButton).perform()
    time.sleep(5)

def test_dragDrop(browser):
    url = 'http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html'
    browser.get(url)

    source = browser.find_element_by_css_selector('#box6')
    target =  browser.find_element_by_css_selector('#box106')

    action = ActionChains(browser)
    action.drag_and_drop(source,target).perform()
    time.sleep(5)

def test_uploadFile(browser):
    url = 'https://testautomationpractice.blogspot.com/'

    browser.get(url)
    browser.switch_to_frame(0)
    browser.find_element_by_id('RESULT_FileUpload-10').send_keys("E:\\firstFile.txt")

    time.sleep(5)
    browser.find_element_by_css_selector('.button').click()
    time.sleep(5)

def test_downloadFile(browser):

    url = 'http://demo.automationtesting.in/FileDownload.html'
    browser.get(url)

    browser.find_element_by_id('textbox').send_keys('File Download test!')
    browser.find_element_by_id('createTxt').click()
    browser.find_element_by_id('link-to-download').click()

    browser.switch_to_active_element()
    time.sleep(10)

def test_cookies(browser):
    url = 'https://www.flipkart.com'
    browser.get(url)

    cookies = browser.get_cookies()
    cookiesLen = len(cookies)
    print('----------BEFORE ADDING NEW COOKIE---------')
    print("Num of cookies : ",cookiesLen )

    for i in range(0,len(cookies)+1):
        print(cookies[i])
        i = i + 1
        if i == len(cookies):
            break

    newCookie = {'name':'CustomerName','value':'Pushkar'}
    print()
    print('----------AFTER ADDING NEW COOKIE---------')
    browser.add_cookie(newCookie)
    cookies = browser.get_cookies()
    print("Num of cookies : ", len(cookies))
    for i in range(0,len(cookies)+1):
        print(cookies[i])
        i = i + 1
        if i == len(cookies):
            break

    print('----------AFTER DELETING THE COOKIE--------')
    # browser.delete_cookie(cookies[7])
    browser.delete_cookie('CustomerName')
    time.sleep(5)
    cookies = browser.get_cookies()
    print("Num of cookies : ", len(cookies))

    for i in range(0,len(cookies)+1):
        print(cookies[i])
        i = i + 1
        if i == len(cookies):
            break

    browser.delete_all_cookies()
    cookies = browser.get_cookies()
    print('----------AFTER DELETING ALL THE COOKIE--------')
    print("Num of cookies : ", len(cookies))

def test_screenshot(browser):
    url = 'https://www.flipkart.com'
    browser.get(url)

    browser.save_screenshot('E:\\Pushkar\\flipkart.jpg')

def test_Logging():
    logging.basicConfig(filename='E:/Pushkar/test.log',
                        format='%(asctime)s: %(levelname)s: %(message)s',
                        datefmt='%m/%d/%y %I:%M:%S %p  ')

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.debug('This is a debug log')
    logger.info('This is a info log')
    logger.warning('This is a warning log')
    logger.error('This is a error log')
    logger.critical('This is a critical log')

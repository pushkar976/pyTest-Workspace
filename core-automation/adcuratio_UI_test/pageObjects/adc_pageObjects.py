from selenium.webdriver import ActionChains
from adcuratio_UI_test.Locators import element_locators as EL
from Utils import random_string as RS
from adcuratio_UI_test.TestCases.init_browser import Browser
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

import time

class PageObjects():
    agency_name = RS.generate_random_agency()
    agency_admin_lname = RS.generate_agency_admin_lname()
    phone_num = RS.generate_random_phone()
    email = RS.generate_agency_admin()

    def __init__(self,url):
        self.BROWSER = Browser()
        self.browser = self.BROWSER.chrome_browser()
        self.url = url
        self.browser.get(self.url)
        self.browser.implicitly_wait(10)
        self.browser.maximize_window()


    def login(self,email,password):
        self.BROWSER.get_ele_by_xpath(EL.ElementLocators.EMAIL_INPUT_TXTBOX).send_keys(email)
        self.BROWSER.get_ele_by_xpath(EL.ElementLocators.PASSWORD_INPUT_TXTBOX).send_keys(password)
        self.BROWSER.get_ele_by_xpath(EL.ElementLocators.LOGIN_BTN).click()

    def pagetitle(self,locator):
        page_title = self.BROWSER.get_ele_by_xpath(locator).click()
        return page_title.text

    def create_agency(self):
        self.BROWSER.get_ele_by_xpath(EL.ElementLocators.ADD_AGENCY_BUTTON).click()
        self.BROWSER.get_ele_by_xpath(EL.ElementLocators.AGENCY_NAME_TXT_BOX).send_keys(self.agency_name)
        self.BROWSER.get_ele_by_xpath(EL.ElementLocators.SAVE_AGENCY_NAME).click()
        self.BROWSER.get_ele_by_xpath(EL.ElementLocators.CLOSE_NOTIFICATION).click()

    def create_agency_admin(self):
        self.BROWSER.get_ele_by_xpath(
            "//b[@class='mr10 word-break-break-word' and contains(text(),'" + self.agency_name + "')]").click()

        if self.BROWSER.get_ele_by_xpath(EL.ElementLocators.CHECK_AGENCY).text == "Agency Admin for "+self.agency_name+"":
            self.BROWSER.get_ele_by_xpath(EL.ElementLocators.ADD_AGENCY_ADMIN).click()
        else:
            print("Something wrong with the xpath")
        time.sleep(2)

        self.browser.find_element_by_xpath(EL.ElementLocators.AGENCY_ADMIN_FIRST_NAME).send_keys("AgencyAdmin")
        time.sleep(2)
        self.browser.find_element_by_xpath(EL.ElementLocators.AGENCY_ADMIN_LAST_NAME).send_keys(self.agency_admin_lname)
        time.sleep(2)
        self.browser.find_element_by_xpath(EL.ElementLocators.AGENCY_ADMIN_PHONE_NUM).send_keys(self.phone_num)
        time.sleep(2)
        self.browser.find_element_by_xpath(EL.ElementLocators.AGENCY_ADMIN_EMAIL).send_keys(self.email)
        time.sleep(2)

        if self.url == "":
            self.browser.find_element_by_xpath(EL.ElementLocators.AGENCY_ADMIN_PASSWORD).send_keys("")
            self.browser.find_element_by_xpath(EL.ElementLocators.AGENCY_ADMIN_CONFIRM_PASSWORD).send_keys("")
        elif self.url == "http://localhost:8080/":
            self.browser.find_element_by_xpath(EL.ElementLocators.AGENCY_ADMIN_PASSWORD).send_keys("")
            self.browser.find_element_by_xpath(EL.ElementLocators.AGENCY_ADMIN_CONFIRM_PASSWORD).send_keys("")
        time.sleep(2)
        self.browser.find_element_by_xpath(EL.ElementLocators.ADENCY_ADMIN_SAVE_BUTTON).click()
        time.sleep(2)
        self.browser.find_element_by_xpath(EL.ElementLocators.CLOSE_NOTIFICATION).click()
        time.sleep(1)
        self.browser.quit()

    def deal_table_elements(self,deal_num,str_message):
        rows = len(self.browser.find_elements_by_xpath('//*[@id="main"]/advertiser-schedule/div/div/table/tbody/tr'))
        column = len(
            self.browser.find_elements_by_xpath('//*[@id="main"]/advertiser-schedule/div/div/table/thead/tr/th'))
        actual_deal_num = ''
        row = ''
        tableValues = ''
        # print('Rows :', rows)
        # print('Column : ', column)
        for r in range(1, rows + 1):
            for c in range(1, column + 1):
                try:
                    tableValues = self.BROWSER.get_ele_by_xpath(
                    "//*[@id='main']/advertiser-schedule/div/div/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
                except AttributeError as AE:
                    print(str(AE))
                if tableValues == deal_num:
                    actual_deal_num = tableValues
                    row = r
                    print('Deal found in ',str_message,'tab!')
                    break
            else:
                continue
            break
        return actual_deal_num,row

    def creative_table_elements(self,creative_isci):
        rows = len(self.browser.find_elements_by_xpath('//*[@id="table_top"]/tbody/tr'))
        column = len(
            self.browser.find_elements_by_xpath('//*[@id="table_top"]/thead/tr/th'))
        actual_creative_isci = ''
        row = ''
        tableValues = ''
        # print('Rows :', rows)
        # print('Column : ', column)
        for r in range(1, rows + 1):
            for c in range(1, column + 1):
                try:
                    tableValues = self.BROWSER.get_ele_by_xpath(
                    "//*[@id='table_top']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text

                except AttributeError as AE:
                    print(str(AE))
                if tableValues == creative_isci:
                    actual_creative_isci = tableValues
                    row = r
                    print('Uploaded creative found in creatives UI page!')
                    break
            else:
                continue
            break
        return actual_creative_isci,row


    def upload_deal(self,dealfilepath,deal_num):
        adv_schedule = self.BROWSER.get_ele_by_xpath(EL.ElementLocators.ADVERTISER_SCHEDULE)
        self.browser.execute_script("arguments[0].click();", adv_schedule)
        time.sleep(3)
        button = self.browser.find_elements_by_xpath(EL.ElementLocators.UPLOAD_DEAL)
        for item in button:
            if item.text == 'Upload New Deal File':
                time.sleep(2)
                item.click()
                break

        self.browser.find_element_by_xpath(EL.ElementLocators.FILE_TO_UPLOAD).send_keys(dealfilepath)
        button = self.browser.find_elements_by_xpath(EL.ElementLocators.UPLOAD_DEAL)
        for item in button:
            if item.text == 'Upload':
                item.click()
                break

        self.BROWSER.get_ele_by_xpath(EL.ElementLocators.CLOSE_NOTIFICATION).click()
        time.sleep(2)
        # calling function for getting deal data from deal table
        actual_deal_num,row = self.deal_table_elements(deal_num,'Pending agency approval')
        approve_deal = self.browser.find_element_by_xpath(
            "//*[@id='main']/advertiser-schedule/div/div/table/tbody/tr["+str(row)+"]/td["+str(7)+"]/button[1]")
        self.browser.execute_script("arguments[0].click();", approve_deal)

        self.BROWSER.get_ele_by_xpath(EL.ElementLocators.DEAL_APPROVE_BUTTON).click()
        self.BROWSER.get_ele_by_xpath(EL.ElementLocators.CLOSE_NOTIFICATION).click()

        return actual_deal_num

    def logout(self):
        admin_btn = self.browser.find_element_by_xpath(EL.ElementLocators.ADMIN_BTN)
        logout_btn = self.browser.find_element_by_xpath(EL.ElementLocators.LOGOUT_BTN)
        mouse_action = ActionChains(self.browser)
        mouse_action.move_to_element(admin_btn).click().move_to_element(logout_btn).click().perform()

    def adv_approval_for_deal(self,deal_num):
        adv_schedule = self.BROWSER.get_ele_by_xpath(EL.ElementLocators.ADVERTISER_SCHEDULE)
        self.browser.execute_script("arguments[0].click();", adv_schedule)
        time.sleep(2)
        self.BROWSER.get_ele_by_xpath(EL.ElementLocators.ADV_APPROVAL).click()
        time.sleep(2)
        actual_deal_num, row = self.deal_table_elements(deal_num, 'Pending advertiser approval')
        approve_deal = self.browser.find_element_by_xpath(
            "//*[@id='main']/advertiser-schedule/div/div/table/tbody/tr[" + str(row) + "]/td[" + str(7) + "]/button[1]")
        self.browser.execute_script("arguments[0].click();", approve_deal)
        self.BROWSER.get_ele_by_xpath(EL.ElementLocators.DEAL_APPROVE_BUTTON).click()
        self.BROWSER.get_ele_by_xpath(EL.ElementLocators.CLOSE_NOTIFICATION).click()
        try:
            self.BROWSER.get_ele_by_xpath(EL.ElementLocators.APPROVED_DEAL).click()
        except WebDriverException as WDE:
            print(str(WDE))

        approved_deal,row = self.deal_table_elements(deal_num, 'Approved')
        if approved_deal == deal_num:
            print('Deal approved successfully')

    def verify_creative_upload(self,creative_isci):
        creative = self.BROWSER.get_ele_by_xpath(EL.ElementLocators.CREATIVE_PAGE)
        self.browser.execute_script("arguments[0].click();", creative)
        actual_creative_iscii,row = self.creative_table_elements(creative_isci)
        return actual_creative_iscii

    def create_segment(self,filters):
        time.sleep(4)
        target_segment_button = self.browser.find_elements_by_xpath(EL.SEGMENT_LOCATORS.TARGET_SEGMENT)
        for item in target_segment_button:
            # print(item.text)
            if item.text == 'Target Segments':
                time.sleep(2)
                item.click()
                break
        time.sleep(3)
        button = self.browser.find_elements_by_xpath(EL.SEGMENT_LOCATORS.CREATE_NEW_SEGMENT)
        for item in button:
            if item.text == 'Create New Segment':
                time.sleep(2)
                item.click()
                break
        time.sleep(3)
        filter_cat = self.browser.find_element_by_xpath(EL.SEGMENT_LOCATORS.SEGMENT_FILTER_CATEGORIES)
        filter_items = filter_cat.find_elements_by_tag_name('li')
        for item in filter_items:
            if item.text == filters[0]:
                item.click()
        time.sleep(3)
        self.browser.find_element_by_xpath(EL.SEGMENT_LOCATORS.ADD_FILTERS).click()
        time.sleep(3)
        demo_filter_cat = self.browser.find_elements_by_xpath(EL.SEGMENT_LOCATORS.DEMORGRAPHICS_FILTERS)
        for item in demo_filter_cat:
            if item.text == filters[1]:
                item.click()

        time.sleep(2)
        self.browser.find_element_by_xpath(EL.SEGMENT_LOCATORS.CLOSE_FILTER).click()
        time.sleep(2)

        all_filters = self.browser.find_element_by_xpath(EL.SEGMENT_LOCATORS.DEMORGRAPHICS_DROP_DOWN)
        options = all_filters.find_elements_by_tag_name('a')
        for item in options:
            print(item.text)
            if item.text == filters[2]:
                item.click()


        time.sleep(10)




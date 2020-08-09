class flipkartLogin():
    def __init__(self,driver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    def setUserName(self,username):
        self.driver.find_element_by_css_selector('input[class="_2zrpKA _1dBPDZ"]').send_keys(username)

    def setPassword(self,password):
        self.driver.find_element_by_css_selector('input[type=password]').send_keys(password)

    def clickLoginButtom(self):
        self.driver.find_element_by_css_selector('button[class="_2AkmmA _1LctnI _7UHT_c"]').click()

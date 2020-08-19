import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    FFdriverloc = 'E:\\Python\\lib\\geckodriver'
    firefox_option = webdriver.FirefoxProfile()
    firefox_option.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain,application/pdf")
    firefox_option.set_preference("browser.download.folderList", 2)
    firefox_option.set_preference("browser.download.manager.showWhenStarting", False)
    firefox_option.set_preference("browser.download.dir", 'E:\\Pushkar')

    '''<------- ABOVE 4 LINES CODE JOB ------->
    1. Values could be either 0, 1, or 2. Default value is ‘1’.
                0 – To save all files downloaded via the browser on the user’s desktop.
                1 – To save all files downloaded via the browser on the Downloads folder
                2 – To save all files downloaded via the browser on the location specified for the 
                    most recent download
    2. This setting allows the user to specify whether the Download Manager window should be
       displayed or not when file downloading starts. Default value is ‘true which is for 
       ‘Display Download Manager window’.

    3. The directory name to save the downloaded files.

    4. A comma-separated list of MIME types to save to disk without asking what to use to 
       open the file. Default value is an empty string.'''

    driver = webdriver.Firefox(executable_path=FFdriverloc, firefox_profile=firefox_option)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
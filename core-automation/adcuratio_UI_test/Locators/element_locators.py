
class ElementLocators:

    # LoginPage elements
    EMAIL_INPUT_TXTBOX = "//input[@type='email']"
    PASSWORD_INPUT_TXTBOX = "//input[@type='password']"
    LOGIN_BTN = "//button[@type='button' and contains(text(),'LOGIN')]"

    # Agency creation elements
    ADD_AGENCY_BUTTON = "//button[@type='button' and contains(text(),'Add Agency')]"
    AGENCY_NAME_TXT_BOX = "//input[@type='text']"
    SAVE_AGENCY_NAME = "//button[@type='button' and contains(text(),'Save')]"
    CLOSE_NOTIFICATION = "//button[@type='button' and contains(text(),'OK')]"
    NOTIFICATION_BOX = "//b[@class='mr10 word-break-break-word' and contains(text(),'')]"

    # Agency Admin creation
    CHECK_AGENCY = "//*[@id='rightModal']/div/p"
    ADD_AGENCY_ADMIN = "//button[@type='button' and contains(text(),'Add New Agency Admin')]"
    AGENCY_ADMIN_FIRST_NAME = "//input[@name='first_name']"
    AGENCY_ADMIN_LAST_NAME = "//input[@name='last_name']"
    AGENCY_ADMIN_PHONE_NUM = "//input[@name='phone']"
    AGENCY_ADMIN_EMAIL = "//input[@name='email']"
    AGENCY_ADMIN_PASSWORD = "//input[@name='password']"
    AGENCY_ADMIN_CONFIRM_PASSWORD = "//input[@name='confirm_passpord']"
    ADENCY_ADMIN_SAVE_BUTTON = "//button[@type='button' and contains(text(),'Save')]"
    MANAGE_AGENCIES = "//h1[@class='sc-bZQynM OMzFj' and contains(text(),'Manage Agencies')]"

    ADVERTISER_SCHEDULE = "//div[@class='sc-kvZOFW ggWDvA' and contains(text(),'Advertiser Schedule')]"

    UPLOAD_DEAL = "//button[@class='sc-dnqmqq kMZabu ml10']"
    FILE_TO_UPLOAD = "//input[@id='uploadFile']"
    DEAL_APPROVE_BUTTON = "//button[@class='sc-iwsKbI kVMdSk capitalize' and contains(text(),'approve')]"
    ADMIN_BTN = "//*[@id='header_user_nav']"
    LOGOUT_BTN = "//div[@class='sc-VJcYb gRMLwb' and contains(text(),'Logout')]"

    ADV_APPROVAL = "//a[@aria-controls='pending_advertiser_approval' and contains(text(),'Pending Advertiser Approval')]"
    APPROVED_DEAL = "//*[@id='main']/advertiser-schedule/div/div/div[2]/ul/li[3]/a"

    CREATIVE_PAGE = "//div[@class='sc-kvZOFW ggWDvA' and contains(text(),'Creatives')]"

class SEGMENT_LOCATORS:

    TARGET_SEGMENT = "//div[@class='sc-kvZOFW ggWDvA']"
    CREATE_NEW_SEGMENT = "//button[@class='sc-dnqmqq kMZabu mr10']"
    SEGMENT_FILTER_CATEGORIES = "//ul[@class='segments-tab']"
    DEMORGRAPHICS_FILTERS = "//label[@class='checkbox-container mr10 mb10']"
    ADD_FILTERS = "//a[@class='add-filters segement-add-remove-button' and contains(text(),'Add/Remove Filters')]"
    CLOSE_FILTER = "//button[@class='sc-iwsKbI kVMdSk' and contains(text(),'Close')]"
    DEMORGRAPHICS_DROP_DOWN = "//ul[@class='dropdown-width']"













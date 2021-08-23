import sys
import os
curr_dir_path = os.path.dirname(__file__).split('/')
deal_script_path = []
for i in curr_dir_path:
    deal_script_path.append(i)
    if i == "adcuratio_UI_test":
        idx = curr_dir_path.index(i)
        deal_script_path[idx] = 'automate_sftp'
        break
deal_script_path = '/'.join(deal_script_path)
sys.path.append(deal_script_path)
from adcuratio_UI_test.pageObjects.adc_pageObjects import PageObjects
from adcuratio_UI_test.TestCases import init_browser
from adcuratio_UI_test.Locators import element_locators as EL
from Utils import random_string as RS
from Utils import create_deal
from Utils import helper_api
from Utils.download_creative import CreativeDownload
import time
import getpass

# login to super admin
def test_agency_agencyadmin_creation():
    browser = PageObjects(init_browser.SERVER.TEST_SERVER_URL)
    # browser.login(email, password)
    page_title = browser.pagetitle(EL.ElementLocators.MANAGE_AGENCIES)
    assert page_title == "Manage Agencies"
    browser.create_agency()
    browser.create_agency_admin()

def test_deal_creation():
    # get user data required for deal upload
    agency, agency_admin, advertiser, advertiser_admin, brand, sub_brand = create_deal.user_data()
    deal_file_path, expected_deal_num = create_deal.create_deal_file(agency, advertiser, brand)
    return agency, agency_admin, advertiser, advertiser_admin, brand,sub_brand, deal_file_path, expected_deal_num

def test_deal_upload():
    # Create deal
    agency, agency_admin, advertiser, advertiser_admin, brand, sub_brand, deal_file_path, expected_deal_num = test_deal_creation()
    print()
    print("Enter the Agency password")
    password = getpass.getpass()
    print('==================================')

    # Login to UI for deal upload
    browser = PageObjects(init_browser.SERVER.TEST_SERVER_URL)
    browser.login(agency_admin, password)
    actual_deal_num = browser.upload_deal(deal_file_path,expected_deal_num)
    print('Expected Deal Num : ', expected_deal_num)
    print('Actual Deal Num : ', actual_deal_num)

    # Check the deal uploaded is present on UI and approve
    if actual_deal_num == expected_deal_num:
        assert actual_deal_num == expected_deal_num
        print('Deal uploaded successfully : ', actual_deal_num)
        browser.logout()
    browser.login(advertiser_admin,password)
    browser.adv_approval_for_deal(actual_deal_num)

def test_creative_upload():
    print()
    # get user data required for deal upload
    agency, agency_admin, advertiser, advertiser_admin, brand, sub_brand = create_deal.user_data()
    print("Enter the Agency password")
    password = getpass.getpass()

    # Agency Admin Token
    token = helper_api.get_user_token(agency_admin, password, helper_api.login_api)

    # Data to be searched in the get_company_list_API response
    search_string = [advertiser, brand, sub_brand]

    # Get user id's of data searched in get_company_list_API
    user_ids = helper_api.get_user_ids(token, helper_api.get_company_list_api, search_string)
    print()

    # Creative to be downloaded for the company
    CD = CreativeDownload(VIDEO_COLLECTION_PAGE="https://www.ispot.tv/search/")
    video_link = CD.get_video_links()
    file = CD.download_video_series(video_link)
    file_name = file.split('.')[0]

    uploaded_creative_isci = RS.generate_rand_creative_isci(file_name)

    print('Uploading creative.....')
    resp_message = helper_api.upload_creative(token,user_ids,file,file_name,uploaded_creative_isci)
    print(resp_message)
    print('Expected Creative_isci: ', uploaded_creative_isci)
    assert resp_message == 'Creative successfully created'
    CD.move_creative_file(os.path.dirname(__file__)+'/'+file)

    # Verifying if creative successfully uploaded on UI
    browser = PageObjects(init_browser.SERVER.TEST_SERVER_URL)
    browser.login(agency_admin, password)
    actual_isci_on_ui = browser.verify_creative_upload(uploaded_creative_isci)
    print('Actual creative isci : ',actual_isci_on_ui)
    assert actual_isci_on_ui == uploaded_creative_isci,"Creative ISCI doesn't match on UI"

def test_segment_creation():
    agency, agency_admin, advertiser, advertiser_admin, brand, sub_brand = create_deal.user_data()
    print("Enter the Agency password")
    password = getpass.getpass()
    import create_segment
    filters = create_segment.select_filters()

    browser = PageObjects(init_browser.SERVER.TEST_SERVER_URL)
    browser.login(agency_admin, password)
    browser.create_segment(filters)



















from Utils.get_user import UserCredentials
from automate_sftp import execute_command as EC

def user_data():

    uc = UserCredentials('admin_cred.csv')
    print()
    uc.display_user_details()
    print()
    user_resp = input('Is required user data present in the above datasets for file upload ??(y/n)')
    if user_resp == 'y':
        num = int(input('Please select the row which has required data : '))
        print()
        data = uc.select_row_data(num)
        print()
        data_dict = dict(data)
        agency = data_dict['AgencyName']
        agency_admin = data_dict['AgencyAdmin']
        advertiser = data_dict['AdvertiserName']
        advertiser_admin = data_dict['AdvertiserAdmin']
        brand = data_dict['BrandName']
        sub_brand = data_dict['Sub_brand']
    else:
        print("Enter the new user data:")
        print()
        agency = input('Enter new Agency name: ')
        agency_admin = input('Enter new Agency admin email: ')
        advertiser = input('Enter new Advertiser: ')
        advertiser_admin = input('Enter new Adv Admin: ')
        brand = input('Enter new Brand name: ')
        sub_brand = input('Enter new Sub-Brand name: ')
        new_cred = {'AgencyName': agency,
                    'AgencyAdmin': agency_admin,
                    'AdvertiserName': advertiser,
                    'AdvertiserAdmin': advertiser_admin,
                    'BrandName': brand,
                    'Sub_brand': sub_brand
                    }
        uc.add_new_credentials(new_cred)

    return agency,agency_admin,advertiser,advertiser_admin,brand,sub_brand

def create_deal_file(agency,advertiser,brand):
    _created_deal_file, _deal_file_split, _deal_dir = EC.create_deal_file(agency,advertiser,brand)
    print("Newly created Deal file :", _created_deal_file, _deal_dir)
    deal_file_path = _deal_dir + '/' + _created_deal_file
    print(deal_file_path)
    expected_deal_num = _created_deal_file.split('_')[0]
    return deal_file_path,expected_deal_num

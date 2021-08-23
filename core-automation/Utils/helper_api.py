import json
import requests

host = ""
login_api = "https://" + host + "/login/"
creative_upload_api = "https://" + host + "/pilot/upload_creative_files/"
get_company_list_api = "https://" + host + "/advertiser/get_company_list/"

def get_user_token(username,password,login_api):

    data = {
        "username": username,
        "password": password
        }
    response = requests.post(login_api, data=data)
    if response.status_code != 200:
        print("Invalid user credentials..")
    else:
        print("Token Generated")
        response = response.json()
        return response['token']


def get_user_ids(token, get_company_list_api, search_string):
    '''
        Provide list of Company ID/Brand ID/Sub Brand ID
        based on search string provided
    '''
    header = {
        "Authorization": "Token " + token
    }

    response = requests.get(get_company_list_api, headers=header)
    data = json.loads(response.text)['data']

    company_id = 0
    brand_id = 0
    sub_brand_id = 0

    for company in data:
        if search_string[0] == 0:
            print("Advertiser(Mandatory field) not present in the admin_cred.csv file. Please add and re-run the script")
            break
        for brand in company['company']['brands']:
            if search_string[1] == 0:
                print("Brand(Mandatory field) not present in the admin_cred.csv file. Please add and re-run the script")
                break
            elif search_string[1].lower() == brand['name'].lower():
                company_id = company['company']['id']
                brand_id = brand['id']
                print('COMPANY NAME: ',company['company']['name'],'| COMPANY ID: ',company_id)
                print('BRAND NAME: ', brand['name'],'| BRAND ID: ',brand_id)
                
            for sub_brand in brand['sub_brands']:
                if search_string[2] == 0:
                    print("Sub brand not present in the admin_cred.csv file")
                    break
                elif search_string[2].lower() == sub_brand['name'].lower():
                    company_id = company['company']['id']
                    brand_id = brand['id']
                    sub_brand_id = sub_brand['id']
                    print('SUB-BRAND NAME: ',sub_brand['name'],'| SUB-BRAND ID: ',sub_brand_id)


    return company_id, brand_id, sub_brand_id


def upload_creative(token, user_ids, file, creative_name,creative_isci):

    print()
    print("ENTER CREATIVE UPLOAD DETAILS:")
    print()
    entity = {
        '1': 'brand',
        '2': 'company',
    }
    print(entity)
    
    entity_type = input("Select for which entity type you want to upload creative: ")
    
    brand_id = user_ids[1]
    delivery_vendor = {
        '1': 'YANGAROO',
        '2': 'Comcast',
        '3': 'Extreme Reach',
        '4': 'On The Spot Media'
    }
    print(delivery_vendor)
    vendor = input('Select delivery vendor: ')
    
    payload={
        'creative_name': creative_name,
        'identifier': creative_isci,
        'entity_id': brand_id,
        'entity_type': entity[entity_type],
        'delivery_vendor': delivery_vendor[vendor]
    }
    files={
      "creative_file_name": open(file, 'rb')
    }
    headers = {
      "Authorization": "Token " + token
    }
    
    response = requests.request("POST", creative_upload_api, headers=headers, data=payload, files=files)
    
    return response.json()['message']

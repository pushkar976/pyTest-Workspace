import os
import json
from deal_script import Deal_Dates as DD

dealjson_path = os.path.dirname(__file__)+'/deal.json'
showntw_json = os.path.dirname(__file__)+'/show_ntw.json'


def get_deal_dir():

    deal_script_path = os.path.dirname(__file__)
    deal_json_file_path = dealjson_path
    deal_dir = deal_script_path+"/Deals"
    md5sum_deal = deal_script_path
    return deal_script_path,deal_json_file_path,deal_dir,md5sum_deal


def create_deal_json(AGENCY,ADVERTISER,BRAND):
    agency = AGENCY
    advertiser = ADVERTISER
    brand = BRAND
    flight_start = DD.flight_start_date()
    flight_end = DD.camp_end_date()
    channelDict = {'1': 'A&E', '3': 'FYI', '5': 'His', '6': 'Life', '7': 'Lifemov', '10': 'Vice'}
    print(channelDict)
    channel = input("Select the Channel for Deal creation : ")
    print('===============DEAL JSON=====================')
    with open('/home/pushkar/Workspace/core-automation/deal_script/deal.json') as json_file:
        data = json.load(json_file)

    key = ""
    for key in data['1'].keys():
        print(key)

    newdata = data['1']
    newdata[agency] = newdata.pop(key)
    newdata[agency]['Advertiser'] = advertiser
    newdata[agency]['FlightStart'] = flight_start
    newdata[agency]['FlightEnd'] = flight_end
    newdata[agency]['Brand'] = brand
    data['1'] = newdata
    data = dict(data)

    json_data = json.dumps(data, indent=3)
    print(json_data)

    with open(dealjson_path, 'w') as json_file:
        json_file.write(json_data)

    with open(showntw_json) as ntw_json_file:
        channel_data = json.load(ntw_json_file)

    channel_name = ""
    for channel_name in channel_data.keys():
        channel_name = channel_name

    channel_data[channelDict[channel]] = channel_data.pop(channel_name)

    dayparts_list = channel_data[channelDict[channel]]

    for dayparts in dayparts_list:
        dayparts['ShowStartMonday'] = flight_start

    channel_data[channelDict['3']] = dayparts_list

    print('===============SHOW NTW JSON=====================')
    ntw_json = json.dumps(channel_data, indent=3)

    with open(showntw_json, 'w') as ntw_json_file:
        ntw_json_file.write(ntw_json)

    print(json.dumps(channel_data, indent=3))
    return channel










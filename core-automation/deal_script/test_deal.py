import errno
import json
import os
import random
import xml.etree.ElementTree as ET
from datetime import datetime
import more_itertools as mit
import pandas as pd
from xml.dom import minidom
import sys


def generateSellingName(show_meta):
    week_days = ["M", "Tu", "W", "Th", "Fr", "Sa", "Su"]
    for show in show_meta:
        show["showName"] = show['sellingName']
        iterable = [i for i in range(len(show['dayPart'])) if show['dayPart'][i] == 'Y']
        index_list = [list(group) for group in mit.consecutive_groups(iterable)]
        day = " ".join([" - ".join([week_days[index[0]], week_days[index[-1]]]) if len(index) > 1 else week_days[index[0]] for index in index_list])
        timing = " ".join([show['showStartTime'].replace(':00',''), show['showEndTime'].replace(':00', '')])
        show['sellingName'] += " " + day + " " + timing

    return show_meta

# from engine.configurations import DEAL_FILE_DIR_PATH, ANELOG_FILE_DIR_PATH

def generateData(brand, start, end, dataStore):
    dataList = []
    x, y = 37819650, 39842650
    # import pdb; pdb.set_trace()
    flightStart = datetime.strptime(dataStore[0]['ShowStartMonday'], '%d/%m/%Y')
    # flightStart = datetime.strptime(dataStore[0]['ShowStartMonday'], '%m/%d/%Y')
    dayCount = dataStore[0]['weeksCount']
    for info in dataStore:
        showStartMonday = datetime.strptime(info['ShowStartMonday'], '%d/%m/%Y')
        # showStartMonday = datetime.strptime(info['ShowStartMonday'], '%m/%d/%Y')
        spot_count = info['weeksCount'] * info['weeklySpotCount']
        total_spot = random.sample(range(x, y), spot_count)
        weekStartList = pd.date_range(start=showStartMonday, periods=info['weeksCount'],
                                      freq='7D').to_pydatetime().tolist()
        if flightStart > showStartMonday:
            flightStart = showStartMonday
        if dayCount < info['weeksCount']:
            dayCount = info['weeksCount']
        c = 0
        for weekStart in weekStartList:
            if start <= weekStart <= end:
                for i in range(info['weeklySpotCount']):
                    data = [weekStart.strftime('%m/%d/%Y'), info['dayPart'], info['sellingName'], info['showStartTime'],
                            info['showEndTime'], info['UnitCost'], info['impression'], brand, str(total_spot[c])]
                    dataList.append(data)
                    c += 1

        x += 10000000
        y += 10000000

    # flightEnd = flightStart + timedelta(days=(dayCount*7-1))
    # return flightStart, flightEnd, dataList
    return dataList


def createDemoImps(tag):
    demoName = ['F18-34',
                'F18-49',
                'F18-54',
                'F25-49',
                'F25-54',
                'F35-54',
                'HH',
                'M18-34',
                'P18-34',
                'P18-49',
                'P18-54',
                'P25-49',
                'P25-54',
                'P35-54']
    for i in range(len(demoName)):
        Impression = ET.SubElement(tag, 'Impression', {})
        DemoName = ET.SubElement(Impression, 'DemoName', {})
        DemoImp = ET.SubElement(Impression, 'DemoImps', {})
        DemoName.text, DemoImp.text = demoName[i], str(random.randint(20, 200) * 1000)


# Create Line

def createNode(Line, details):
    # Node Creation
    WeekStart = ET.SubElement(Line, 'WeekStart', {})
    DaysOfWeek = ET.SubElement(Line, 'DaysOfWeek', {})
    SellingName = ET.SubElement(Line, 'SellingName', {})
    ShowStartTime = ET.SubElement(Line, 'ShowStartTime', {})
    ShowEndTime = ET.SubElement(Line, 'ShowEndTime', {})
    Brand = ET.SubElement(Line, 'Brand', {})
    SellingElement = ET.SubElement(Line, 'SellingElement', {})
    CPM = ET.SubElement(Line, 'CPM', {})
    SpotUSN = ET.SubElement(Line, 'SpotUSN', {})

    # Assign of Value
    weekStart, daysOfWeek, sellingName, showStartTime, showEndTime, unitCost, impression, brand, spot_USN = details
    WeekStart.text = weekStart
    DaysOfWeek.text = daysOfWeek  # format-> Mon - Sun
    SellingName.text = sellingName
    ShowStartTime.text = showStartTime + ':00'
    ShowEndTime.text = showEndTime + ':00'
    Brand.text = brand
    SpotUSN.text = spot_USN
    # ------------------------------------------------------------
    SellingElement.text = 'NS'
    CPM.text = impression
    ET.SubElement(Line, 'ParentUSN', {})
    DemoImps = ET.SubElement(Line, 'DemoImps', {})
    createDemoImps(DemoImps)
    Duration = ET.SubElement(Line, 'Duration', {})
    Duration.text = '30'
    UnitCount = ET.SubElement(Line, 'UnitCount', {})
    UnitCount.text = '1'
    UnitCost = ET.SubElement(Line, 'UnitCost', {})
    UnitCost.text = unitCost


# create Deal file

def createFile(filePath, file, xmlString):

    if not os.path.exists(os.path.dirname(filePath)):
        try:
            os.makedirs(os.path.dirname(filePath))

        # Guard against race condition
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise

    with open(filePath + file, "w+") as f:
        f.write(xmlString)
    f.close()


def deal_xml(channel_name, agency_name, advertiser_name, brand, start, end, showMeta):
    global dealFileDir

    tree = ET.parse(os.path.dirname(__file__)+'/sample_deal.xml')

    flightStart = datetime.strptime(start, '%d/%m/%Y')
    flightEnd = datetime.strptime(end, '%d/%m/%Y')

    # flightStart = datetime.strptime(start, '%m/%d/%Y')
    # flightEnd = datetime.strptime(end, '%m/%d/%Y')

    if flightStart >= flightEnd:
        print('FlightStart can\'t be same or greater than FlightEnd')
        return None, None

    dataList = generateData(brand, flightStart, flightEnd, showMeta)

    if not dataList:
        print('No Active Show between {} to {}'.format(start, end))
        return None, None
    # ----------------------------------------------------------------
    tree.find('.//Property').text = channel_name
    tree.find('.//Advertiser').text = advertiser_name
    tree.find('.//Agency').text = agency_name

    DealNumber = random.randint(50000, 99999)
    tree.find('.//DealNumber').text = str(DealNumber)
    tree.find('.//DealName').text = str(DealNumber) + ' ' + advertiser_name + ' - ' + channel_name

    tree.find('.//FlightStart').text = flightStart.strftime('%m/%d/%Y')
    tree.find('.//FlightEnd').text = flightEnd.strftime('%m/%d/%Y')
    tree.find('.//TotalUnitCount').text = str(len(dataList))

    tree.find('.//TotalImpressions').text = str(sum([int(data[6]) for data in dataList]))
    tree.find('.//TotalCost').text = str(sum([int(data[5]) for data in dataList]))

    # ----------------------------------------------------------------
    # Get root node of the tree and reach to the 'Units' node
    root = tree.getroot()  # NetworkDeal
    units = root[2]  # Units

    for data in dataList:
        Line = ET.SubElement(units, 'Line', {})
        createNode(Line, data)

    # xml pretty print
    fileName = str(DealNumber) + '_' + channel_name + '_' + advertiser_name + '_' + flightStart.strftime(
        '%m%d%Y') + '_' + flightEnd.strftime('%m%d%Y') + '_.xml'

    xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
    createFile(dealFileDir, fileName, xmlstr)

    print('Deal {} Created for {} with {} spot'.format(fileName, advertiser_name, len(dataList)))


if __name__ == "__main__":
    '''
        Channel ID Channel Name
        1          A&E Television Network
        3          FYI
        5          The History Channel
        6          Lifetime Television
        7          Lifetime Movie Network
        10         Viceland
    '''
    channelDict = {'1': 'A&E', '3': 'FYI', '5': 'His', '6': 'Life', '7': 'Lifemov', '10': 'Vice'}
    # channelDict = {'1': 'A&E', '3': 'FOX', '5': 'FOX NEWS NETWORK', '6': 'FOX BUSINESS NETWORK', '7': 'Lifemov', '10': 'Vice'}
    print(channelDict)
    # "FOX NEWS NETWORK, FOX, FOX BUSINESS NETWORK"
    channel_list = input('Enter a list channel_id separated by space: ').split() or ['10']
    # Show Data
    show_json_file = os.path.dirname(__file__)+'/show_ntw.json'
    with open(show_json_file, 'r') as f:
        shows = json.load(f)
    try:
        for show_list in shows.values():
            for show in show_list:
                duration = (datetime.strptime(show['showEndTime'], '%H:%M:%S') - datetime.strptime(show['showStartTime'], '%H:%M:%S')).seconds
                assert duration in [1800, 3600], "{}: Invalid Show Duration! Allow only 1hr or 30mins show".format(show['sellingName'])
        showData = {k: generateSellingName(shows[channelDict[k]]) for k in channel_list}
    except AssertionError as e:
        print(e)
        sys.exit()

    '''
        showData = {
            "Vice":
            [
                {
                    "sellingName": "Live PD",
                    "showStartTime": "08:00:00",
                    "showEndTime": "08:30:00",
                    "dayPart": "YYYYYNN",
                    "weeksCount" : 12,
                    "weeklySpotCount" : 5,
                    "ShowStartMonday" : "06/01/2020",
                    "UnitCost" : "20000",
                    "impression" : "6215737"
                }
            ]
        }
    '''

    # dealFileDir = DEAL_FILE_DIR_PATH
    dealFileDir = os.path.dirname(__file__)+'/Deals/'

    # Deal Data
    with open(os.path.dirname(__file__)+'/deal.json', 'r') as f:
        dealData = json.load(f)

    '''
        dealData = {
                "1":{"Zenith Media":{
                "Advertiser": "Toyota",
                "FlightStart": "27/01/2020",
                "FlightEnd": "12/07/2020",
                "Brand" : "Toyota Camry",
            }}}
    '''

    for channel in channel_list:
        for deal in dealData.values():
            agency, deal_info = next(iter(deal.items()))
            deal_xml(channelDict[channel], agency, deal_info['Advertiser'], deal_info['Brand'],
                deal_info['FlightStart'], deal_info['FlightEnd'], showData[channel]
            )

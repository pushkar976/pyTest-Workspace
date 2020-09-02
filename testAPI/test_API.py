import requests
import json
# import pytest_html
import logging

BASE_URL = 'https://reqres.in'
page1 = {'page': 1}
page2 = {'page': 2}
def test_api_get():
    param = {'page':2}
    resp = requests.get(BASE_URL+"/api/users",params=page2)
    assert (resp.status_code == 200), "Status code is not 200. Rather found : " + str(resp.status_code)
    print(resp.status_code)

    #Prints the response in json format
    print(json.dumps(resp.json(),indent=4))

    #Jason is structured in form of dictionary having Key Value pairs
    #Hence dictionary operations can easily be performed to extract information.
    jsonResponse = resp.json()
    assert jsonResponse['total_pages'] == 2

    #Below statement will extract the data from the json array "data"

    record = resp.json()['data']

    #iPython debugger
    # import ipdb;ipdb.set_trace()

    for i in record:
        print(i['id'], i['first_name'])

    # print('DATA-------: ', resp.json()['data'])
    for record in resp.json()['data']:
        if record['id'] == 12:
            assert record['first_name'] == "Rachel",\
                "Data not matched! Expected : Eve, but found : " + str(record['first_name'])
            assert record['last_name'] == "Howell",\
                "Data not matched! Expected : Holt, but found : " + str(record['last_name'])

def test_api_post():

    postdata = {'name': 'John',
            'job': 'QA'}
    resp = requests.post(url=BASE_URL+"/api/users", data=postdata)
    new_data = resp.json()
    print('DATA---------',json.dumps(new_data,indent=4))
    assert (resp.status_code == 201), "Status code is not 201. Rather found : " \
                                      + str(resp.status_code)
    assert new_data['name'] == "John", "User created with wrong name. \
            Expected : John, but found : " + str(new_data['name'])
    assert new_data['job'] == "QA", "User created with wrong job. \
            Expected : QA, but found : " + str(new_data['name'])

    resp = requests.get(url=BASE_URL+"/api/users", params=page1)
    print(json.dumps(resp.json(),indent=4))
    print('-------------------------------------------------')
    resp = requests.get(url=BASE_URL + "/api/users", params=page2)
    print(json.dumps(resp.json(), indent=4))

def test_api_Put():
    updatedata = {
            "id": 1,
            "email": "pushkartiwari@gmail.com",
            "first_name": "Pushkar",
            "last_name": "Tiwari",
        }

    resp = requests.put(url=BASE_URL+"/api/users", data=updatedata)
    print(json.dumps(resp.json(),indent=4))
    print('-----------------')
    resp = requests.get(url=BASE_URL+"/api/users", params=page1)
    data = resp.json()["data"]
    print(json.dumps(data,indent=4))

    for record in data:
        print(record["first_name"])


def test_countryAPI():
    url = "https://covid-19-data.p.rapidapi.com/help/countries"

    querystring = {"format": "json"}

    headers = {
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
        'x-rapidapi-key': "95bf7eb63bmshd85da20246a7e32p1a16a8jsncabf7d1e8798"
    }

    response = requests.get(url, headers=headers, params=querystring)

    assert response.status_code == 200
    Resp = response.json()
    print(type(Resp))
    print(json.dumps(response.json(),indent=4))

    country = []
    countryCode = []

    for i in range(len(Resp)):
        myd = dict(Resp[i])
        # print(myd)
        country.append(myd['name'])
        countryCode.append(myd['alpha2code'])
        assert myd['name'] == country[i]
        assert myd['alpha2code'] == countryCode[i]
        countryDict = {country[i] : countryCode[i]}
        print(countryDict)

def test_flipkartLoginAPI():
    PY_BASE_URL = "https://rome.api.flipkart.com/api/4/user/authenticate"
    null = "null"
    true = "true"
    payload = {"loginId":"8147070507","password":"flipkart"}

    resp = requests.post(BASE_URL,payload)

    print(resp.status_code)

    print(json.dumps(resp.json(),indent=4))





import requests
import json


def test_api_get():
    BASE_URL = 'https://reqres.in'
    param = {'page':2}
    resp = requests.get(BASE_URL+"/api/users",params=param)
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
    data = {'name': 'John',
            'job': 'QA'}
    resp = requests.post(url="https://reqres.in/api/users", data=data)
    data = resp.json()
    print('DATA---------',data)
    assert (resp.status_code == 201), "Status code is not 201. Rather found : " \
                                      + str(resp.status_code)
    assert data['name'] == "John", "User created with wrong name. \
            Expected : John, but found : " + str(data['name'])
    assert data['job'] == "QA", "User created with wrong job. \
            Expected : QA, but found : " + str(data['name'])

    data = {'id': '1',
            'first_name': 'Pushkar'}
    resp = requests.post(url="https://reqres.in/api/users", data=data)
    print(resp.json())
    print('-----------------')
    resp = requests.get(url="https://reqres.in/api/users")
    data = resp.json()["data"]
    for i in range(len(resp.json()["data"])):
        print(data[i])

    for record in resp.json()['data']:
        if record['id'] == 1:
            assert record['first_name'] == "Pushkar",\
                "Data not matched! Expected : Pushkar, but found : " + str(record['first_name'])


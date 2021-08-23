import locust.clients
from locust import HttpUser, TaskSet, task, between,runners,events,constant_pacing
import random
import string
from locust.runners import MasterRunner
from locust.contrib.fasthttp import FastHttpUser
import time


@events.init.add_listener
def on_locust_init(environment, **kwargs):
    if isinstance(environment.runner, MasterRunner):
        print("================== MASTER NODE ====================")
    else:
        print("================== WORKER NODE ====================")


'''
TaskSet class is a collection of defined tasks.
-  When a running User thread picks a TaskSet class for execution, 
   an instance of this class will be created and execution will then go into this TaskSet.
'''
class Adcuratio_UserBehaviour(TaskSet):
    ''''''
    '''
        A User’s wait_time method is used to determine how long a simulated user
        should wait between executing tasks.
    '''
    min_wt = int(input("Minimum Wait : "))
    max_wt = int(input("Maximum Wait : "))
    print(min_wt,max_wt)
    wait_time = between(min_wt,max_wt)

    @task
    def adcuratio_get(self):
        ''''''
        '''
        A lambda function to create IFA as a random generated key
        '''

        randStr = lambda chars = string.ascii_lowercase + \
            string.digits, N=0: ''.join(random.choice(chars) for _ in range(N))

        ifa = F'{randStr(N=8)}-{randStr(N=4)}-{randStr(N=4)}-{randStr(N=5)}-{randStr(N=12)}'

        channels = ['FNCHD', 'FBNHD', 'POPHD', 'HSTRYHD',
                    'WCBSHD', 'WSBCHD', 'FOXHD', 'LIFEHD', 'MTVHD']

        # channels = ['WCBSDT','KPIXDT','WCNCDT','WJWDT','WBBMDT']

        '''
        get API call to the server passing random channel from list of channels and IFA,
        remove name parameter from the call if individual API calls are to be viewed
        '''

        with self.client.get(
            F'channel={random.choice(channels)}&show=TMS%2fEP018949880579&mediatime=2886849&airdate=2020-10-06T00%3a00%3a00Z&lts=0&sts=148012&mdl=300&signal=false&bundle=inscape.oar&ifa={ifa}&ifatype=vida&cua=OAR%2f1.0%2fVIZIO%2fTV&ts=2020-10-05T18%3a03%3a29.293-1&c=1154472659',
            name="adcuratio_get",catch_response=True) as response:
            if response.status_code == 0:
                print(response.status_code)
                response.success()

    


class Adcuratio_User(HttpUser):
    ''''''

    '''
    Here Tasks attribute is specified as a list, each time a task is to be performed,
    it will be randomly chosen from the tasks attribute
    '''
    tasks = [Adcuratio_UserBehaviour]

    host = ""


   





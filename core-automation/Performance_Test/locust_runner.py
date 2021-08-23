import os
import time
import authentication
import subprocess
from pathlib import Path
from selenium import webdriver
import requests
from selenium.webdriver.chrome.options import Options

select_server = {1: "LOCAL", 2: "REMOTE"}
print(select_server)
server = int(input("Please select the server for Performance Test : "))
min_wait = input("Minimum Wait : ")
max_wait = input("Maximum Wait : ")
worker = int(input("Enter the number of workers to start : "))

with open('data.txt', 'w') as file:
    file.writelines(min_wait+'\n')
    file.writelines(max_wait)
file.close()

with open('locust_master_script_runner.sh', 'r') as file1:
    # read a list of lines into data
    master_data = file1.readlines()
file1.close()

with open('locust_worker_script_runner.sh', 'r') as file2:
    # read a list of lines into data
    worker_data = file2.readlines()
file2.close()


def locust_bash_script(worker,locust_master_bash_script,locust_worker_bash_script):

    # Gives sudo authentication
    master_auth = subprocess.Popen(['echo', authentication.SUPER_USER_PASS], stdout=subprocess.PIPE, )
    subprocess.Popen(['chmod', 'u+r+x', locust_master_bash_script], shell=False, stdout=subprocess.PIPE, )

    worker_auth = subprocess.Popen(['echo', authentication.SUPER_USER_PASS], stdout=subprocess.PIPE, )
    subprocess.Popen(['chmod', 'u+r+x', locust_worker_bash_script], shell=False, stdout=subprocess.PIPE, )
    MASTER_SERVER_PATH = ""

    # Runs the bash script to start master
    with open('locust_master_script_runner.sh', 'w') as file:
        if select_server[server] == 'REMOTE':
            master_data[1] = MASTER_SERVER_PATH
            file.writelines(master_data)
            file.close()
            time.sleep(1)
            start_contain = subprocess.Popen(
                ['sudo', '-S', './' + str(locust_master_bash_script)], shell=False, text=True, stdin=master_auth.stdout,
                stdout=subprocess.PIPE,
            )
            start_contain.wait()
        if select_server[server] == 'LOCAL':
            master_data[1] = "python3 -m locust -f locustfile_adcuratio.py --master\n"
            file.writelines(master_data)
            file.close()
            os.system("sh " + str(locust_master_bash_script))

    WORKER_SERVER_PATH = ""
    # Runs the bash script to start worker
    with open('locust_worker_script_runner.sh', 'w') as file1:
        if select_server[server] == 'REMOTE':
            worker_data[1] = WORKER_SERVER_PATH
            file1.writelines(worker_data)
            file1.close()
            time.sleep(1)
            for i in range(worker):
                start_contain = subprocess.Popen(
                    ['sudo', '-S', './' + str(locust_worker_bash_script)], shell=False, text=True, stdin=worker_auth.stdout,
                    stdout=subprocess.PIPE,
                )
            start_contain.wait()
        if select_server[server] == 'LOCAL':
            worker_data[1] = "python3 -m locust -f locustfile_adcuratio.py --worker\n"
            file1.writelines(worker_data)
            file1.close()
            for i in range(worker):
                os.system("sh " + str(locust_worker_bash_script))

def start_locust():
    locust_master_bash_script = Path("locust_master.sh")
    locust_worker_bash_script = Path("locust_worker.sh")

    locust_bash_script(worker,locust_master_bash_script,locust_worker_bash_script)



#start_locust()
# start_locust_interface()




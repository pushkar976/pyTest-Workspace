# ReadMe for executing Locust Script.
	There are two scripts for Locust Execution.
####    1. locustfile_adcuratio.py

    This script is responsible for initialising the locust task and starting web interface at http://0.0.0.0:8089.

####    2. locust_runner.py

    - This script is responsible for running the locust in distributed manner. (Master and Slave)
    - Its takes few inputs like (Server to run, Minimum and Maximum wait time and Number of workers to start)
    - After taking these inputs it triggers the bash script which starts the locust in distributed mode.

## Running steps:

	1. Run the locust_runner.py.
	2. Provide desired inputs.
Above steps will trigger the commands based on the input provided.

#### 3. Command to run the locust on Web UI in master and worker mode:
  
#####Local:
    $ python3 -m locust -f locustfile_adcuratio.py --master
#####Remote:
    $ sudo ssh -t -i /home/pushkar/Desktop/server25 -p 21025 adcadmin@blackbox.adcuratio.org python3 -m locust -f locust_test.py --master

    NOTE: To run the locust in worker mode just replace "--master" with "--worker"

    
                            
#### 4. Command to run the locust on Terminal in master and worker mode:

    - python3 -m locust -f locustfile_adcuratio.py --headless -u 5000 -r 500 --run-time=30 --csv=Adcuratio_get  --master
    - python3 -m locust -f locustfile_adcuratio.py --worker

Here  -u : **Number of total users to simulate**, -r : **Spawn rate** (users spawned/second), --run-time(**duration of test execution in seconds**), --csv : **Save the reports in current directory**.

## Significance of authentication.py
	1. It is only to keep Sudo password at one place. Password is passed using subprocess.
	2. So for every execution we shouldn't need to enter password.
	3. Also for every master and worker terminal open we shouldn't need to enter password.
	

## Significance of data.txt
	1. This file is basically created to store minimum and maximum wait time.
    2. Python input function was taking input at each master and slave terminals before starting locust,
       and so for each terminals we had to explicitly give the max and min wait time manually.
    3. So to overcome this, data.txt is created and passed as below.
        
        $ gnome-terminal --maximize -- sh -c 'sh locust_worker_script_runner.sh <data.txt

    This command reads the data.txt and pass the containing min and max time in all the master and worker terminals automatically.


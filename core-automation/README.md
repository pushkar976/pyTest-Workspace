# Core-Automation
    
    It consist of core-module wise automation scripts.
    
**NOTE** : To know about the **scripts execution steps**. Please refer the Execution steps ReadMe under Utils folder.
# Modules
####  1. Deal Creation, Uplodation and Approval (UI)

    - Script shows the available user data(Agency, Adveriser, Brand, Channel and user admins) required to creates the deal file.
      User can select the data or can add new as well. 
      Flight start and end date is automatically set to the upcoming Monday, i.e 14 days ahead of the deal creation date. 
    
    - Script then opens up the Adcuration UI and uploads the created deal to the respective Agency/Advertiser admin.

    - Approves the uploaded deal from both Agency admin and Advertiser admin.

    - Checks if the deal is moved to the Approved tab.
    
####  2. Creative Download and Upload (API and UI)

    - Script shows the available user data(Agency, Adveriser, Brand, Sub-brand and user admins) required to upload the creative.
      User can select the data or can add new as well.
    
    - Based on the selected data, it extracts the user ids from the backend using get_company_list api.

    - It then ask user which company creative the user wants to upload and downloads the same.

    - Then using the Userid's it uploads the creative file to the associated advertiser or brand using upload_creative api

    - It then login's into the UI portal and verifies if the creative is been successfully uploaded or not.

####  3. Deal transfer through SFTP (Backend)

    - Script shows the available user data(Agency, Adveriser, Brand, Channel and user admins) required to creates the deal file.
      User can select the data or can add new as well. 
      Flight start and end date is automatically set to the upcoming Monday, i.e 14 days ahead of the deal creation date.

    - Calculates the md5sum of the created deal file.

    - Renames the deal file with md5sum value inserted.

    - Logins to sftp server and navigates to the location where deal file needs to be dropped.

    - Drops the deal file.
####  4. Performance test scripts for Api's

    - Script uses Locust as a performance tool.

    - It can test the API performance locally as well as on any server.
      **Currently the server is hardcoded to blackbox server url.**

    - It can run the test in master mode as well as in both master and worker mode.

    - It is capable of passing dynamic parameters to the API in run-time.
      **Currently handles dynamic parameters only for Vizio API's**

    - Upon executing, it creates a local server at 8089 port and provids a web-based interface for user interaction.

    - User can pass the Total number of users to simulate and User Sparwn/sec rate.

    - The Locust UI, shows the performance on every API hit, and provides the graphs and charts for user visualisation.

    - User can also download, the test reports and error reports from the Locust UI.

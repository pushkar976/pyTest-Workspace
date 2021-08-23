import authentication
import subprocess
import os
from pathlib import Path
import sys
path = os.path.dirname(__file__).split('/')
path.pop()
sys.path.append('/'.join(path))

# from adcuratio_UI_test.Utils import get_deal_json_file
from deal_script import get_deal_json_file

curr_dir = os.getcwd()
md5sum_deal = ""

def create_deal_file(agency,advertiser,brand):
    # Creates the deal file
    global md5sum_deal
    channel_code = get_deal_json_file.create_deal_json(agency,advertiser,brand)
    process_channel_code = subprocess.Popen(['echo', channel_code], stdout=subprocess.PIPE, )
    deal_creation_script_file,deal_json_file_path,deal_dir,md5sum_deal = get_deal_json_file.get_deal_dir()
    deal_creation_script_file = deal_creation_script_file+"/test_deal.py"
    deals_file_creation = subprocess.Popen(['python3', deal_creation_script_file], shell=False, text=True,
                                           stdin=process_channel_code.stdout, stdout=subprocess.PIPE,
                                           )
    deals_file_creation.wait()
    deal_creation_output = str(deals_file_creation.stdout.read().splitlines())
    deal_creation_output_list = deal_creation_output.split()

    # Extracts the deal file name from the subprocess output
    deal_file = deal_creation_output_list[20]
    split_deal_file_name = (deal_file.split("_"))
    if len(split_deal_file_name) == 3:
        deal_file = deal_creation_output_list[20] +" "+ deal_creation_output_list[21]
        split_deal_file_name = (deal_file.split("_"))
    return deal_file, split_deal_file_name, deal_dir


def create_deal_with_md5sum(deal_file, split_deal_file_name, deal_dir):
    advertiser_name = split_deal_file_name[2]
    # Check if Advertiser name has any space
    for a in advertiser_name:
        if (a.isspace()) is True:
            advertiser_name = "_".join(split_deal_file_name[2].split(" "))
            split_deal_file_name[2] = advertiser_name

    # Calculate the md5sum of the deal file
    deal_file_path = deal_dir+"/" + deal_file
    calculate_md5sum = subprocess.Popen(
        ['md5sum', deal_file_path], shell=False,
        text=True, stdout=subprocess.PIPE,
    )
    calculate_md5sum.wait()
    deal_md5sum = str(calculate_md5sum.stdout.read())
    md5sum = deal_md5sum.split()

    # Create new Deal file with md5sum
    split_deal_file_name[5] = 'md5sum'
    split_deal_file_name.append(md5sum[0])
    md5sum_deal_file_name = "_".join(split_deal_file_name) + ".xml"

    move_md5sum_deal = subprocess.Popen(
        ['mv', '-v', deal_file_path, md5sum_deal_file_name], shell=False, text=True, stdout=subprocess.PIPE,
    )
    move_md5sum_deal.wait()

    return md5sum_deal_file_name


def put_file_to_sftp_server(md5sum_deal_file_name):
    curr_work_dir = os.getcwd()
    sftp_bash_script_file = Path("./bash_scripts/run_sftp_script.sh")
    with open(sftp_bash_script_file, 'r') as file:
        # read a list of lines into data
        data = file.readlines()

    # Writes the put command in run_sftp_scripts.sh file

    md5sum_file = curr_work_dir+"/"+md5sum_deal_file_name
    data[4] = "put"+" "+str(md5sum_file) + "\n"

    if "EOF\n" not in data:
        data.append("EOF")

    with open('bash_scripts/run_sftp_script.sh', 'w') as file:
        file.writelines(data)

    # Gives sudo authentication
    process_auth = subprocess.Popen(['echo', authentication.SUPER_USER_PASS], stdout=subprocess.PIPE, )
    subprocess.Popen(['chmod', 'u+r+x', sftp_bash_script_file], shell=False, stdout=subprocess.PIPE, )

    # Runs the bash script to transfer file in sftp
    sftp_file_transfer_process = subprocess.Popen(
        ['sudo', '-S', './'+str(sftp_bash_script_file)], shell=False, text=True, stdin=process_auth.stdout,
        stdout=subprocess.PIPE,
    )
    sftp_file_transfer_process.wait()


def delete_md5sum_file(md5sum_deal_file_name):

    md5sum_file_path = md5sum_deal+"/"+md5sum_deal_file_name
    if os.path.exists(md5sum_file_path):
        os.remove(md5sum_file_path)
    else:
        print("The file does not exist")







import csv


def write_to_csv(csv_file,user,user_dmin,password):
    with open(csv_file,mode='w',newline='') as adc_cred:
        writer = csv.writer(adc_cred)
        writer.writerow([user,user_dmin,password])


def read_csv(csv_file):

    with open(csv_file,mode='r') as adc_cred:
        return adc_cred.readlines()


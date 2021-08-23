import pandas as pd
import os


class UserCredentials:
    def __init__(self,filename):
        pd.set_option('display.max_rows', 500)
        pd.set_option('display.max_columns', 500)
        pd.set_option('display.width', 1000)
        self.csv_filename = os.path.dirname(__file__)+'/'+filename
        print(self.csv_filename)
        self.admins = pd.read_csv(self.csv_filename)

    def display_user_details(self):
        self.admins.fillna(0, inplace=True)
        print(self.admins.head(20))

    def add_new_credentials(self,new_cred):
        self.admins = self.admins.append(new_cred, ignore_index=True)
        self.admins.fillna(0, inplace=True)
        self.admins.to_csv(self.csv_filename, index=False)

    def select_row_data(self,row):
        data = self.admins.iloc[row]
        print(data.to_string())
        return data

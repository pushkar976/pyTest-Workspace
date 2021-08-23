import sys
import os
path = os.path.dirname(__file__)
sys.path.append(path)
import execute_command as EC
from Utils import create_deal as CD


class TestDeal:
    def create_dealfile(self):
        data = CD.user_data()
        agency = data[0]
        advertiser = data[2]
        brand = data[4]

        self._created_deal_file, self._deal_file_split, self._deal_dir = EC.create_deal_file(agency,advertiser,brand)
        print("Newly created Deal file :",self._created_deal_file,self._deal_dir)
        return self._created_deal_file, self._deal_file_split, self._deal_dir

    def create_md5sum_deal(self):
        self._created_deal_file, self._deal_file_split, self._deal_dir = self.create_dealfile()
        self._md5sum_deal_file = EC.create_deal_with_md5sum(self._created_deal_file, self._deal_file_split, self._deal_dir)
        print("md5sum converted Deal file : ",self._md5sum_deal_file)
        return self._md5sum_deal_file

    def test_transfer_deal_to_sftp(self):
        self._md5sum_deal_file = self.create_md5sum_deal()
        EC.put_file_to_sftp_server(self._md5sum_deal_file)
        # EC.delete_md5sum_file(self._md5sum_deal_file)







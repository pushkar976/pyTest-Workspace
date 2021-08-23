from Utils.get_user import UserCredentials
class UserLoginData:

    def select_server(self):
        self.test_server = {"1": "LOCAL_SERVER", "2": "TEST_SERVER"}
        print(self.test_server)
        self.server_input = input("Select the server to test : ")
        return self.test_server[self.server_input]

    def select_user(self):
        self.user = {
            "1": "Network Admin",
            "2": "Super Admin",
            "3": "Agency Admin",
            "4": "Advertiser Admin",
            "5": "Dish operator Admin",
            "6": "Dish1 operator Admin",
            "7": "Xandr operator Admin",
            "8": "Xandr1 operator Admin"
        }
        print(self.user)
        self.select_usr = input("Please select the user to Login :")
        # self.select_usr = '3'
        # self.password = input("Please enter the {0} password :".format(self.user[self.select_usr]))
        return self.user[self.select_usr]

    def user_email(self):
        uc = UserCredentials()
        user = self.select_user()
        # self.password = 'Adcuratio@123'
        if user == "Super Admin":
            email = 'super_admin@adcuratio.com'
            password = input("Please enter the {0} password :".format(user))
            return user,email,password

        if user == 'Agency Admin':
            # agencyadmin_email = input("Please enter the {0} email :".format(user))
            agencyadmin_email = uc.select_agency_admin()
            adv_admin = uc.select_advertiserAdmin()
            password = input("Please enter the {0} password :".format(user))
            return user,agencyadmin_email,password,adv_admin



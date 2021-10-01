from file_handler import FileHandler
from hashlib import sha256
#import pandas as pd
import csv
import hashlib


class user:
    # file_handler_users = FileHandler("users.csv")
    # file_handler_products = FileHandler("product.csv")
    # file_handler_admin = FileHandler("admin.csv")
    # file_handler_receipts = FileHandler("receipt.csv")

    def __init__(self, username, password, loginstatus, signup):
        """create a new object when manager signs in or logs in"""
        self.username = username
        self.password = password
        self.loginstatus = loginstatus
        self.signup = signup

    def to_dict(self):
        return {"loginstatus": self.loginstatus, "username": self.username, "password": self.password}


class administartor(user):
    def __init__(self, name_shop, starttime_shop, endtime_shop, phonenumber_shop, owner_shop, username, password,loginstatus, signup):
        super().__init__(username, password, loginstatus, signup)
        self.name_shop = name_shop
        self.starttime_shop = starttime_shop
        self.endtime_shop = endtime_shop
        self.phonenumber_shop = phonenumber_shop
        self.owner_shop = owner_shop

    def add_file(self):  # file moshakhasat admin
        fields = ["name_shop", "starttime_shop", "endtime_shop", "phonenumber_shop", "owner_shop","username","password","loginstatus","signup"]
        with open("ListOfStores.csv", "a") as our_file:
            writer = csv.DictWriter(our_file, fieldnames=fields)
            if our_file.tell() == 0:
                writer.writeheader()
            writer.writerow(
                {"name_shop": self.name_shop, "starttime_shop": self.starttime_shop, "endtime_shop": self.endtime_shop,
                 "phonenumber_shop": self.phonenumber_shop, "owner_shop": self.owner_shop,"password":self.password,"loginstatus":self.loginstatus,"signup":self.signup})

    @staticmethod
    def signup_store():
        try:
            name_shop = input("nameshop")
            starttime_shop = int(input("starttime"))
            endtime_shop = int(input("starttime"))
            phonenumber_shop = input("phonnumber")
            loginstatus=None
            signup=None
        except TypeError as a:
            print(a)
        with open('users_customer.csv', 'r') as f:
            reader = csv.reader(f)
            find1 = False
            for row in reader:
                if row != []:
                    if row[0] == phonenumber_shop:
                        find1 = True
                        print("in mobile mojod ast ")
        if find1 != True:
            pass_signup_shop = input("password").encode()
            owner_shop = input("ownrshop")
            username = phonenumber_shop
            pas = pass_signup_shop
            fields = ["username", "password"]
            with open("users_admin.csv", "a") as our_file:
                writer = csv.DictWriter(our_file, fieldnames=fields)
                if our_file.tell() == 0:
                    writer.writeheader()
                writer.writerow({"username": username, "password": hashlib.sha256(pas).hexdigest()})
            store_new = administartor(name_shop, starttime_shop, endtime_shop, phonenumber_shop, owner_shop, username,pas, loginstatus, signup)
            store_new.add_file()


class coustomer(user):
    def __init__(self, customer_name, phone_number,username, password, loginstatus, signup):
        super().__init__(username, password, loginstatus, signup)
        self.customer_name = customer_name
        self.phone_number = phone_number
    def add_file(self):
        fields = ['customer_name',"phone_number","password","loginstatus","signup"]
        with open("Listofcostumeer.csv", "a") as our_file:
            writer = csv.DictWriter(our_file, fieldnames=fields)
            if our_file.tell() == 0:
                writer.writeheader()
            writer.writerow({"customer_name": self.customer_name, "phone_number": self.phone_number,"password":self.password,"loginstatus":self.loginstatus,"signup":self.signup})


    @staticmethod
    def signup_user():
        try:
            username_signup = input("user name")
            customer_name = input("customer_name")
            phone_number = int(input("phone_number"))
            password = int(input("password"))
            loginstatus=None
            signup=None
        except TypeError as a:
            print(a)
        with open('users_customer.csv', 'r') as f:
            reader = csv.reader(f)
            find2 = False
            for row in reader:
                if row != []:
                    if row[0] == username_signup:
                        find2 = True
                        print("in mobile mojod ast ")
        if find2 != True:
            pass_signup = input("password")
            repassword_signup = input("repassword")
            if repassword_signup != pass_signup:
                print("re password incorrect please try again \n")
                while repassword_signup != pass_signup:
                    repassword_signup = input("repassword")
            username = username_signup
            pas1 = pass_signup.encode()
            fields = ["username", "password", "active"]
            with open("users_customer.csv", "a") as our_file:
                writer = csv.DictWriter(our_file, fieldnames=fields)
                if our_file.tell() == 0:
                    writer.writeheader()
                writer.writerow({"username": username, "password": hashlib.sha256(pas1).hexdigest(), "active": 1})
            customer_new = coustomer(customer_name, phone_number,username, password, loginstatus, signup)
            customer_new.add_file()
    @staticmethod
    def login_user():
        username_login = input("user name")
        pass_login = input("password")
        username = username_login
        pas1 = pass_login
        result = sha256(pas1.encode())
        hashed = result.hexdigest()
        with open('users_customer.csv', 'r') as f:
            reader = csv.reader(f)
            find = False
            for row in reader:
                if row != []:
                    x = row[0].split(".")
                    row[0] = x[0]  # eslah shodeye inactivemon
                    if row[0] == username:
                        find = True
                        if hashed == row[1]:
                            if row[2] == "0.0":
                                print("you been banneded by admin")
                            else:
                                print("Correct")
                        else:
                            print("Wrong")
            if not find:
                print("There is not such a username!")

    @staticmethod
    def show_customer():
        with open("Listofcostumeer.csv", 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row != []:
                    print(row[0], row[1])

    @staticmethod
    def block_customer():
        customer_number = input("Enter customer Number:")
        with open('users_customer.csv', 'r') as f:
            reader = csv.reader(f)
            i = 0
            for row in reader:
                if row != []:
                    if row[0] != "username":
                        x = row[0].split(".")
                        if customer_number == x[0]:
                            df = pd.read_csv("users_customer.csv")
                            df.loc[i - 1, 'active'] = 0
                            df.to_csv("users_customer.csv", index=False)
                i += 1

# sample_admin=administartor("dorsa",8 ,21 ,"9122222222","alizade","9121111111", "123456","loginstatus","signup")
# sample_admin.add_file()
# sample_costomer=coustomer("kafsh",5,1000000,5000000,9125555555,123456,"","","","",",","")
# sample_costomer.add_file()

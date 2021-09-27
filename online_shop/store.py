import csv
import logging
import pandas as pd
import hashlib
import datetime
class Admin_users:
    def __init__(self,name_shop,starttime_shop ,endtime_shop ,phonenumber_shop,owner_shop):
        self.name_shop=name_shop
        self.starttime_shop=starttime_shop
        self.endtime_shop=endtime_shop
        self.phonenumber_shop=phonenumber_shop
        self.owner_shop=owner_shop
    def add_file(self):#file moshakhasat admin
        fields = ["name_shop", "starttime_shop", "endtime_shop", "phonenumber_shop", "owner_shop"]
        with open("ListOfStores.csv", "a") as our_file:
            writer = csv.DictWriter(our_file, fieldnames=fields)
            if our_file.tell() == 0:
                writer.writeheader()
            writer.writerow({"name_shop": self.name_shop,"starttime_shop":self.starttime_shop,"endtime_shop":self.endtime_shop,"phonenumber_shop":self.phonenumber_shop,"owner_shop":self.owner_shop})
class Add_product:
    def __init__(self,name,barcode ,quantity,price,brand):
        self.name = name
        self.barcode = barcode
        self.quantity = quantity
        self.price = price
        self.brand = brand
    def add_file(self,filename):
        fields = ["name","barcode","quantity","price","brand"]
        with open(filename, "a") as our_file:
            writer = csv.DictWriter(our_file, fieldnames=fields)
            if our_file.tell() == 0:
                writer.writeheader()
            writer.writerow({"name": self.name,"barcode":self.barcode,"quantity":self.quantity,"price":self.price,"brand":self.brand})

class factor:
    def __init__(self,customer_name,phone_number,barcode,serial_factor,product_name,quantity,price,all_price):
        self.customer_name = customer_name
        self.phone_number = phone_number
        self.barcode = barcode
        self.serial_factor = serial_factor
        self.product_name = product_name
        self.quantity = quantity
        self.price = price
        self.all_price = all_price

def read_factor(name_storage):
    with open(name_storage, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row != []:
                print(row)
def block_customer():
    customer_number=input("Enter customer Number:")
    with open('users_customer.csv', 'r') as f:
        reader = csv.reader(f)
        i=0
        for row in reader:
            if row != []:
                if row[0]!="username":
                    x=row[0].split(".")
                    if customer_number==x[0]:
                        df = pd.read_csv("users_customer.csv")
                        df.loc[i-1, 'active'] = 0
                        df.to_csv("users_customer.csv", index=False)
            i+=1
def signup_store():
    name_shop = input("nameshop")
    starttime_shop = int(input("starttime"))
    endtime_shop = int(input("starttime"))
    phonenumber_shop = input("phonnumber")

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
        store_new = Admin_users(name_shop, starttime_shop, endtime_shop, phonenumber_shop, owner_shop)
        store_new.add_file()
def add_product(name_storage):
    try:
        name = input("Enter product name = ")
        barcode = int(input("Enter product barcode = "))
        quantity = int(input("Enter product quantity = "))
        price = int(input("Enter product price = "))
        brand = input("Enter product brand = ")
    except TypeError as a:
        print("error")
    product = Add_product(name, barcode, quantity, price, brand)
    product.add_file(name_storage)
def show_quantity(name_storage):
    with open(name_storage, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row != []:

                logging.basicConfig(level=logging.DEBUG,
                                    filename="loging.log", filemode="w",
                                    format=" %(asctime)s — %(name)s — %(levelname)s — %(message)s \n",
                                    datefmt='%d-%b-%y %H:%M:%S')
                if row[2] != "quantity":
                    if int(row[2]) == 0:
                        logging.info(f'mahsole {row[0]}, tedade {row[2]} mojodi darad .')
                        print("etmam mojodi mahsol", row[0])

                print(row[0], " , ", row[2])
def search_factor(name_factor):
    search_type=int(input("if you want search factores with name type 1\nsearch factores with date type 2\n"))
    if search_type==1:
        search_username=input("Enter user name =  ")
        with open(name_factor, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row != []:
                    if row[1] != "phone_number":
                        x = row[1].split(".")
                        if search_username == x[0]:
                            print(row)
    if search_type==2:
        search_date_main=input("Enter Date like this 2021-07-05=")
        search_date_arr=search_date_main.split("-")
        search_date=datetime.date(int(search_date_arr[0]), int(search_date_arr[1]), int(search_date_arr[2]))
        with open(name_factor, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row != []:
                    if row[8] != "date":
                        x = row[8].split("-")
                        valid_date = datetime.date(int(x[0]), int(x[1]),int(x[2]))

                        if search_date >= valid_date:
                            print(row)
def show_customer(name_factor):
    with open(name_factor, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row != []:
                print(row[0],row[1])
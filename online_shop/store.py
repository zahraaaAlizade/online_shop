import csv
from csv import DictWriter
class Admin_users:
    mobilenumber=0
    def __init__(self,name_shop,starttime_shop ,endtime_shop ,phonenumber_shop,owner_shop):
        self.name_shop=name_shop
        self.starttime_shop=starttime_shop
        self.endtime_shop=endtime_shop
        self.phonenumber_shop=phonenumber_shop
        self.owner_shop=owner_shop
        Admin_users.mobilenumber=phonenumber_shop
    def add_file(self):
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





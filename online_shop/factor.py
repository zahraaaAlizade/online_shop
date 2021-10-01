import csv
import datetime
class factor:
    def __init__(self,customer_name,phone_number,barcode,serial_factor,product_name,quantity,price):
        self.customer_name = customer_name
        self.phone_number = phone_number
        self.barcode = barcode
        self.serial_factor = serial_factor
        self.product_name = product_name
        self.quantity = quantity
        self.price = price

    def add_file(self):
        fields = ["customer_name","phone_number","barcode","serial_factor","product_name","quantity","price"]
        with open("ListOfFactor.csv", "a") as our_file:
            writer = csv.DictWriter(our_file, fieldnames=fields)
            if our_file.tell() == 0:
                writer.writeheader()
            writer.writerow({"customer_name": self.customer_name, "phone_number": self.phone_number, "barcode": self.barcode,
                 "serial_factor": self.serial_factor,"product_name": self.product_name,"quantity": self.quantity,"price": self.price})

    @staticmethod
    def read_factor(name_storage):
        with open(name_storage, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row != []:
                    print(row)
    @staticmethod
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



from datetime import time
from datetime import datetime
import logging
import csv
import hashlib

import product
logging.basicConfig(level=logging.DEBUG,
                        filename="loging.log", filemode="w",
                        format=" %(asctime)s — %(name)s — %(levelname)s — %(message)s \n",
                        datefmt='%d-%b-%y %H:%M:%S')

class user:

    def __init__(self, username, password,roll):
        """create a new object when manager signs in or logs in"""
        self.username = username
        self.password = password
        self.roll = roll

class Administartor(user):
    def __init__(self, username, password,roll):
        super().__init__(username, password,roll)
    def add_file(self):
        hash_pass = hashlib.sha256(self.password.encode('utf-8')).hexdigest()
        with open("customer_admin.csv", "a") as our_file:
            fields = ["username", "password", "roll"]
            writer = csv.DictWriter(our_file, fieldnames=fields)
            admin=[{"username":self.username,"password":hash_pass,"roll":self.roll}]
            if our_file.tell() == 0:
                writer.writeheader()
            writer.writerows(admin)
        logging.info("user add nashode ast")
    @staticmethod
    def signup_store(username):
        try:
            name_shop = input("nameshop")
            starttime_shop = time(int(input("starttime")))
            endtime_shop = time(int(input("endtime")))
            roll=input("roll")
            with open('customer_admin.csv', 'r') as f:
                reader = csv.reader(f)
                lst=list(reader)
                for dic in lst:
                    if dic!=[]:
                        if dic[0]==username:
                            with open("customer_admin.csv", "a") as our_file:
                                fields = ["username", "name_shop", "starttime_shop", "endtime_shop", "roll"]
                                writer = csv.DictWriter(our_file, fieldnames=fields)
                                CA=[{"username":username,"name_shop":name_shop,"starttime_shop":starttime_shop,"endtime_shop":endtime_shop,"roll":roll}]
                                if our_file.tell() == 0:
                                    writer.writeheader()
                                writer.writerows(CA)
            logging.info("foroshgah vared nashode")
        except Exception as a:
            print(a)

    @staticmethod
    def login_admin(username, password):
        try:
            hash_pass = hashlib.sha256(password.encode('utf-8')).hexdigest()
            with open('customer_admin.csv', 'r') as f:
                reader = csv.reader(f)
                lst = list(reader)
                find_store=0
                for dic in lst:
                    if dic!=[]:
                        if dic[0] == username and dic[1] == hash_pass:
                            find_store+=1
                        elif dic[0]==username:
                            find_store += 1
                            if find_store == 2:
                                shop_name=dic[1]
                                Administartor.show_dastresi(username,shop_name)

                if find_store==1:

                    Administartor.signup_store(username)
            logging.info("admin nist")
        except Exception as a:
            print(a)
    @staticmethod
    def show_dastresi(username,shop_name):
        try:
            with open('customer_admin.csv', 'r') as f:
                reader = csv.reader(f)
                lst = list(reader)
                find_store=0
                for dic in lst:
                    if dic != []:
                        if dic[0] == username:
                            find_store = 1
                            print("hello", dic[0], "welcome to the manager side ")
                            manager_side_option=int(input("if you want add new product type 1 :\nif you want see the storage quantity type 2 :\nsee factors type 3  :\nsee customer type 4 :\nblock a customer type 5 :\nexit type 6\n"))
                            if manager_side_option==1:
                                name = input("Enter product name = ")
                                barcode = int(input("Enter product barcode = "))
                                name_shop = input("Enter name_shop = ")
                                quantity = int(input("Enter product quantity = "))
                                price = int(input("Enter product price = "))
                                brand = input("Enter product brand = ")
                                new_product=product.Product(username,name, barcode,name_shop, quantity, price, brand)
                                new_product.add_file()
                                Administartor.show_dastresi(username, shop_name)
                            elif manager_side_option==2:
                                product.Product.show_quantity(username)
                                Administartor.show_dastresi(username,shop_name)
                            elif manager_side_option == 3:
                                Administartor.read_factor(shop_name)
                                Administartor.show_dastresi(username, shop_name)
                            elif manager_side_option==4:
                                Customer.show_customer()
                                Administartor.show_dastresi(username, shop_name)
                            elif manager_side_option==5:
                                pass
                            elif manager_side_option==6:
                                exit()
                if find_store==0:
                    Administartor.signup_store(username)

        except Exception as a:
            print(a)

    @staticmethod
    def read_factor(shop_name):
        with open("factor.csv", 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row != []:
                    if row[0]==shop_name:
                        print (row)



class Customer(user):
    def __init__(self,username, password,roll):
        super().__init__(username, password,roll)
    def add_file(self):
        with open("customer_admin.csv", "a") as our_file:
            hash_pass = hashlib.sha256(self.password.encode('utf-8')).hexdigest()
            fields = ["username", "password", "roll"]
            writer = csv.DictWriter(our_file, fieldnames=fields)
            customer = [{"username": self.username, "password": hash_pass, "roll": self.roll}]
            if our_file.tell() == 0:
                writer.writeheader()
            writer.writerows(customer)
    logging.info("user vared nashode")

    @staticmethod
    def login_customer(username,password):

            hash_pass = hashlib.sha256(password.encode('utf-8')).hexdigest()
            with open('customer_admin.csv', 'r') as f:
                reader = csv.reader(f)
                lst=list(reader)
                for dic in lst:
                    if dic != []:

                        if dic[0]==username and dic[1]==hash_pass:
                            if dic[2]=="customer":
                                print("hello", dic[0], "welcome to the customer side ")
                                customer_side_option = int(input(
                                    "see factor type 1 :\nsee store type 2 :\nsearch store type 3 : \nselection stor type 4 :\nsee pruduct type 5 :\nselection product type 6:\nconfirm purchase type 7:\nexit type 8:\n"))
                                if customer_side_option == 1:
                                    Customer.read_factor(username)
                                elif customer_side_option == 2:
                                    Customer.show_stor()
                                    Customer.login_customer(username, password)
                                elif customer_side_option == 3:
                                    Customer.search_store()
                                    Customer.login_customer(username, password)
                                elif customer_side_option==4:
                                    search = input("store name")
                                    Customer.selection_stor(search)
                                    Customer.login_customer(username, password)
                                elif customer_side_option==5:
                                    search = input("store name")
                                    Customer.see_product_stor(search)
                                    Customer.login_customer(username, password)
                                elif customer_side_option ==6:
                                    name_shop = input("nameshop")
                                    name_product = input("product_name")
                                    quantity_product = input("quantity")
                                    Customer.selection_product(name_shop, name_product,quantity_product,username)
                                    Customer.login_customer(username, password)
                                elif customer_side_option==7:
                                    pass


    @staticmethod
    def show_customer():
        try:
            with open("customer_admin.csv", 'r') as f:
                reader = csv.reader(f)
                lst = list(reader)
                for dic in lst:
                    if dic != []:
                        if dic[2] == "customer":
                            print( dic[0] , dic[2])
        except Exception as a:
            print(a)

    @staticmethod
    def read_factor(username):
        with open("factor.csv", 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row != []:
                    if row[0] == username:
                        print(row)


    @staticmethod
    def show_stor():
        try:
            with open("customer_admin.csv", 'r') as f:
                reader = csv.reader(f)
                lst = list(reader)
                now=datetime.now()
                b=str(time(now.hour,now.minute))
                for dic in lst:
                    if dic != []:
                        if dic[2] < b < dic[3]:
                            if dic[4] == "admin":
                                print(dic[1], dic[2],dic[3])
        except Exception as a:
            print(a)
    @staticmethod
    def search_store():
        search = input("store name")
        with open("customer_admin.csv", 'r') as f:
            reader = csv.reader(f)
            lst = list(reader)
            find=0
            for dic in lst:
                if dic != []:
                    if search==dic[1]:
                        find+=1
                        print(dic[1],dic[2],dic[3])
            if find==0:
                print("mojod nist")


    @staticmethod
    def selection_stor(search):
        try:
            with open("customer_admin.csv", 'r') as f:
                reader = csv.reader(f)
                lst = list(reader)
                find = 0
                for dic in lst:
                    if dic != []:
                        if search == dic[1]:
                            find += 1
                            print(dic[1], dic[2], dic[3])
                if find == 0:
                    print("mojod nist")
        except Exception as a:
            print(a)

    @staticmethod
    def see_product_stor(search):
        try:
            with open("product.csv", 'r') as f:
                reader = csv.reader(f)
                lst = list(reader)
                find = 0
                for dic in lst:
                    if dic != []:
                        if search == dic[3]:
                            find+=1
                            print(dic[1], dic[5], dic[6])
        except Exception as a:
            print(a)




    @staticmethod
    def selection_product(name_shop,name_product,quantity,username):
        f = open('product.csv', 'r')
        reader = csv.reader(f)
        mylist = list(reader)
        f.close()


        with open("product.csv", 'r') as f:
            reader = csv.reader(f)
            lst = list(reader)
            lst1=[]
            x=0
            for dic in lst:
                x+=1
                if dic != []:
                    if name_product==dic[1] and name_shop==dic[3] :


                        if quantity < dic[4]:

                            dic[4]=int(dic[4])-int(quantity)
                            mylist[x - 1][4] =dic[4]
                            price=dic[5]
                            price_all=(int(quantity)*int(price))
                            print(price_all)
                            with open("factor.csv", "a") as our_file:
                                fields = ["name_shop", "name_product", "quantity","price","price_all", "username"]
                                writer = csv.DictWriter(our_file, fieldnames=fields)
                                admin = [{"name_shop": name_shop, "name_product": name_product, "quantity": quantity,"price": price,"price_all": price_all,"username":username}]
                                if our_file.tell() == 0:
                                    writer.writeheader()
                                writer.writerows(admin)

        my_new_list = open('product.csv', 'w', newline='')
        csv_writer = csv.writer(my_new_list)
        csv_writer.writerows(mylist)
        my_new_list.close()











    @staticmethod
    def confirmpurchase():
        pass


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

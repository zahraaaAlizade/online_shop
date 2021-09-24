import store
import hashlib
from hashlib import sha256
import csv
Home=int(input("welcome to the online_shop\n1.Sign Up \n2.log in\n3.exit\n"))
if Home==1:
    signup_home = int(input("1.user\n2.admin\n"))
    if signup_home==1:
        username_signup = input("user name")
        with open('users_customer.csv', 'r') as f:
            reader = csv.reader(f)
            find2 = False
            for row in reader:
                if row != []:
                    if row[0] == username_signup:
                        find2 = True
                        print("in mobile mojod ast ")
        if find2!=True:
            pass_signup = input("password")
            repassword_signup=input("repassword")
            if repassword_signup!=pass_signup:
                print("re password incorrect please try again \n")
                while repassword_signup!=pass_signup:
                    repassword_signup = input("repassword")
            username = username_signup
            pas1 = pass_signup.encode()
            fields = ["username", "password"]
            with open("users_customer.csv", "a") as our_file:
                writer = csv.DictWriter(our_file, fieldnames=fields)
                if our_file.tell() == 0:
                    writer.writeheader()
                writer.writerow({"username": username, "password": hashlib.sha256(pas1).hexdigest()})

    elif signup_home==2:
        name_shop=input("nameshop")
        starttime_shop=int(input("starttime"))
        endtime_shop=int(input("starttime"))
        phonenumber_shop=input("phonnumber")

        with open('users_customer.csv', 'r') as f:
            reader = csv.reader(f)
            find1 = False
            for row in reader:
                if row != []:
                    if row[0] == phonenumber_shop:
                        find1 = True
                        print("in mobile mojod ast ")
        if find1!=True:
            pass_signup_shop = input("password").encode()
            owner_shop=input("ownrshop")
            username = phonenumber_shop
            pas = pass_signup_shop
            fields = ["username", "password"]
            with open("users_admin.csv", "a") as our_file:
                writer = csv.DictWriter(our_file, fieldnames=fields)
                if our_file.tell() == 0:
                    writer.writeheader()
                writer.writerow({"username": username, "password": hashlib.sha256(pas).hexdigest()})
            store_new=store.Admin_users(name_shop,starttime_shop,endtime_shop,phonenumber_shop,owner_shop)
            store_new.add_file()

elif Home==2:
    login_home = int(input("1.user\n2.admin\n"))
    if login_home == 1:
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
                    if row[0] == username:
                        find = True
                        if hashed == row[1]:
                            print("Correct")
                        else:
                            print("Wrong")
            if not find:
                print("There is not such a username!")
    if login_home == 2:
        username_login1 = input("user name")
        pass_login1 = input("password")
        username1 = username_login1
        pas2 = pass_login1
        result1 = sha256(pas2.encode())
        hashed1 = result1.hexdigest()
        with open('users_admin.csv', 'r') as f:
            reader = csv.reader(f)
            find = False
            for row in reader:
                if row != []:
                    if row[0] == username1:
                        find = True
                        if hashed1 == row[1]:
                            with open('ListOfStores.csv', 'r') as f:
                                reader = csv.reader(f)
                                for row in reader:
                                    if row != []:

                                        if row[3] == username1:
                                            print("hello",row[4],"welcome to the ",row[0]," manager side ")
                                            manager_side_option=int(input("if you want add new product type 1 :\nif you want see the storage quantity type 2 :\nsee factors type 3 : \nsearch factor type 4 :\nsee customer type 5 :\nblock a customer type 6 :\nexit type 7\n"))
                                            name_storage = (f'{username1}_storage.csv')
                                            name_factor = (f'{username1}_factor.csv')
                                            if manager_side_option==1:
                                                name=input("Enter product name = ")
                                                barcode=int(input("Enter product barcode = "))
                                                quantity=int(input("Enter product quantity = "))
                                                price=int(input("Enter product price = "))
                                                brand=input("Enter product brand = ")
                                                product=store.Add_product(name,barcode,quantity,price,brand)
                                                product.add_file(name_storage)
                                            elif manager_side_option==2:
                                                with open(name_storage, 'r') as f:
                                                    reader = csv.reader(f)
                                                    for row in reader:
                                                        if row != []:
                                                            print(row[0]," , ",row[2])
                                            elif manager_side_option==3:
                                                store.read_factor(name_factor)




                        else:
                            print("Wrong")
            if not find:
                print("There is not such a username!")
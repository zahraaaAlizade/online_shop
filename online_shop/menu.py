
import store
from hashlib import sha256
import csv
import customer
def main_menu():
    Home=int(input("welcome to the online_shop\n1.Sign Up \n2.log in\n3.exit\n"))
    if Home==1:
        signup_home = int(input("1.user\n2.admin\n"))
        if signup_home==1:
            customer.signup_user()#dakhel  filecustomer amaliat tabtenam moshtariro anjam mide va dakhel yek file csv zakhire mikonad
        elif signup_home==2:
            store.signup_store()#dakhel file store amaliat ro anjam mide
        main_menu()
    elif Home==2:
        login_home = int(input("1.user\n2.admin\n"))
        if login_home == 1:
            customer.login_user()
        if login_home == 2:
            username_login1 = input("user name")
            pass_login1 = input("password")
            username1 = username_login1
            pas2 = pass_login1
            result1 = sha256(pas2.encode())
            hashed1 = result1.hexdigest()#zakhire password hash shode
            with open('users_admin.csv', 'r') as f:
                reader = csv.reader(f)
                find = False
                for row in reader:
                    if row != []:#mokhalef khali bod
                        if row[0] == username1:
                            find = True
                            if hashed1 == row[1]:#pas hayi ke hash shodan
                                with open('ListOfStores.csv', 'r') as f:
                                    reader = csv.reader(f)
                                    for row in reader:
                                        if row != []:
                                            if row[3] == username1:
                                                manager_side_option=0
                                                while manager_side_option!=7:
                                                    print("hello",row[4],"welcome to the ",row[0]," manager side ")
                                                    manager_side_option=int(input("if you want add new product type 1 :\nif you want see the storage quantity type 2 :\nsee factors type 3 : \nsearch factor type 4 :\nsee customer type 5 :\nblock a customer type 6 :\nexit type 7\n"))
                                                    name_storage = (f'{username1}_storage.csv')
                                                    name_factor = (f'{username1}_factor.csv')
                                                    if manager_side_option==1:
                                                        store.add_product(name_storage)
                                                    elif manager_side_option==2:
                                                        store.show_quantity(name_storage)
                                                    elif manager_side_option==3:
                                                        store.read_factor(name_factor)
                                                    elif manager_side_option==4:
                                                        store.search_factor(name_factor)
                                                    elif manager_side_option==5:
                                                        store.show_customer(name_factor)
                                                    elif manager_side_option==6:
                                                        store.block_customer()
                                                    elif manager_side_option==7:
                                                        main_menu()
                            else:
                                print("Wrong")
                if not find:
                    print("There is not such a username!")
        main_menu()
    elif Home==3:
        print("thank's for you're time ")
main_menu()
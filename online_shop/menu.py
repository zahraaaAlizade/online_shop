
from admin import Customer
from admin import Administartor
def main_menu():
    Home=int(input("welcome to the online_shop\n1.Sign Up \n2.log in\n3.exit\n"))
    if Home==1:
        signup_home = int(input("1.user\n2.admin\n"))
        if signup_home==1:
            username=input("username")
            password=input("password")
            roll=input("roll")
            sampel_customer=Customer(username,password,roll)
            sampel_customer.add_file()
        elif signup_home==2:
            username1 = int(input("username"))
            password1 = input("password")
            roll1 = input("roll")
            sampel_admin = Administartor(username1, password1, roll1)
            sampel_admin.add_file()

        main_menu()
    elif Home==2:
        login_home = int(input("1.user\n2.admin\n"))
        if login_home == 1:
            username = input("username")
            password = input("password")
            roll = input("roll")
            sampel_customer = Customer(username, password,roll)
            sampel_customer.login_customer(username,password)
        elif login_home == 2:
            username = input("username")
            password = input("password")
            roll = input("roll")
            sampel_admin = Administartor(username, password, roll)
            sampel_admin.login_admin(username, password)

main_menu()
import hashlib
import main
from hashlib import sha256

import csv
def signup_user():
    username_signup = input("user name")
    main.validate_phone(username_signup)
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
def login_user():
    username_login = input("user name")
    main.validate_phone(username_login)
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
                row[0] = x[0]

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
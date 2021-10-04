import csv
import logging
class Product:
    def __init__(self,username,name, barcode,name_shop, quantity, price, brand):
        self.username=username
        self.barcode = barcode
        self.price = price
        self.brand = brand
        self.name = name
        self.quantity = quantity
        self.name_shop = name_shop


    def add_file(self):
        with open("product.csv", "a") as our_file:
            fields = ["username", "name", "barcode", "name_shop","quantity", "price", "brand"]
            writer = csv.DictWriter(our_file, fieldnames=fields)
            product=[{"username": self.username, "name": self.name, "barcode": self.barcode,
                 "name_shop": self.name_shop,"quantity": self.quantity,"price": self.price,"brand": self.brand}]
            if our_file.tell() == 0:
                writer.writeheader()
            writer.writerows(product)


    @staticmethod
    def show_quantity(username):
        with open("product.csv", 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row != []:
                    if row[0]==username:
                        logging.basicConfig(level=logging.DEBUG,
                                            filename="loging.log", filemode="w",
                                            format=" %(asctime)s — %(name)s — %(levelname)s — %(message)s \n",
                                            datefmt='%d-%b-%y %H:%M:%S')
                        if row[4] != "quantity":
                            if int(row[4]) == 0:
                                logging.info(f'mahsole {row[1]}, tedade {row[4]} mojodi darad .')
                                print("etmam mojodi mahsol", row[1])

                        print(row[1], " , ", row[4])

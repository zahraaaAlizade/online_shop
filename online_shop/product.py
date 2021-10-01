import csv
import logging
class Product:
    def __init__(self,name, barcode, quantity, price, brand,expiration_date):
        self.barcode = barcode
        self.price = price
        self.brand = brand
        self.name = name
        self.quantity = quantity
        self.expiration_date = expiration_date
        #self.__dict__.update({k: v for k, v in kwargs.items()})

    def add_file(self,filename):
        fields = ["name","barcode","quantity","price","brand","expiration_date"]
        with open(filename, "a") as our_file:
            writer = csv.DictWriter(our_file, fieldnames=fields)
            if our_file.tell() == 0:
                writer.writeheader()
            writer.writerow({"name": self.name,"barcode":self.barcode,"quantity":self.quantity,"price":self.price,"brand":self.brand,"expiration_date":self.expiration_date})
    @staticmethod
    def add_product(name_storage):
        try:
            name = input("Enter product name = ")
            barcode = int(input("Enter product barcode = "))
            quantity = int(input("Enter product quantity = "))
            price = int(input("Enter product price = "))
            brand = input("Enter product brand = ")
            expiration_date=input("Enter product expiration_date = ")
        except TypeError as a:
            print(a)
        product = Product(name, barcode, quantity, price, brand,expiration_date)
        product.add_file(name_storage)
    @staticmethod
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

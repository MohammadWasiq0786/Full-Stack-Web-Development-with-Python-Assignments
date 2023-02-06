#  Write a python program to create a Laptop class with 4 attributes (brand, ram, cpu,
# hdd) and 2 methods (showConfig() to print the values, __init__() to initialize the values).

class laptop:
    def __init__(self,brand,ram,cpu,hdd) -> None:
        self.brand=brand
        self.wasiq=wasiq
        self.cpu=cpu
        self.hdd=hdd

    def showConfig(self):
        print("Brand : ",self.brand)
        print("Wasiq : ",self.wasiq)
        print("Cpu : ",self.cpu)
        print("Hdd : ",self.hdd)


user1=laptop("Apple","8gb","m1","500gb")
user2=laptop("Lenovo",'16gb','i5','1tb')

user1.showConfig()
user2.showConfig()
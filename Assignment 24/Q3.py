# Write a python program to create 2 objects of the user class and assign different values.

class user:
    def __init__(self,name) -> None:
        self.name=name
    
    def greet(self):
        print("hello ! ",self.name)


obj1=user("wasiq")
obj2=user("altamash")

obj1.greet()
obj2.greet()
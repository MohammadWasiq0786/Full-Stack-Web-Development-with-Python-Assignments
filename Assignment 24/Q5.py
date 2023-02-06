# Write a python program to delete the age property of the user

class user:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def showdata(self):
        print("Name :" ,self.name)
        print("Age ; ",self.age)


obj1=user("Wasiq",22)
obj2=user("Altamash",20)

obj1.showdata()
obj2.showdata()

del obj1.age
del obj2.age


#  Write a python script to create a SmartPhone class by inheriting Calculator 2.0 and Phone Class.

class Phone:
    def calling(self):
        print("Calling..........")
    
    def sms(self):
        print("SMS...........")

class Calculator:

    def __init__(self) -> None:
        self.x=None
        self.y=None
    
    def setdata(self, x, y):
        self.x=x
        self.y=y
    
    def adding(self):
        return self.x+self.y
    
    def subtracting(self):
        return self.x-self.y

class Calculator2(Calculator):
    def multiplication(self):
        return self.x*self.y

    def division(self):
        return self.x/self.y

class Smartphone(Calculator2,Phone):
    pass

obj=Smartphone()
obj.setdata(6,3)
print(obj.division())
obj.calling()

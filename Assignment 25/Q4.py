#  Write a python script to update 2nd Question, add a class variable (platform) and create a classmethod to access it.


import profile


class Profile:
    platform='INEURON'
    @classmethod
    def getplatform(cls):
        return cls.platform


    def __init__(self) -> None:
        self.name=None
        self.__age=None
        self.__email=None

    def setdata(self,name,email,age):
        self.name=name
        self.__age=age
        self.__email=email

    def getdata(self):
        print(self.name)
        print(self.__email)
        print(self.__age)
        
    
obj=Profile()

obj.setdata('Wasiq', 'mohammadwasiq0786@gmail.com', 22)
print("instance variables are : ")
obj.getdata()
print("class variable are : ")
print(Profile.getplatform())
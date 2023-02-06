#  Write a python program to create a School class and 3 instance variables and 1 class variable


class school:
    school='iNeuron'
    
    def __init__(self,name,age,gender) -> None:
        self.name=name
        self.age=age
        self.gender=gender

    def showdata(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
        print("Gender : ",self.gender)
        print("School : ",self.school)


user1=school('Wasiq',22,'Male')
user2=school("Aurat",20,'Female')
user3=school("Altamash",19,'Male')

user1.showdata()
user2.showdata()
user3.showdata()
#  Define a class Employee with instance object variables empid, name, salary. Write
# __init__() method in the class to initialize instance object variables. Also define
# instance methods to input fields and display field values

class Employee:

    def __init__(self) -> None:
        self.empid=0
        self.name=0
        self.salary=0
    
    def input(self,id,name,salary):
        self.empid=id
        self.name=name
        self.salary=salary
    
    def display(self):
        print("Emp_Id :",self.empid)
        print("Name : ",self.name)
        print("Salary : ",self.salary)


user1= Employee()
user2= Employee()

user1.input("101","Wasiq",10000000)
user2.input("203","Altamash",8000000)

user1.display()
user2.display()


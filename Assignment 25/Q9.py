#  Write a python script to create an application like Truecaller where names and
# numbers are stored. Truecaller class will have 2 methods (1st to fetch the name of a number and 2nd to add a new entry).

class truecaller:

    

    def __init__(self) -> None:
        self.data={'9876543210':"Wasiq",'9988776655':"Altamash","9878767890":"Zainul"}

    # @staticmethod
    def add_data(self,key,value):
        self.data[key]=value

    # @staticmethod
    def fetch(self,key):
        return self.data[key]


obj=truecaller()
while True:
    print("*"*51)
    print("Press 1 for fetch the name ")
    print("Press 2 for add entry ")
    print("Press any other for exit ")
    print("*"*51)
    choice=int(input("Enter the choice : "))
    if choice==1:
        num=input("Enter the number : ")
        print("Name : ",obj.fetch(num))
    elif choice==2:
        num=input("Number : ")
        name=input("Name : ")
        obj.add_data(num,name)
    else:
        break

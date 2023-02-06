#  Write a python program to create a user class with 3 properties : name, age, email.

class user:
    def __init__(self,name,age,email) -> None:
        self.name=name
        self.age=age
        self.email=email
    
    def showdata(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
        print("Email : ",self.email)


wasiq=user('Wasiq',22,"mohammadwasiq0786@gmail.com")
altamash=user("Altamash",20,"altamash0143@mail.com")

wasiq.showdata()
altamash.showdata()

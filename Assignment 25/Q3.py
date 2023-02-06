# Write a python script to update 2nd Question, change email and age to __email and __age

class Profile:
    def __init__(self, name, email, age) -> None:
        self.name=name
        self.__age=age
        self.__email=email
    
    def show(self):
        print(self.name)
        print(self.__email)
        print(self.__age)
        
    

obj1=Profile('Wasiq', 'mohammadwasiq0786@gmail.com', 22)

obj1.name='Altamash'
obj1.email='altamash143@gmail.com'
obj1.age=20

obj1.show()
# Write a python script to update the above Profile class with encapsulation

class Profile:
    def __init__(self,name,email,age) -> None:
        self.name=name
        self.age=age
        self.email=email
    
    def show(self):
        print(self.name)
        print(self.email)
        print(self.age)
        
    

obj1=Profile('Wasiq', 'mohammadwasiq0786@gmail.com', 22)
obj1.show()
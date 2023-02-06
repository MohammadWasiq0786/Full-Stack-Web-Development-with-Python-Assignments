# Write a python script to create a Profile class with 3 attributes (name, email, age)

class Profile:
    def __init__(self,name,email,age) -> None:
        self.name=name
        self.age=age
        self.email=email
    

obj1= Profile('Wasiq', 'mohammadwasiq0786@gmail.com', 22)
# Write a python program to create a user class with a method to greet the user.

class user:
    def __init__(self,name):
        self.name=name
    
    def greet(self):
        print("Welcome ! ",self.name)


user1_name=input("Enter the name of user 1 : ")
user1=user(user1_name)
user2_name=input("Enter the name of user 2 : ")
user2=user(user2_name)

user1.greet()
user2.greet()
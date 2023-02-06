#  Write a python program to init default values for user object using __init__ method.

class company:
    def __init__(self):
        self.company="Google"
    

user1=company()
user2=company()

print("default value of user 1 are : ",user1.company)
print("default value of user 2 are : ",user2.company)

# Write a python program to create 3 user objects and find the youngest of all.

class user:
    def __init__(self,age):
        self.age=age


user1_age=int(input("Enter the age of user 1 : "))
user1=user(user1_age)

user2_age=int(input("Enter the age of user 2 : "))
user2=user(user2_age)

user3_age=int(input("Enter the age of user 3 : "))
user3=user(user3_age)

youngest=min(user1.age,user2.age,user3.age)
 
if youngest==user1_age:
    youngest_user="user1"
elif youngest==user2_age:
    youngest_user='user2'
else:
    youngest_user='user3'

print("Youngest age are : ",youngest," of ",youngest_user)



# Write a Python script to create a list of city names taken from the user

lis=[]

print("Enter the name of city :")
print("Press 0 to exit ")
while True:
    x=input()
    if x!='0':
        lis.append(x)
    else:
        break

print("list of city are : ",lis)

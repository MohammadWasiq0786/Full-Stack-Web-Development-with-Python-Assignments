# Write a python program to create a function and print a list where the values are square of numbers between 1 and 30.


def printvalue():
    lis=[]
    for i in range(1,31):
        lis.append(i**2)
    print(lis)

printvalue()

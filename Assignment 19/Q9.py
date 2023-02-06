#  Write a python program to create a function to check whether a number falls in a given range

def check(num,ran):
    for i in ran:
        if num==i:
            print("number is falling in a given range ")
            break
    else:
        print("number is not falling in the given range ")

num= int(input("Enter the number : "))
a= int(input("Enter the starting range : "))
b= int(input("Enter the ending range : "))
check(num,range(a,b+1))


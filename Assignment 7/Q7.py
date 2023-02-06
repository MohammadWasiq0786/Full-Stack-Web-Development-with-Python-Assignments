# Write a python program to check whether a given number is positive, negative or zero using match case statement

num= int(input("enter the number :"))
match num:
    case 0:
        print("Zero")
    case _ if num>0:
        print("Positive ")
    case _ if num<0:
        print("Negative ")
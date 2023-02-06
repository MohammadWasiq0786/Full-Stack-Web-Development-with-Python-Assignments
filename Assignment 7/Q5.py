# . Write a program which takes a number from user. Print Saurabh Shukla if the number
# is even, print Prateek Jain if the number is negative odd number and print Aditya
# Choudhary if number is positive odd number.

num= int(input("Enter a number :"))
x=num%2
match x:
    case 0:
        print("Saurabh Shukla")
    case _ if num<0 and x!=0:
        print("Prateek Jain")
    case _ if num>0 and x!=0:
        print("Aditya Choudhary")
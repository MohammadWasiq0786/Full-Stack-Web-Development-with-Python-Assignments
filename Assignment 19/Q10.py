#  Write a python program to create a function to check whether a given number is even or odd.

def fun(num):
    if num%2==0:
        print("Number is even number i.e ", num)
    else:
        print("Number is odd number i.e ", num)

num=int(input("Enter the number : "))
fun(num)
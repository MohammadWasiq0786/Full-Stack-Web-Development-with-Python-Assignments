# Write a python program to create a function that takes a number as a parameter and checks if the number is prime or not.

def primecheck(num):
    for i in range(2,num//2+1):
        if num%i==0:
            print("Numner is not prime number i.e ",num)
            break
    else:
        print("Number is a prime number i.e ",num)

num=int(input("Enter the number : "))
primecheck(num)
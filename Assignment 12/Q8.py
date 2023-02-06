#  Write a python script to print first N terms of a Fibonacci series

def fibonacci(n):

    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)   
n=int(input("Enter the value of n to print first n terms of fibonaccir series "))
print("First ",n,"  terms of fibonacci series are : ")

for i in range(n):
    print(fibonacci(i))

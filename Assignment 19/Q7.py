# Write a python program to sum all the numbers in a list.

def add(lis):
    s=0
    for i in lis:
        s+=i
    return s

lis=[int(i) for i in input("Enter the numbers seperated by space : ").split(' ')]
print("Given list are : ",lis)
print("Sum of the numbers in a list are : ",add(lis))
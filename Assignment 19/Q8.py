# Write a python program to multiply all the numbers in a list.

def mul(lis):
    m=1
    for i in lis:
        m*=i
    return m

lis=[int(i) for i in input("Enter the numbers in the list seperated by space : ").split(' ')]
print("Given list are : ",lis)
print("Multiplication of the elements of the list are : ",mul(lis))
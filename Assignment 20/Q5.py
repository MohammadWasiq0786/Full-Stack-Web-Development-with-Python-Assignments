# Write a python program to create a function to find the Min of three numbers.

def min_number(a,b,c):
    if a<b and a<c:
        return a
    elif b<a and b<c:
        return b
    elif c<a and c<b:
        return c

a=int(input("Enter the 1st number : "))
b=int(input("Enter the 2nd number : "))
c=int(input("Enter the 3rd number : "))

print("Minimum number among these three are : ",min_number(a,b,c))
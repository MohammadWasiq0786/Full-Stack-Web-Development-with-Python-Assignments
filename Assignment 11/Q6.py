# Write a python script to calculate factorial of a given numbe
from re import I


n=int(input("enter the number that factorial you want to calculate : "))
f=1
for i in range(1,n+1):
    f*=i
print("factorial of ",n," are : ",f)
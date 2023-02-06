# Write a python script to calculate sum of digits of a given number
n=int(input("Enter the number : "))
s=0
while n:
    s+=n%10
    n=n//10
print("sum of digits of a given number : ",s)
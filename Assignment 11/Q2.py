# Write a python script to calculate sum of squares of first N natural numbers

n=int(input("Enter the number : "))
s=0
for i in range(1,n+1):
    s+=i**2
print("Sum of sqaure of first ",n," natural numbers are : ",s)

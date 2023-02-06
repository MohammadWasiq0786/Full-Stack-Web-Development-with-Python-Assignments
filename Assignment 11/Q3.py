# Write a python script to calculate sum of cubes of first N natural numbers
n=int(input("Enter the number : "))
s=0
for i in range(1,n+1):
    s+=i**3
print("Sum of cube of first ",n," natural numbers are : ",s)


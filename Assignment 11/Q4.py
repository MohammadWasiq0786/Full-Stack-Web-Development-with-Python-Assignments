# Write a python script to calculate sum of first N odd natural numbers
n=int(input("Enter the number : "))
s=0
for i in range(2*n-1,0,-2):
    s+=i
print("sum of first ",n," odd natural numbers are : ",s)
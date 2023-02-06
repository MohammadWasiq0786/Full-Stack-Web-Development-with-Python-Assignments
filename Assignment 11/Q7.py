# Write a python script to count digits in a given number
n=int(input("enter the number : "))
j=0

while n:
    j+=1
    n=n//10
print("total numbers of digits in given number are : ",j)
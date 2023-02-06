# Write a python script to reverse a number

n=int(input("Enter the number : "))
x=n
s=0
while n:
    r=n%10
    s=r+s*10
    n=n//10
print("The reverse of the ",x, " are : ",s)
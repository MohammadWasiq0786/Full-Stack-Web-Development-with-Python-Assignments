# Write a Python script to create a list of first N even natural numbers.

n= int(input("Enter the range of even natural numbers : "))
lis=[]
i=2
c=1
while c<=n:
    lis.append(i)
    i+=2
    c+=1
print("The list of first ",n," natural numbers are : ")
print(lis)
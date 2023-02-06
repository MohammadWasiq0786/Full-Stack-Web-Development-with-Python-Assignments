# Write a python script to print binary equivalent of a given decimal number. (do not use bin() method)

n=int(input("Enter the decimal number : "))
x=n
lis=[]
while n:
    r=n%2
    lis.append(r)
    n=n//2
lis.reverse()
s=0
for i in lis:
    s=i+s*10

print("The binary of the ",x," are : ",s)



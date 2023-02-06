# . Write a python script to print the octal equivalent of a given decimal number. (do not use oct() method)

n=int(input("Enter the number : "))
x=n
lis=[]
while n:
    r=n%8
    lis.append(r)
    n=n//8
lis.reverse()
s=0
for i in lis:
    s=i+s*10

print("The octal equivalent of ",x," decimal number are : ",s)
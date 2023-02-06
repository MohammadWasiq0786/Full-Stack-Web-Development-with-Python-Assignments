# Write a python script to print first N odd natural numbers in reverse order

n= int(input("enter the number : "))
i,j=1,1
lis=[]
while(i<=n):
    if(j%2!=0):
        lis.append(j)
        i+=1
    j+=1

lis.reverse()
for i in lis:
    print(i, end=" ")


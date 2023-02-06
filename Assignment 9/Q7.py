# Write a python script to print first N even natural numbers in reverse order

n= int(input("Enter the number : "))
i,j=1,1
lis=[]
while n:
    if(i%2==0):
        lis.append(i)
        n-=1
    i+=1
lis.reverse()
for i in lis:
    print(i,end=' ')




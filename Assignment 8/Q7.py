# Write a python script to print first 10 even natural numbers in reverse order

i,j=1,1
lis=[]
while(i<=10):
    if(j%2==0):
        lis.append(j)
        i+=1
    j+=1
lis.reverse()
for i in lis:
    print(i)
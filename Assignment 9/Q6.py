# Write a python script to print first N even natural numbers

n= int(input("Enter the number : "))

i,j=1,1
while(i<=n):
    if(j%2==0):
        print(j)
        i+=1
    j+=1

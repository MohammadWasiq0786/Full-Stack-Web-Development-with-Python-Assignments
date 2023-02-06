# Write a python script to print first N odd natural numbers

n=int(input("Enter the number : "))
j=1
for i in range(1,n+1):
    while(j%2==0):
        j+=1
    print(j)
    j+=1


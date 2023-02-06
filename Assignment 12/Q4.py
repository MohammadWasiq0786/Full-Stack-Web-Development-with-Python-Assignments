# Write a python script to print all Prime numbers between two given numbers (both values inclusive)

a=int(input("Enter the 1st number : "))
b=int(input("Enter the 2nd number : "))

print("Prime numbers between ",a," and ",b," are : ")
for i in range(a,b+1):
    n=1
    for j in range(2,i//2+1):
        if(i%j==0):
            n=0
    if n==1:
        print(i,end=" ")

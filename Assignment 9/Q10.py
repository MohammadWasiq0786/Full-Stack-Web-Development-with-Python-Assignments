#  Write a python script to print first 10 multiples of N

num= int(input("Enter the number that multiple you want : "))
print("first 10 multiple of ",num," are :")
i=1
while i<=10:
    print(num*i,end=' ')
    i+=1

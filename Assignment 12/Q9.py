# Write a python script to calculate LCM of two numbers

print("Enter the two numbers")

a= int(input("1st number "))
b= int(input("2nd number "))
c= max(a,b)

for i in range(c,a*b+1):
    if i%a==0 and i%b==0:
        print("LCM of ",a," and ",b," are : ",i)
        break


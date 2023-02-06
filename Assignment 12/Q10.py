#  Write a python script to calculate HCF of two numbers

print("Enter the two numbers")

a= int(input("1st number "))
b= int(input("2nd number "))
c= min(a,b)

for i in range(1,c+1):
    if a%i==0 and b%i==0:
        fac=i
print("HCF of ",a," and",b," are : ",fac)


# Write a python script to print greater between two numbers. Print number only once
# even if the numbers are the same

num1=int(input("Enter the 1st number : "))
num2=int(input("Enter the 2nd number : "))

# if num1>=num2:
#     print(num1," is greater number ")
# else:
#     print(num2," is greater number ")

print((num1,"is greater number") if num1>num2 else (num2,"is greater number "))
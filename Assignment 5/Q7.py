# Write a python script which takes a three digit number from the user and displays only its last digit.

num= int(input("Enter the three digit number :"))
num= num%10
print("The last digit of given number are : ", num)

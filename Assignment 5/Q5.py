# Write a python script which takes a three digit number from the user and displays only its first digit.

num= int(input("Enter the three digit number : "))
num= num//100
print('The first digit of given number are : ', num)
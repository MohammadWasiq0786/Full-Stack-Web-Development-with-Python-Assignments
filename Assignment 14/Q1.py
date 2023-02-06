# Write a Python script to create a list of first N natural numbers

n=int(input("Enter the range of natural numbers : "))
lis=[int(i) for i in range(1,n+1)]
print("The list of first ",n," natural numbers are : ")
print(lis)
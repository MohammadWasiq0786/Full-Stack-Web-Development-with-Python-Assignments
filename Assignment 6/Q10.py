# . Write a python script to print greater among three numbers. Print number only once even if the numbers are the same.

print("Enter three number :")
a,b,c= int(input("1st number : ")),int(input("2nd number : ")),int(input("3rd number : "))
print(( a if a>c else c) if a>b else (b if b>c else c))
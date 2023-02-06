#  Write a recursive python function to calculate the factorial of a number.

def fac(num):
    if num==0:
        return 1
    else:
        return num*fac(num-1)

num=int(input("Enter the number : "))
print("The factorial of ",num," are : ")
print(fac(num))
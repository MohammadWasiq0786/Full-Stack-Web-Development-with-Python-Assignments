# Write a recursive python function to print squares of first N natural numbers

def sqaure_recursive(num,i):
    if i<=num:
        print(i**2,end=" ")
        i+=1
        return sqaure_recursive(num,i)

num=int(input("Enter the number : "))
print("Sqaure of first ",num," numbers are : ")
sqaure_recursive(num,1)
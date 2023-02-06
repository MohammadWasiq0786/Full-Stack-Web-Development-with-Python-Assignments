#  Write a recursive python function to print first N natural numbers in reverse order

def natural_number(n):
    if n>0:
        print(n,end=" ")
        return natural_number(n-1)


num=int(input("Enter the number : "))
print("The first ",num," natural number in reverse order are : ")
natural_number(num)
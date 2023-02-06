#  Write a recursive python function to print cubes of first N natural numbers

from reprlib import recursive_repr

def cube_recursive(num,i):
    if num>=i:
        print(i**3,end=" ")
        i+=1
        return cube_recursive(num,i)


num=int(input("Enter the number : "))
print("cube of first ",num," numbers are : ")
cube_recursive(num,1)
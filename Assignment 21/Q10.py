#  Write a recursive python function to print a number in reverse order

def rev(num):
    if num:
        print(num,end=" ")
        num-=1
        return rev(num)

num=int(input("Enter the number : "))
print("Numbers in reverse order are : ")
rev(num)
#  Write a recursive python function to calculate sum of squares of first N natural numbers

def sqsum(num,sum):
    if num:
        sum+=num**2
        num-=1
        return sqsum(num,sum)
    return sum

num=int(input("Enter the number : "))
print("Sum of sqaure of first ",num," natural numbers are : ")
print(sqsum(num,0))
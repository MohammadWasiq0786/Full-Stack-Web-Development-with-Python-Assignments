#  Write a recursive python function to calculate sum of first N odd natural numbers

def oddsum(num,sum):
    if num:
        sum+=2*num-1
        num-=1
        return oddsum(num,sum)
    return sum

num=int(input("Enter the number : "))
print("Sum of first ",num," odd natural numbers are : ")
print(oddsum(num,0))
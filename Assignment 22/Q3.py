# Write a recursive python function to calculate sum of first N even natural numbers

def evensum(num,sum):
    if num:
        sum+=2*num
        num-=1
        return evensum(num,sum)
    return sum

num=int(input("Enter the number : "))
print("Sum of first ",num," even natural numbers are : ")
print(evensum(num,0))

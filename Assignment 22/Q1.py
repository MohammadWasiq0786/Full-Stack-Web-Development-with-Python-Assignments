# Write a recursive python function to calculate sum of first N natural numbers

def sum_of_natural(num,sum):
    if num:
        sum+= num
        num-=1
        return sum_of_natural(num,sum)
    return sum


num=int(input("Enter the number : "))
print("Sum of first ",num," natural numbers are : ")
print(sum_of_natural(num,0))

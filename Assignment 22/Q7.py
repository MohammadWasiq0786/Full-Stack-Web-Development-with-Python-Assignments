# Write a recursive python function to calculate sum of the digits of a given number

def digit_sum(num,sum):
    if num:
        r=num%10
        sum+=r
        num=num//10
        return digit_sum(num,sum)
    return sum

num=int(input("Enter the number : "))
print("The sum of the digits of a given number (",num,") are : ")
print(digit_sum(num,0))

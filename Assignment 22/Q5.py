# Write a recursive python function to calculate sum of cubes of first N natural numbers

def cubesum(num,sum):
    if num:
        sum+=num**3
        num-=1
        return cubesum(num,sum)
    return sum

num=int(input("Enter the number : "))
print("Sum of cubes of first ",num," natural numbers are : ")
print(cubesum(num,0))
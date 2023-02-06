# Write a recursive python function to print first N odd natural numbers in reverse order

def recursive_odd(num):
    if num>0:
        print(2*num-1,end=" ")
        return recursive_odd(num-1)

num=int(input("Enter the number : "))
print("First ",num," odd natural numbers in reverse order are : ")
recursive_odd(num)
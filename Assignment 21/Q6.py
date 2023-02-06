# Write a recursive python function to print first N even natural numbers in reverse order.

def recursive_even(num):
    if num>0:
        print(2*num,end=" ")
        return recursive_even(num-1)

num=int(input("Enter the number : "))
print("first ",num," even numbers in reverse order are : ")
recursive_even(num)

#  Write a recursive python function to find the Nth term of the Fibonacci series.

def term(n):
    if n<=2:
        return n-1
    return term(n-1)+term(n-2)

num=int(input("Enter the number : "))
print("The ",num," term of fibonacci series are : ")
print(term(num))
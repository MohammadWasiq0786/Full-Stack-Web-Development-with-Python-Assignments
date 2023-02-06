# Write a python program to create a function which expects a list as an argument.

def fun(a):
    print("type of argument : ",type(a))
    print("Argument are : ",a)
    s=0
    for i in a:
        s+=i
    print("sum of given argument are : ",s)



x=[int(i) for i in input("Enter the numbers seperated by space ").split(' ')]
fun(x)


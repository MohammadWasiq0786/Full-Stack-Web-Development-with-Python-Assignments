# Write a python program to create a function that finds a maximum of four numbers.

def maximun(args):
    m=0
    for i in args:
        if i>m:
            m=i
    return m


x=(int (i) for i in input("Enter the 4 numbers seperated by space : ").split(" "))
print("maximum of four numbers are : ",maximun(x))

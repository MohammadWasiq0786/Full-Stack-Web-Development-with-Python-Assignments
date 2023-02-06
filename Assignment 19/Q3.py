# Write a python program to create a function which expects an unknown number of arguments.
def fun(*t):
    s=0
    # doing sum of the arguments that passed on the function
    for i in t:
        for j in i:
            s+=j
    return s
    

arg=[int(i) for i in (input("Enter the numbers seperated by space : ").split(' '))]
print("sum of the arguments you entered is : ",fun(arg))
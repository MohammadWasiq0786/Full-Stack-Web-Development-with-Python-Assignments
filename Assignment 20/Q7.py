# Write a python program to access a function inside a function

def fun1():
    print("Function 1 ")

def fun2():
    fun1()

fun2()
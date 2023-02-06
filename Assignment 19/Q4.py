# Write a python program to create a function which expects kwargs arguments


def sum(**kwargs):
    print("type  : ",type(kwargs))
    for i,j in kwargs.items():
        print("key = ",i," and values : ",j)




sum(name="Wasiq", age=22, state= "U.P")
    






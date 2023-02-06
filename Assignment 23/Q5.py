# Create a generator to produce first n terms of Fibonacci series

def fibgenerator(n):
    a,b=0,1
    while n:
        yield a
        a,b=b,a+b
        n-=1

for it in fibgenerator(int(input("enter the number to generate fibonacci serie : "))):
    print(it , end=" ")

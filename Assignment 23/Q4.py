# Create a generator to produce squares of first N natural numbers

def squaregenrator(n):
    j=1
    while n:
        yield j**2
        j+=1
        n-=1


for e in squaregenrator(int(input("Enter the number to generate square of n natural numbers : "))):
    print(e,end=" ")
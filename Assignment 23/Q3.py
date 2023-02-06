# Create a generator to produce first n even natural numbers

def generator(n):
    # for i in range(n):
    #     yield(2*i+2)
    k=2
    while n:
        yield k
        k+=2
        n-=1

n=int(input("Enter the number : "))
print("First n even numbers are : ")
for it in generator(n):
    print(it,end=" ")
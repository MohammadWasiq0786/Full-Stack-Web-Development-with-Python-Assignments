# Create a generator to produce first n odd natural numbers

def generator(n):
    l=1
    for i in range(n):
        yield l
        l+=2

n=int(input("Enter the number : "))
it=generator(n)
print("The first n odd numbers are :")
for it in generator(n):
    print(it,end=" ")


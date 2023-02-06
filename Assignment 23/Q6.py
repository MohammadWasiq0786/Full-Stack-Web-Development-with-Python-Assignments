# Create a generator to produce first n prime numbers

def prime_genrator(n):
    a=2
    yield a
    while n-1:
        a+=1
        for i in range(2,a//2+1):
            if a%i==0:
                break
        else:
            yield a
            n-=1


for it in prime_genrator(int(input("Enter the number to generate first n prime numbers : "))):
    print(it,end=" ")

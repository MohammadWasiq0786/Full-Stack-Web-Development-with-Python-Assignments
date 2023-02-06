#  Create an endless iterator using generator method to produce Prime numbers

from re import A

def endless_prime():
    a=2
    yield a
    while True:
        a+=1
        for i in range(2,a//2+1):
            if a%i==0:
                break
        else:
            yield a


lis=[]
it=iter(endless_prime())

while True:
    ans=input("Do you want to generate another prime number [y/n] ")
    if ans=='y':
        lis.append(next(it))
        print(lis[-1])
    else:
        print("The list of generated prime numbers are : ")
        print(lis)
        break
# Write a python script to print first N prime numbers

def nextprime(n):
    while True:
        n+=1
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            return n
def primegenerator(n):
    num,count=1,1
    # for i in range(n):
    #     p=nextprime(num)
    #     num=p
    #     yield p
    while count<=n:
        num=nextprime(num)
        yield num
        count+=1

n=int(input("Enter the number : "))
print("first ",n," prime numbers are : ")
for i in primegenerator(n):
    print(i,end=" ")


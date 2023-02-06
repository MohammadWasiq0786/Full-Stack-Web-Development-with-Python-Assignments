# Write a python script to find next prime number of a given number

def nextprime(n):
    while True:
        n+=1
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            return n

n=int(input("Enter the prime number : "))

# n=n+1
# while n:
#     j=1
#     for i in range(2,(n//2)+1):
#         if(n%i==0):
#             j=0
#             break
#     if j==1:
#         print("Next prime number are : ",n)
#         break
#     n+=1
print("Next prime number are : ",nextprime(n))

            
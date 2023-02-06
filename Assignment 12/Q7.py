# Write a python script to check whether a given pair of numbers are co-Prime numbers or not.

print("Enter the two pair of number to check weather they are co-prime or not : ")

a,b=int(input()),int(input())
# alis=[]
# blis=[]
# for i in range (1,a+1):
#     if (a%i==0):
#         alis.append(i)
# for j in range(1,b+1):
#     if b%j==0:
#         blis.append(j)

# if alis[0]==blis[0] and alis[1]!=blis[1]:
#     print(a,b," are co-prime numbers ")
# else:
#     print(a,b,"are not co-prime numbers")

m= min(a,b)
for i in range(2,m):
        if(a%i==0 and b%i==0):
            flag=0
            print(a,b," are not co-prime numbers ")
            break
else:
        print(a,b,"are co-prime numbers")


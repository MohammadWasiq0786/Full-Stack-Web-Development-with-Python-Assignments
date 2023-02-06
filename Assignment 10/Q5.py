# Write a python script to print first N odd natural numbers in reverse order

n=int(input("ENter the number"))
# for i in range(1,n+1):
#     print(2*n-2*i+1)

for i in range(2*n-1,0,-2):
    print(i)
# Write a Python script to create a list of first N odd natural numbers

n=int(input("Enter the range of odd natural numbers are  : " ))
i=0
j=1
lis=[]
while i<n:
    lis.append(j)
    j+=2
    i+=1

# lis=[int(i) for i in range(1,n+1) if i%2!=0]
print("The list of first ",n," odd natural numbers are :")
print(lis)
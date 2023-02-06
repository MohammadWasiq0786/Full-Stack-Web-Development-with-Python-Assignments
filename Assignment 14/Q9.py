# Write a Python script to print indices of all occurrences of a given element in a given list.

lis=[1,2,3,4,5,3,5,4,7,4]
print("the list are : ")
print(lis)

n=int(input("Enter the element : "))
i=0
ind=[]
for j in lis:
    if j==n:
        ind.append(i)
    i+=1
print("The indices of ",n," in a list are : ")
print(ind)
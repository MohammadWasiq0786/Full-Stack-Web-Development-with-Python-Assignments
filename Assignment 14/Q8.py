# Write a Python script to print distinct elements along with their frequencies of occurrence in the list

lis=[1,2,3,2,4,5,3,4]
tup=[]
for i in lis:
    if i not in tup:
        print("element - ",i, "frequency of occurance - ",lis.count(i)) 
        tup.append(i)   


# Write a Python script to remove all non int values from a list.

lis=[1,"hello","c#",5,"Python",6,7]
print("Initial list are : ")
print(lis)

# ls=[]
# for i in lis:
    
#     if type(i)==int:
#         ls.append(i)
# print(ls)

lis=[x for x in lis if type(x)==int]
print("After the removal of all non int values list are : ")
print(lis)
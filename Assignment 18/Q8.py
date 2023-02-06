# Write a python program to convert two lists into a dictionary in a way that item from
# list1 is the key and item from list2 is the value.

lis1=['a','b','c','d']
lis2=['apple','ball','cat','dog']

dic={i : j for (i,j) in zip(lis1,lis2) }
print(dic)

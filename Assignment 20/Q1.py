# Write a python program to create a function that takes a list and returns a new list with the original list's unique elements.

def unique(lis):
    lis2=[]
    for i in lis:
        if i not in lis2:
            lis2.append(i)
    return lis2


lis=[int(i) for i in input("Enter the list elements seperated by space : ").split(' ')]
print("Original list are : ",lis)
lis2=unique(lis)
print("New list with unique elements of the original list are :  ",lis2)



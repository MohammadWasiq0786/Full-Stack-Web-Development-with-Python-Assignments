#  Write a python program to Sort a tuple of tuples by the second item.
# tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))

def sort_tup(tup):
    l=len(tup)
    for i in range(l):
        for j in range(0,l-i-1):
            if (tup[j][1]>tup[j+1][1]):
                temp=tup[j]
                tup[j]=tup[j+1]
                tup[j+1]=temp
    return tuple(tup)

tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))
print("Before sorting : ")
print(tuple1)
tuple1=list(tuple1)
tup=sort_tup(tuple1)

print("After sorting by second item : ")
print(tup)



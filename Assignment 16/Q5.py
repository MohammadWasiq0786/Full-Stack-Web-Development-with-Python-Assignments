#  Write a python program to check if all items in the tuple are the same

tup=(1,1,1,1)
flag=0
for i in tup:
    for j in tup:
        if (i!=j):
            print("All the items of tuple are not same i.e ",tup)
            flag=1
            break
    if flag==1:
        break
else:
    print("All the items of tuple are same i.e ",tup)
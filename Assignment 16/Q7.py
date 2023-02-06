# Write a python program to copy elements 4 and 5 from the following tuple into a new tuple. tuple1=(1,2,3,4,5,6)

tuple1=(1,2,3,4,5,6)
tup=()
for i in tuple1:
    if i==4 or i==5:
        tup=tup+(i,)

print("after copy the tuple become : ",tup)
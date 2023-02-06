# Write a python program to change the first item (22) of a list within the following tuple to 222.
# tuple1 = (11, [22, 33], 44, 55)

tuple1 = (11, [22, 33], 44, 55)

# tup=()
# for i in tuple1:
#     if type(i)!=int:
#         lis=[]
#         for j in i :
#             if j==22:
#                 lis.append(222)
                
#             else:
#                 lis.append(j)
#                 tup=tup+(lis,)  
#     else:
#         tup=tup+(i,)

tuple1[1][0]=222
print("tuple are : ",tuple1)


#  Write a python program to append elements from another list to the current list.(
# firstlist = ["Java", "Python", "SQL"]
# secondlist = ["C", "Cpp", "NoSQL"] )

firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"] 

print("First list are : ",firstlist)
print("Second list are : ",secondlist)

print("after the append of elements from one list to another list : ")
for i in secondlist:
    firstlist.append(i)
print(firstlist)
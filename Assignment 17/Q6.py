# Write a python program to add elements of list to a set
# thisset = {"Python", "Django", "JavaScript"}
# mylist = ["Java", "C"]

thisset = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]

print("set : ",thisset)
print("list : ",mylist)

for i in mylist:
    thisset.add(i)


print("After the addition of list element to the set : ")
print(thisset)
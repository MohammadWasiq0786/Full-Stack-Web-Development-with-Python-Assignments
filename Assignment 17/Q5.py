# Write a python program to add items from another set to the current set. 
# thisset= {"Java", "Python", "SQL"}
# secondset= {"C", "Cpp", "NoSQL"}

thisset = {"Java", "Python", "SQL"}
secondset= {"C", "Cpp", "NoSQL"}

print("thisset set :",thisset)
print("second set : ",secondset)

for i in secondset:
    thisset.add(i)

print()
print("After addition of items from another set to the current set are : ")
print(thisset)
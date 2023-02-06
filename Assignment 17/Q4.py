#  Write a Python script to find if “Python” is present in the set thisset = {"Java", "Python", "Django"}

thisset = {"Java","Python", "Django"}
for i in thisset:
    if i=='Python':
        print("Python is present in given set ")
        break
else:
    print("Python is not present in given set")


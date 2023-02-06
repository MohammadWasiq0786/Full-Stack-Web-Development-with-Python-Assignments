# Write a python program to store your own information {name, age, gender, so on..}

print("ENter your details : ")
s=set()
s.add(input("Name : "))
s.add(int(input("Age : ")))
s.add(input("Gender : "))
s.add(input("State : "))

print("Details in the set are : ",s)

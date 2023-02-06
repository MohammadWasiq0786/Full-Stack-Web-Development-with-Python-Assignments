# Write a python program to remove last item of the given set
# thisset = {"Python", "Django", "JavaScript", “SQL”}

thisset = { "Python", "Django", "JavaScript", "SQL" }
print("set : ",thisset)
x=list(thisset)[-1]
print("Last element are : ",x)
thisset.discard(x)
print("After removing the last item of the given set : ")
print(thisset)



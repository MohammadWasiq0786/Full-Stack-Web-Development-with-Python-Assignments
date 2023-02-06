#  Write a python script to Change the values "SQL" and "Reactnative" with the values
# "NoSQL" and "Flutter" (List is thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]

thislist = ["Java", "SQL", "C", "Reactnative","Javascript", "Python"]
print("Initial list are : ",thislist)
sql_index=thislist.index("SQL")
thislist[sql_index]="NoSQL"
react_index=thislist.index("Reactnative")
thislist[react_index]="Flutter"
print("List are : ",thislist)

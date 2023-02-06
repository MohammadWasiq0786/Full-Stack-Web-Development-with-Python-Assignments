# Write a python script to store multiple items in a single variable ( Items are “Java” ,“Python”, “SQL”, “C” ) using list

lis=[]
print("Enter the items : ")
while True:
    x=int(input("Press 1 to enter more and 0 to exit "))
    if x==1:
        lis.append(input("item :"))
    else:
        break
    
print("The items are : ",lis)
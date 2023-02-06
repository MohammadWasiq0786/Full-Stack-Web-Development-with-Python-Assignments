# Write a python program to create a function that accepts a string and calculate the
# number of upper case letters and lower case letters.

def count(st):
    up=0
    low=0
    for i in st:
        if i.isupper():
            up+=1
        elif i.islower():
            low+=1
    print("Number of upper case letters are : ",up)
    print("Number of lower case letters are : ",low)


st=input("Enter the string : ")
count(st)
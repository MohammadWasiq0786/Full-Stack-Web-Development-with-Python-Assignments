#  Write a python program to create a function to check whether a string is an anagram or not

def anagram(a,b):
    l1=len(a)
    l2=len(b)
    if l1 !=l2:
        return False
    a=sorted(a)
    b=sorted(b)

    for i in range(l1):
        if a[i]!=b[i]:
            return False
    return True

a=input("Enter the string 1 : ")
b=input("Enter the string 2 : ")

if anagram(a,b):
    print("Given two string are anagram i.e",a,b)
else:
    print("Given two string are not anagram i.e",a,b)
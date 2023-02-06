# Write a python program to create a function to check whether a string is a pangram or not.

def panagram(st):
    lis=[False]*26
    
    for i in st:
        if i>='A' and i<='Z':
            j=ord(i)-65
            lis[j]=True
        elif i>='a' and i<='z':
            j=ord(i)-97
            lis[j]=True
        j+=1
    return all(lis)


st=input("Enter the string : ")

if panagram(st):
    print("Given string are pangram i.e ",st)
else:
    print("Given string are not pangram i.e ",st)


#  Write a python script to determine whether a string contains a specific substring

st= input("Enter the string : ")
sub= input("Enter the substring : ")

if sub in st:
    print(sub," is found in ",st)
else:
    print(sub," is not found in ",st)
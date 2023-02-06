# Write a python script to check whether two given strings are identical, first string
# comes before the second in dictionary order or first string comes after the second
# string in dictionary order using match case statement

s1= input("Enter the first string : ")
s2= input("Enter the second string : ")

match (s1,s2):
    case (s1,s2) if s1==s2:
        print("Identical string")
    case (s1,s2) if s1>s2:
        print(s2)
        print(s1)
    case (s1,s2) if s2>s1:
        print(s1)
        print(s2)
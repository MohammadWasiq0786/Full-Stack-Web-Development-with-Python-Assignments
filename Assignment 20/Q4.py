# Write a python program to create a function that checks whether a passed string is palindrome or not.

def check_palindrome(s):
    l=len(s)
    for i in range(l):
        if s[i]!=s[l-i-1]:
            print("Given string is not palindrome i.e ",s)
            break
    else:
        print("Given string are palindrome i.e ",s)

s=input("Enter the string : ")
check_palindrome(s)
# . Write a python program to check whether a given string is a multiword string or single
# word string using match case statement

st= input("ENter the string : ")
st=st.strip()
match st:
    case st if " " in st:
        print("Multiword string")
    case st if " " not in st:
        print("Single word")
    case _:
        print("Enter valid string")
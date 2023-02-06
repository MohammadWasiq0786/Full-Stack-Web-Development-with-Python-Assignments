#  Write a python script to print two given words in dictionary order

str1=input("Enter the 1st word : ")
str2=input("Enter the 2nd word : ")
print("The words are in dictionary order are : ")

# if str1>str2:
#     print(str2)
#     print(str1)
# else:
#     print(str1)
#     print(str2)

print((str2,str1) if str1>str2 else (str1,str2))
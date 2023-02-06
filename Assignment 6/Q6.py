# Write a python script to check whether a given number is a three digit number or not.

num=int(input("Enter a three digit number : "))

# i=0
# r=1
# x=num
# while num!=0:
#     num=num//10
#     i+=1
    
# if i==3:
#     print(x,"is a three digit number ")
# else:
#     print(x,"is not a three digit number ")

if 99<num<1000:
    print(num,"is a three digit number ")
else:
    print(num,"is not a three digit number ")
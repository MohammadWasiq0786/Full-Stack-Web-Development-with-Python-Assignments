#  Write a python script to check whether a given number is Prime or not

num= int(input("enter the number : "))
check= num//2
n=0
for i in range(2,check+1):
    if(num%i==0):
        
        print(num,"  is not primary number ")
        break
else:
    print(num," is a primary number ")


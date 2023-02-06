# Write a python script to print any number and its binary equivalent.

num= int(input('Enter a number :'))
x= num
result= 0
lis= []
while x!=0:
    r= x%2
    lis.append(r)
    x= x//2

lis.reverse()
bin=0
for i in lis:
    bin=bin*10+i

print('The binary of the ',num,' are : ',bin)
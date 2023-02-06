# Write a python script to print any number and its octal equivalent.

num= int(input("Enter the num :"))
x=y= num
lis= []
while x!=0:
    r= x%2
    lis.append(r)
    x= x//2

lis.reverse()
bin= 0
for i in lis:
    bin= bin*10+i

print('The binary of the ',num,' are : ', bin)

oct= []
count= len(lis)

while y!=0:
    r= y%8
    oct.append(r)
    y= y//8


oct.reverse()
octal=0
for i in oct:
    octal=octal*10+i
print('Octal number of ',num," is : ", octal)


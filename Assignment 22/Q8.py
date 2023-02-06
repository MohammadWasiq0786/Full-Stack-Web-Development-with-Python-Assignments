# Write a recursive python function to print binary of a given decimal number

def binary(num,lis):
    if num:
        r=num%2
        lis.append(r)
        num=num//2
        return binary(num,lis)
    return lis


num=int(input("Enter the number : "))
print("The binary of given decimal number (",num,") are : ")
lis=binary(num,[])
lis.reverse()
num=0
for i in lis:
    num=num*10+i

print(num)

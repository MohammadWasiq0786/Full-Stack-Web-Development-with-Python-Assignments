# Write a recursive python function to print octal of a given decimal number


def octal(num,lis):
    if num:
        r=num%8
        lis.append(r)
        num=num//8
        return octal(num,lis)
    return lis


num=int(input("Enter the number : "))
print("octal of given decimal number (",num,") are : ")
lis=octal(num,[])
lis.reverse()
num=0
print(lis)
for i in lis:
    num=num*10+i
print(num)

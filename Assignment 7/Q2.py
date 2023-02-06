#  Write a menu driven program to perform following operations - Addition, Subtraction, Multiplication, Division

print("Press 1 for the addition ")
print("Press 2 for the subtraction ")
print("Press 3 for the multiplication ")
print("Press 4 for the division ")
num= int(input())

match num:
    case 1:
        a,b=(float(i) for i in input("Enter the operands seperated by space :").split(' '))
        print("The addition of two number are :",'%.2f'%(a+b))
    case 2:
        a,b=(float(i) for i in input("Enter the operands seperated by space :").split(' '))
        print("The subtraction of two number are :",'%.2f'%(a-b))
    case 3:
        a,b=(float (i) for i in input("Enter the operands seperated by space :").split(' '))
        print("The multiplication of two number are :",'%.2f'%(a*b))
    case 4:
        a,b=(float(i) for i in input("Enter the operands seperated by space :").split(' '))
        print("The division of two number are :",'%.2f'%(a/b))
    case _:
        print("Enter the valid option ")
        

        
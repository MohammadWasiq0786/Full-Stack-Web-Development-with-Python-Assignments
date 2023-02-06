# Write a menu driven program with the following options:

# a. Check whether a given set of three numbers are lengths of an isosceles
# triangle or not
# b. Check whether a given set of three numbers are lengths of sides of a right
# angled triangle or not
# c. Check whether a given set of three numbers are equilateral triangle or not
# d. Exit

a,b,c=(float(i) for i in input("Enter the three numbers seperated by space :").split(' '))

print("*"*51)
print("Press 1 to Check whether a given set of three numbers are lengths of an isosceles triangle or not ")
print("Press 2 to Check whether a given set of three numbers are lengths of sides of a right angled triangle or not ")
print("Press 3 to Check whether a given set of three numbers are equilateral triangle or not ")
print("Press 4 to Exit")
print("*"*51)

num= int(input())
match num:
    case 1:
        if a==b or a==c or b==c :
            print("Given set of numbers are length of an isosceles triangle")
        else:
            print("Given set of numbers are not length of an isosceles triangle")
    case 2:
        if (a*a)+(b*b)==(c*c) or (a*a)+(c*c)==(b*b) or (c*c)+(b*b)==(a*a):
            print("Given set of three numbers are lengths of sides of a right angled triangle")
        else:
            print("Given set of three numbers are not lengths of sides of a right angled triangle")
    case 3:
        if a==b==c:
            print("Given set of three numbers are equilateral triangle")
        else:
            print("Given set of three numbers are not equilateral triangle")
    case 4:
        print("Exit successfully")
        exit()
    case _:
        print("Enter the valid option")
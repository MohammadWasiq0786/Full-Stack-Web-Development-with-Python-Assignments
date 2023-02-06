# Write a python script to display the number of days in a given month number

num= input("Enter the month number :")
match num:
    case '1' | '3' | '5' | '7' | '8'|  '10' |'12':
        print('Number of days are  31 ')
    case '4'|'6'|'9'|'11':
        print("Number of days are 30")
    case '2':
        print("Number of days are 28/29 ")
    case _:
        print("Please enter valid month number ")
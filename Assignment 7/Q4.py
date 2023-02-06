# . Write a program which takes user’s age and display the category of person. Age
# below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -
# Experienced, Age above or equal 60 - Senior Citizena.

age= int(input("Enter your age : "))
match age:
    case _ if 0<=age<10:
        print(age," = Kid")
    case  _ if 10<=age<20:
        print(age," = Teen")
    case _ if 20<=age<40:
        print(age," = Young")
    case _ if 40<=age<60:
        print(age," = Experienced")
    case _ if age>=60:
        print(age," = Senior citizen")

# Write a python script to check whether a given quadratic equation has two real & distinct roots, real & equal roots or imaginary roots

print("The quadratic equation are in the form of Ax^2 + Bx + C = 0")

a= int(input("Enter the value of A :"))
b= int(input("Enter the value of B :"))
c= int(input("Enter the value of C :"))

d= (b**2)-(4*a*c)

if d>0:
    print("Roots are real and distinct ")
elif d<0:
    print("Roots are Imaginary ")
else:
    print("Roots are real and equal ")
# Define a function which takes lengths of three sides of a triangle as arguments and
# display the perimeter or triangle. Define and apply a decorator which checks for the
# validity of the triangle on the basis of lengths of the side. This makes the perimeter to
# be displayed when the triangle can exist with the given lengths of the sides

def valid_triangle(perimeter):
    def check(a,b,c):
        if a+b>c and b+c>a and c+a>b:
            print("triangle is valid with given sides : ",a,b,c)
            perimeter(a,b,c)
            
        else:
            print("Triangle is not valid with given sides : ",a,b,c)      
    return check      

@valid_triangle
def perimeter(a,b,c):
    print("Perimeter : ",a+b+c)


s1=int(input("Enter the 1st side of triangle : "))
s2=int(input("Enter the 2nd side of triangle : "))
s3=int(input("Enter the 3rd side of triangle : "))
perimeter(s1,s2,s3)
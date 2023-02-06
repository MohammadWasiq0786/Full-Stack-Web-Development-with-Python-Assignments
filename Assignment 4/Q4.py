# Write a python script which takes the radius from the user and display area of a circle.

from cmath import pi
radius= float(input('Enter the radius of circle :'))
areaofcircle= pi*radius**2
print('Area of circle is :','%.2f'%areaofcircle)

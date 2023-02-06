# Write a python script to display the current date and time. First create variables to
# store date and time, then display date and time in proper format (like: 13-8-2022 and 9:00 PM)

from datetime import datetime
from time import strftime

dt= datetime.today()

# day month yearfull and 12 hout time format
l1=dt.strftime("%d-%m-%Y and %I-%M-%p")
print(l1)
print()

# 12 hour format
l2 =strftime("%H-%M-%S")
print(l1)
print()

# print month in date
m= strftime('%d/%B/%Y')
print(m)

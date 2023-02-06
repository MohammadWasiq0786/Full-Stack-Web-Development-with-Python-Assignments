# Use iter and next method to access all the elements of a given set using while loop

l1={1,2,3,4,5,6}
it=iter(l1)

print("The elements of a given set are : ")
while True:
    try:
        print(next(it),end=" ")
    except StopIteration:
        break
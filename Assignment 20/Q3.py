# Write a python program to create a function that prints the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]

def even(lis):
    for i in lis:
        if i%2==0:
            print(i,end=" ")
        

Sample_List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Given list are : ")
print(Sample_List)
print()
print("The even numbers in the list are : ")
even(Sample_List)

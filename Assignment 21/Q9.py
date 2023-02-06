# Write a recursive python function to print first N multiples of a given number

def  multiple(num,m,i):
    if m>=i:
        print(num*i,end=" ")
        i+=1
        return multiple(num,m,i)

num=int(input("Enter the number : "))
m=int(input("Enter the number of multiples you want : "))
print("First ",m," multiples of given number ",num,"are : " )
multiple(num,m,1)
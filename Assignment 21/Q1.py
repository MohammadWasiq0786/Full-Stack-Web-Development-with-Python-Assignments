# Write a recursive python function to print first N natural numbers

def naturalnum(n):
   if n>0:
    naturalnum(n-1)
    print(n,end=" ")
        

n=int(input("Enter the number : "))
print("the first ",n," natural numbers are : ")
naturalnum(n)
# Write a recursive python function to print first N odd natural numbers

def odd(n,flag,j):
    if flag<n:
        print(j,end=" ")
        flag+=1
        return odd(n,flag,j+2)
    


num=int(input("Enter the number : "))
print("First ",num,"off natural numbers are : ")
odd(num,0,j=1)

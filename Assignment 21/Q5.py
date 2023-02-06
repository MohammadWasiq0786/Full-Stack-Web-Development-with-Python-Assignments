# Write a recursive python function to print first N even natural numbers

def even_recursive(num,flag,i):
    if flag<num:
        print(i,end=" ")
        i+=2
        flag+=1
        return even_recursive(num,flag,i)


num=int(input("Enter the number : "))
print("first ",num," even natural numbers are : ")
even_recursive(num,0,2)
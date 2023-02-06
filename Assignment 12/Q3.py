# Write a python script to print all Prime numbers under 100

print("All primary number under 100 are : ")

for i in range(1,100+1):
    n=1
    for j in range(2,i//2+1):
        if(i%j==0):
            n=0  
    if n==1:
         print(i,end=" ")     
#  Write a python script to print first 10 multiples of 5

i,j=1,1
# while(i<=10):
#     print(5*i)
#     i+=1

while(i<=10):
    if(j%5==0):
        print(j)
        i+=1
    j+=1
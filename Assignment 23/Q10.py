#  Define a function which calculates HCF of two numbers. Define and apply a
# decorator to check whether two given numbers are co-prime or not

def co_prime(hcf):
    h=1
    def check(a,b):
        l=min(a,b)
        for i in range(2,l+1):
            if a%i==0 and b%i==0:
                hcf(a,b)
                break
        else:
            print("Two numbers",a," and ",b,"  are co-prime number ")

    return check


@co_prime
def hcf(a,b):
    l=min(a,b)
    for i in range(2,l+1):
        if a%i==0 and b%i==0:
            h=i
    print("Hcf of ",a," and ",b," are : ",h)


num1=int(input("Enter the 1st number : "))
num2=int(input("Enter the 2nd number : "))
hcf(num1,num2)
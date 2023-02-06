# Write a python script to accept one complex number from the user and display the greater number between real part and imaginary part

com= complex(input("Enter a complex number : "))

print((com.real,"is a greater number ")if com.real>com.imag else (com.imag,"is a greater number")) 
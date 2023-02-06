# Write a python script to calculate simple interest

principle= float(input('Enter the initial interest balance :'))
rate= float(input('Enter the annual rate interest :'))
time= float(input('Enter the time in years :'))
final_amount= ((principle*rate*time)/100)
print('The final amount is :','%.2f'%final_amount)


#!/usr/bin/python
# _*_ coding = UTF-8 _*_

balance = 999999
annualInterestRate = 0.18
monthly_interest_rate = annualInterestRate / 12.0

updated_balance = balance
payment_lower_bound = balance / 12.0
payment_upper_bound = (balance*(1+monthly_interest_rate)**12)/12.0
epsilon = 0.01

while updated_balance > epsilon:
    paid = (payment_upper_bound + payment_lower_bound) / 2.0
    updated_balance = balance
    for month in range(1,13):     
        monthly_unpaid_balance = updated_balance - paid
        updated_balance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
    if updated_balance > 0:        
        payment_lower_bound = paid
    else:
        payment_upper_bound = paid
        updated_balance = balance             
print  'Lowest Payment: ' + str(round(paid,2))
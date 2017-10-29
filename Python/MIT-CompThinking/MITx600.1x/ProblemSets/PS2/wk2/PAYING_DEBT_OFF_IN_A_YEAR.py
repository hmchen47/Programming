#!/usr/bin/python
# _*_ coding = UTF-8 _*_

balance = 3926
annualInterestRate = 0.2
monthly_interest_rate = annualInterestRate / 12.0

updated_balance = balance
paid = 0

while updated_balance > 0:
    paid += 10
    updated_balance = balance
    for month in range(1,13):     
        monthly_unpaid_balance = updated_balance - paid
        updated_balance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
print  'Lowest Payment: ' + str(paid)
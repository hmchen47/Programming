#!/usr/bin/env python
# _*_coding=UTF-8 _*_

#balance = 4213; annualInterestRate = 0.2; monthlyPaymentRate = 0.04
#balance = 4842; annualInterestRate = 0.2; monthlyPaymentRate = 0.04
#balance = 4213; annualInterestRate = 0.2; monthlyPaymentRate = 0.04
#balance = 4842; annualInterestRate = 0.2; monthlyPaymentRate = 0.04
#balance = 3164; annualInterestRate = 0.2; monthlyPaymentRate = 0.08
#balance = 3335; annualInterestRate = 0.22; monthlyPaymentRate = 0.05
#balance = 3244; annualInterestRate = 0.18; monthlyPaymentRate = 0.08
#balance = 3845; annualInterestRate = 0.22; monthlyPaymentRate = 0.05


#print 'Result Your Code Should Generate:'
#print '-------------------'

monthlyInterestRate = annualInterestRate / 12
totalPaid = 0.0

for month in range(12):
    minMonthPayment = monthlyPaymentRate * balance
    totalPaid += minMonthPayment
    monthlyUnpaidBalance = balance - minMonthPayment
    balance = monthlyUnpaidBalance + \
                (monthlyInterestRate*monthlyUnpaidBalance)
    print 'Month: ', month+1
    print 'Minimum monthly payment: ', round(minMonthPayment, 2)
    print 'Remaining balance: ', round(balance, 2)

print 'Total paid: ', round(totalPaid, 2)
print 'Remaining balance: ', round(balance, 2)

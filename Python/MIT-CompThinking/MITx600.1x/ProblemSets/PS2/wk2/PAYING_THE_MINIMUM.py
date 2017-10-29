#!/usr/bin/python
# _*_ coding = UTF-8 _*_

balance = 4213; annualInterestRate = 0.2; monthlyPaymentRate = 0.04

def monthly_payment(balance, monthlyPaymentRate):
    return balance * monthlyPaymentRate

def paying_the_minimum(balance, annualInterestRate, monthlyPaymentRate):
    total_paid = 0
    for month in range(1,13):               
        print 'Month: ' + str(month)
        print 'Minimum monthly payment: ' + str(round(monthly_payment(balance, monthlyPaymentRate),2))
        total_paid += monthly_payment(balance, monthlyPaymentRate)
        unpaid_balance = balance - monthly_payment(balance, monthlyPaymentRate) 
        balance = unpaid_balance + (annualInterestRate / 12.0) * unpaid_balance
        print 'Remaining balance: ' + str(round(balance,2))
    print 'Total paid: ' + str(round(total_paid,2))
    print 'Remaining balance: ' + str(round(balance,2))    

paying_the_minimum(balance, annualInterestRate, monthlyPaymentRate) 
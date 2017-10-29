#!/usr/bin/env python
# _*_coding=UTF-8 _*_

'''
Monthly interest rate = (Annual interest rate) / 12.0
Monthly payment lower bound = Balance / 12
Monthly payment upper bound = 
        (Balance x (1 + Monthly interest rate)^12) / 12
'''

#balance = 320000; annualInterestRate = 0.2         #29157.09
#balance = 999999; annualInterestRate = 0.18            #90325.03
#balance = 123380; annualInterestRate = 0.2             #11241.88
#balance = 66941; annualInterestRate = 0.18             #6046.45
#balance = 448237; annualInterestRate = 0.22            #41197.18
#balance = 224468; annualInterestRate = 0.15            #20009.98
#balance = 203565; annualInterestRate = 0.21            #18628.7
#balance = 485183; annualInterestRate = 0.22            #44592.87
#balance = 267920; annualInterestRate = 0.22            #24624.36
#balance = 300348; annualInterestRate = 0.21            #27485.54
#balance = 438908; annualInterestRate = 0.21            #40165.48
#balance = 297102; annualInterestRate = 0.15            #26484.86


monthlyInterestRate = annualInterestRate / 12
monthlyPaymentLB = balance / 12
monthlyPaymentUP = balance * (1+monthlyInterestRate)**12 / 12
finalBalance = balance

#cnt = 0

while abs(finalBalance) > 0.01:
    monthlyPayment = (monthlyPaymentLB + monthlyPaymentUP) / 2
    finalBalance = balance
    for month in range(12):
        monthlyUnpaidBalance = finalBalance - monthlyPayment
        finalBalance = monthlyUnpaidBalance + \
                    (monthlyInterestRate*monthlyUnpaidBalance)

#    print 'payment = ', monthlyPayment, \
#        'final balance = ', finalBalance

    if finalBalance > 0:
        monthlyPaymentLB = monthlyPayment
    else:
        monthlyPaymentUP = monthlyPayment

#    if cnt > 10000:
#        break
#    else:
#        cnt += 1

print 'Lowest Payment: ', round(monthlyPayment, 2)

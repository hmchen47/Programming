#!/usr/bin/env python
# _*_coding=UTF-8 _*_

''' Monthly interest rate = (Annual interest rate) / 12.0
    Monthly unpaid balance = (Previous balance) - 
        (Minimum fixed monthly payment)
    Updated balance each month = (Monthly unpaid balance) + 
        (Monthly interest rate x Monthly unpaid balance)
'''

#balance = 3329; annualInterestRate = 0.2       #310
#balance = 4773; annualInterestRate = 0.2       #440
#balance = 3926; annualInterestRate = 0.2       #360
#balance = 884; annualInterestRate = 0.2        #90
#balance = 592; annualInterestRate = 0.2        #60
#balance = 270; annualInterestRate = 0.18       #30
#balance = 857; annualInterestRate = 0.2        #80
#balance = 3050; annualInterestRate = 0.04      #260
#balance = 4109; annualInterestRate = 0.04      #350
#balance = 4040; annualInterestRate = 0.2       #370
#balance = 4349; annualInterestRate = 0.04      #370
#balance = 4558; annualInterestRate = 0.2       #420
#balance = 4817; annualInterestRate = 0.18      #440
#balance = 3448; annualInterestRate = 0.18      #320
#balance = 4872; annualInterestRate = 0.04      #420

# initial values 
monthlyInterestRate = annualInterestRate / 12
finalBalance = balance
monthlyPayment = 0
lastMonthlyPayment = 0
lastFinalBalance = balance

# calculate the final balance by increase monthlyPayment by $10
while finalBalance > 0 or monthlyPayment > balance:
    lastMonthlyPayment = monthlyPayment
    monthlyPayment += 10
    lastFinalBalance = finalBalance
    finalBalance = balance
    for month in range(12):
        monthlyUnpaidBalance = finalBalance - monthlyPayment
        finalBalance = monthlyUnpaidBalance + \
                    (monthlyInterestRate*monthlyUnpaidBalance)

#    print 'Monthly payment =', monthlyPayment, \
#          '    final balance =', finalBalance

print 'Lowest Payment: ', monthlyPayment

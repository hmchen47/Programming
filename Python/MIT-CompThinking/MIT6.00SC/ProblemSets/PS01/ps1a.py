#!/usr/bin/python
# __*__ coding: utf-8 __*__

# Problem Set 1 - paying the minimum
# Name: Fred Chen
# Collaborators: None
# Time Spent:
#

# Minimum monthly payment = mininum monthly payment rate x Balance
# Interest Paid = Annual interest rate / 12 months x Balance
# Principle paid = Minimum month payment - Interest paid
# Remaining balance = Balance - Principle paid
 
str_bal = raw_input('Enter the outstanding balance on your credit card: ')
str_airate = raw_input('Enter the annual credit card interest rate as a decimal: ')
 
bal = float(str_bal)
airate = float(str_airate)
mirate = airate / 12.0
mmprate = float(str_mmprate)

new_bal = bal
total_paid = 0.0

for month in range(12):
    mmp = round(mmprate * new_bal, 2)
    ipd = round(mirate * new_bal, 2)
    total_paid += mmp
    pp = mmp - ipd
    new_bal = new_bal * (1+mirate) - mmp
    print '\nMonth: ', month + 1
    print 'Minimum monthly payment: ', mmp
    print 'Principle paid: ', pp
    print 'Remaining balance: ', new_bal

print '\nRESULT'
print 'Total amount paid: ', total_paid
print 'Remaining balance: ', new_bal

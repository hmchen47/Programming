#!/usr/bin/python
# __*__ coding: utf-8 __*__

# Problem Set 1 - Problem 3 Using Bisection Search to Make the Program Faster
# Name: Fred Chen
# Collaborators: None
# Time Spent: 2:00
#

# Monthly payment lower bound = Balance / 12.0 
# Monthly payment upper bound = (Balance * (1 + (Annual interest rate / 12.0)) 
#                                   ** 12.0) / 12.0

  
str_bal = raw_input('Enter the outstanding balance on your credit card: ')
str_airate = raw_input('Enter the annual credit card interest rate as a decimal: ')
 
bal = float(str_bal)
airate = float(str_airate)
mirate = airate / 12.0

lmmp = bal / 12.0
ummp = (bal * (1+mirate)**12.0) / 12.0
mmmp = (lmmp+ummp) / 2.0
new_bal = bal

print 'low bound = ', lmmp, 'upper bound = ', ummp, 'middle = ', mmmp

cnt = 0
epsilon = 0.2

while (abs(new_bal) >= epsilon):
    new_bal = bal
    for month in range(12):
        new_bal = (new_bal * (1+mirate) - mmmp)
        if (new_bal < epsilon):
            months = month + 1
            break
#    print 'new_bal = ', new_bal
    if (new_bal > 0.0):
        lmmp = mmmp
        mmmp = (mmmp+ummp) / 2.0
    else:
        ummp = mmmp
        mmmp = (mmmp+lmmp) / 2.0
#    print 'new mmmp = ', mmmp
    
    cnt += 1
#    if cnt >= 10:
#        break


print 'cnt = ', cnt
print '\nRESULT'
print 'Monthly payment to pay off debt in 1 year: ', round(mmmp, 2)
print 'Number of months needed: ', months
print 'Balance: ', round(new_bal, 2)


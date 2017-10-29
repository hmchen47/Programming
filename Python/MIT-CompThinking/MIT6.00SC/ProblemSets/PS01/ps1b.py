#!/usr/bin/python
# __*__ coding: utf-8 __*__

# Problem Set 1 - Problem 2 Paying Debt off in a year
# Name: Fred Chen
# Collaborators: None
# Time Spent: 2:00
#

# Monthly interest rate = Annual interest rate / 12.0 
# Updated balance each month = Previous balance * (1 + Monthly interest rate) - 
#           Minimum monthly payment

# Hints
# Start at $10 payments per month and calculate whether the balance will be 
# paid off (taking into account the interest accrued each month). If $10 
# monthly payments are insufficient to pay off the debt within a year, 
# increase the monthly payment by $10 and repeat.

  
str_bal = raw_input('Enter the outstanding balance on your credit card: ')
str_airate = raw_input('Enter the annual credit card interest rate as a decimal: ')
 
bal = float(str_bal)
airate = float(str_airate)
mirate = airate / 12.0

mmp = 0.0
new_bal = bal

while (new_bal > 0.0):
    mmp += 10.0
    new_bal = bal
    for month in range(12):
        new_bal = (new_bal * (1+mirate) - mmp)
        if (new_bal <= 0.0):
            months = month+1
            break



# x <= balance * (1+rate)^12 / sum_k=0^11{(1+rate)^k}

#rate_sum = 0.0
#for month in range(12):
#    rate_sum += (1 + mirate)**month
#
#mpp = int(bal * (1+mirate)**12/rate_sum)
#
#months = 12
#print bal-mpp*months
#while (bal - mpp*months < 0.0):
#    months -= 1
#
#months += 1

print '\nRESULT'
print 'Monthly payment to pay off debt in 1 year: ', int(mmp)
print 'Number of months needed: ', months
print 'Balance: ', round(new_bal, 2)


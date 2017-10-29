## PAYING THE MINIMUM
## code
monthlyIntRate = annualInterestRate/12
tot = 0
for i in range(1,13):
    minMonthlyPay = monthlyPaymentRate * balance
    unpaidBalance = balance - minMonthlyPay
    balance = unpaidBalance + monthlyIntRate * unpaidBalance
    print "Month: "+str(i)
    print "Minimum monthly payment: "+str(round(minMonthlyPay,2))
    print "Remaining balance: "+str(round(balance,2))
    tot += minMonthlyPay
print "Total paid: "+str(round(tot,2))
print "Remaining balance: "+str(round(balance,2))          


## PAYING DEBT OFF IN A YEAR
## code
monthlyIntRate = annualInterestRate/12
bal = balance
pay = 0
while bal>0:
    bal = balance
    pay += 10
    for i in range(12):
        mub = bal - pay
        bal = mub + mub*monthlyIntRate
print "Lowest Payment: "+str(pay)              

##USING BISECTION SEARCH TO MAKE THE PROGRAM FASTER
## code
mir = annualInterestRate/12.0    #monthlyInterestRate
lb = balance/12                  #lower bound
ub = balance*((1+mir)**12)/12.0  #upper bound
bal = balance
while bal!=0:
    bal = balance
    avg = (lb + ub)/2
    for i in range(12):
        mub = bal - avg
        bal = round((mub + mub*mir),2)
    if bal>0:
        lb = avg
    elif bal<0:
        ub = avg
print "Lowest Payment: "+str(round(avg,2))   
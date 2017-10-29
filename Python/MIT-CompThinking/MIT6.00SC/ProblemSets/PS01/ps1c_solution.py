# 6.00 PS1-C Solution
# Uses bisection search to find the fixed minimum monthly payment needed
# to finish paying off credit card debt within a year

# Retrieve input
original_balance = float(raw_input("Enter the outstanding balance on your credit card: "))
interest_rate = float(raw_input("Enter the annual credit card interest rate as a decimal: "))

# Initialize state variables
balance = original_balance
low_payment = balance/12
high_payment = (balance*(1+(interest_rate/12))**12)/12

# Use bisection search until the search space is sufficiently small
while True:
    balance = original_balance
    monthly_payment = (low_payment + high_payment)/2

    # Simulate passage of time until outstanding balance is paid off
    # Each iteration represents 1 month
    for month in range(1,13):
        interest = round(balance*interest_rate/12, 2)
        balance += interest - monthly_payment
        if balance <= 0:
            break
        
    if (high_payment - low_payment < 0.005):
        # Bisection search space is small enough
        # Print result
        print "RESULT"

        # Round monthly payment up to the nearest cent
        monthly_payment = round(monthly_payment + 0.004999, 2)
        print "Monthly payment to pay off debt in 1 year:", round(monthly_payment,2)

        # Recompute remaining balance and the number of months needed
        balance = original_balance
        for month in range(1,13):
            interest = round(balance*interest_rate/12, 2)
            balance += interest - monthly_payment
            if balance <= 0:
                break
        print "Number of months needed:", month
        print "Balance:", round(balance,2)
        break
    elif balance < 0:
        #Paying too much
        high_payment = monthly_payment
    else:
        #Paying too little
        low_payment = monthly_payment


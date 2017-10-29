# 6.00 PS1-B Solution
# Determines fixed minimum monthly payment needed to finish paying off credit card debt in 1 year

# Retrieve input
initialBalance = float(raw_input("Enter the outstanding balance on your credit card: "))
interestRate = float(raw_input("Enter the annual credit card interest rate as a decimal: "))

# Initialize state variables
monthlyPayment = 0
monthlyInterestRate = interestRate/12
balance = initialBalance

# Test increasing amounts of monthlyPayment in increments of $100
# until it can be paid off in a year
while balance > 0:

    monthlyPayment += 10
    balance = initialBalance
    numMonths = 0
    
    # Simulate passage of time until outstanding balance is paid off
    # Each iteration represents 1 month
    while numMonths < 12 and balance > 0:
        
        # Count this as a new month     
        numMonths += 1

        # Interest for the month
        interest = monthlyInterestRate * balance
        
        # Subtract monthly payment from outstanding balance
        balance -= monthlyPayment

        # Add interest
        balance += interest

# Round final balance to 2 decimal places
balance = round(balance,2)

print "RESULT"
print "Monthly payment to pay off debt in 1 year:", monthlyPayment
print "Number of months needed:", numMonths
print "Balance:",balance
        
        
    
    


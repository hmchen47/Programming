
# Exercises 4.6
# Rewrite your pay computation with time-and-a-half for overtime and create 
# a function called computepay which takes two parameters (hours and rate).
#
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

def computepay(hrs, pay_rate):
    if (hours > 40.0):
        pay = pay_rate * (40.0 + (hrs - 40) * 1.5)
    else:
        pay = pay_rate * hrs
    return pay

print "\n"
hours = raw_input("Enter Hours: ")
try:
    hours_ = float(hours)
except ValueError:
    print "Hours must be numerical value"
    exit()   
 
rate = raw_input("Enter Rate: ")
try:
    rate_ = float(rate)
except ValueError:
    print "Rate must be numerical vlaue"
    exit()

payment = computepay(hours_, rate_)

print "Pay: ", payment

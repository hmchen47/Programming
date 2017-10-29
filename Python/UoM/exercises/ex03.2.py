
# Cheapter 3 Conditional execution
#
# 3.10 Exercise
#
#
# Exercise 3.2
# Rewrite your pay prgram usingf try and exxcept so that your program handles 
# non-numeric input gracefully by printing a message and exiting the program.
# The following shows two executions of the program:
# 
# Enter Hours: 20
# Enter Rate: nine
# Error, Please enter numeric input
#
# Enter Hours: forty
# Error, please enter numeric input
#

hours = raw_input("Enter Hours:")
try:
    hrs = float(hours)
except ValueError:
    print "Error, please enter numeric input"
    exit()

rates = raw_input("Enetr Rate:")
try:
    rts = float(rates)
except ValueError:
    print "Enror, please enter numeric input"
    exit()

if (hrs > 40):
    pay = rts * (40 + (hrs - 40) * 1.5)
else:
    pay = rts * hrs

print "Pay", pay

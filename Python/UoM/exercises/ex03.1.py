
# Cheapter 3 Conditional execution
#
# 3.10 Exercise
#

# Exercise 3.1 
# Review your pay compution to give the employee 1.5 times the hourly rate for hours 
# worked above 40 hours.
#
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

hours = raw_input('Enter Hours:')
hrs = float(hours)

rates = raw_input("Enter Rate:")
rts = float(rates)

if (hrs > 40):
    pay = rts * (40 + (hrs - 40)* 1.5)
else:
    pay = rts * hrs

print "Pay:", pay



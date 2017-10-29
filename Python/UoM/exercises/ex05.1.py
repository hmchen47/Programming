
# Exercise 5.1
#
# Write a program which repeatedly reads numbers until the user enters 
# "done". Once "done" is entered, print out the total, count, and 
# average of the numbers.  If the user enters anything other than a number, 
# detect their mistake using try and except and print an error message 
# and skip to the next number.
#
# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid input
# Enter a number: 7
# Enter a number: done
# 16 3 5.3333333333
#

sum = 0.0
count = 0

while True:
    number = raw_input("Enter a number: ")
    try:
        num = float(number)
        sum = sum + num
        count = count + 1
    except ValueError:
        if (number.lower() == "done"):
            break
        print "Invalid input"

print "Total = ", sum, "   Count = ", count, \
    "   average = ", sum/count

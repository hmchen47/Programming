
# Exercise 5.2
# 
# Write another program that promots for a list of numbers as above and
# at the end prints out both the maximum and minimum of the numbers 
# instead of the average.
#

maximum = minimum = 0

while True:
    num = raw_input("Enter number: ")
    try:
        number = float(num)
        if ((maximum == 0) and (minimum == 0)):
            maximum = minimum = number
        if (number > maximum):
            maximum = number
        if (number < minimum):
            minimum = number
    except ValueError:
        if (num.lower() == "done"):
            break
        print "Invalid input"

print "maximum = ", maximum, "  minimum = ", minimum


# Exercise 6.5
#
# Take the following Python code that stores a string:
#   str = 'X-DSPAM-Condifence: 0.8475'
# Use find and string slicing to extract the portion of the string after
# the colon character and the use the floast function to convert the 
# extracted string into a floating point number
#

# string manupulate
str1 = 'X-DSPAM-Condifence: 0.8475'

cpos = str1.find(':')

str2 = str1[cpos+1:]

str2.strip()

print float(str2)

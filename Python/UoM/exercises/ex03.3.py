
# Cheapter 3 Conditional execution
#
# 3.10 Exercise
#
#
# Exercise 3.3
# Wite a progra,m to promote for a core between 0.0 and 1.0. If the score is out of 
# range print an error.  If the score is between 0.0 and 1.0, print a grade using
# the following table
#
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F

print "\n"

str_score = raw_input("Enter score:")

try: 
   score = float(str_score) 
except ValueError:
   print ("Error: please enter numeric input")

if (score > 1.0):
    print "Bas score, score = ", score, " greater than 1.0"
elif (score >= 0.9):
    print "A"
elif (score >= 0.8):
    print "B"
elif (score >= 0.7):
    print "C"
elif (score >= 0.6):
    print "D"
elif (score > 0.0):
    print "F"
else:
    print "Bas score, score = ", score, " less than 0.0"




# Enter score: 0.95
# A

# Enter score: perfect
# Bad score

# Enter score: 10.0
# Bad score

# Enter score: 0.75
# C

# Enter score: 0.5
# F




# Exercise 4.6
#
# Rewrite the grade program from the previous chapter using a function
# called computegrade that takes a score as its parametre and returns
# a grade as a string.
#
#   Score   Grade
#   > 0.9   A
#   > 0.8   B
#   > 0.7   C
#   > 0.6   D
#   <= 0.6  F
# Run the progra repeatedly to test the various differnet values for input.
#

def computegrade(score):
    if (score >= 10.0):
        grade = "Bad score: score should not greater or equal to 10"
    elif (score > 0.9):
        grade = "A"
    elif (score > 0.8):
        grade = "B"
    elif (score > 0.7):
        grade = "C"
    elif (score > 0.6):
        grade = "D"
    elif (score >= 0.0):
        grade = "F"
    else:
        grade = "Bad score: score shoule not less than 0.0"
    return grade

while True:
    in_score = raw_input("Enter score: ")
    try:
        nu_score = float(in_score)
        print computegrade(nu_score)
    except ValueError:
        if (in_score.lower() == "done"):
            exit()
        print "Bad core: score should be numeric value"
    print "\n"

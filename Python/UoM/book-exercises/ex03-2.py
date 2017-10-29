
s = raw_input("Enter score:")

score = float(s)

if score > 1.0:
	grade = "Score must be bwteen 1.0 and 0.0"
elif  score >= 0.9:
	grade = "A"
elif score >= 0.8:
	grade = "B"
elif score >= 0.7:
	grade = "C"
elif score >= 0.6:
	grade = "D"
elif score > 0:
	grade = "F"
else:
	grade = "The score must between 1.0 and 0.0"

print grade
	
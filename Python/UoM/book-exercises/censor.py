'''
Instructions

Write a function called censor that takes two strings, text and word, as input. It should return the text with the word you chose replaced with asterisks.

For example:

censor("this hack is wack hack", "hack") 
should return

"this **** is wack ****"
Assume your input strings won't contain punctuation or upper case letters.
The number of asterisks you put should correspond to the number of letters in the censored word.
'''

def censor(a, b):
	asterisks = "*" * len(b)
	words = a.split()
	newstrlst = []
	for word in words:
		if (word == b):
			newstrlst.append(asterisks)
		else:
			newstrlst.append(word)
	return " ".join(newstrlst)

censor("this hack is wack hack", "hack") 



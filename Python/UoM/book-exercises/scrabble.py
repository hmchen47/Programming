#!/def/bin/python
# __*** Coding: UTF-8 __*__
'''
scrabble_score

Scrabble is a game where players get points by spelling words. Words are scored by adding together the point values of each individual letter (we'll leave out the double and triple letter and word scores for now).

To the right is a dictionary containing all of the letters in the alphabet with their corresponding Scrabble point values.

For example: the word "Helix" would score 15 points due to the sum of the letters: 4 + 1 + 1 + 1 + 8.

Instructions
Define a function scrabble_score that takes a string word as input and returns the equivalent scrabble score for that word.

1. Assume your input is only one word containing no spaces or punctuation.
2. As mentioned, no need to worry about score multipliers!
3. Your function should work even if the letters you get are uppercase, lowercase, or a mix.
4. Assume that you're only given non-empty strings.
'''

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

def scrabble_score(word):
	tscore = 0
	word = word.lower()
	for idx in range(len(word)):
		tscore += score[word[idx]]
	return tscore

scrabble_score("Helix")



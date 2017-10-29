#!/usr/bin/env python
# _*_ coding = UTF-8 _*_

def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.
    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.
    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)
    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    # TO DO ... <-- Remove this comment when you code this function
    score = 0
    for i in word:
        score += SCRABBLE_LETTER_VALUES[i]
    if len(word) == n:
        return (score * len(word)) + 50
    else:
        return score * len(word)
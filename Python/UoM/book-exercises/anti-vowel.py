#!/usr/bin/python

def anti_vowel(text):
    strlst = text.split()
    astrlst = []
    for word in strlst:
        tmpword = []
        for idx in range(len(word)):
            if (word[idx] not in "aeiouAEIOU"):
                tmpword.append(word[idx])
        astrlst.append("".join(tmpword))
    return " ".join(astrlst)

anti_vowel("Make sure to remove lowercase!")
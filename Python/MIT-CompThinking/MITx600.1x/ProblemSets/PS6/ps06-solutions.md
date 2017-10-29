Here is my solution for PS6. Ask if you don't understand my code in comments below. 
Post your code too.

ENCRYPTION (BUILDCODER)
## code 
import string
def buildCoder(shift):
    uc = string.ascii_uppercase
    lc = string.ascii_lowercase
    d = {}

    for i in uc:
        d[i] = uc[(uc.index(i)+shift)%26]
    for i in lc:
        d[i] = lc[(lc.index(i)+shift)%26]
    return d             

ENCRYPTION (APPLYCODER)
## code
def applyCoder(text, coder):
    ans = ""
    d = coder
    for i in text:
        ans += d[i] if i in d else i
    return ans           
ENCRYPTION (APPLYSHIFT)
## code    
def applyShift(text, shift):
    return applyCoder(text, buildCoder(shift))                

DECRYPTION (FINDBESTSHIFT)
## code
import string
def findBestShift(wordList, text):
    finalCnt = 0
    ans = 0
    ltr = string.ascii_letters
    for i in range(26):
        text1 = applyShift(text, i)
        ls = text1.split()
        cnt = 0
        for word in ls:
            word1 = ""
            for c in word:
                if c in ltr:
                    word1 += c
            if word1 in wordList:
                cnt += 1
        if cnt>finalCnt:
            finalCnt = cnt
            ans = i
    return ans             

DECRYPTION (DECRYPTSTORY)
## code
def decryptStory():
    story = getStoryString()
    wordList = loadWords()
    n = findBestShift(wordList, story)
    return applyShift(story, n)              
I hope beginners understand this code.
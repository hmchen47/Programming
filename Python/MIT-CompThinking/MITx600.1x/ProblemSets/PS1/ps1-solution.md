
As deadline for PS1 submission has passed, I am giving my solutions for PS1 here. This is not the shortest (shortest code is not always the best) or most elegant code, but I hope beginners would be able to understand it. 
Please comment below if you have any questions about PS1. I also request other CTAs to add their codes at the end of my post.
COUNTING VOWELS 
just check if each letter in given string is vowel. increment count if it is vowel. print the result.
## code
cnt = 0
for i in s:
    if i in ['a','e','i','o','u']:
        cnt += 1
print cnt         
COUNTING BOBS 
take three contiguous letters in a string at a time. check if it is 'bob'.
## code
cnt = 0
for i in range(len(s)-2):
    if s[i:i+3] == 'bob':
        cnt += 1
print cnt        
ALPHABETICAL SUBSTRINGS initialize maximum substring as empty string. iterate over given string. find the longest substring as done in code. 
ord -> returns ascii value of char 
len -> length of string
## code
maxs = ""
tmp = s[0]
for i in range(1,len(s)):
    if ord(s[i])>=ord(tmp[-1]):
        tmp += s[i]
    else:
        if len(tmp)>len(maxs):
            maxs = tmp
        tmp = s[i]
if len(tmp)>len(maxs):
    maxs = tmp
print maxs
There are many other ways to solve these questions, but most of them are not yet introduces in this course. 
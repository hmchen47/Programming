#!/usr/bin/python
# _*_ coding = UTF-8 _*_

print 'Please think of a number between 0 and 100!'
low = 0
high = 100
ans = abs((low + high) / 2)
print 'Is your secret number ' + ans + ' ?'
x = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
while str(x) != 'c':
    if str(x) == 'h':
        high = ans
    elif str(x) == 'l':
        low = ans
    else:
        print 'Sorry, I did not understand your input.'
    ans = abs((low + high) / 2) 
    print 'Is your secret number ' + str(ans) + ' ?'
    x = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
print 'Game over. Your secret number was: ' + str(ans)  
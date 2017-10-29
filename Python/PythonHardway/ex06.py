#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# Exercise 6: Strings and Text

x = "there ar e%d types of people" % 10 # assign the formated string to variable
binary = "binary"                       # assign string
do_not = "don't"                        # assign string
y = "Those who know %s and those who %s." % (binary, do_not) 
                                        # assign formated string with variables

print(x)                                # print the formated string, x
print(y)                                # print the formated string, y

print("I said: %r." % x)                # print formated string with the quotation
print("I also said: %s" % y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r" 
                    # assign the formated string without the formated value
print(joke_evaluation % hilarious)      # assign value before print

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)        # contcatnate the two trings

"""
Study Drills
1. Go through this program and write a comment above each line explaining it.
2. Find all the places where a string is put inside a string. There are four places.
    line 6, 9, 21, and 26
3. Are you sure there are only four places? How do you know? Maybe I like lying.
4. Explain why adding the two strings w and e with + makes a longer string.
"""

#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# Exercise 14: Prompting and Passing

"""
usage: python3 ex14.py zed
"""

from sys import argv

script, user_name = argv
prompt = '> '

print("Hi %s, I'm the %s script." % (user_name, script))
print("I'd like to ask you a few questions.")
print("Do you like me, %s?" % user_name)
likes = input(prompt)

print("Where do you live, %s?" % user_name)
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""
    Alright, so you said %r about liking me.
    You live in %r.  Not sure where that is.
    And you have a %r computer. Nice.
    """ %(likes, lives, computer))

"""
Study Drills
1. Find out what Zork and Adventure were. Try to find a copy and play it.
2. Change the prompt variable to something else entirely.
3. Add another argument and use it in your script, the same way you did in the previous 
    exercise with first, second = ARGV.
4. Make sure you understand how I combined a \"\"\" style multiline string with the % 
    format activator as the last print.
"""

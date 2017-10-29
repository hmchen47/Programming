#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# Exercise 11: Asking Questions

print("How old are you?")
age = input()
print("How tall are you?")
height = input()
print("How much do you weight?")
weight = input()

print("So, you're %r old, %r tall, and %r heavy" % (age, height, weight))


"""
Study Drills
1. Go online and find out what Python's raw_input does.
2. Can you find other ways to use it? Try some of the samples you find.
3. Write another "form" like this to ask some other questions.
4. Related to escape sequences, try to find out why the last line has '6\'2"' with that 
    \' sequence. See how the single-quote needs to be escaped because otherwise it 
    would end the string?


NB:
The input() function will try to convert things you enter as if they were Python code, 
    but it has security problems so you should avoid it. --> Python3 only provide 
    input() fucntion.
When my strings print out there's a u in front of them, as in u'35'
    That's how Python tells you that the string is Unicode. Use a %s format instead and 
    you'll see it printed like normal.
"""
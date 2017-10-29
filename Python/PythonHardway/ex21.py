#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# Exercise 21: Functions Can Return Something

"""
Usage:  python3 ex21.py
"""

def add(a, b):
    print("ADDING: %d + %d" %(a, b))
    return a + b

def substract(a, b):
    print("SUBSTRACTING: %d - %d" % (a, b))
    return a - b

def multiply(a, b):
    print("MULTIPLYING: %d * %d" % (a, b))
    return a * b

def divide(a, b):
    print("DIVIDING: %d / %d" % (a, b))
    return a / b

print("Let's do some math with just functions!")

age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))

# A puzzle for the extra credit, type it in anyway
print("Here is a puzzle")

what = add(age, substract(height, multiply(weight, int(divide(iq, 2)))))

print("That becomes: {} Can you do it by hand?".format(what))


"""
Study Drills
1. If you aren't really sure what return does, try writing a few of your own functions 
    and have them return some values. You can return anything that you can put to the 
    right of an =.
2. At the end of the script is a puzzle. I'm taking the return value of one function 
    and using it as the argument of another function. I'm doing this in a chain so that 
    I'm kind of creating a formula using the functions. It looks really weird, but if 
    you run the script you can see the results. What you should do is try to figure out 
    the normal formula that would recreate this same set of operations.
3. Once you have the formula worked out for the puzzle, get in there and see what 
    happens when you modify the parts of the functions. Try to change it on purpose to 
    make another value.
4. Do the inverse. Write a simple formula and use the functions in the same way to 
    calculate it.
"""
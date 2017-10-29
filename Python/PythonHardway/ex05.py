#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# Exercise 5: More Variables and Printing

my_name = "Fred Chen"
my_age = 53
my_height = 172
my_weight = 85
my_eyes = "Brown"
my_teeth = "White"
my_hair = "Black"

print("Let's talk about %s." % my_name)
print("He's %d cm height." % my_height)
print("He's %d Kg heavy." % my_weight)
print("Actually that's really heavy.")
print("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print("His teeth are usually %s depending on the cofee." % my_teeth)

# this link is tricky, try to get it exactly right
print("If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight))


"""
Study Drills
1. Change all the variables so there is no my_ in front of each one. Make sure you  
    change the name everywhere, not just where you used = to set them.
2. Try to write some variables that convert the inches and pounds to centimeters and 
    kilograms. Do not just type in the measurements. Work out the math in Python.
3. Search online for all of the Python format characters.
4. Try more format characters. %r is a very useful one. It's like saying "print this no 
    matter what."
"""
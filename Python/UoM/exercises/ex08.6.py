#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Exercise 8.6 
# Rewrite the program that prompts the user for a list of numbers and
# prints out the maximum and minimum of the numbers at the end when the 
# user enters “done”. Write the program to store the numbers the user 
# enters in a list and use the max() and min() functions to compute the 
# maximum and minimum numbers after the loop completes.
#   Enter a number: 6
#   Enter a number: 2
#   Enter a number: 9
#   Enter a number: 3
#   Enter a number: 5
#   Enter a number: done
#   Maximum: 9.0
#   Minimum: 2.0

print "Enter numbres and \"done\" when findish to get maximum and " \
    "minumum numbers"

num_lst = list()
while True:
    numstr = raw_input("Enter a number: ")
    if (numstr.lower() == "done"):
        break;
    try:
        num_lst.append(float(numstr))
    except ValueError:
        print "Please enter a number or \'done\'"
        continue
 
print "Maximum: ", max(num_lst)
print "Minimum: ", min(num_lst)
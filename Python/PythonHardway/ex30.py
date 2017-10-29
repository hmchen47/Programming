#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# Exercise 30: Else and If

"""
Usage:  python3 ex30.py
"""

people = 30
cars = 40
buses = 15

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if buses > cars:
    print("That's too many buses")
elif buses < cars:
    print("Maybe we could take the buses.")
else:
    print("We still can't decide.")

if people > buses:
    print("Alright, let's just take the buses.")
else:
    print("Fine, let's stay home then.")


"""
Study Drills
1. Try to guess what elif and else are doing.
2. Change the numbers of cars, people, and trucks and then trace through each if-
    statement to see what will be printed.
3. Try some more complex boolean expressions like cars > people or trucks < cars.
4. Above each line write an English description of what the line does.
"""
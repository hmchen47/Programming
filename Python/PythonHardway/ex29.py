#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# Exercise 29: What If

"""
Usage: python3 ex29.py
"""

people = 20
cats = 30
dogs = 15

if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")

dogs += 5

if people >= dogs:
    print("People are greater than equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")


"""
Study Drills
1. What do you think the if does to the code under it?
2. Why does the code under the if need to be indented four spaces?
3. What happens if it isn't indented?
4. Can you put other boolean expressions from Exercise 27 in the if-statement? Try it.
5. What happens if you change the initial values for people, cats, and dogs?
"""

#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# Exercise 24: More Practice

"""
Usage:  python3 ex24.py
"""

print("Let's practice everything.")
print('You\'d need to know \'bout with \\ the do \n newlines ad \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehens passion from intuition
and requires and explanation
\n\t\twhere there is non
"""

print("_______________")
print(poem)
print("_______________")

five = 10 - 2 + 3 - 6
print("This should be five: %s" % five)

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("We can also do that this way:")
print("We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates))

start_point /= 10

print("We can also do that this way:")
print("We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point))


"""
Study Drills
1. Make sure to do your checks: read it backward, read it out loud, and put comments 
    above confusing parts.
2. Break the file on purpose, then run it to see what kinds of errors you get. Make 
    sure you can fix it.
"""
#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
Usage:  python3 ex32.py
"""

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print("This is count %d" % number)

# same as above
for fruit in fruits:
    print("A fruit of type: %s" % fruit)

# also we can go through mixed listed too
# notice we have to use %r since we don't know what's in it
for i in change:
    print("I got %r" % i)

# we can also build lists, first start with an empty one
elements = []

# then use the range fucntion to ddo 0 to 5 counts
for i in range(0, 6):
    print("Adding %d to the list." % i)
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print("Element was: %d" % i)


"""
Study Drills
1. Take a look at how you used range. Look up the range function to understand it.
2. Could you have avoided that for-loop entirely on line 22 and just assigned 
    range(0,6) directly to elements?
3. Find the Python documentation on lists and read about them. What other operations 
    can you do to lists besides append?
"""


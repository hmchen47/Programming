#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# Exercise 38: Doing Things to Lists

"""
Usage:  python3 ex38.py
"""

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there's not 10 things in that list, let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: %s" % next_one)
    stuff.append(next_one)
    print("There's %d items now." % len(stuff))

print("There we go: {}".format(stuff))

print("Let's do some things with stuff")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))

"""
Study Drills
1. Take each function that is called, and go through the steps for function calls to 
    translate them to what Python does. For example, more_stuff.pop() is pop(
    more_stuff).
2. Translate these two ways to view the function calls in English. For example, 
    more_stuff.pop() reads as, "Call pop on more_stuff." Meanwhile, pop(more_stuff) 
    means, "Call pop with argument more_stuff." Understand how they are really the same 
    thing.
3. Go read about "object-oriented programming" online. Confused? I was too. Do not 
    worry. You will learn enough to be dangerous, and you can slowly learn more later.
4. Read up on what a "class" is in Python. Do not read about how other languages use 
    the word "class." That will only mess you up.
5. Do not worry If you do not have any idea what I'm talking about. Programmers like to 
    feel smart so they invented object-oriented programming, named it OOP, and then 
    used it way too much. If you think that's hard, you should try to use "functional 
    programming."
6. Find 10 examples of things in the real world that would fit in a list. Try writing 
    some scripts to work with them.
"""

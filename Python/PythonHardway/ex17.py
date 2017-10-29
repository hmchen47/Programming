#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# Exercise 17: More Files

"""
Usage: python ex17.py test.txt new_file.txt
"""

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from %s to %s" % (from_file, to_file))

# we ccould do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()

print("The input file is %d bytes long" % len(indata))

print("Does the output file exist? %r" % exists(to_file))
print("Ready, hit RETURN to continue. CTRL-C to abort")
try:
    input()
except:
    print("Continue...")

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")
out_file.close()
in_file.close()


"""
Study Drills
1. This script is really annoying. There's no need to ask you before doing the copy, 
    and it prints too much out to the screen. Try to make the script more friendly to 
    use by removing features.
2. See how short you can make the script. I could make this one line long.
3. Notice at the end of the What You Should See I used something called cat? It's an 
    old command that "con*cat*enates" files together, but mostly it's just an easy way 
    to print a file to the screen. Type man cat to read about it.
4. Find out why you had to write out_file.close() in the code.
5. Go read up on Python's import statement, and start python to try it out. Try 
    importing some things and see if you can get it right. It's alright if you do not.
"""
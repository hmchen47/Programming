#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# Exercise 10: What Was That?

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split \non a line"
backslash_cat = "I'm \\ a \\cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)


# Escape Sequences
# ESCAPE      WHAT IT DOES.
# \\          Backslash (\)
# \'          Single-quote (')
# \"          Double-quote (")
# \a          ASCII bell (BEL)
# \b          ASCII backspace (BS)
# \f          ASCII formfeed (FF)
# \n          ASCII linefeed (LF)
# \N{name}    Character named name in the Unicode database (Unicode only)
# \r          Carriage Return (CR)
# \t          Horizontal Tab (TAB)
# \uxxxx      Character with 16-bit hex value xxxx (Unicode only)
# \Uxxxxxxxx  Character with 32-bit hex value xxxxxxxx (Unicode only)
# \v          ASCII vertical tab (VT)
# \ooo        Character with octal value ooo
# \xhh        Character with hex value hh

# Study Drills
# 1. Memorize all the escape sequences by putting them on flash cards.
# 2. Use ''' (triple-single-quote) instead. Can you see why you might use that instead 
#     of """ (triple-double-quote)?
# 3. Combine escape sequences and format strings to create a more complex format.
# 4. Remember the %r format? Combine %r with double-quote and single-quote escapes and 
#     print them out. Compare %r with %s. Notice how %r prints it the way you'd write it 
#     in your file, but %s prints it the way you'd like to see it?

# NB:
# %r is printing out the raw representation of what you typed, which is going to  
#     include the original escape sequences. Use %s instead. Always remember this: %r  
#     is for debugging, %s is for displaying.

# Fun code:
# while True:
#     for i in ["/","-","|","\\","|"]:
#         print("%s\r" % i, end=" ")



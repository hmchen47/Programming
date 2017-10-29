#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# Exercise 3: Numbers and Math

"""
+   plus
-   minus
/   slash
*   asterisk
%   percent
<   less-than
>   greater-than
<=  less-than-equal
>=  greater-than-equal

Order: PEMDAS
Prenethese Exponents Multiplication DSivision Addition Substration
"""

print("I will now count my chickens:")

print("Hens", 25 + 30 / 6)                  # calculate 25 + (30/6)
print("Roosters", 100 - 25 * 3 % 4)         # (25*3)%4 = 3

print("Now I will count the eggs:")
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)    # 3 + 2 + 1 - 5 + (4%2) - (1/4) + 6

print("Is it ture that 3 + 2 < 5 - 7?")
print(3 + 2 < 5 - 7)                        # logical operation

print("What is 3 + 2?", 3 + 2)              # adding
print("What is 5 - 7?", 5 - 7)              # substraction

print("Oh, that's why it's False.")

print("How about some more.")               

print("Is it greater?", 5 > -2)             # 5 is greater than -2
print("Is it greater or equal?", 5 >= -2)   # 5 is greater than or equal to -2
print("Is it less or equal?", 5 <= -2)      # 5 is less than or equal to -2


"""
Study Drills
1. Above each line, use the # to write a comment to yourself explaining what the line 
    does.
2. Remember in Exercise 0 when you started python? Start python this way again and 
    using the math operators, use Python as a calculator.
3. Find something you need to calculate and write a new .py file that does it.
4. Notice the math seems "wrong"? There are no fractions, only whole numbers. You need 
    to use a "floating point" number, which is a number with a decimal point, as in 
    10.5, or 0.89, or even 3.0. --> Pthon3 conver to floating
5. Rewrite ex3.py to use floating point numbers so it's more accurate. 20.0 is floating 
    point.
"""


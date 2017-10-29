
PP2 - "#Sharp" Recursion
You must have heard about factorial (5!), square root(root 5), etc of a number. Let us assume there exists an operation “#” on integers greater than equal to 2 such that for any integer x >= 2, 
x# = ((((((2 ^ 3) ^ 4) ^ 5)  …)  …)     x-1) ^  x)
Given: 2# = 2

Example:
3# = (2 ^ 3) = 8
4# = ((2 ^ 3) ^ 4) = (8 ^ 4) = 4096

1. Write a function “sharp” (using recursion) that takes an integer ‘x’ as argument. This function should return the value of x#. Paste your Python code for this function in the appropriate space below. Write 'NA' if you are unable to design this function.

2. Write a function “ndigits” (using recursion) that takes an integer ‘x’ as argument. This function should return the number of digits in the integer x. Paste your Python code for this function in the appropriate space below. Write 'NA' if you are unable to design this function.

3. Determine the value of the expression: 
Result = ndigits(7#) + 2 * ndigits(6#) + ndigits(5#) + ndigits(4#)
You must use the sharp function you designed before for finding the values. Enter the value of the expression in the Result field below. Enter '-1' if you are unable to find this value.

--------
This Practice Problem has been prepared by Nitish Mittal (Email: nitish_mittal [at] outlook [dot] com, Facebook: https://www.facebook.com/nitish94), Teaching Assistant for course MITx 6.00.1x Fall 2015 on edX and is in reference to the course material of Week 3 (Lecture - 5).


def sharp(x):
    '''
    (int) -> int
    x: a natural number, x > 0

    return return of sharp operation which follows the defintion
    x# = ((((((2 ^ 3) ^ 4) ^ 5)  …)  …)     x-1) ^  x)
    with 2# = 2 as base function
    '''
    if x < 2:
        print 'Invalid input, x must greater ttha or equal to 2'
    if x == 2:
        return 2
    else:
        return sharp(x-1)**x

def ndigits(x):
    '''
    (int) -> int
    x: a integer

    return the number of digits in the integer x
    base function when x = 0 ~ 9 as ndigit = 1
    '''
    if (abs(x) - abs(x)%10) < 10:
        return 1
    else:
        return 1 + ndigits(x/10)

Result = ndigits(sharp(7)) + 2 * ndigits(sharp(6)) + ndigits(sharp(5)) + ndigits(sharp(4))
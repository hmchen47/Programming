PP1 - Regular Polygons 'funsum'

URL: https://docs.google.com/forms/d/1Lea6ZJlEVWsXcPiqPZ0JmGDDdvGO1OnXHAqNEtLu1cM/viewform?c=0&w=1

Consider a regular polygon with the number of sides 'n'  and the length of each side 's'.

Area of regular polygon: A quarter of the product of 'n', square of 's' and the reciprocal of tan of angle 'pi' by 'n', where 'pi' is the irrational Mathematical constant.

Perimeter of a polygon: Length of the boundary of the polygon.

Write a function 'funsum' that takes 2 arguments, 'n' and 's'. This function should return the sum of the area and square of the perimeter of the regular polygon, rounded till 4 digits of precision after the decimal point. Paste your Python code for this function in the appropriate space below.

Calculate the value returned by your implemented function 'funsum' for n=7 and s=3. Enter this value in the Result field below.

Example:
For n=5, s=7, funsum(5, 7) = 1309.3034

--------
This Practice Problem has been prepared by Nitish Mittal (nitish_mittal [at] outlook [dot] com), Teaching Assistant for course MITx 6.00.1x Fall 2015 on edX and is in reference to the the course material upto and including Week 2.


import math

def funcsum(n, s):
    # area = n * s^2 / (4*tan(pi/4))
    area = n * s**2.0 / (4.0 * math.tan(math.pi/n))
    #print 'area =', area
    perimeter = n * s * 1.0
    #print 'periemeter =', perimeter
    return round((area + perimeter ** 2), 4)
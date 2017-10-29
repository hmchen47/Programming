#!/usr/bin/env python2
# __*** coding = utf-8 __*__

def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.

    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to
      between start and stop times.
    '''
    # FILL IN YOUR CODE HERE...
    total = 0

    # dealing with step and setpWidth - general
    steps = int((stop - start) / step)
    stepWidth = step

    # calculate the radiation
    for idx in range(0, steps):
        total += (f(start+idx*stepWidth) * stepWidth)

    return total


def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

#print radiationExposure(0, 5, 1)
#    39.10318784326239
print radiationExposure(5, 11, 1)
#    22.94241041057671
#print radiationExposure(0, 11, 1)
#    62.0455982538
#print radiationExposure(40, 100, 1.5)
#    0.434612356115


'''
Cobalt-60.Half-life: 5.27 years. Initial Activity: 10 MBq.
Find total exposure from years 0 - 5.
def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)
Function call: radiationExposure(0, 5, 1)
#   39.10318784326239

Function call: radiationExposure(5, 11, 1)
#   22.94241041057671

Function call: radiationExposure(12, 16, 1)
#   .848645835538622


Radium-224.Half-life: 3.66 days. Initial Activity: 400 MBq.
Find total exposure from days 0 - 4.
def f(x):
    import math
    return 400*math.e**(math.log(0.5)/3.66 * x)

Function call: radiationExposure(0, 4, 0.25)
#   1148.6783342153556

Function call: radiationExposure(5, 10, 0.25)
#   513.4662018628549

Function call: radiationExposure(0, 3, 0.1)
#   559.2259707824549

Function call: radiationExposure(14, 20, 0.1)
#   523.4527522388152

Function call: radiationExposure(48, 72, 0.4)
#   268.79947333082833

Function call: radiationExposure(72, 96, 0.4)
#   82.61081970598869


Cesium-138.Half-life: 32.2 minutes. Initial Activity: 150 MBq.
Find total exposure from minutes 0 - 40.
def f(x):
    import math
    return 150*math.e**(math.log(0.5)/32.2 * x)

Function call: radiationExposure(0, 40, 1)
#   4066.0849302266774

Function call: radiationExposure(100, 400, 4)
#   843.5828023451531

Function call: radiationExposure(1000, 4000, 15)
#   3.6525375905841067e-06


Radon-220.Half-life: 55.6 seconds. Initial Activity: 60 MBq.
Find total exposure from seconds 0 - 60.
def f(x):
    import math
    return 60*math.e**(math.log(0.5)/55.6 * x)

Function call: radiationExposure(0, 60, 0.5)
#   2542.768831286683

Function call: radiationExposure(60, 120, 0.5)
#   1203.5229215597114

Function call: radiationExposure(600, 1200, 5)
#   2.799597134148232
'''

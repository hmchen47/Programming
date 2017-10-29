###########################
# Problem Set 9: Space Cows 
# Name: SOLUTION
# Collaborators:
# Time:

import pylab
import math

#=================================
# Helper functions (solution only)
#=================================
def f(coeffs, xval):
    """
    Helper function to calculate f(x) for a given coefficient array of
    a function f and x value
    """
    result = 0
    coeffs = coeffs[::-1]   # reverse the coefficients
    for deg, c in enumerate(coeffs):
        result += c * (xval ** deg)
    return result

#============================
# Part A: Breeding Alien Cows
#============================

# Problem 1: File I/O
def loadData(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated x,y pairs.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    (x, y) - a tuple containing a Pylab array of x values and
             a Pylab array of y values
    """
    x = []
    y = []
    
    try:
        f = open(filename, "r")
        for line in f:
            pt = line.strip().split(",")
            x.append(int(pt[0]))
            y.append(int(pt[1]))
        f.close()
    except:
        print "Error opening file: {0}".format(filename)

    return (pylab.array(x), pylab.array(y))

# Problem 2a: Curve Fitting: Finding a polynomial fit
def polyFit(x, y, degree):
    """
    Find the best fit polynomial curve of the specified degree for the data
    contained in x and y and return the coefficients for the best fit
    polynomial curve of the given degree using the original set of x values.

    Parameters:
    x - a Pylab array of x values
    y - a Pylab array of y values
    degree - the degree of the desired best fit polynomial

    Returns:
    a Pylab array of coefficients for the polynomial fit function of the
    specified degree, corresponding to the input domain x.
    """
    return pylab.polyfit(x, y, degree)

# Problem 2b: Curve Fitting: Finding an exponential fit
def expFit(x, y):
    """
    Find the best fit exponential curve's coefficients for the data contained
    in x and y.

    Parameters:
    x - a Pylab array of x values
    y - a Pylab array of y values

    Returns:
    a Pylab array of coefficients for the exponential fit function
    corresponding to the input domain x.
    """
    assert len(x) == len(y)
    y = pylab.log2(y)
    return polyFit(x, y, 1)

# Problem 3: Evaluating regression functions
def rSquare(measured, estimated):
    """
    Calculate the R-squared error term.

    Parameters:
    measured - one dimensional array of measured values
    estimate - one dimensional array of predicted values

    Returns: the R-squared error term
    """
    assert len(measured) == len(estimated)
    EE = ((estimated - measured)**2).sum()
    mMean = measured.sum()/float(len(measured))
    MV = ((mMean - measured)**2).sum()
    return 1 - EE/MV

def generatePlots(datasets):
    """
    Generate plots to compare the different fit functions for the given
    data sets.

    Parameters:
    datasets - a list of data sets stored as (x, y) tuples, where x and y
        are each a list of data points (x or y values)
    """
    xdata1, ydata1 = datasets[0]
    m = 2
    n = 6
    funcs = [ polyFit(xdata1, ydata1, 1),
              polyFit(xdata1, ydata1, 2),
              polyFit(xdata1, ydata1, 4),
              expFit(xdata1, ydata1) ]
    
    pylab.figure()
    pylab.title("Comparison of fit functions to space cow data sets")
    # Generate the polynomial plots
    for i in range(0, m*n - 3, 3):
        p = funcs[i/3]

        for j, data in enumerate(datasets):
            x = data[0]
            y = data[1]
            pylab.subplot(m, n, i+j+1)
            ey = [ f(p, xval) for xval in x ]
            pylab.plot(x, y, 'bo', x, ey, 'r-')
            pylab.title("R2 = %s" % round(rSquare(y, ey), 6))
            pylab.xlabel("Time")
            pylab.ylabel("# of cows")
            
    # Generate the exponential plots
    i = 9
    for j, data in enumerate(datasets):
        x = data[0]
        y = data[1]
        pylab.subplot(m, n, i+j+1)

## TWICE-FIXED CODE
        b, ln_a = funcs[3] #WRONG: expFit(x, y)
        a = pylab.exp2(ln_a)
        ey = [a * math.pow(2, b * xval) for xval in x]
        pylab.plot(x, y, 'bo', x, ey, 'r-')
        pylab.title("R2 = %s" % round(rSquare(y, ey), 6))
        pylab.xlabel("Time")
        pylab.ylabel("# of cows")

    pylab.subplots_adjust(wspace = 0.75, hspace = 0.35)
    pylab.show()

# Problem 4: Choosing a model
"""
The quartic polynomial fits best for the training data by a small amount over
the quadratic polymonial. However, given more data, we can see that the quadratic
is a much better model over time.

The best fit curve should be x^2 + 10.  Using this model, the aliens will have
bred 40,000 cows in 200 days
"""

#======================
# TESTING CODE
#======================
def main():
    # Problem 1
    data1 = loadData("ps9a_data1.txt")
    data2 = loadData("ps9a_data2.txt")
    data3 = loadData("ps9a_data3.txt")

    # Checks for Problem 1
    assert all( [len(data) == 25 for xy in data] for data in [data1, data2] ), \
        "Error loading data from files; number of terms does not match expected"
    assert all( [len(data) == 100 for xy in data] for data in [data1, data2] ), \
        "Error loading data from files; number of terms does not match expected"

    # Problem 4
    # TODO: Make calls to other functions here for calculating errors and
    # generating plots.
    generatePlots( [ data1, data2, data3 ] )

if __name__ == "__main__":
    main()

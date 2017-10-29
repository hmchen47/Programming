###########################
# Problem Set 9: Space Cows 
# Name: 
# Collaborators:
# Time:

import pylab

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
    # Open the file and set up the result lists
    f = open(filename, 'r')
    x = []
    y = []

    # Iterate through each line of the file, casting both values in the x,y
    # tuples as ints and storing them in their respesctive lists
    for line in f:
        splitLine = line.strip().split(',')
        x.append(int(splitLine[0]))
        y.append(int(splitLine[1]))

    # Close the file and return the tuple of pylab arrays
    f.close()
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
    log_y = pylab.log2(y)
    return polyFit(x, log_y, 1)

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

## My additional code for problem 4
def getCoeffs(data, degree):
    """
    Computes the coefficients for the best-fit curve of degree degree, and
    returns the coefficients as a list, with the highest order first and
    constant term last.

    data: (x,y) tuple of pylab.array instances
    degree: int >= 1
    returns: list of coefficients
    """
    x,y = data
    return polyFit(x, y, degree)

def evalPoly(data, coeffs):
    """
    Uses the coefficients in coeffs to estimate the y-values for the data,
    given its x-values.

    data: (x,y) tuple of pylab.array instances
    coeffs: a list of coefficients, with the highest order first and constant
            term last

    returns: a pylab.array containing the estimated y values given the
             coefficients
    """
    x,y = data
    degree = len(coeffs) - 1
    y_est = 0
    for i in range(len(coeffs)):
        y_est += coeffs[i] * x**(degree-i) # y = a*x^deg + b*x^(deg-1) + ...
    r2 = rSquare(y, y_est)
    return y_est, r2

def getCoeffsExp(data):
    x,y = data
    return expFit(x, y)

def evalExp(data, coeffs):
    x,y = data
    b, loga = coeffs
    a = 2**loga # y = a * 2*(b**x)
    y_est = a * pylab.exp2(b*x)
    r2 = rSquare(y, y_est)
    return y_est, r2

#======================
# TESTING CODE
#======================
def plotCurve(plotNum, data, model, evalFn, bounds, title):
    """
    Helper function to plot the subplots -- given the data and the model,
    it uses evalFn to generate an approximate curve and plots that as a line
    against the measured data, plotted as a scatterplot.
    """
    # Set this as the plotNum-th plot, and add the title
    pylab.subplot(220 + plotNum) # 2x2 layout of 4 subplots

    # Approximate the curve using the model, and plot both the data as a
    # scatterplot and the approximated curve as a solid line
    curve, r2 = evalFn(data, model)
    pylab.scatter(data[0], data[1])
    pylab.plot(data[0], curve, 'r')
    pylab.title(title + "\nR2: " + str(round(r2,6)))
    pylab.subplots_adjust(wspace=0.25, hspace=0.35)

    # Set the bounds so all 4 subplots have the same bounds
    if bounds == []:
        bounds.append(pylab.xlim())
        bounds.append(pylab.ylim())
    else:
        pylab.xlim(bounds[0])
        pylab.ylim(bounds[1])
        
def main():
    # Problem 1
    data1 = # TODO: your code here
    data2 = # TODO: your code here
    data3 = # TODO: your code here

    # Checks for Problem 1
    assert all( [len(data) == 25 for xy in data] for data in [data1, data2] ), \
        "Error loading data from files; number of terms does not match expected"
    assert all( [len(data) == 100 for xy in data] for data in [data1, data2] ), \
        "Error loading data from files; number of terms does not match expected"

    # Problem 4
    # TODO: Make calls to other functions here for calculating errors and
    # generating plots.

    # Generate the models using data1
    linearModel = getCoeffs(data1, 1)
    quadraticModel = getCoeffs(data1, 2)
    quarticModel = getCoeffs(data1, 4)
    exponentialModel = getCoeffsExp(data1)
        
    # Plot the curves against the scatterplot for the data
    for data in [data1, data2, data3]:
        x, y = data
        bounds = []

        # Plot each of the four curves
        pylab.figure()
        plotCurve(1, data, linearModel, evalPoly, bounds, "Linear fit")
        plotCurve(2, data, quadraticModel, evalPoly, bounds, "Quadratic fit")
        plotCurve(3, data, quarticModel, evalPoly, bounds, "Quartic fit")
        plotCurve(4, data, exponentialModel, evalExp, bounds, "Exponential fit")
        
    pylab.show()



if __name__ == "__main__":
    main()
    
# Correct R^2 values:
#
# data1:
##    0.61775
##    0.668
##    0.681936
##    0.651161
# data2:
##    0.409526
##    0.418002
##    0.432838
##    0.479279
# data3:
##    0.422134
##    0.956673
##    -0.263859
##    0.874737

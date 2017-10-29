# 6.00 Problem Set 2
#
# Successive Approximation: Newton's Method
#
# Name          : Solutions
# Collaborators : <your collaborators>
# Time spent    : <total time>
#

def evaluate_poly(poly, x):
    """
    Computes the value of a polynomial function at given value x. Returns that value.

    Example:
    >>> poly = [0.0, 0.0, 5.0, 9.3, 7.0]    # f(x) = 5x^2 + 9.3x^3 + 7x^4 
    >>> x = -13
    >>> print evaluate_poly(poly, x)  # f(-13) = 5(-13)^2 + 9.3(-13)^3 + 7(-13)^4 
    180339.9

    poly: list of numbers, length > 0
    x: number
    returns: float
    """
    total = 0.0
    for i in xrange(len(poly)):
        total += poly[i] * (x ** i)
    return total

def compute_deriv(poly):
    """
    Computes and returns the derivative of a polynomial function. If the
    derivative is 0, returns [0.0].

    Example:
    >>> poly = [-13.39, 0.0, 17.5, 3.0, 1.0]    # - 13.39 + 17.5x^2 + 3x^3 + x^4
    >>> print compute_deriv(poly)        # 35^x + 9x^2 + 4x^3
    [0.0, 35.0, 9.0, 4.0]

    poly: list of numbers, length > 0
    returns: list of numbers
    """
    poly_deriv = []
    if len(poly) < 2:
        return [0.0]
    for j in xrange(1, len(poly)):
        poly_deriv.append(float(j * poly[j]))
    return poly_deriv
    

def compute_root(poly, x_0, epsilon):
    """
    
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a list containing the root and the number of iterations required
    to get to the root.

    Example:
    >>> poly = [-13.39, 0.0, 17.5, 3.0, 1.0]    # - 13.39 + 17.5x^2 + 3x^3 + x^4
    >>> x_0 = 0.1
    >>> epsilon = .0001
    >>> print compute_root(poly, x_0, epsilon)
    [0.80679075379635201, 8]

    poly: list of numbers, length > 1.
         Represents a polynomialfunction containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: list [float, int]
    """
    root = x_0
    counter = 1
    while abs(evaluate_poly(poly, root)) >= epsilon:
        root = (root - evaluate_poly(poly, root) /
                evaluate_poly(compute_deriv(poly), root))
        counter += 1
    return [root, counter]

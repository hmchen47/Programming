###########################
# Problem Set 9b: Space Cows 
# Name: SOLUTION
# Collaborators:
# Time:

import math
import copy
from ps9b_partition import getPartitions
import time

#================================
# Part 2: Transporting Space Cows
#================================

# Problem 5
def loadCows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name, weight pairs
    """
    try:
        f = open(filename, "r")
        d = {}
        for line in f:
            pt = line.strip().split(",")
            d[str(pt[0])] = float(pt[1])
        f.close()
    except:
        print "Error opening file: {0}".format(filename)

    return d

# Problem 6
def greedyTransport(cows,limit):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via a greedy heuristic (always choose the heaviest cow to fill the
    remaining space).
    
    Parameters:
    cows - a dictionary of name (string), weight (float) pairs
    limit - weight limit of the spaceship
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """    
    trips = []
    cows_tuple = [(weight,name) for name, weight in cows.items()]
    cows_tuple.sort(reverse=True)
    
    while len(cows_tuple) > 0:
        updated = []
        t = {}
        for weight, name in cows_tuple:
            if sum(t.values()) + weight <= limit:
               t[name] = weight
            else:
                updated.append((weight,name))
        cows_tuple = updated[:]
        trips.append(t.keys())
    return trips

# Problem 7
def bruteForceTransport(cows,limit):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.
    
    Parameters:
    cows - a dictionary of name (string), weight (float) pairs
    limit - weight limit of the spaceship
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """ 
    min_trip = len(cows.keys())
    ans_trip = {}
    
    for part in getPartitions(cows.keys()): # Specific partition
        # Weights for each trip
        weights = [sum(cows[name] for name in p) for p in part] 
        if False not in [x <= limit for x in weights]:
            if len(part) < min_trip:
                min_trip = len(part)
                ans_trip = part

    return ans_trip
            

# Problem 8
if __name__ == "__main__":

    """
    Using the data from ps9b_data.txt and the specified weight limit, run your
    greedyTransport and bruteForceTransport functions here. Print out the
    number of trips returned by each method, and how long each method takes
    to run in seconds.
    """
    cows_data = loadCows("ps9b_data.txt")

    start = time.time()
    greedy = greedyTransport(cows_data, 1.0)
    end = time.time()
    print "== Greedy Transport Results =="
    print "Minimum no. trips: ", len(greedy)
    print "Trip: ", greedy
    print "Time: ", round((end-start),5), "seconds",
    print "(" + str(round((end-start)*1000, 5)) + " milliseconds)"

    print

    start = time.time()
    brute = bruteForceTransport(cows_data, 1.0)
    end = time.time()
    print "== Brute Force Transport Results =="
    print "Minimum no. trips: ", len(brute)
    print "Trip: ", brute
    print "Time: ", round((end-start),5), "seconds",
    print "(" + str(round((end-start)*1000, 3)) + " milliseconds)"


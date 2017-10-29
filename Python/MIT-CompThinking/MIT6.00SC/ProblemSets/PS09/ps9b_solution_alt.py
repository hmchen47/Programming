###########################
# Problem Set 9b: Space Cows 
# Name: Solutions
# Collaborators:
# Time:

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
    cows = {}

    # Read the file
    f = open(filename, 'r')
    for line in f:

        # Line is name, weight
        name, weight = line.strip().split(',')
        cows[name] = float(weight)

    # Close the file and return the dictionary
    f.close()
    return cows

# More correct problem 6
def getHeaviestFittingCow(cows_dict, weightLeft):
    poss_weights = [val for val in cows_dict.values() if val <= weightLeft]
    if poss_weights == []: return None

    weight = max(poss_weights)
    for cow in cows_dict:
        if cows_dict[cow] == weight:
            return cow

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
    # Set up the data structures
    trips_list = []
    current_trip = []
    current_weight = 0

    # Loop until we've placed all cows in a trip
    cows_left = cows.copy() # safe copy!
    while len(cows_left) > 0:

        # Get the maximum-weight cow and remove it from the dictionary
        heavycow = getHeaviestFittingCow(cows_left, limit - current_weight)

        # If the heaviest cow is not None, add it to the trip
        if heavycow != None:
            # Remove the cow from the list
            weight = cows_left[heavycow]
            del cows_left[heavycow]

            # Add the cow to the trip
            current_trip.append(heavycow)
            current_weight += weight

        # Otherwise, add the old trip to the list and start a new one
        else:
            trips_list.append(current_trip)
            current_trip = []
            current_weight = 0

    # The last trip hasn't been added to the list yet, so do so and return it
    if current_trip != []: trips_list.append(current_trip)
    return trips_list

# Problem 6
##def getHeaviestCow(cows_dict):
##    weight = max(cows_dict.values())
##    for cow in cows_dict:
##        if cows_dict[cow] == weight:
##            return cow, weight
##
##def greedyTransport(cows,limit):
##    """
##    Finds the allocation of cows that minimizes the number of spaceship trips
##    via a greedy heuristic (always choose the heaviest cow to fill the
##    remaining space).
##    
##    Parameters:
##    cows - a dictionary of name (string), weight (float) pairs
##    limit - weight limit of the spaceship
##    
##    Returns:
##    A list of lists, with each inner list containing the names of cows
##    transported on a particular trip and the overall list containing all the
##    trips
##    """
##    # Set up the data structures
##    trips_list = []
##    current_trip = []
##    current_weight = 0
##
##    # Loop until we've placed all cows in a trip
##    cows_left = cows.copy() # safe copy!
##    while len(cows_left) > 0:
##
##        # Get the maximum-weight cow and remove it from the dictionary
##        heavycow, weight = getHeaviestCow(cows_left)
##        del cows_left[heavycow]
##
##        # If the cow fits in the current trip, add it!
##        if current_weight + weight <= limit:
##            current_trip.append(heavycow)
##            current_weight += weight
##
##        # Otherwise, add the old trip to the list and start a new one, with this
##        # cow on it first
##        else:
##            trips_list.append(current_trip)
##            current_trip = [heavycow]
##            current_weight = weight
##
##    # The last trip hasn't been added to the list yet, so do so and return it
##    trips_list.append(current_trip)
##    return trips_list

# Problem 7
def calculateTripWeight(trip, cows):
    return sum([cows[name] for name in trip])

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
##    # Play with generators
##    for part in getPartitions([1,2,3]):
##        print part
    
    # Set up the data structures
    best_trips_list = []
    best_trips_count = len(cows) # can't be worse than 1 cow per trip

    # Use the generator-returning getPartitions to partition the cows into all
    # possible trip combinations
    for part in getPartitions(cows.keys()):

        # Check if the current partition contains only valid trips
        isValid = False not in [calculateTripWeight(trip,cows) <= 1.0 for trip in part]

        # If it is valid, see if it has a better trip count than the best we've
        # seen so far, and if so replace it
        if isValid and len(part) < best_trips_count:
            best_trips_list = part
            best_trips_count = len(part)

    # Return the best trip partition found
    return best_trips_list

# Problem 8
if __name__ == "__main__":

    """
    Using the data from ps9b_data.txt and the specified weight limit, run your
    greedyTransport and bruteForceTransport functions here. Print out the
    number of trips returned by each method, and how long each method takes
    to run in seconds.
    """
    # Question: How do the results compare? Which ran faster?
    # First, load the cows
    cows = loadCows("ps9b_data.txt")
    for cow in cows:
        print cow + ":", cows[cow]
    print

    # Question: How do the results compare? Which ran faster?
    import time
    start = time.time()
    greedy = greedyTransport(cows, 1.0)
    end = time.time()
    greedy_time = end - start

    start = time.time()
    bruteForce = bruteForceTransport(cows, 1.0)
    end = time.time()
    bruteforce_time = end - start

    print greedy_time # 2.88486480713e-05 = 0.0000288 seconds
    print bruteforce_time # 1.51596808434 = 1.516 seconds
    
    print greedy
    print bruteForce

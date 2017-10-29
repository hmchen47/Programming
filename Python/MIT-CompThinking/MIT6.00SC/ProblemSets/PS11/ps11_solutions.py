########################
# Problem Set 11: The 6.00 Social Network
# Name: Solutions
# Collaborators: 
# Time:
#

from graph import *

#
# PROBLEM 1a
#

def buildFBGraph(filename):
    """
    Reads the contents of the given file. Assumes the file contents contain
    data in the form of space-separated unique x y pairs of itegers. Each x y pair
    is unique and represents a pair of friends on facebook. Resturns a graph
    representing the data.

    Parameters:
    filename - the name of the data file as a string. 

    Returns:
    a Graph structure representing the facebook network of friends encoded in the data
    file. Each node is a student and each pair of students are connected if they are
    friends on facebook.
    """
    
    g = Graph()
    f = open(filename)
    for i in range(120):
        g.addNode(Node(i))
    for line in f:
        line = line.strip()
        student1, student2 = line.split()
        node1 = Node(student1)
        node2 = Node(student2)
        g.addEdge(Edge(node1, node2))
    f.close()
    return g
    

#
# PROBLEM 1b
#

def degOfSeparation(graph, student1, student2):
    """
    Takes in a graph respresenting a facebook network of 6.00 friends and returns
    the degree of separation between two 6.00 students.

    Parameters:
    graph - a Graph structure representing a network of 6.00 friends.
    student1 - integer reprsenting student1
    student2 - integer represnting student2

    Returns: an integer representing degree of seperation between student1 and
    student2, i.e. how many steps away in the friendship chain A is from B. For
    example, if A and B are friends, then their degree of separation is 1; if A
    and B are not friends, but they have a mutual friend C, then their degree of
    separation is 2. If student1 and student2 are not connected, then return -1.
    """
   
    path = BFS(graph, Node(str(student1)), Node(str(student2)))
   
    if path:
        return path.getLength()
    else:
        return -1
    


#
# PROBLEM 2a
#

def buildRatedFBGraph(filename):
    """
    Read the contents of the given file. Assumes each line in the file has three space separated
    numbers; the first two numbers represent the two students who are Facebook friends, and the
    third number is their friendship rating. Resturns a graph representing the data.

    Parameters:
    filename - the name of the data file as a string. 

    Returns:
    a Graph structure representing the facebook network of friends and friendship ratings encoded
    in the data file.
    """
    
    g = Graph()
    f = open(filename)
    for i in range(120):
        g.addNode(Node(i))
    dummyIndex = 0
    for line in f:
        line = line.strip()
        student1, student2, rating = line.split()
        node1 = Node(student1)
        node2 = Node(student2)
        # Store dummy nodes in a collection 
        way = [node1]
        for i in range(int(rating)-1):
            dummy = Node('d'+str(dummyIndex))
            g.addNode(dummy)
            way.append(dummy)
            dummyIndex += 1
        way.append(node2)
        for i in range(len(way)-1):
            g.addEdge(Edge(way[i], way[i+1]))
    f.close()
    return g
    
  


#
# PROBLEM 2b
#

def ratedDegOfSeparation(graph, student1, student2):
    """
    Takes in a graph respresenting a facebook network of friends as well as their friendship ratings
    and returns a rated degree of separation between two 6.00 students.

    Parameters:
    graph - a Graph structure representing a network of 6.00 friends as well as their friendship ratings.
    student1 - integer reprsenting student1
    student2 - integer represnting student2

    Returns: an integer representing rated degree of seperation between student1 and student2
    If student1 and student2 are not connected, then return -1.
    """
    path = BFS(graph, Node(str(student1)), Node(str(student2)))
    if path:
        return path.getLength()
    else:
        return -1


#
# PROBLEM 3
#

def findGroups(graph):
    """
    Takes in a graph respresenting a facebook network of friends and returns a list of sets,
    where each set is a separate group of friends in the network. 

    Parameters:
    graph - a Graph structure representing a network of 6.00 friends.

    Returns:
    A list of sets where each set is collection of integers, representing the group of friends
    in the network. In one group of friends, each student is reachable from every other student
    in the group through some number of friends in the group. A member in one group of friends
    cannot reach a member in another group.
    """
    nodes = graph.getNodes()
    res = []
    while len(nodes) > 0:
        group = set()
        group_ints = set()
        source = nodes.pop()
        for node in nodes:
            if degOfSeparation(graph, source, node) != -1:
                group.add(node)
                group_ints.add(int(node.getName()))
        for node in group:
            nodes.remove(node)
        group_ints.add(int(source.getName()))
        res.append(group_ints)
    return res
        


Quiz - MITx 600.2x Final Exam
=============================

6.00.2X - INTRODUCTION TO COMPUTATIONAL THINKING AND DATA SCIENCE
-----------------------------------------------------------------

FINAL EXAM, FALL 2015

Out December 17, 2015 at 14:00 UTC (2 pm)

Due December 21, 2015 at 23:30 UTC (11:30 pm)

What time is it in UTC right now?

 ------------------------------------
** there is no time limit, submit your answers before the deadline **
------------------------------------

This exam is designed to take on average roughly 3 hours of time.  You can start the exam when it is convenient for you, but you must complete this examination by 23:30 pm UTC on December 21. Please look up this time in your local time zone.

When you open the next page, you will have started the exam. You do not need to start now.

Note that during the exam period, the discussion forum will be shut down, to avoid any accidental discussion of exam material. It will reopen at the end of the exam period. 

If you have a bug or error to report during the exam, you may email 6.00.2x-exams@mit.edu. Include your edX ID (found at the top right of any edX page, by the house icon). Only bug or error reports will be accepted; all other emails will be discarded. We try to respond to emails within 7 hours. Since the entire staff is on the Unites States east coast, we will take about that long to reply to emails sent overnight and apologize for this inconvenience.

If there is an error with the exam, we will fix it and then post a message on the course updates page. Check that page often! It is the fastest way we have to announce errors and fixes.

You may use as a resource anything we posted online, the course textbook, any other textbooks you may possess, and any notes you have prepared yourself. We ask you not to use the Internet to search for solutions. You may not communicate with any person about this examination while working on it. Furthermore, you may not communicate about the exam until the exam has been closed for everyone.

For non-coding problems, you will be allowed as little as one submission; for coding questions you will be allowed 10 submissions, so that you may have a chance to fix any errors.

Part of what we are testing on this exam is your ability to write comprehensive test suites for your own functions, which is why we limit the number of submissions allowed per coding problem. For problems that ask you to write your own code, you may use Canopy or IDLE - or an online Python interpreter such as CodeSkulptor or Python Tutor - to test your solution before pasting it into the answer box. We ask that you do not run code provided in non-coding questions in Canopy.

If you want to go back and study some more before starting this exam you can do so.

Good Luck!

Issues
------

Below are some issues you may encounter while completing this exam, along with solutions recommended by the staff.


SPINNING QUEUE ICON

![Spinning Queue](https://goo.gl/8TjIJl)

It is possible that when you submit your code to the grader (by hitting Check), you will get the spinning processig icon. Usually, this should only last a few seconds and you will get a reply back from the grader within those few seconds.

If the spinning queued icon lasts longer than a few seconds:
Go to another problem in the course that uses code submission. For example, [L2 Problem 5](https://goo.gl/u8NMgl). Hit Check with any code there to check if the spinning Processing issue is with all problems or just one.

* If spinning Processing doesn't happen in another problem, then check whether you have pasted the function definition twice (nested inside the same function definition). If so, only use one function definition and click Check again.
* If spinning Processing doesn't happen in another problem, you might have a syntax error. The best way to check this is to paste the code you have from the box in your local IDE and run it -- any syntax error or indentation error will show up.
* If spinning Processing doesn't happen in another problem, then check your code for any special characters. In the past, the offending character showed up in your pasted code as a one or more '\b' (no quotes) or a non-ASCII character (\u200b for example). If you remove the character, your code should give you a grader reply.
* If spinning Processing doesn't happen in another problem and you have followed the previous three points, try clicking Check again.

If spinning Processing happens in another problem as well, the graders are probably down. If there is no recent post in the Updates and News page about the grader being down, please email the staff. Someone will update that page and look into the issue.

PROGRAM TIMED OUT (SLOW CODE OR INFINITE LOOPS)

![Time Out](https://goo.gl/7VTT5r)

If you see this error, you have an infinite loop in your program (or more rarely, slow code). The grader uses test cases not shown in the problem, so check your code with more test cases. Most likely, there is a path through your code that leads to an infinite loop. Good test cases use unique inputs -- try very small or very large values, or uncommon combinations of inputs.

SUBMISSION CANNOT BE GRADED

![Not Graded](http://goo.gl/nez0zN)

After pasting code from your own working environment and hitting Check, you may see this message (or a similar one inside a yellow box). Those students who use non-ascii characters are most likely to see this. After pasting, some special characters (like accented letters) were introduced. To the grader, they are a sequence of characters (\u200b for example). Go through the code in the textbox and check that all your characters are ASCII ( a-z and 0-9 but none with accents). These special characters may appear in bright red font so should be easy to spot.


PROBLEM 1-1  (1 point possible)
-------------------------------
"Coefficient of variation" means the coefficient of the polynomial curve that fits the data best. (True/False)

Ans:


PROBLEM 1-2  (1 point possible)
-------------------------------
If we let the k-means clustering algorithm run for a very long time, we will eventually end up with all the data points in one cluster.(True/False)

Ans:


PROBLEM 1-3  (1 point possible)
-------------------------------
Training an algorithm on data set A and then testing it on a completely separate data set B is an example of unsupervised learning. (True/False)

Ans:


PROBLEM 1-4  (1 point possible)
-------------------------------
Consider an undirected graph with non-negative weights that has an edge between each pair of nodes. The shortest distance between any two nodes is always the path that is the edge between the two nodes.(True/False)

Ans:


PROBLEM 1-5  (1 point possible)
-------------------------------
A bimodal distribution is a probability distribution with two different modes. For example, exam grades can be bimodal when the students can be classified into one of two groups: either they understand the material or they understand less than half the material. A distribution made up of two normal distributions with equal standard deviations is noticeably bimodal if the means of each distribution are separated by at least 2 standard deviations.

The following line of python code will produce a bimodal distribution if called repeatedly:
    random.gauss( 50,10) + random.gauss( 70, 10 ) (True/False)

Ans:


PROBLEM 2-1  (5 points possible)
--------------------------------
What does the following code print? Assume Pylab's estimation code is perfect - that is, if you calculate that it would print 0.25, type 0.25 into the box rather than something like 0.24999999999. You may type in strings with or without quotes and separate the numbers by a space.

```python
a = 1.0
b = 2.0
c = 4.0
yVals = []
xVals = range(-20, 20)
for x in xVals:
    yVals.append(a*x**2 + b*x + c)
yVals = 2*pylab.array(yVals)
xVals = pylab.array(xVals)
try:
    a, b, c, d = pylab.polyfit(xVals, yVals, 3)
    print a, b, c, d
except:
    print 'fell to here'
```

Ans: 

PROBLEM 2-2  (1 point possible)
-------------------------------
Consider the following sets of measurements and answer the following 3 questions:
A. [0,1,2,3,4,5,6,7,8]
B. [5,10,10,10,15]
C. [0,1,2,4,6,8]
D. [6,7,11,12,13,15]
E. [9,0,0,3,3,3,6,6]

Select the two lists that have the same mean and variance.
A. A 
B. B 
C. C 
D. D 
E. E 
F. No two sets have the same mean and variance.

Ans:

PROBLEM 2-3  (1 point possible)
-------------------------------
Consider following Python functions:

```python
def possible_mean(L):
    return sum(L)/len(L)

def possible_variance(L):
    mu = possible_mean(L)
    temp = 0
    for e in L:
        temp += (e-mu)**2
    return temp / len(L)
```
Select the two lists that return the same values when passed into the possible_variance function that is defined above.

A. A 
B. B 
C. C 
D. D 
E. E 
F. No two sets return the same values.

Ans:

PROBLEM 2-4  (1 point possible)
-------------------------------
Is the the answer to Problem 2-2 the same as the answer to Problem 2-3? If not, why are they different?

A. They are the same. 
B. They are different because the possible_mean function adds up the wrong values. 
C. They are different because of the way Python 2.7 handles division of integers. 
D. They are different because of floating point precision issues.

Ans:



PROBLEM 3
---------
For this problem you are going to simulate growth of fox and rabbit population in a forest!

The following facts are true about the fox and rabbit population:
* The maximum population of rabbits is determined by the amount of vegetation in the forest, which is relatively stable.
* There are never fewer than 10 rabbits; the maximum population of rabbits is 1000.
* For each rabbit during each time step, a new rabbit will be born with a probability of prabbit reproduction

    $$p_{rabbit reproduction} = 1.0 − (current rabbit population) / (max rabbit population)$$

  In other words, when the current population is near the maximum, the probability of giving birth is very low, and when the current population is small, the probability of giving birth is very high.
* The population of foxes is constrained by number of rabbits.
  There are never fewer than 10 foxes.
* At each time step, after the rabbits have finished reproducing, a fox will try to hunt a rabbit with success rate of pfox eats rabbit
pfox eats rabbit=current rabbit populationmax rabbit population
In other words, the more rabbits, the more likely a fox will eat one.

  If a fox succeeds in hunting, it will decrease the number of rabbits by 1 immediately. Remember that the population of rabbits is never lower than 10.

  Additionally, if a fox succeeds in hunting, then it has a 1/3 probability of giving birth in the current time-step.

  If a fox fails in hunting then it has a 10 percent chance of dying in the current time-step.
* If the starting population is below 10 then you should do nothing. You should not increase the population nor set the population to 10. 
Start with 500 rabbits and 30 foxes.

At the end of each time step, record the number of foxes and rabbits.

Run the simulation for 200 time steps, and then plot the population of rabbits and the population of foxes as a function of time step.

Use the following steps, and the template file [exam_problem3.py](https://goo.gl/mcrXjK) (click to download .py file), as guides in your implementation of this simulation.

Step 1: Write the procedure, `rabbitGrowth`, that updates the number of rabbits during the first part of a time step

Step 2: Write the procedure, `foxGrowth`, that updates the number of rabbits and foxes during the second part of a time step

Step 3: Write the master procedure, `runSimulation`, that loops for some amount of time steps, doing the first part and then the second part of the simulation. Record the two populations in two different lists, and return those lists.

Paste your code for the three functions `rabbitGrowth`, `foxGrowth`, and `runSimulation` in the following box.

WARNING

DO NOT define the global variables MAXRABBITPOP, CURRENTRABBITPOP, or CURRENTFOXPOP in this box. We alter the values of these variables to test your code. If you define the variables in this box, you may overwrite our values, causing your code to be marked incorrect.

"See Full Output": If you are getting the line "0 10" in your output for "Test 4 foxGrowth" then for this particular test, your code changes the CURRENTFOXPOP (increases it if the fox population has gone below the minimum fox population), which is not the right behavior -- the code should not reset CURRENTFOXPOP.

PROBLEM 3-1  (15 points possible)
---------------------------------
Enter the code for the functions rabbitGrowth, foxGrowth, and runSimulation below.

```python
# Enter the code for the functions rabbitGrowth, foxGrowth, and runSimulation
# in this box.
```


Follow the next steps of the simulation to answer the remaining questions.

Step 4: Assume `MAXRABBITPOP = 1000`, `CURRENTRABBITPOP = 500`, `CURRENTFOXPOP = 30`, `numSteps = 200`. Plot two curves, one for the rabbit population and one for the fox population. You won't be submitting the plots. They are for your own understanding.

Step 5: Use polyfit to find the coefficients of a 2nd degree polynomial for the rabbit curve and the same for the fox curve. Then use `polyval` to evaluation the 2nd degree polynomial and plot it, e.g.

```python
 coeff = polyfit(range(len(rabbitPopulationOverTime)), rabbitPopulationOverTime, 2)

 plot(polyval(coeff, range(len(rabbitPopulationOverTime))))
```
Of course your variables and plotting commands may not look identical to the above code; the above code is shown just to give you an idea of what we mean.

Once you have finished Steps 4 and 5, continue on to answer the following questions.

PROBLEM 3-2  (1 point possible)
-------------------------------
At some point in time, there are more foxes than rabbits. (True/False)

Ans:

PROBLEM 3-3  (1 point possible)
-------------------------------
The polyfit curve for the rabbit population is:
A. A straight line 
B. A concave up curve (looks like a U shape) 
C. A concave down curve (looks like a ∩ shape) 
D. An exponentially decreasing curve 
E. An exponentially increasing curve  None of the above

Ans:


PROBLEM 3-4  (1 point possible)
-------------------------------
The polyfit curve for the fox population is:
A. A straight line  A concave up curve (looks like a U shape) 
B. A concave down curve (looks like a ∩ shape) 
C. An exponentially decreasing curve 
D. An exponentially increasing curve  None of the above

Ans: 

PROBLEM 3-5  (1 point possible)
-------------------------------
Changing the initial conditions from 500 rabbits and 30 foxes to 50 rabbits and 300 foxes changes the general shapes of both the polyfit curves for the rabbit population and fox population. (True/False)

Ans:


PROBLEM 3-6  (1 point possible)
-------------------------------
Let's say we make a change in the original simulation. That is, we are going to change one detail in the original simulation, but everything else will remain the same as it was explained in Problem 3 - Part A.

Now, if a fox fails in hunting, it has a 90 percent chance of dying (instead of a 10 percent chance, as in the original simulation).

Changing the probability of an unsuccessful fox dying from 10% to 90% changes the general shapes of both the polyfit curves for the rabbit population and fox population. (True/False)

Ans:


PROBLEM 4 - PART A
------------------

In lecture, we explored the concept of a random walk, using a set of different models of drunks. Here is the code ([randomWalks-segment2.py](https://goo.gl/pysYLe)) that we used in lecture for Locations, Fields, and the base class of Drunk – you should not have to study this code in detail, since you have seen it in lecture.

Rather than assuming the drunk is walking in a large field, we can assume that the field is enclosed with a fence. When the drunk reaches the fence different things may happen:
1. SW (Solid Walls): The drunk cannot go through the fence. If the drunk sees that his move will make him run into the fence, the drunk will hesitate and not move from the spot.
2. SP (Small Planet): The rightmost edge is connected to the leftmost edge, and the top edge is connected to the bottom edge.
3. WW (Warped World): If the drunk moves past the right-most edge, he ends up on the top edge and vice versa. If the drunk moves past the left edge, he ends up on the bottom edge and vice versa.
4. BH (Back to Home): Whenever the drunk reaches any edge, the drunk is transported back to the center of the world.

Here are several routines, where `leftEdge` is always less than `rightEdge`, and `topEdge` is always greater than `bottomEdge`. dx and dy can be positive or negative numbers. You can assume the drunk will not land directly on an edge (for example, the case x + dx == leftEdge will not happen).

For each of the following code segments, select the type of wall (SW, SP, WW, or BH) that is being implemented. Choose option `NA` (None of the Above) to indicate that the code segment does not correctly implement any of the given types of wall.

PROBLEM 4-1  (1 point possible)
-------------------------------

```python
if x+dx > leftEdge and x+dx < rightEdge:
    x += dx
if  y+dy > bottomEdge and y+dy < topEdge:
    y += dy
```
A. SW 
B. SP 
C. WW 
D. BH 
E. NA

Ans:

PROBLEM 4-2  (1 point possible)
-------------------------------

```python
if x+dx < rightEdge and x+dx > leftEdge:
    x += dx
elif x+dx > rightEdge:
    x = leftEdge
elif x+dx < leftEdge:
    x =rightEdge
if y+dy < topEdge and  y+dy > bottomEdge:
    y += dy
elif y+dy > topEdge:
    y = topEdge
elif y+dy < bottomEdge:
    y = bottomEdge
```
A. SW 
B. SP 
C. WW 
D. BH 
E. NA

Ans:

PROBLEM 4-3  (1 point possible)
-------------------------------

```python
if x+dx > leftEdge and x+dx < rightEdge:
    x += dx
elif x+dx > rightEdge:
    x = leftEdge + (x+dx - rightEdge)
elif x+dx < leftEdge:
    x = rightEdge - (leftEdge - (x+dx))

if  y+dy > bottomEdge and y+dy < topEdge:
    y += dy
elif y+dy > topEdge:
    y = bottomEdge + (y+dy - topEdge)
elif y+dy < bottomEdge:
    y = topEdge - (bottomEdge - (y+dy))
```
A. SW 
B. SP 
C. WW 
D. BH 
E. NA

Ans:

PROBLEM 4-4  (1 point possible)
-------------------------------

```python
if x+dx < rightEdge and x+dx > leftEdge:
    x += dx
elif x+dx > rightEdge:
    x = bottomEdge
elif x+dx < leftEdge: 
    x = topEdge
if y+dy < topEdge and  y+dy > bottomEdge:
    y += dy
elif y+dy > topEdge: 
    y = leftEdge
elif y+dy < bottomEdge:  
    y = rightEdge
```
A. SW 
B. SP 
C. WW 
D. BH 
E. NA

Ans:

PROBLEM 4-5  (1 point possible)
-------------------------------

```python
if x+dx > rightEdge:  
    x = y
if x+dx < leftEdge: 
    x = y
if x+dx < rightEdge and x+dx > leftEdge:
    x += dx
if y+dy > topEdge: 
    y = x
if y+dy < bottomEdge:  
    y = x
if y+dy < topEdge and  y+dy > bottomEdge:
    y += dy
```
A. SW 
B. SP 
C. WW 
D. BH 
E. NA

Ans:

PROBLEM 4-6  (1 point possible)
-------------------------------

```python
if x+dx > rightEdge:
    x,y = (rightEdge-leftEdge)/2
if x+dx < leftEdge:
    x,y = (rightEdge-leftEdge)/2
if x+dx < rightEdge and x+dx > leftEdge:
    x += dx
if y+dy > topEdge:
    x,y = (rightEdge-leftEdge)/2
if y+dy < bottomEdge:
    x,y = (rightEdge-leftEdge)/2
if y+dy < topEdge and  y+dy > bottomEdge:
    y += dy
```
A. SW 
B. SP 
C. WW 
D. BH 
E. NA

Ans:

PROBLEM 4-7  (1 point possible)
-------------------------------
```python
if x+dx < rightEdge and x+dx > leftEdge and y+dy < topEdge and y+dy > bottomEdge:
    x += dx
    y += dy
else:
    x = leftEdge + (rightEdge-leftEdge)/2
    y = bottomEdge + (topEdge-bottomEdge)/2
```
A. SW 
B. SP 
C. WW 
D. BH 
E. NA

Ans:



PROBLEM 4 - PART B
------------------
In lecture, we explored the concept of a random walk, using a set of different models of drunks. Here is the code ([randomWalks-segment2.py](https://goo.gl/pysYLe)) that we used in lecture for Locations, Fields, and the base class of Drunk – you should not have to study this code in detail, since you have seen it in lecture.

Rather than assuming the drunk is walking in a large field, we can assume that the field is enclosed with a fence. When the drunk reaches the fence different things may happen:
1. SW (Solid Walls): The drunk cannot go through the fence. If the drunk sees that his move will make him run into the fence, the drunk will hesitate and not move from the spot.
2. SP (Small Planet): The rightmost edge is connected to the leftmost edge, and the top edge is connected to the bottom edge.
3. WW (Warped World): If the drunk moves past the right-most edge, he ends up on the top edge and vice versa. If the drunk moves past the left edge, he ends up on the bottom edge and vice versa.
4. BH (Back to Home): Whenever the drunk reaches any edge, the drunk is transported back to the center of the world.
N-Random-Step: The drunk takes N*N steps with

```python
dx,dy = random.choice(
    [(-1.0,-1.0),(-1.0,0.0),(-1.0,1.0),(0.0,1.0),(0.0,-1.0),(1.0,-1.0),
    (1.0,0.0),(1.0,1.0)]
)
```

Assume the drunk walks for long enough that he has reached a wall. A mark is made on the graph for each position that the drunk occupies. For each of the graphs, indicate which type of walls (SW, SP, WW, or BH) bound the field. Choose option NA (None of the Above) to indicate that the graph is not consistent with a field that has any of the given types of wall.

Click on each graph to see the image at full size.

PROBLEM 4-8  (1 point possible)
-------------------------------
![blue diagram](https://goo.gl/aixs96)
A. SW 
B. SP 
C. WW 
D. BH 
E. NA

Ans:


PROBLEM 4-9  (1 point possible)
-------------------------------
![yellow diagram](https://goo.gl/j03Iq5)
A. SW 
B. SP 
C. WW 
D. BH 
E. NA

Ans:


PROBLEM 4-10  (1 point possible)
-------------------------------
![red diagram](https://goo.gl/0yZYEJ)
A. SW 
B. SP 
C. WW 
D. BH 
E. NA

Ans:


PROBLEM 4-11  (1 point possible)
-------------------------------
![green diagram](https://goo.gl/cITLrC)
A. SW 
B. SP 
C. WW 
D. BH 
E. NA

Ans:



PROBLEM 5-1  (1 point possible)
-------------------------------
Graphs are a convenient way to represent the relations between people, objects, concepts, and more.

There are many ways to create a graph, some of which are random. A random graph is one that is generated by randomly adding edges to a list of nodes. The list of nodes for this problem is initialized as follows:

```python
nodes = []
for i in range(n):
    nodes.append(newNode(i)) # newNode takes one parameter, the number of the node
```

A helper method, addEdge, is referenced in this problem. The addEdge method takes two integers - representing nodes in the graph - and adds a directed edge from the first node to the second node. So, addEdge(8, 2) adds a directed edge from Node 8 to Node 2.

In each code piece below, a graph is generated using the above node set by adding edges in some fashion. Your job is to examine the code and select the type of graph that will be generated. Your choices for each question will be: tree; graph (undirected graph); line graph; digraph (directed graph); complete graph or clique; bar graph; bipartite graph; loop or connected chain of nodes. Note that this last option refers to a graph that consists of one single, large loop or connected chain of nodes.

```python
for i in range(len(nodes)):
    x = random.choice(nodes)
    y = random.choice(nodes)
    addEdge(x,y)
```
 
Ans:


PROBLEM 5-2  (1 point possible)
-------------------------------
```python
for i in range(len(nodes)):
    x = random.choice(nodes)
    y = random.choice(nodes)
    addEdge(x,y)
    addEdge(y,x)
```

Ans: 
 

PROBLEM 5-3  (1 point possible)
-------------------------------
```python
for i in range(len(nodes)):
    w = random.choice(nodes)
    x = random.choice(nodes)
    y = random.choice(nodes)
    z = random.choice(nodes)
    addEdge(w,x)
    addEdge(x,y)
    addEdge(y,z)
    addEdge(z,w)
```

Ans: 
 

PROBLEM 5-4  (1 point possible)
-------------------------------

```python
for x in nodes:
    for y in nodes:
        addEdge(x,y)
        addEdge(y,x)
```

Ans: 

PROBLEM 5-5  (1 point possible)
-------------------------------
The out degree of a node is the number of its neighbors, i.e. for a node x, its degree is the number edges, of the form `(x, y_i)`, where `y_i` is some other node.

Which graph has the largest out degree per node?

Ans:


PROBLEM 6-1  (1 point possible)
-------------------------------
Suppose are given a stack of documents and are told that documents with similar sets of keywords are about the same topic. Your job is to organize the documents as best you can by topic. The following 4 questions refer to this situation.

For this situation, it is best to use an unsupervised learning algorithm. (True/False)

Ans: 


PROBLEM 6-2  (1 point possible)
-------------------------------
Given the above information, which of the following would be the most appropriate feature to use?
A. The author's name. 
B. The number of pages in a document. 
C. The number of times a particular keyword appears in a document. 
D. The number of times particular keywords and common words (for example, "the", "in", "at") appear in a document.

Ans: 


PROBLEM 6-3  (1 point possible)
-------------------------------
Your boss comes back with a list of 60 specific keywords as well as 5 specific topics that each keyword is best associated with. Which of the following is true, given this additional information?
A. We can switch to a supervised learning algorithm. 
B. We can use the k-means clustering algorithm with k = 60 
C. We can use the k-means clustering algorithm with k = 5

Ans:

PROBLEM 6-4  (1 point possible)
-------------------------------
Your boss comes back one last time with new information. He can now tell you the topic of each document. However, he found some more documents for which the topic is still unknown. Given this information, can we use a supervised learning algorithm to classify the new documents? (Yes/No)

Ans: 


PROBLEM 6-5  (1 point possible)
-------------------------------
Remember that in Problem Set 6, we used different linkage distance measures to calculate the distances between clusters and decide which cluster a point should belong to. Consider this new method of finding linkage distances, which makes use of the linkage distance methods from the problem set:

```python
    def mysteryLinkageDist(self, other):
        av_dist = self.averageLinkageDist(other)
        max_dist = self.maxLinkageDist(other)
        min_dist = self.singleLinkageDist(other)
        retDist = 0.0
        if av_dist == max_dist and max_dist == min_dist:
            retDist = av_dist
        elif av_dist == max_dist:
            retDist = av_dist
        elif av_dist == min_dist:
            retDist = av_dist
        elif max_dist == min_dist:
            retDist = min_dist
        else:
            retDist = random.choice([av_dist,min_dist,max_dist])
        return retDist
```

You are given the following data points with the following feature values:

```python
a 4
b 9
c 9
d 9
e 8
f 0
g 8
```
  
Answer the following 3 questions based on the above code.

You are asked to run the hierarchical clustering algorithm from Problem Set 6 with the singleLinkage, maxLinkage, averageLinkage, and mysteryLinkage distance metrics and asked to report the results at a cutoff of 4 clusters. The final clusters will be the same, no matter which linkage we use. (True/False)

Ans: 


PROBLEM 6-6  (1 point possible)
-------------------------------
Now you run the hierarchical clustering algorithm from Problem Set 6 with the mysteryLinkage distance metric and look at the results at a cutoff of 3 clusters. The final clusters will be:
A. C0:a ||| C1:b,c,d,e,g ||| C2:f 
B. C0:a,f |||C1:b,c,d ||| C2:e,g 
C. C0:a,f,e,g ||| C1:b,c ||| C2:d,e 
D. C0:a,e,g ||| C1:b,c,d ||| C2:f

Ans:


PROBLEM 6-7  (1 point possible)
-------------------------------
Conceptually, the mysteryLinkage distance metric takes a vote for each data point and decides which cluster to assign the point to based on the majority vote. (True/False)

Ans: 



PROBLEM 7
---------
Some random graphs have more structure than others. For the graph that represents the internet, nodes are web sites and there is a directed edge from one site, say x, to another site, say y, whenever site x has a link to site y. There are a few sites that are massively popular, like Google, Facebook, Twitter, and EdX, that have lots of incoming edges. However, most sites have very few incoming edges.

It is interesting to build random graphs that mimic this structure. The best way to do this is to grow the graph. There are `n` nodes and initially no edges. Edges are added at random, but in a non-uniform way.

To add in new edges to a graph, first choose a node x at random. Then choose another node y with a probability proportional to the popularity, or _connectedness_, of the node. For example, if a node has `k` edges it is twice as likely to be chosen than an node that has $k/2$ edges. Finally, add the edge from x to y to the graph.

Each node has a set of incoming edges and a set of outgoing edges. Each node has an _in-degree_, which is the number of incoming edges to the node, and an _out-degree_, the number of outgoing edges from the node. An edge cannot connect a node to itself and there can be at most one edge from a given x to a given y.

Suppose whenever a new edge—say it is (x,y)—is added, there are three things updated:
* node y is added as an outgoing edge (or "out-edge") of node x
* node x is added as an incoming edge (or "in-edge") of node y
* (x,y) is added to the list allEdges

PROBLEM 7-1  (1 point possible)
-------------------------------
Now consider how to write some code to add an edge to a graph G, with all the nodes of G contained in the list G.allNodes and all the edges of G contained in the list G.allEdges. The items in G.allEdges are pairs of nodes, such as (x, y). (x, y) indicates a directed edge from node x to node y.

Assume we have built a graph G according to the above rules. Consider the lines of pseudocode:

```python
z = random.choice(G.allNodes)
(x,y) = random.choice(G.allEdges)
add new edge z -> y
```
True or False? The node y is chosen with probability proportional to its popularity. (True/False)

Ans:

PROBLEM 7-2  (1 point possible)
-------------------------------
To avoid selecting a self-edge (an edge from z to z), all edges pointing to z are first removed from allEdges before making the choice.

True or False? The following Python expression creates a list of all edges that does not include any edges into node z:

```python
allEdgesExceptZ = []
for (x,y) in G.allEdges:
    if y != z:
        allEdgesExceptZ.append((x, y))
```

Ans: 

PROBLEM 7-3  (1 point possible)
-------------------------------
The time to construct the list allEdgesExceptZ is `O(E2)`, where `E` is the number of edges. (True/False)

Ans:

PROBLEM 7-4  (1 point possible)
-------------------------------
Consider the following procedure used to initialize a graph with n nodes:

```python
def initializeGraph(n): # n is an integer, the number of nodes in the graph
    G = siteGraph() # Initializes an empty graph, with G.graphNodes set to []
    for i in range(n):
        G.graphNodes.append(newNode(i)) # newNode takes one parameter, the number of the node
    for i in range(n):
        x = G.graphNodes[i]
        y = G.graphNodes[ (i+1) % n ]
        x.addOutEdge(y)
    y.addInEdge(x)
    G.allEdges.append((x, y))
    return G.graphNodes
```
True or False? The procedure initializeGraph ensures that there is at least one path between any two nodes in the graph. (True/False)

Ans:

PROBLEM 7-5  (4 points possible)
--------------------------------
Assume a random power-graph is created using the procedures explained above with 100 nodes. The following values are computed and plotted as a function of the number of edges, according to the following code:

```python
maxDegrees, meanDegrees, meanDegreeVariances, meanShortestPaths = [],[],[],[]
graph = initializeGraph(n) 
for nEdges in range(n, n*n, n*n/10 ):
   graph.addEdges(nEdges)
   maxDegrees.append(graph.maxDegree())
   meanDegrees.append(graph.meanDegree())
   meanDegreeVariances.append(graph.meanDegreeVariances())
   meanShortestPaths.append(graph.meanShortestPath())
```
For each of the following plots, indicate which list was used to generate the plot:

![plot1](https://goo.gl/ZJaNsK)
 
A. maxDegrees 
B. meanDegrees 
C. meanDegreeVariances 
D. meanShortestPaths

Ans: 
 
![plot2](https://goo.gl/T1r1ee)
 
A. maxDegrees 
B. meanDegrees 
C. meanDegreeVariances 
D. meanShortestPaths

Ans: 
 
![plot3](https://goo.gl/9CP7JB)
 
A. maxDegrees 
B. meanDegrees 
C. meanDegreeVariances 
D. meanShortestPaths

Ans: 
 

![plot4](https://goo.gl/1CU73O)
 
A. maxDegrees 
B. meanDegrees 
C. meanDegreeVariances 
D. meanShortestPaths

Ans: 


SURVEY QUESTIONS  (6 points possible)
-------------------------------------
1. Overall, I found the material in the course to be:
A. Too Easy 
B. Just Right 
C. Too Hard

Ans: 

2. Overall, I found the lectures in the course to be:
A. Too Easy 
B. Just Right 
C. Too Hard

Ans: 

3. Overall, I found the finger exercises to be:
A. Too Easy 
B. Just Right 
C. Too Hard

Ans: 

4. Overall, I found the problem sets to be:
A. Too Easy 
B. Just Right 
C. Too Hard

Ans: 

5. I also completed 6.00.1x this term. (True/False)

Ans: 

6. I will recommend 6.00.2x to friends and/or colleagues in the future.
A. Yes, definitely! 
B. Yes, with a few reservations 
C. No


Ans: 
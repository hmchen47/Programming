
6.00.1X - INTRODUCTION TO COMPUTER SCIENCE

Final Quiz
==========
This exam is designed to take on average roughly 3 hours of time You can start the exam when it is convenient for you, but you must complete this examination by 23:30 pm UTC on October 27. Please look up this time in your local time zone.

When you open the next page, you will have started the exam. You do not need to start now. 

Note that during the exam period, the discussion forum will be shut down, to avoid any accidental discussion of exam material. It will reopen at the end of the exam period. 

If you have a bug or error to report during the exam, you may email 6.00.1x-exams@mit.edu. Include your edX ID (found at the top right of any edX page). Only bug or error reports will be accepted; all other emails will be discarded. We try to respond to emails within 7 hours. Since the entire staff is on the Unites States east coast, we will take about that long to reply to emails sent overnight and apologize for this inconvenience.

If there is an error with the exam, we will fix it and then post a message on the course updates page. Check that page often! It is the fastest way we have to announce errors and fixes.

You may use as a resource anything we posted online (including the textbook), any other textbooks you may possess, and any notes you have prepared yourself. We ask you not to use the Internet to search for solutions. You may not communicate with any person about this examination while working on it. Furthermore, you may not communicate about the exam until the exam has been closed for everyone.

For multiple choice problems you will be allowed exactly one submission; for coding questions you will be allowed 10 submissions, so that you may have a chance to fix any errors.

Part of what we are testing on this exam is your ability to write comprehensive test suites for your own functions, which is why we limit the number of submissions allowed per coding problem. For problems that ask you to write your own code, you may use Canopy or IDLE - or an online Python interpreter such as CodeSkulptor or Python Tutor- to test your solution before pasting it into the answer box. We ask that you do not run code provided in non-coding questions in Canopy.

If you want to go back and study some more before starting this exam you can do so.

Good Luck!

Issues to Concern
------------------
Below are some issues you may encounter while completing this exam, along with solutions recommended by the staff.

SPINNING QUEUE ICON
It is possible that when you submit your code to the grader (by hitting Check), you will get the spinning processig icon. Usually, this should only last a few seconds and you will get a reply back from the grader within those few seconds.

If the spinning queued icon lasts longer than a few seconds:
Go to another problem in the course that uses code submission. For example, L2 Problem 8. Hit Check with any code there to check if the spinning Processing issue is with all problems or just one.

If spinning Processing doesn't happen in another problem, then check whether you have pasted the function definition twice (nested inside the same function definition). If so, only use one function definition and click Check again.

If spinning Processing doesn't happen in another problem, you might have a syntax error. The best way to check this is to paste the code you have from the box in your local IDE and run it -- any syntax error or indentation error will show up.

If spinning Processing doesn't happen in another problem, then check your code for any special characters. In the past, the offending character showed up in your pasted code as a one or more '\b' (no quotes) or a non-ASCII character (\u200b for example). If you remove the character, your code should give you a grader reply.

If spinning Processing doesn't happen in another problem and you have followed the previous three points, try clicking Check again.

If spinning Processing happens in another problem as well, the graders are probably down. If there is no recent post in the Updates and News page about the grader being down, please email the staff. Someone will update that page and look into the issue.

PROGRAM TIMED OUT (SLOW CODE OR INFINITE LOOPS)
If you see this error, you have an infinite loop in your program (or more rarely, slow code). The grader uses test cases not shown in the problem, so check your code with more test cases. Most likely, there is a path through your code that leads to an infinite loop. Good test cases use unique inputs -- try very small or very large values, or uncommon combinations of inputs.

SUBMISSION CANNOT BE GRADED
After pasting code from your own working environment and hitting Check, you may see this message (or a similar one inside a yellow box). Those students who use non-ascii characters are most likely to see this. After pasting, some special characters (like accented letters) were introduced. To the grader, they are a sequence of characters (\u200b for example). Go through the code in the textbox and check that all your characters are ASCII ( a-z and 0-9 but none with accents). These special characters may appear in bright red font so should be easy to spot.

PROBLEM 1
---------
PROBLEM 1-1
In the statement L = [1,2,3], L is a class.

Ans: False

PROBLEM 1-2  (1 point possible)
The orders of growth of O(n^2+1) and O(n^5+1) are both polynomial.

Ans: True

PROBLEM 1-3  (1 point possible)
The complexity of binary search on a sorted list of n items is O(logn).

Ans: True

PROBLEM 1-4  (1 point possible)
Let d be a dictionary. For all type combinations of a and b, the following is allowed:
    d = {}
    d[a] = 0
    d[b] = d[a]

Ans: False

PROBLEM 1-5  (1 point possible)
Performing binary search on an unsorted list will always return the correct answer in O(n) time where n is the length of the list.

Ans: False

PROBLEM 2
---------
PROBLEM 2-1  (1 point possible)
The function 8000*n*log(n)+1000*log(n)+40*n^300+2^n is
A. O(2^n)  
B. O(n*log(n))  
C. O(n^300)  
D. O(log(n))

Ans: A

PROBLEM 2-2  (1 point possible)
Consider the function f below. What is its Big O complexity?
    def f(n):
        def g(m):
            m = 0
            for i in range(m):
                print m
        for i in range(n):
            g(n)
A. O(1)  
B. O(log(n))  
C. O(n)  
D. O(n^2)

Ans: C (m=0 to initialize)

PROBLEM 2-3  (1 point possible)
Consider the statement: L = {'1':1, '2':2, '3':3}. Which is correct?
A. L is a list  
B. L is a class  
C. L is immutable  
D. L contains 6 elements  
E. L has integer keys  
F. L maps strings to integers

Ans: F

PROBLEM 2-4  (1 point possible)
Consider a list of length n. Assume you want to search that list for k different elements. What is the smallest value of k for which the asymptotic running time of sorting the list before performing the k searches would be no larger than the asymptotic running time of doing the k searches on the original unsorted list. Assume that the fastest known algorithms are used for sorting and searching in each case.
A. k=1  
B. k=log(n)  
C. k=n  
D. k=n^2

Ans: D (c migt not hold, 2log(n) < n)

PROBLEM 2-5  (1 point possible)
Consider the code:
L = [1,2,3]
d = {'a': 'b'}
def f(x):
    return 3
Which of the following does NOT cause an exception to be thrown?
A. print L[3]  
B. print d['b'] 
C. for i in range(10000001, -1, -2):
       print f(i)
D. print int('abc')  
E. None of the above

Ans: C

PROBLEM 3
---------
Below are four different functions for sorting a list of elements in increasing order. For simplicity, assume that the list only contains ints. For each, we are going to ask you about how the algorithm creates its output and about the worst case time complexity - or order of growth - of the algorithm. Answer the questions without running the code on your computer.

PROBLEM 3-1
-----------
Answer the following 5 questions based on this code.
    def sort1(lst):
        swapFlag = True
        iteration = 0
        while swapFlag:
            swapFlag = False
            for i in range(len(lst)-1):
                if lst[i] > lst[i+1]:
                    temp = lst[i+1]
                    lst[i+1] = lst[i]
                    lst[i] = temp
                    swapFlag = True

            L = lst[:]  # the next 3 questions assume this line just executed
            iteration += 1
        return lst

PROBLEM 3-1 A  (1 point possible)
When we reach the marked spot in the code, and the variable iteration has value n, the smallest n+1 elements of the sorted version of lst are in L in the correct order.

Ans: False

PROBLEM 3-1 B  (1 point possible)
When we reach the marked spot in the code, and the variable iteration has value n, the largest n+1 elements of the sorted version of lst are in L in the correct order.

Ans: True

PROBLEM 3-1 C  (1 point possible)
When we reach the marked spot in the code, and the variable iteration has value n, the first n+1 elements of the original list, lst, appear in the correctly sorted places in L. The "correctly sorted places" refers to the order of the elements in the list, not the index. In other words, the first n+1 elements of the original list lst will be in numeric order relative to each other in list L.

Ans: True

PROBLEM 3-1 D  (1 point possible)
The function sorts the list lst in place without using a new list.

Ans: True

PROBLEM 3-1 E  (1 point possible)
The complexity of this algorithm is:

Ans: O(n^2)

PROBLEM 3-2
-----------
Answer the following 5 questions based on this code.
    def sort2(lst):
        for iteration in range(len(lst)):
            minIndex = iteration
            minValue = lst[iteration]
            for j in range(iteration+1, len(lst)):
                if lst[j] < minValue:
                    minIndex = j
                    minValue = lst[j]
            temp = lst[iteration]
            lst[iteration] = minValue
            lst[minIndex] = temp

            L = lst[:]  # the next 3 questions assume this line just executed
        return lst

PROBLEM 3-2 A  (1 point possible)
When we reach the marked spot in the code, and the variable iteration has value n, the smallest n+1 elements of the sorted version of lst are in L in the correct order.

Ans: True

PROBLEM 3-2 B  (1 point possible)
When we reach the marked spot in the code, and the variable iteration has value n, the largest n+1 elements of the sorted version of lst are in L in the correct order.

Ans: False

PROBLEM 3-2 C  (1 point possible)
When we reach the marked spot in the code, and the variable iteration has value n, the first n+1 elements of the original list, lst, appear in the correctly sorted places in L. The "correctly sorted places" refers to the order of the elements in the list, not the index. In other words, the first n+1 elements of the original list lst will be in numeric order relative to each other in list L.

Ans: False

PROBLEM 3-2 D  (1 point possible)
The function sorts the list lst in place without using a new list.

Ans: True

PROBLEM 3-2 E  (1 point possible)
The complexity of this algorithm is:

Ans: O(n^2)

PROBLEM 3-3
-----------
Answer the following 5 questions based on this code.
    def sort3(lst):
        out = []
        for iteration in range(0,len(lst)):
            new = lst[iteration]
            inserted = False
            for j in range(len(out)):
                if new < out[j]:
                    out.insert(j, new)
                    inserted = True
                    break
            if not inserted:
                out.append(new)

            L = out[:]  # the next 3 questions assume this line just executed
        return out

PROBLEM 3-3 A  (1 point possible)
When we reach the marked spot in the code, and the variable iteration has value n, the smallest n+1 elements of the sorted version of lst are in L in the correct order.

Ans: False

PROBLEM 3-3 B  (1 point possible)
When we reach the marked spot in the code, and the variable iteration has value n, the largest n+1 elements of the sorted version of lst are in L in the correct order.

Ans: False

PROBLEM 3-3 C  (1 point possible)
When we reach the marked spot in the code, and the variable iteration has value n, the first n+1 elements of the original list, lst, appear in the correctly sorted places in L. The "correctly sorted places" refers to the order of the elements in the list, not the index. In other words, the first n+1 elements of the original list lst will be in numeric order relative to each other in list L.

Ans: True (recheck)

PROBLEM 3-3 D  (1 point possible)
The function sorts the list lst in place without creating a new list.

Ans: False

PROBLEM 3-3 E  (1 point possible)
The complexity of this algorithm is:

Ans: O(n^2)

PROBLEM 3-4
-----------
Answer the following 5 questions based on this code.
    def sort4(lst):
        def unite(l1, l2):
            if len(l1) == 0:
                return l2
            elif len(l2) == 0:
                return l1
            elif l1[0] < l2[0]:
                return [l1[0]] + unite(l1[1:], l2)
            else:
                return [l2[0]] + unite(l1, l2[1:])

        if len(lst) == 0 or len(lst) == 1:
            return lst
        else:
            front = sort4(lst[:len(lst)/2])
            back = sort4(lst[len(lst)/2:])

            L = lst[:]  # the next 3 questions assume this line just executed
            return unite(front, back)

PROBLEM 3-4 A  (1 point possible)
When we reach the marked spot in the code on the nth recursive call of sort4, the smallest n+1 elements of the sorted version of lst are in L in the correct order.

Ans: Fasle

PROBLEM 3-4 B  (1 point possible)
When we reach the marked spot in the code on the nth recursive call of sort4, the largest n+1 elements of the sorted version of lst are in L in the correct order.

Ans: False

PROBLEM 3-4 C  (1 point possible)
When we reach the marked spot in the code on the nth recursive call of sort4, the first n+1 elements of the original list, lst, appear in the correctly sorted places in L. The "correctly sorted places" refers to the order of the elements in the list, not the index. In other words, the first n+1 elements of the original list lst will be in numeric order relative to each other in list L.

Ans: False

PROBLEM 3-4 D  (1 point possible)
The function sorts the list lst in place without creating a new list.

Ans: False

PROBLEM 3-4 E  (1 point possible)
The complexity of this algorithm is:

Ans: O(nlog(n))

PROBLEM 4
---------
PROBLEM 4 - PART 1  (10 points possible)
Write a function called getSublists, which takes as parameters a list of integers named L and an integer named n.

assume L is not empty
assume 0 < n <= len(L)
This function returns a list of all possible sublists in L of length n without skipping elements in L. The sublists in the returned list should be ordered in the way they appear in L, with those sublists starting from a smaller index being at the front of the list.

Example 1, if L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2] and n = 4 then your function should return the list [[10, 4, 6, 8], [4, 6, 8, 3], [6, 8, 3, 4], [8, 3, 4, 5], [3, 4, 5, 7], [4, 5, 7, 7], [5, 7, 7, 2]]

Example 2, if L = [1, 1, 1, 1, 4] and n = 2 then your function should return the list [[1, 1], [1, 1], [1, 1], [1, 4]]


Your function does not have to be recursive. Do not leave any debugging print statements when you paste your code in the box.

```
def getSublists(L, n):

see p4-1.py
```


PROBLEM 4 - PART 2  (10 points possible)
----------------------------------------
Write a function called longestRun, which takes as a parameter a list of integers named L (assume L is not empty). This function returns the length of the longest run of monotonically increasing numbers occurring in L. A run of monotonically increasing numbers means that a number at position k+1 in the sequence is either greater than or equal to the number at position k in the sequence.

For example, if L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2] then your function should return the value 5 because the longest run of monotonically increasing integers in L is [3, 4, 5, 7, 7].


You may find it useful to use the function getSublists as defined above but you do not have to use this function. If you do use getSublists, the graders will use our implementation for getSublists. In the box for this problem, only paste the definition for the function longestRun.

Hint if you are Using getSublists

Your function does not have to be recursive. Do not leave any debugging print statements when you paste your code in the box.

```
def longestRun(L):

See p4-2.py
```

PROBLEM 5  (10 points possible)
-------------------------------
In this problem, you will implement a class according to the specifications in the template file usresident.py. The file contains a Person class similar to what you have seen in lecture and a USResident class (a subclass of Person). Person is already implemented for you and you will have to implement two methods of USResident.

For example, the following code:
    a = USResident('Tim Beaver', 'citizen')
    print a.getStatus()
    b = USResident('Tim Horton', 'non-resident')
will print out:
    citizen
    ## will show that a ValueError was raised at a particular line

usresident.py

Paste only your implementation of the USResident class in the box below. Do not leave any debugging print statements.

For this question, you will not be able to see the test cases we run. This problem will test your ability to come up with your own test cases.

PROBLEM 6
---------
PROBLEM 6-1  (10 points possible)
There are 2 coding problems on this page. Consider the following class definition:
    class Frob(object):
        def __init__(self, name):
            self.name = name
            self.before = None
            self.after = None
        def setBefore(self, before):
            # example: a.setBefore(b) sets b before a
            self.before = before
        def setAfter(self, after):
            # example: a.setAfter(b) sets b after a
            self.after = after
        def getBefore(self):
            return self.before
        def getAfter(self):
            return self.after
        def myName(self):
            return self.name

A Frob is an object that has a name, and two connections or links: a "before" and an "after" link that are intended to point to other instances of objects.

We can use Frobs to form a data structure called a doubly linked list. In a doubly linked list, each element has the property that if element A has a "before" link to element B, then element B has an "after" link to element A. We want to create a doubly linked collection of Frob instances with the property that all Frobs with names that are alphabetically before a specific Frob's name appear ordered along the "before" link, and all Frobs with names that are alphabetically after a specific Frob's name appear ordered along the "after" link.

In other words, overall the chain will be sorted alphabetically. Here is an example:
    eric = Frob('eric')
    andrew = Frob('andrew')
    ruth = Frob('ruth')
    fred = Frob('fred')
    martha = Frob('martha')

    insert(eric, andrew)
    insert(eric, ruth)
    insert(eric, fred)
    insert(ruth, martha)

And here is a diagram of the resulting data structure: (https://courses.edx.org/asset-v1:MITx+6.00.1x_7+3T2015+type@asset+block/files_final_exam_Slide1.jpg)

Note that if a Frob is inserted with the same name as a pre-existing Frob, both names should be inserted in the final data structure (the exact ordering of the two identical Frobs does not matter). So in the above example, if we were to next execute the line insert(eric, Frob('martha')), we would expect the doubly linked list to have the elements in the following order: andrew - eric - fred - martha - martha - ruth.

Provide a definition for an insert function that will create an ordered doubly linked list. This function is defined outside of the class Frob, and takes two arguments: a Frob that is currently part of a doubly linked list, and a new Frob. The new Frob will not initially have any "before" or "after" links to other Frobs. The function should mutate the list to place the new Frob in the correct location, with the resulting doubly linked list having appropriate "before" and "after" links. Complete the following function definition:
    def insert(atMe, newFrob):
        """
        atMe: a Frob that is part of a doubly linked list
        newFrob:  a Frob with no links 
        This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
        """

Please try the problem first without looking at the hints.
* What two cases should you think about?
    Whether the newFrob should be before or after atMe.
* I's still stuck
    There are several scenarios to consider. 
    (1) You are inserting the newFrob at an end. 
    (2) You are inserting the newFrob immediately next to atMe. 
    (3) You are not inserting the newFrob immediately next to atMe.

```
def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """
    # Your Code Here
```

PROBLEM 6-2  (10 points possible)
Now assume that you have a working insert procedure. Starting with any Frob in a doubly linked list, we would like to find the "front" Frob, i.e., the one whose name is closest to the beginning of the alphabet. Write a recursive function called findFront to do this. findFront should take as an argument any Frob that is part of a doubly linked list.

```
def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list 
    """
    # Your Code Here
```

Note: In programming there are many ways to solve a problem. For your code to check correctly here, though, you must write your recursive function such that you make a recursive call directly to the function findFront. Thank you for understanding.
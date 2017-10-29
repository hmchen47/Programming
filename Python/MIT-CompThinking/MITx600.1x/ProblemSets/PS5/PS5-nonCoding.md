Problem Set 5
=============

This Problem Set 5 will be non-coding. Please refrain from posting your answer in the forums until after the deadline. Any answers posted will be immediately taken down.

If you think there is a mistake, preface your forum post subject with [PSET 5]. Write a description in your post but do not reveal the answer. Please be very sure there is a mistake before posting. Thank you!

Problem 1 - True or False
-------------------------

1. The ONLY thing we are interested in when designing programs is that it returns the correct answer.

Ans: False

2. Roughly speaking, under the RAM model of computation, adding two numbers takes the same amount of time as dividing them.

Ans: True

3. When determining asymptotic complexity, we discard all terms except for the one with the largest growth rate.

Ans: true

4. Bisection search is an example of linear time complexity

Ans: False

5. For large values of n, an algorithm that takes 20000n^2 steps has better time complexity (takes less time) than one that takes 0.001n^5 steps

Ans: True

problem 2 - True or False
-------------------------

1. Indirection, as talked about in lecture, means you have to traverse the list more than once.

Ans: False

2. The complexity of binary search on a sorted list of n items is O(logn).

Ans: True

3. The worst case time complexity for selection sort is O(n2).

Ans: True

4. The base case for the recursive version of merge sort from lecture is checking ONLY for the list being empty.

Ans: False

5. An ideal hash function maps all the input keys to the same output.

Ans: False

Problem 3
----------

1. For each of the following expressions, select the order of growth class that best describes it from the following list: O(1),O(log(n)),O(n),O(nlog(n)),O(nc) or O(cn). Assume c is some constant.

Clicking Check will grade ALL the sub-problems. You have 2 attempts for this problem.

1. 0.0000001n+1000000                       # O(n)
2. 0.0001n^2+20000n−90000                   # O(n^c)
3. 20n+900log(n)+100000                     # O(n)
4. (log(n))^2+5n^7                          # O(n^c)
5. n^200−2n^30                              # O(n^c)
6. 30n^2+nlog(n)                            # O(n^c)
7. nlog(n)−3000n                            # O(nlog(n))
8. 3                                        # O(1)
9. 5^n+n^5+n+5                              # O(n^c)
10. nlog(n)+n^2+n+logn+1+2^n                # O(n^c)


Problem 4
---------

1. Consider the following Python procedure. Specify its order of growth.
    def modten(n):
        return n%10

Ans: O(1)

2. Consider the following Python procedure. Specify its order of growth.
    def multlist(m, n):
        '''
        m is the multiplication factor
        n is a list.
        '''
        result = []
        for i in range(len(n)):
            result.append(m*n[i])
        return result  

Ans: O(len(n))

3. Consider the following Python procedure. Specify its order of growth.
    def foo(n):
        if n <= 1:
            return 1
        return foo(n/2) + 1

Ans: O(log(n))

4. Consider the following Python procedure. Specify its order of growth.
    def recur(n):
        if n <= 0:
            return 1
        else:
            return n*recur(n-1)

Ans: O(n)

5. Consider the following Python procedure. Specify its order of growth.
    def baz(n):
        for i in range(n):
            for j in range(n):
                print i,j 

Ans: O(n^2)


Problem 5
---------
You have 2 attempts for this problem.

In lecture, we saw a version of linear search that used the fact that a set of elements is sorted in increasing order. Here is the code from lecture:
      
def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False
      
    
Consider the following code, which is an alternative version of search.
      
def newsearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False

Which of the following statements is correct? You may assume that each function is tested with a list L whose elements are sorted in increasing order; for simplicity, assume L is a list of positive integers.
A. search and newsearch return the same answers for all L and e.  
B. search and newsearch return the same answers provided L is non-empty.  
C. search and newsearch return the same answers provided L is non-empty and e is in L.  
D. search and newsearch never return the same answers.  
E. search and newsearch return the same answers for lists L of length 0, 1, or 2.

Ans: E


Problem 6
---------
Answer the questions below based on the following sorting function. If it helps, you may paste the code in your programming environment. Study the output to make sure you understand the way it sorts.
      
def swapSort(L): 
    """ L is a list on integers """
    print "Original L: ", L
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print L
    print "Final L: ", L

1. Does this function sort the list in increasing or decreasing order? (items at lower indices being smaller means it sorts in increasing order, and vice versa)
A. Increasing
B. Decreasing

Ans: A

2. What is the worst case time complexity of swapSort? Consider different kinds of lists when the length of the list is large.
A. O(n2)  
B. O(n)  
C. O(log(n))  
D. O(1)

Ans: A

3. If we make a small change to the line for j in range(i+1, len(L)): such that the code becomes:
      
def modSwapSort(L): 
    """ L is a list on integers """
    print "Original L: ", L
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print L
    print "Final L: ", L
  
What happens to the behavior of swapSort with this new code?
A. No change  
B. modSwapSort now orders the list in descending order for all lists.  
C. modSwapSort now orders the list in descending order for SOME lists but not all  
D. modSwapSort enters an infinite loop.

Ans: B


4. What happens to the time complexity of this modSwapSort?
A. Best and worst cases stay the same.
B. Worst case stays the same but best case changes.
C. Best and worst cases change.

Ans: A
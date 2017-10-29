6.00.1X - INTRODUCTION TO COMPUTER SCIENCE - QUIZ, SPRING 2016
==============================================================

You may use as a resource anything we posted online (including the textbook), any other textbooks you may possess, and any notes you have prepared yourself. We ask you not to use the Internet to search for solutions. You may not communicate with any person about this examination while working on it. Furthermore, you may not communicate about the exam until the exam has been closed for everyone.

For multiple choice problems you will be allowed exactly one submission; for coding questions you will be allowed 10 submissions, so that you may have a chance to fix any errors.

Part of what we are testing on this exam is your ability to write comprehensive test suites for your own functions, which is why we limit the number of submissions allowed per coding problem. For problems that ask you to write your own code, you may use Canopy or IDLE - or an online Python interpreter such as CodeSkulptor or Python Tutor- to test your solution before pasting it into the answer box. We ask that you do not run code provided in non-coding questions in Canopy.

A reminder to students pursuing credit for this course from Charter Oak:
* re-verification is required for credit
* the passing score for credit is 65% overall

Problem 1
---------
A reminder to students pursuing credit for this course from Charter Oak:

re-verification is required for credit
the passing score for credit is 65% overall
Re-verification is not required if you are just taking this course for the verified certificate.

Answer all questions before clicking Final Check. (True/False)

1. In the statement L = [1,2,3], L is a class.

Ans: False

2. The orders of growth of O(n2+1) and O(n5+1) are both polynomial.

Ans: True

3. The complexity of binary search on a sorted list of n items is O(log⁡n).

Ans: True

4. A bisection search algorithm always returns the correct answer when searching for an element in a sorted list.

Ans: True

5. Performing binary search on an unsorted list will always return the correct answer in O(n) time where n is the length of the list.

Ans: False

Problem 2
---------
#Problem 2-1
You have the following class hierarchy:

```python
class A(object):
    def foo(self):
        print 'hi'
class B(A):
    def foo(self):
        print 'bye'
```
Which of the following is correct?
A. When a = A() we say that a is an instance of A 
B. When b = B() we say that b is a subclass of A 
C. Both of the above 
D. Neither of the above

Ans: A

#Problem 2-2
Consider the function f below. What is its Big O complexity?

```python
def f(n):
    def g(m):
        m = 0
        for i in range(m):
            print m
    for i in range(n):
        g(n)
```
A. O(1) 
B. O(log(n)) 
C. O(n) 
D. O(n2)

Ans: C

#Problem 2-3
A dictionary is an immutable object because its keys are immutable.
A. True 
B. False because its keys can be mutable 
C. False because a dictionary is mutable

Ans: C

#Problem 2-4
Consider the following two functions and select the correct choice below:

```python
def foo_one(n):
    """ Assume n is an int >= 0 """
    answer = 1.0
    while n > 1:
        answer *= n
        n -= 1
    return answer

def foo_two(n):
    """ Assume n is an int >= 0 """
    if n <= 1: 
        return 1.0
    else: 
        return n*foo_two(n-1)
```
A. The worst case Big Oh time complexity of foo_one is worse than the worst case Big Oh time complexity of foo_two. 
B. The worst case Big Oh time complexity of foo_two is worse than the worst case Big Oh time complexity of foo_one. 
C. The worst case Big Oh time complexity of foo_one and foo_two are the same. 
D. Impossible to compare the worst case Big Oh time complexities of the two functions.

Ans: C

#Problem 2-5
The complexity of $1^n + n^4 + 4n + 4$ is
A. constant 
B. logarithmic 
C. linear 
D. polynomial 
E. exponential

Ans: D

Problem 3
---------
Write a function called dict_invert that takes in a dictionary with immutable values and returns the inverse of the dictionary. The inverse of a dictionary d is another dictionary whose keys are the unique dictionary values in d. The value for a key in the inverse dictionary is a sorted list of all keys in d that have the same value in d.

Here are some examples:
* If `d = {1:10, 2:20, 3:30}` then `dict_invert(d)` returns `{10: [1], 20: [2], 30: [3]}`
* If `d = {1:10, 2:20, 3:30, 4:30}` then `dict_invert(d)` returns `{10: [1], 20: [2], 30: [3, 4]}`
* If `d = {4:True, 2:True, 0:True}` then `dict_invert(d)` returns `{True: [0, 2, 4]}`

```python
def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    # Your code here
```
Paste your entire function, including the definition, in the box below. Do not leave any debugging print statements.


Problem 4
---------
#Problem 4 - Part 1

Write a function called `getSublists`, which takes as parameters a list of integers named `L` and an integer named `n`.
* assume L is not empty
* assume 0 < n <= len(L)

This function returns a list of all possible sublists in `L` of length `n` without skipping elements in `L`. The sublists in the returned list should be ordered in the way they appear in `L`, with those sublists starting from a smaller index being at the front of the list.

Example 1, if `L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]` and `n = 4` then your function should return the list `[[10, 4, 6, 8], [4, 6, 8, 3], [6, 8, 3, 4], [8, 3, 4, 5], [3, 4, 5, 7], [4, 5, 7, 7], [5, 7, 7, 2]]`

Example 2, if `L = [1, 1, 1, 1, 4]` and `n = 2` then your function should return the list `[[1, 1], [1, 1], [1, 1], [1, 4]]`

Your function does not have to be recursive. Do not leave any debugging print statements when you paste your code in the box.

```python
def getSublists(L, n):

```

#Problem 4 - Part 2
Write a function called `longestRun`, which takes as a parameter a list of integers named `L` (assume `L` is not empty). This function returns the length of the longest run of monotonically increasing numbers occurring in `L`. A run of monotonically increasing numbers means that a number at position `k+1` in the sequence is either greater than or equal to the number at position `k` in the sequence.

For example, if `L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]` then your function should return the value 5 because the longest run of monotonically increasing integers in L is `[3, 4, 5, 7, 7]`.

You may find it useful to use the function `getSublists` as defined above but you do not have to use this function. If you do use `getSublists`, the graders will use our implementation for `getSublists`. In the box for this problem, only paste the definition for the function `longestRun`.

Hint if you are Using `getSublists`

Your function does not have to be recursive. Do not leave any debugging print statements when you paste your code in the box.

```python
def longestRun(L):
```

Problem 5
---------
In this problem, you will implement a class according to the specifications in the template file usresident.py. The file contains a `Person` class similar to what you have seen in lecture and a `USResident` class (a subclass of `Person`). `Person` is already implemented for you and you will have to implement two methods of `USResident`.

For example, the following code:

```python
a = USResident('Tim Beaver', 'citizen')
print a.getStatus()
b = USResident('Tim Horton', 'non-resident')
```
will print out:

```python
citizen
## will show that a ValueError was raised at a particular line
```
usresident.py

Paste only your implementation of the `USResident` class in the box below. Do not leave any debugging print statements.

For this question, you will not be able to see the test cases we run. This problem will test your ability to come up with your own test cases.

```python
## DO NOT MODIFY THE IMPLEMENTATION OF THE Person CLASS ##
class Person(object):
    def __init__(self, name):
        #create a person with name name
        self.name = name
        try:
            firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank+1:]
        except:
            self.lastName = name
        self.age = None
    def getLastName(self):
        #return self's last name
        return self.lastName
    def setAge(self, age):
        #assumes age is an int greater than 0
        #sets self's age to age (in years)
        self.age = age
    def getAge(self):
        #assumes that self's age has been set
        #returns self's current age in years
        if self.age == None:
            raise ValueError
        return self.age
    def __lt__(self, other):
        #return True if self's name is lexicographically less
        #than other's name, and False otherwise
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    def __str__(self):
        #return self's name
        return self.name
        
class USResident(Person):
    """ 
    A Person who resides in the US.
    """
    def __init__(self, name, status):
        """ 
        Initializes a Person object. A USResident object inherits 
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """
        # Write your code here
        
    def getStatus(self):
        """
        Returns the status
        """
        # Write your code here
```

Problem 6
---------
#Problem 6-1

Consider the following hierarchy of classes:

```python
class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return 'It is obvious that ' + self.say(stuff)
```

As written, this code leads to an infinite loop when using the `Arrogant Professor` class.

Change the definition of `ArrogantProfessor` so that the following behavior is achieved:

```python
e = Person('eric') 
le = Lecturer('eric') 
pe = Professor('eric') 
ae = ArrogantProfessor('eric')

>>> e.say(‘the sky is blue’)
eric says: the sky is blue

>>> le.say(‘the sky is blue’)
eric says: the sky is blue

>>> le.lecture(‘the sky is blue’)
I believe that eric says: the sky is blue

>>> pe.say(‘the sky is blue’)
eric says: I believe that eric says: the sky is blue

>>> pe.lecture(‘the sky is blue’)
I believe that eric says: the sky is blue

>>> ae.say(‘the sky is blue’)
eric says: It is obvious that eric says: the sky is blue

>>> ae.lecture(‘the sky is blue’)
It is obvious that eric says: the sky is blue
```
Paste ONLY your `ArrogantProfessor` class in the box below. Do not leave any debugging print statements.

For this question, you will not be able to see the test cases we run. This problem will test your ability to come up with your own test cases.

#Problem 6-2

You change your mind, and now want the behavior as described in Part 1, except that you want:

```python
>>> ae.say(‘the sky is blue’)
eric says: It is obvious that I believe that eric says: the sky is blue

>>> ae.lecture(‘the sky is blue’)
It is obvious that I believe that eric says: the sky is blue
```
Change the definition of `ArrogantProfessor` so that the behavior described above is achieved.

Paste ONLY your `ArrogantProfessor` class in the box below. Do not leave any debugging print statements.

For this question, you will not be able to see the test cases we run. This problem will test your ability to come up with your own test cases.

#Problem 6-3
You change your mind once more. You want to keep the behavior from Part 2, but now you would also like:

```python
>>> pe.say(‘the sky is blue’)
Prof. eric says: I believe that eric says: the sky is blue 

>>> ae.say(‘the sky is blue’)
Prof. eric says: It is obvious that I believe that eric says: the sky is blue
```
Change the Professor class definition in order to achieve this.

Paste ONLY the one class that you changed in the box below. Do not leave any debugging print statements.


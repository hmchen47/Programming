6.00.1X - INTRODUCTION TO COMPUTER SCIENCE
==========================================

QUIZ, SPRING 2016

Out February 12, 2016 at 14:00 pm UTC (2:00 pm)

Due February 16, 2016 at 23:30 UTC (11:30 pm)

[What time is it in UTC right now?](http://time.is/UTC)

 ** there is no time limit, submit your answers before the deadline **

This exam is designed to take on average roughly 3 hours of time. You can start the exam when it is convenient for you, but you must complete this examination by the deadline. Please look up this time in [your local time zone](http://www.timeanddate.com/worldclock/).

When you open the next page, you will have started the exam. You do not need to start now. 

Note that during the exam period, the discussion forum will be shut down, to avoid any accidental discussion of exam material. It will reopen at the end of the exam period. 

If you have a bug or error to report during the exam, you may email 6.00.1x-exams@mit.edu. Include your edX ID name (found at the top right of any edX page). Only bug or error reports will be accepted; all other emails will be discarded. We try to respond to emails within 7 hours. Since the entire staff is on the Unites States east coast, we will take about that long to reply to emails sent overnight and apologize for this inconvenience.

If there is an error with the exam, we will fix it and then post a message on the [course updates page](https://goo.gl/L9sVJg). Check that page often! It is the fastest way we have to announce errors and fixes.

You may use as a resource anything we posted online (including the textbook), any other textbooks you may possess, and any notes you have prepared yourself. We ask you not to use the Internet to search for solutions. You may not communicate with any person about this examination while working on it. Furthermore, you may not communicate about the exam until the exam has been closed for everyone.

For multiple choice problems you will be allowed exactly one submission; for coding questions you will be allowed 10 submissions, so that you may have a chance to fix any errors.

Part of what we are testing on this exam is your ability to write comprehensive test suites for your own functions, which is why we limit the number of submissions allowed per coding problem. For problems that ask you to write your own code, you may use Canopy or IDLE - or an online Python interpreter such as [CodeSkulptor](http://www.codeskulptor.org/) or [Python Tutor](http://pythontutor.com/) - to test your solution before pasting it into the answer box. We ask that you do not run code provided in non-coding questions in Canopy.

If you want to go back and study some more before starting this exam you can do so.

Good Luck!

Common Issues
-------------
Below are some issues you may encounter while completing this exam, along with solutions recommended by the staff.

# SPINNING QUEUE ICON

[!Spinning Icon](https://goo.gl/aYDlJY)

It is possible that when you submit your code to the grader (by hitting Check), you will get the spinning processig icon. Usually, this should only last a few seconds and you will get a reply back from the grader within those few seconds.

If the spinning queued icon lasts longer than a few seconds:
*Go to another problem in the course that uses code submission. For example, [L2 Problem 8](https://goo.gl/TDka9h). Hit Check with any code there to check if the spinning Processing issue is with all problems or just one.
    - If spinning Processing doesn't happen in another problem, then check whether you have pasted the function definition twice (nested inside the same function definition). If so, only use one function definition and click Check again.
    - If spinning Processing doesn't happen in another problem, you might have a syntax error. The best way to check this is to paste the code you have from the box in your local IDE and run it -- any syntax error or indentation error will show up.
    - If spinning Processing doesn't happen in another problem, then check your code for any special characters. In the past, the offending character showed up in your pasted code as a one or more '\b' (no quotes) or a non-ASCII character (\u200b for example). If you remove the character, your code should give you a grader reply.
    - If spinning Processing doesn't happen in another problem and you have followed the previous three points, try clicking Check again.
* If spinning Processing happens in another problem as well, the graders are probably down. If there is no recent post in the Updates and News page about the grader being down, please email the staff. Someone will update that page and look into the issue.

# PROGRAM TIMED OUT (SLOW CODE OR INFINITE LOOPS)

[!Time Out](https://goo.gl/AfCRGl)

If you see this error, you have an infinite loop in your program (or more rarely, slow code). The grader uses test cases not shown in the problem, so check your code with more test cases. Most likely, there is a path through your code that leads to an infinite loop. Good test cases use unique inputs -- try very small or very large values, or uncommon combinations of inputs.

#SUBMISSION CANNOT BE GRADED

[!Not Graded](http://goo.gl/eX6TIR)

After pasting code from your own working environment and hitting Check, you may see this message (or a similar one inside a yellow box). Those students who use non-ascii characters are most likely to see this. After pasting, some special characters (like accented letters) were introduced. To the grader, they are a sequence of characters (\u200b for example). Go through the code in the textbox and check that all your characters are ASCII ( a-z and 0-9 but none with accents). These special characters may appear in bright red font so should be easy to spot.


Problem 1
---------
Problem 1
(10 points possible)
Answer all questions before clicking Final Check.

1.Suppose `x = "pi"` and `y = "pie"`. The line of code `x, y = y, x` will swap the values of `x` and `y`, resulting in `x = "pie"` and `y = "pi"`.

Ans: False  --> x, y = y, x --> (x, y) = (y, x), Python swaps pointer

2. Suppose `x` is an integer in the following code:

```python
def f(x):
    while x > 3:
        f(x+1)
```
For any value of `x`, all calls to `f` are guaranteed to never terminate.

Ans: False

3. A Python program always executes every line of code written at least once.

Ans: False

4. Suppose you have two different functions that each assign a variable called `x`. Modifying `x` in one function means you always modify `x` in the other function for any `x`.

Ans: False

5. The following code will enter an infinite loop for all values of i and j.

```python
while i >= 0:
    while j >= 0:
        print i, j
```

Ans: False

6. It is always possible and feasible for a programmer to come up with test cases that run through every possible path in a program.

Ans: False  -->  iteration and recursive will covers none, one, and more runs

7. Assume `f()` is defined. In the statement `a = f()`, a is always a function.

Ans: False  -->  a binds with the returned object

8. A program that keeps running and does not stop is an example of a syntax error.

Ans: False

9. Consider the following function.

```python
def f(x):
    a = []
    while x > 0:
        a.append(x)
        print a
        f(x-1)
```
A new object of type list is created for each recursive invocation of f.

Ans: True

10. A tuple can contain a list as an element.

Ans: True

Problem 2
---------
# Problem 2-1
(1 point possible)
Consider the statement: L = {'1':1, '2':2, '3':3}. Which is correct?
A. L is a list 
B. L is immutable 
C. L contains 6 elements 
D. L has integer keys 
E. L maps strings to integers

Ans: E

# Problem 2-2
(1 point possible)
Assume a break statement is executed inside a loop and that the loop is inside a function. Which of the following is correct?
A. The program might immediately terminate. 
B. The function might immediately terminate. 
C. The loop will always immediately terminate. 
D. All of the above. 
E. None of the above.

Ans: D  (A & B use 'might')

# Problem 2-3
(1 point possible)
In Python, which of the following is a mutable object?
A. a string 
B. a tuple 
C. a list  
D.all of the above 
E. none of the above

Ans: C

# Problem 2-4
(1 point possible)
Assume the statement s[1024] = 3 does not produce an error message. This implies:
A. type(s) can be str 
B. type(s) can be tuple 
C. type(s) can be list 
D. All of the above

Ans: D --> ?

# Problem 2-5
(1 point possible)
Consider the code:

```python
L = [1,2,3]
d = {'a': 'b'}
def f(x):
    return 3
```
Which of the following does NOT cause an exception to be thrown?
A. print L[3] 
B. print d['b'] 
C.  
for i in range(1000001, -1, -2):
    print f
D. print int('abc') 
E. None of the above

Ans: C

Problem 3
---------
# Problem 3-1
(2 points possible)
Examine the following code snippet:

```python
stuff  = _____
stuff = "iQ"
for thing in stuff:
    if thing == 'iQ':
       print "Found it"
```
Select all the values of the variable "stuff" that will make the code print "Found it".
A. ["iBoy", "iGirl", "iQ", "iC","iPaid","iPad"] 
B. ("iBoy", "iGirl", "iQ", "iC","iPaid","iPad") 
C. [ ( "iBoy", "iGirl", "iQ", "iC","iPaid","iPad") ] 
D. ( [ "iBoy", "iGirl", "iQ", "iC","iPaid","iPad" ], ) 
E. ["iQ"] 
F. "iQ"

Ans: A, B, E

# Problem 3-2
(3 points possible)
The following Python code is supposed to compute the square of an integer by using successive additions.

```python
def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x
```
Not considering recursion depth limitations, what is the wrong with this implementation of procedure `Square`? Check all that apply.
A.  It is going to return a wrong value. 
B. The term Square is a reserved Python keyword. 
C. Function names cannot start with a capital letter. 
D. The function is never going to return anything. 
E. Python has arbitrary precision arithmetic. 
F. This function will not work for negative numbers. 
G. The call SquareHelper(abs(x), abs(x)) won't work because you can't have abs(x) as both parameters. 
H. Nothing is wrong; the code is fine as-is.

Ans: H --> Python is not an arbitrary precision arithmetic

Problem 4
---------
(10 points possible)
Write a Python function that returns `True` if `aString` is a palindrome (reads the same forwards or reversed) and `False` otherwise. Do not use Python's built-in `reverse` function or `aString[::-1]` to reverse strings.

This function takes in a string and returns a boolean.

```python
def isPalindrome(aString):
    '''
    aString: a string
    '''
    # Your code here
```

Problem 5
---------
(10 points possible)
Write a Python function that returns the sum of the pairwise products of listA and listB. You should assume that `listA` and `listB` have the same length and are two lists of integer numbers. For example, if `listA = [1, 2, 3]` and `listB = [4, 5, 6]`, the dot product is $1*4 + 2*5 + 3*6$, meaning your function should return: $32$

Hint: You will need to traverse both lists in parallel.

This function takes in two lists of numbers and returns a number.

```python
def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here
```

Problem 6
-----------
(15 points possible)
Write a function to flatten a list. The list contains other lists, strings, or ints. For example, `[[1,'a',['cat'],2],[[[3]],'dog'],4,5]` is flattened into `[1,'a','cat',2,3,'dog',4,5]`

```python
def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
```
# Click to expand Hint: How to think about this problem
Recursion is extremely useful for this question. You will have to try to flatten every element of the original list. To check whether an element can be flattened, the element must be another object of type list.

Paste your entire function, including the definition, in the box below. Do not leave any debugging print statements.

Problem 7
---------
(20 points possible)
Assume you are given two dictionaries `d1` and `d2`, each with integer keys and integer values. You are also given a function `f`, that takes in two integers, performs an unknown operation on them, and returns a value.

Write a function called `dict_interdiff` that takes in two dictionaries (`d1` and `d2`). The function will return a tuple of two dictionaries: a dictionary of the intersect of `d1` and `d2` and a dictionary of the difference of `d1` and `d2`, calculated as follows:
* __intersect__: The keys to the intersect dictionary are keys that are common in both `d1` and `d2`. To get the values of the intersect dictionary, look at the common keys in `d1` and `d2` and apply the function f to these keys' values -- the value of the common key in `d1` is the first parameter to the function and the value of the common key in `d2` is the second parameter to the function. Do not implement `f` inside your `dict_interdiff` code -- assume it is defined outside.
* __difference__: a key-value pair in the difference dictionary is (a) every key-value pair in `d1` whose key appears only in d1 and not in `d2` or (b) every key-value pair in `d2` whose key appears only in `d2` and not in `d1`.
Here are two examples:

* 
If f(a, b) returns a + b
d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
then dict_interdiff(d1, d2) returns ({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90})
*
If f(a, b) returns a > b
d1 = {1:30, 2:20, 3:30}
d2 = {1:40, 2:50, 3:60}
then dict_interdiff(d1, d2) returns ({1: False, 2: False, 3: False}, {})

```python
def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # Your code here
```
Paste your entire function, including the definition, in the box below. The function f will be automatically added to your code, do not paste it in the box. Do not leave any debugging print statements.


Problem 8
---------
(20 points possible)
Write a Python function called `satisfiesF` that has the specification below. Then make the function call `run_satisfiesF(L, satisfiesF)`. Your code should look like:

```python
def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    # Your function implementation here

run_satisfiesF(L, satisfiesF)
```
For your own testing of `satisfiesF`, for example, see the following test function f and test code:

```python
def f(s):
    return 'a' in s
      
L = ['a', 'b', 'a']
print satisfiesF(L)
print L
```
Should print:

```python
2
['a', 'a']
```
Paste your entire function `satisfiesF`, including the definition, in the box below. __After you define your function, make a function call to `run_satisfiesF(L, satisfiesF)`. Do not define `f` or `run_satisfiesF`.__ Do not leave any debugging print statements.

__For this question, you will not be able to see the test cases we run. This problem will test your ability to come up with your own test cases.__




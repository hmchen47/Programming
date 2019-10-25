# Welcome

## 0.1 Course Information

I am so happy that you're going to join me for my course, Programming for Lovers.  The course starts on October 14, with lectures on Monday and Thursday evenings ET (they will be recorded if you want to join us at your own pace).  It runs for nine weeks and I am donating up to $2,500 to charity; see Charitable Contribution Disclosure for more details.  I will provide information about how the course will operate when the course begins.

I have found in my own students that exposure to programming is at an all-time high.  But many of the online materials teaching programming are not as rigorous as a course at an institution like Carnegie Mellon University, where I work.  Sometimes, offline programming courses are rigorous, but they get mired in technical details (such as the implementation details of a language) and miss the critical fact that programming is supposed to be fun.

In order to be fun, this course will teach programming by constantly pointing to practical topics. Here is a sampling of what we will start with; some of these topics show how computation has revolutionized biology, and some are taken from other practical disciplines.  There will be bonus topics too!  But I want to keep them a surprise.

1. Prologue: The Ancient Greeks and the Origins of Computational Thinking
2. Hunting for Replication Origins in Bacterial Genomes
3. Monte Carlo Simulation and Hacking the 2016 US Presidential Election
4. Top-Down Programming and Building a Self-Replicating Automaton
5. Object-Oriented Programming 1: Building a Physics Engine Simulating Gravity
6. Object-Oriented Programming 2: Constructing the Tree of Life

The language that we will use is [Go](http://golang.org/) (hence the Gophers in love, which is a modification of Renee French's work).  Go is a very nice language with some powerful features; we will  get to see how it makes parallel programming a breeze, for example. But much of what we will learn in this course is not confined to a specific language.

Please take the time to introduce yourself at the following discussion forum: Welcome!


## 0.2 The P4❤️ Manifesto

Every crazed radical must have a manifesto, and I cannot consider myself above this law.  So here goes.

The past several years have brought a boom in online education, a movement that I am very proud to have been a part of.   I co-founded [Rosalind](http://rosalind.info/), an online resource for learning bioinformatics through problem solving, as well as the [Bioinformatics Specialization](https://www.coursera.org/specializations/bioinformatics) on Coursera, the first open online course in computational biology. I want to build a new open online education project that is based on the work that I have done over the past several years in teaching programming to students at Carnegie Mellon University.

There are now many excellent resources for getting more and more learners connected to coding at the beginner level, but I have yet to see an online course on the fundamentals of programming that approaches the rigor of an immersive university course in programming, while also remaining fun.  Part of the issue seems to be that course providers know that by having experiences that are as easy as possible, they will maximize retention and therefore revenue.

My fear is that we are connecting more and more learners to the beautiful discipline of computer science, without ensuring that they have the proper foundational knowledge.  In my own course, I see more and more students who have coded before, and yet they often lack basic programming skills that I would expect a student to master in the first few weeks of my course.

I therefore want this course to build a bridge between existing materials and a more thorough understanding of computer science, while still being accessible to beginners.  My course will have several attributes that I describe below, and that I think that any programming course should strive for.

1. __A programming course should be fun.__ Students of all ages and backgrounds learn the most when they enjoy the experience, and so above all else, I want Programming for Lovers to be fun.

2. __A programming course should be clearly applicable.__ There are many programming courses that are taught for programming’s sake, with examples that are either trite or have no connection to what most learners would want to use their skills to do.  The way that we will have fun in Programming for Lovers is by considering real applications; at any moment of the course, students will be able to put their finger on a real-world application connected to what they are doing.  Here is the structure of what we will do in the course.
  + Prologue: The Ancient Greeks and the Origins of Computational Thinking
  + Hunting for Replication Origins in Bacterial Genomes
  + Monte Carlo Simulation and Predicting the 2016 US Presidential Election
  + Top-Down Programming and Modeling a Self-Replicating Automation
  + Object-Oriented Programming 1: Building a Physics Engine Simulating Gravity
  + Object-Oriented Programming 2: Constructing the Tree of Life
  + So, how does a computer really work?  And can it do everything?
  + Bonus Topics! (Join us to find out)

3. __A programming course should be rigorous.__ My students are very smart, and many have programmed before.  Yet it is rare that I encounter a student at the beginning of an introductory programming course who can already write a well-organized program for even a relatively simple task.   When a programming course is taught rigorously, with a thorough treatment of topics that respect the intelligence of its learners, it makes much stronger, more empowered programmers.  A controversial example of the need for rigor in programming education is pointers.  Pointers should be taught to beginning programmers because pointers help learners understand how the computer manages memory and how the programming language controls the computer, as well as giving them a memory-efficient way of working with objects. I have encountered instructors who are appalled that I would teach pointers to beginners, yet in my experience, my students obtain a complete initial understanding of this topic in less than half an hour.  The reason why this is the case is because the course up to that point has been just as rigorous, and when students have the appropriate foundation, more advanced topics are just an extension of what they have already learned.

4. __A programming course should be unashamedly mathematical.__  Studies have shown that mathematics correlates very well with success in programming, and my experience with teaching the subject reflects this fact despite my best efforts to make my material as accessible as possible. Mathematics is not a surprising pre-requisite for programming, since much of the foundational work in computer science arises directly out of mathematics. For example, courses that bypass the tricky mathematical details of how to build a pseudorandom number generator and only present students with a package to generate “random” numbers are short-changing their students.

5. __A programming course should connect coding to what happens within the computer.__ A computer is an electrical machine whose transfer of information is predicated on sequences of electrical signals that can be represented by strings of ones and zeroes. Very few introductory courses get into the details of how the code that we write can be converted to this level by the machine.  Fewer still take the opportunity to convey that there are some problems that are provably very difficult, and others that are provably undecidable.  Turing machines, undecidability, and P vs. NP are important topics for beginners in programming to understand.  Without this grounding, students run the risk of incorrectly thinking that a computer is a magic box that will, at least eventually, solve all our problems.

6. __A programming course should start with computational thinking.__ The easiest way to remain independent of a language is to start with computational thinking, and teaching the basics of control flow by using pseudocode.  Pseudocode provides a language-neutral way to solve problems, and it gives students a stress-free way of learning the basics of programming without stressing out about syntax, which is handled as a separate objective.

7. __A programming course should be independent of any language.__  We will begin Programming for Lovers with two algorithms discovered by ancient Greek mathematicians, over two millennia before the world’s first computer.  Programming is not coding, but rather the process of devising intelligent algorithms to solve clearly defined problems. Many programming courses will focus on a single language, with no perspective given to the fact that programming languages have vast similarities.  This course will start by using a programming language called [Go](http://golang.org/) because it has a number of features that make it easy to teach to beginners, but this is not a course in how to program in Go.  It is a course about how to program, and Go just happens to be the language that we use.  The course, over time, will become even more language-independent and feature multiple languages.  I would go so far to say that any course named something like “Python for Beginners” or “Programming in Java” is most likely serving its students poorly.  It is not an accident that you will not find courses with titles such as these in Carnegie Mellon’s [School of Computer Science](http://cs.cmu.edu/).

8. __A programming course should convey the strengths and weaknesses of a language.__ No language is perfect, and students should gain exposure as early as possible to identifying strengths and weaknesses of a language. In Go’s case, its handling of concurrency makes it possible to teach this concept in a beginner class, which would be next to impossible in another language. At the same time, how Go handles arrays through the use of slices is at times unwieldy.

9. __A programming course should make students do as much as possible.__ Courses and books that don’t incorporate active learning are doing their learners a disservice. This work facilitates active learning by having constant “just in time” exercises throughout to help tie the material together.



## 0.3 FAQs

+ __Why this Course?__

  This course arose from a course I have taught for the past four years at Carnegie Mellon called "Programming for Scientists".  Its biggest audience is graduate students who have a background in biology and are hoping to bolster their computational skills and make a transition to become computational biologists.  I have spent years making the course rigorous but still accessible and fun, and I want to share it with the larger community.

  You can find more information about my beliefs about how programming courses like this one should be taught at [The P4❤️ Manifesto](https://canvas.instructure.com/courses/1614886/pages/the-p4-manifesto).

+ __What does "for Lovers" mean?__

  "Programming for Scientists" has grown into something else that touches on a wide array of different disciplines. I want this course to be as inclusive as possible, and I welcome learners who aren't necessarily scientists.  "Programming for Lovers" is an an homage to the [Virginia travel slogan](https://en.wikipedia.org/wiki/Virginia_is_for_Lovers), with the idea that if you love learning of any kind, then I want you to feel that you're in the right place here.

+ __What do I need to know in advance?__

  I am very proud to have had quite a few students who have not programmed a single line of code before learning from me and have become "A" students. If you love solving problems, and aren't afraid of math, then I think you will love programming.  I plan to move quickly but am going to start at the very beginning.

+ __How will the course work?__

  I will live stream lectures on Mondays and Thursdays starting at 8 PM ET. For the first few weeks, the Monday lectures will be based on theory and the Thursday lectures will be live code-alongs.  I want to avoid jumping headlong into code because I really want to convey how important it is to think about programming more generally than a single language, and the Monday lectures will be completely free of any language-specific code for the first few weeks.

+ __What will be the assessments?__

  I would love to make high-powered automatically graded assignments in the future, and this is an effort for a version 2.0 of the course as this project continues to grow.  For the time being, I plan to have relatively open-ended assignments.

+ __Do I have to complete the assessments in order to enjoy the course?__

  Not at all.  In fact, from my experience in online education, the best projects allow for learners to experience the material at different levels.  If you want to just follow along the lectures, I am happy to have you.  If you want to complete all the homework assignments and build your own programming project and share it with all of us, I am happy to have you.

+ __Will I receive a certificate of completion?__

  I may produce something fun for you if you finish the course (open to ideas), but the course is not a for-credit course, it is a for-fun course.

+ __I can't make the lecture times.  Can I still attend the course?__

  Absolutely!  I will be posting the lecture videos to Canvas as soon as we complete them.

+ __Will there be a version of this course available later?__

  In short, yes.  I believe strongly in open access to education and plan to make the materials for this course completely open in the coming months.



## 0.4 Prologue: Ancient Greek Math and the Origins of Computational Thinking

### 0.4.1 Streaming Link for Lecture 0

<video src="url" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width=180>
  <track src="subtitle" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video><br/>


### 0.4.2 Lecture 0 Slides

[Slides download](https://canvas.instructure.com/courses/1614886/files/82928037/download?download_frd=1)


#### Our first computational problem

+ Algorithms are everywhere
  + __Algorithm__: a sequence of steps used to solve a problem
  + __Program__: converting an algorithm into code

+ First computational problem
  + __Computational problem__: _input_ data along with a specified _output_ involving the input data that cn be interpreted in _only one way_
  + GCD Problem
    + Input: integers `a` and `b`
    + output: the greatest common divisor of `a` and `b`, denoted `GCD(a, b)`
  + Variables: `a` and `b`, they can change depending on what values we want them to have
  + STOP: does this substitution change the computational problem?

+ Trivial algorithm for computing a GCD
  + a = 378 and b = 273
  + divisors of 378: 1, 2, 3, 6, 7, 9, 14, 18, 21, 27, 42, 54, 63, 126, 189, 378
  + divisors of 273: 1, 3, 7, 13, 21, 39, 91, 273
  + GCD(378, 273) = 1, 3, 7, 21
  + A trivial (obvious) algorithm solving the GCD problem
    1. Start our largest common divisors at 1
    2. for every integer $n$ between 1 and `min(a, b)`
      + is $n$ a divisor of `a`?
      + is $n$ a divisor of `b`?
      + if the answer to both of these questions is "yes", update out largest common divisor found to be equal to `n`
    3. after ranging through all these integers, the largest common divisor found must be `GCD(a, b)`
  + STOP: why might we want a faster approach?


#### A painless intro to pseudocode/control flow

+ programming languages are plentiful

+ pseudocode: a way of describing algorithms by emphasizing ideas that is "just right"
  + not too vague, like human language
  + not too precise, like a specific programming language

+ Illustrating pseudocode with a simple problem
  + Minimum of two number problem
    + input: numbers a and b
    + output: the minimum value of a and b
  + seminal idea in computer science: being able to __branch__ based on testing a condition

+ Algorithms just like functions
  + Input $\to$ Algorithm (computer science) $\to$ output
  + input $\to$ Function (Math) $\to$ output

+ `Min2` function
  + pseudocode

    ```go
    Min2(a, b)
      if a > b
        return b
      else
        return a
    ```

  + __if block__: if the "if statement" is true, entering the code block
  + __else block__: if the "if statement" is false, skip the if block and entering the code block
  + `Min2`: name of the function
  + `a`, `b`: input "__argument__"/"__parameter__" variables
  + `if a > b`: if statement (allows us to branch)
  + `else`: indicating where to go when if statement is false
  + `return b`: return statement (provides output)
  + STOP: does Min2 still return the desired answer if `a` and `b` are equal?

+ General form of if statements

  ```go
  SomeFunction(parameters)
    execute instructions A

    if condition X is true
      execute instructions Y
    else
      execute instructions Z

    execute instructions B
  ```

  + __Control flow__: the sequence of steps that a computer takes when executing a program
  + __keywords__: words with reversed meanings in most languages, such as "if", "else", "return", "true", etc.
  + __STOP__: will A always be executed? Will B always be executed?

+ `Min3` function
  + Problem: Minimum of three numbers of problem
    + input: numbers `a`, `b`, and `c`
    + output: the minimum value of `a`, `b`, and `c`
  + Exercise: write a (pseudocode) function `Min3` that solves this problem
  + nested if statement

    ```go
    Min3(a, b, c)
      if a > b
        if b > c
          return c
        else
          return b
      else
        if a > c
          return c
        else
          return a
    ```

  + STOP: where have we seen the colored code?
  + __Subroutine__: a function used within another function

    ```go
    Min3(a, b, c)
      if a > b
        return Min2(b, c)
      else
        Min2(a, c)
    ```

  + Exercise: write pseudocode for a function `Min4(a, b, c, d)` that compute the minimum for four numbers
  + Multiple approaches for solving even a simple problem

    ```go
    Min4(a, b, c, d)
      if a > b
        return Min3(b, c, d)
      else
        return Min3(a, c, d)

    Min4(a, b, c, d)
      return Min2(Mini2(a, b), Min2(c, d))
    ```

    + STOP: which of these do you prefer?


#### Party trick: knowing day of the week of your birthday

+ The Doomsday algorithm
  + The doomsdays occur on Thursdays in 2019: 1/3, 2/28, 3/0, 4/4, 5, 9, 6/6, 7/11, 8/8, 9/5, 10/10, 11/7, 12/12
  + STOP: how can we use this information to quickly find the day of the week for any given date in 2019?

  ```go
  Doomsday(day, month)
    if month = 1
      if day = 3, 10, 17, 24, or 31
        return "Thursday"
      else
        if day = 4, 11, 18, or 25 # this is ugly!
          return "Friday"
      etc.
    else
      if month = 2
        if day = 7, 14, 21, or 28
          return "Thursday"
        else
          if day = 1, 8, 14, or 22 # this is ugly!
            return "Friday"
        etc.
      else
        etc.
  ```

  + the `else` statements are not needed ...

    ```go
    Doomsday(day, month)
      if month = 1
        if day = 3, 10, 17, 24, or 31
          return "Thursday"
        if day = 4, 11, 18, or 25
          return "Friday"
      if month = 2
        if day = 7, 14, 21, or 28
          return "Thursday"
        if day = 1, 18, 15, or 22
          return "Friday"
      if month = 3
        etc.
    ```

+ Introducing `else if`

  ```go
  Doomsday(day, month)
    if month = 1
      if day = 3, 1-, 17, 24, or 31
        return "Thursday"
      else if day = 4, 11, 18, or 25
        return "Friday"
      etc.
    else if month = 2
      if day = 7, 14, 21, or 28
        return "Thursday"
      else if day = 1, 8, 15, or 22
        return "Friday"
      etc.
    else if month = 3
      etc.
  ```

#### Loops and Trivial GCD algorithm

+ How to convert to Pseudocode?
  + GCD of 378 and 273
  + A trivial (obvious) algorithm solving the GCD problem
    1. start the largest common divisor at 1
    2. for every integer `n` between 1 and `min(a, b)`:
      + is `n` a divisor of `a`?
      + is `n` a divisor of `b`?
      + if the answer of both of these questions is "yes", update the largest common divisor found to be equal to `n`
    3. after ranging through all these integers, the largest common divisor found must be `GCD(a, b)`
  + Key point: how can we do something "for every integer" in a range?

+ A simple problem: factorial
  + Factorial problem
    + input: an integer `n`
    + output: $n! = n \times (n-1) \times (n-2) \times \cdots \times 2 \times 1$
  
  ```go
  Factorial(n)
    p <- 1
    i <- 1
    while i <= n
      p <- p * i
      i <- i + 1
    return p
  ```

  + `p <- 1`:
    + declaring an intermediate variable p equal to 1 (p will eventually hold the factorial product)
    + the variable on the left of `<-` receives the value of the right side
  + `i <- 1`: `i` will allow us to "range" over all integers up to `n`
  + `while i <= n`: example of a __while loop__. Just like an if statement - if `i <= n`, we enter __while block__
  + the difference: after the __while block__,, we test `i <= n` again and (if true) enter the while block _again_
  + STOP: what happens if we remove `i <- i + 1`
  + __Infinite loop__: a loop that never terminates

+ For loop simplify ranging

  ```go
  AnotherFactorial(n)
    p <- 1
    for every integer i from 1 to n
      p <- p * i

    return p
  ```

  + __For loop:__ a way of simplifying the process of "ranging" through a collection of values

+ Note: while loops are more general

  ```go
  PittsburghFebruary()
    While temperature is below freezing
      daydream about moving south
  ```

+ Returning to the Trivial GCD
  + Exercise: write pseudocode for a function `TrivialGCD(a, b)` representing this algorithm (assume any subroutines you like)

  ```go
  TrivialGCD(a, b)
    d <- 1
    m <- Min2(1, b) # subroutine!
    for every integer p from 1 to m
      if p is a divisor of both a and b
        d <- p
    return d
  ```

  + we should discuss how a computer determines if one number is a divisor of another ...

+ Integer division
  + the __integer division__ of x/y is defined by taking the integer part of the division of "throwing away" the remainder
  + e.g., $14/3 = ? \qquad 102/12 = ? \qquad 11/2 = ? \implies 14/3 = 4 \qquad 102/12 = 8 \qquad 11/2 = 5$
  + STOP: how does `p` being a divisor of `n` related to integer division and remainder?
  + Exercise: 
    + write pseudocode for functions IntegerDivision(n, p) and Remainder(n, p) corresponding to the integer division and remainder formed by ``n/p`
    + only allowable arithmetic operations: addition, subtraction, and multiplication.
  + Repeated subtraction

    ```go
    IntegerDivision(n, p)
      c <- 0
      n <- n - p
      while n >= 0
        c <- c + 1
        n <- n - p
      return c
    ```

  + Note: we can check the correctness of our function by testing it on various outputs

+ Remainder() uses IntegerDivision() as subroutine

  ```go
  Remainder(n, p)
    return n - p * IntegerDivision(n, p)
  ```

  + Example
    + Remainder(14, 3) = 14 - 3*IntegerDivision(14, 3) = 2
    + Remainder(102, 12) = 102 - 12*IntegerDivision(102, 12) = 6
    + Remainder(11, 2) = 11 - 2*IntegerDivision(11, 2) = 1

+ Remainder() and Doomsday

  ```go
  Doomsday(day, month)
    if month = 1
      if day = 3, 10, 17, 24, or 31
        return "Friday"
      else if day = 4, 11, 18, or 25
        return "Saturday"
      etc.
    else if month = 2
      if day = 7, 14, 21, or 28
        return "Monday"
      else if day = 1, 8, 15, or 22
        return "Tuesday"
    else if month = 3
      etc.
  ```

  + STOP: how would Remainder be helpful here?

+ TrivialGCD is now good to go

  ```go
  TrivialGCD(a, b)
    d <- 1
    m <- Min2(a, b) # subroutine!
    for every integer p from 1 to m
      if Remainder(a, p) = 0 and Remainder(b, p) = 0
        d <- p
    return d
  ```

  + Note: the word __and__ is a keyword too


#### Euclid's insight and the world's first nontrivial algorithm

+ Euclid's theorem
  + Euclid's theorem: if a > b, then

    \[GCD(a, b) = GCD(a-b, b)\]

  + Two pressing questions
    1. how can we demonstrate this for any possible pair of integers?
    2. why do we really care that this is true computationally?

  + Common problem solving technique in mathematics: sometimes, we can prove a more general statement.
  + more general statement: if $a > b$, then __all__ shared divisors of $a$ and $b$ is the same as __all__ shared divisors of $a - b$ and $b$
  + prove the general statement with two facts
    1. ($\to$) any shared divisors of $a$ and $b$ must also be a divisor of $a - b$
    2. ($\gets$) any shared divisor of $a - b$ and $b$ must also be a divisor of $a$
  + Proof of 1 ($\to$): say $d$ is a divisor of $a$ and $b$.  $\exists \, x, y \in \mathbb{Z}^{\neq}:$

    \[dx = a, \quad dy = b\]

    \[a - b = dx - dy = d(x - y)\]

    $\therefore \, d$ is a divisor of $a - b$ as well.
  + Proof of 2 ($\gets$): Say $e$ is a divisor of $a - b$ and $b$.  $\exists \, p , q \in \mathbb{Z}^{\neq}:$

    \[ep = a - b, \quad eq = b\]

    \[a = (a - b) + b = ep + eq = e(p + q)\]

    $\therefore \, e$ is a divisor of $a$ as well.

+ Euclid's theorem in action
  + Example

    \[\begin{align*}
      GCD(378, 273) &= GCD(105, 273) = GCD(105. 168) = GCD(105, 63) \\
        & = GCD(42, 63) = GCD(42, 21) = GCD(21, 21) = 21
    \end{align*}\]

  + Exercise: brainstorm how we could write a function in pseudocode to compute the GCD of two numbers by repeatedly applying Euclid's theorem

+ Pseudocode for Euclid's algorithm

  ```go
  EuclidGCD(a, b)
    while a != b
      if a > b
        a <- a - b
      else
        b <- b - a
    return a
  ```

  + STOP: if we change `return a`  to `return b`, how does it change the algorithm?
  + Illustrated results

    <table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=70%>
      <thead>
      <tr>
        <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">$a$</th>
        <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">$b$</th>
        <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">is $a \neq b$</th>
        <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">Updated value of $a$</th>
        <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">Updated value of $b$</th>
      </tr>
      </thead>
      <tbody>
      <tr style="text-align: center;">
        <td>378</td> <td>273</td> <td>Yes</td> <td>105</td> <td>273</td>
      </tr>
      <tr style="text-align: center;">
        <td>105</td> <td>273</td> <td>Yes</td> <td>105</td> <td>168</td>
      </tr>
      <tr style="text-align: center;">
        <td>105</td> <td>168</td> <td>Yes</td> <td>105</td> <td>63</td>
      </tr>
      <tr style="text-align: center;">
        <td>105</td> <td>63</td> <td>Yes</td> <td>42</td> <td>63</td>
      </tr>
      <tr style="text-align: center;">
        <td>42</td> <td>63</td> <td>Yes</td> <td>42</td> <td>21</td>
      </tr>
      <tr style="text-align: center;">
        <td>42</td> <td>21</td> <td>Yes</td> <td>42</td> <td>21</td>
      </tr>
      <tr style="text-align: center;">
        <td>21</td> <td>21</td> <td>No</td> <td></td> <td></td>
      </tr>
      </tbody>
    </table>


#### Arrays and a First Attempt at Prime Finding

+ Who first computed Earth's circumference?
  + Eratosthenes of Cyrene (276 - 195 BC)
  + first nontrivial algorithm for identifying prime numbers (soon)
  + Recall that a positive integer is __prime__ if its only divisors are 1 and itself (and __composite__ otherwise)

+ Testing if a number is prime
  + Prime number problem
    + Input: an integer `n`
    + Output: "Yes" if `n` is prime, and "No" otherwise
  + __Decision problem__: a computational problem that always returns a "Yes"/"No" answer
  + using the keywork __true__ and __false__ to represent "Yes" and "No"
  + __Boolean variable__: a variable taking __true__ or __false__
  + pseudocode: 

    ```go
    IsPrime(n)
      if n = 1
        return false
      for every integer p form 2 to n - 1
        if p is a divisor of n
          return false
      return true
    ```

    + running: p = 1 (false), 2 (true), 3 (true), 4 (false), 5 (true), 6 (false), 7 (true), 8 (false), 9 (false), 19 (false), 11 (true)
    + STOP: do you see any improvements to `IsPrime()`?

  + STOP: how does this change the algorithm?

    ```go
    IsPrime(n)
      if n = 1
        return false
      for every integer p form 1 to n - 1
        if p is a divisor of n
          return false
      return true
    ```

    Answer: always return false

+ Theorem: if $ab = n$, $a$ and $b$ must be at most $\sqrt{n}$

  ```go
  IsPrime(n)
    if n = 1
      return false
    for every integer p form 2 to sqrt(n)
      if p is a divisor of n
        return false
    return true
  ```

+ __Euclid's Theorem #2__: There are infinitely many primes.

+ A simpler fact
  + Simpler fact: every composite integer greater than 1 has at least one prime factor
  + consider any composite integer $n$; since it is composite, it has factors other than itself and 1
  + Take the smallest factor $p$ of $n$ other than 1. $p$ must be prime, since any factor that it would have other than 1 and itself would also be a factor of $n$ (but we assumed $p$ was the smallest such factor).

+ Proof of Euclid's Theorem #2
  + Euclid's theorem #2: there are infinitely many primes.
  + __Proof by contradiction:__ assume the opposite of what we want to prove, and show that it leads to a __contradiction__, a statement that we know is false.
  + STOP: what is the opposite of what we want to prove in the case?
  + Proof:
  
    Assume that there are finitely many primes.  This means that there must be some number $n$ of them, and we can label them $p_1, p_2, \dots, p_n$.
  
    Consider the number formed by multiplying all these primes together:

    \[p = (p_1)(p_2) \dots (p_n)\]
  
    + STOP: is $p$ prime or composite? why?
    + Answer: composite, because $p$ has many factors other than 1 and itself.
  
    Now take the number that is 1 larger than $p$:

      \[q = p + 1 = (p_1)(p_2) \dots (p_n) + 1\]

    + STOP: is $q$ prime or composite? why?
    + Answer: $q$ must be composite, because it is clearly larger than all known primes!

    Yet look what happens when we divide $q$ by each of the known primes.

      \[\begin{align*}
        q /p_1 &= (p_2)(p_3) \dots (p_n) + 1 / p_1\\
        q /p_2 &= (p_1)(p_3) \dots (p_n) + 1 / p_2
      \end{align*}\]

    <span style="color: red;">The remainder is always 1!</span>

    + Fact: every composite integer greater than 1 has at least one prime factor.
  
    $q$ is composite, so it has a prime factor. But none of the primes $p_1$ is a factor. <span style="color: red;">Contradiction!</span>
  
+ Returning to factorials
  + __Array__: an ordered table/list of variables
  + Factorial array problem
    + Input: an integer `n`
    + output: an array containing all the $n+1$ factorials $0! = 1, 1!, 2!, \dots, n!$
  + factorial array: a[0] = 1, a[1] = 1, a[2] = 2, a[3] = 6, a[4] = 24, a[5] = 120, a[6] = 720
  +__0-based indexing__: starting numbering at 0, not 1

  ```go
  FactorialArray(n)
    a <- array of length n+1
    a[0] <- 1
    for every integer k from 1 to n
      a[k] <- a[k-1] * k
    return a
  ```

+ Trivial prime finding
  + Prime number array problem
    + Input: an integer `n`
    + output: an array primes of length n+1 such that for every nonnegative integer $p \leq n$, `primes[p]` is true if $p$ is prime and false otherwise
  + Example: primes[0] = false, primes[1] = false, primes[2] = true, primes[3] = true, primes[4] = false, ...

  ```go
  TrivialPrimeFinder(n)
    primes <- array of n+1 false boolean variables
    for every integer p from 2 to n
      if IsPrime(p) = true
        primes[p] <- true
    return primes
  ```

#### The world's second nontrivial algorithm

+ The  Sieve of Eratosthenes
  + Prime number array problem
    + Input: an integer n
    + output: an array primes of length n+1 such that for every nonnegative integer $p \leq n$,, primes[p] is true if p is prime and false otherwise
  + Exercise: write a pseudocode function `SieveOfEratosthenes()` that solves this problem by implementing the Sieve of Eratosthenes. (use a subordinate if it's helpful.)
  
+ Implementing `SieveOfEratosthenes`

  ```go
  SieveOfEratosthenes(n)
    primes <- array of n + 1 true boolean
    primes[0] <- false
    primes[1] <- false
    for every integer p from 2 to sqrt(n)
      if primes[p] = true
        primes <- CrossOff(primes, p)
    return primes

  CrossOff(primes, p)
    for every multiple k of p from 2p to n
      primes[k] <- false
    return primes
  ```

  + Next time, let's implement the sieve of Eratosthenes in Go, and compare it to the trivial prime finder in terms of speed.  Can it really be that much faster?
  + But ... what practical use ae there for primes in the 21th Century?


#### Conclusion: public key cryptography

+ Encryption is vital to Internet Security
  + __Encryption:__ transforming a message so that it cannot be ready by an eavesdropper but can be __decrypted__ by the recipient

+ Most encryption scheme are symmetric
  + A __symmetric__ encryption scheme uses the same __key__ for encrypting/decrypting a message
  + example: HELLO $\xrightarrow{\text{encrypt +1 letter}}$ IFMMP $\xrightarrow{\text{encrypt 11 letter}}$ HELLO
  + Even if we have a complicated key, it must be private: the sender and receiver must agree on the key on the key in advance

+ Primes Save the Day
  + __Public key encryption__ (late 1970s): knowing the key doesn't make it automatically easy to decrypt
  + Examplle: public key $n = p \times q$ where $p, q$ are large primes (typically ~300 digits long)
  + __Key Point:__ the only way to decrypt is by knowing the primes $p$ and $q$. This makes the key __asymmetric__.

+ But an eavesdropper just has to factor n!
  + Integer Factorization Problem
    + Input: an integer n
    + Output: the factorization of n
  + Key Point: no one has ever found a "fast" solution to this problem for 600-digit integer ...


## 0.5 Homework 0: Working with Integers and Arrays

### 0.5.1 Exercise Part 1: Warming Up

#### Combinations, permutations, and a short guide to debugging

+ "write and implementation": write the function in pseudocode first and then implement the function in Go

+ Permutation: choosing objects and placing in buckets with order

  \[P(n, k) = \frac{n!}{(n-k)!}\]

+ Combination: choosing objects and placing buckets w/o order

  \[ C(n, k) = \frac{n!}{(n-k)! \cdot k!} \]

+ Exercise: `Combination` & `Permutation`
  + write and implement functions `Combination(n, k)` and `Permutation(n, k)` computing the combination and permutation statistics
  + pseudocode

    ```go
    Combination(n, k)
      return Factorial(n)/(Factorial(n-k) * Factorial(k))

    Permutation(n, k)
      return Factorial(n)/Factorial(n-k)

    Factorial(n)
      if n = 1
        return 1
      else
        return n*Factorial(n-1)
    ```

  + Answer: [Permutation](./src/00-permutation.go)<br/>
    Answer: [Combination](./src/00-combination.go)


+ Exercise: `ComputationBig` & `PermutationBig`
  + Modify your implementation of Combination and Permutation so that you are able to compute Permutation(1000, 2), Combination(1000, 2) and Combination(1000, 998) without any problem
  + pseudocode

    ```go
    PermutationBig(n, k)
      perm <- 1
      for idx <- (n-k+1) to n
        perm <- perm * idx
      return perm

    CombinationBig(n, k)
      comb <- Permutation(n, min(n-k, k))
      for idx <- 1 to min(n-k, k)
        comb <- comb / idx
      return comb
    ```

  + Answer: [Permutation for Big Number](./src/00-bpermutation.go)<br/>
    Answer: [Combination for Big Number](./src/00-bcombination.go)

#### Working with Arrays

+ Exercise: `FactorialArray`
  + implement a function `FactorialArray` that takes an integer $n$ and returns a slice of length $n+1$ whose $k$-th element is equal to $k!$ Your should not call a factorial function subroutine as s subroutine.
  + pseudocode

    ```go
    FactorialArray(n)
      factArray <- an integer array w/ length (n+1)
      factArray[0] <- 1
      for idx <- 1 to n
        factArray[idx] = factArray[idx-1] * idx

      return factArray
    ```

    + Answer: [FactorialArray](./src/e00-factorialArray.go)

+ Exercise" `FibonacciArray`
  + Write and implement a function `FibonacciArray` that takes an integer $n$ as input and returns an array if length $n$ whose $k$-th element is the $k$-th Fibonacci number.
  + pseudocode
  
    ```go
    FibonacciArray(n)
      fibArray <- an integer array w/ length of n
      fibArray[0] <- 0
      fibArray[1] <- 1
      for i from 2 to n
        fibArray[i] <- fibArray[i-2] + fibArray[i-1]

      return fibArray
    ```

  + Answer: [FibonacciArray](./src/e00-FibonacciAry.go)

+ Exercise: `MinArray`
  + write and implement a function `MinArray` that takes an array of integers as input and return the minimum of all these integers
  + pseudocode:

  ```go
  MinArray(array)
    min <- a very large integer (infinity)
    for i from 1 to length of the array
      if array[i] < min
        min <- array[i]
    return min
  ```

  + Answer: [MinArray](./src/e00-minArray.go)

+ Exercise: `GCDArray`
  + Write and implement a function `GCDArray` that takes an array of integers as input and generalizes the idea in `TrivialGCD` to return the greatest common divisor of all of the integers in the array.  You may wan to use MinArray as a subroutine.
  + pseudocode

    ```go
    GCDArray(array)
      min <- MinArray(array)
      for an integer i from min to 1
        isCommonDivisor <- true
        for an integer j from length of the array
          isCommonDivisor = isCommonDivisor AND (is i a divisor of array[j])
        if isCommonDivisor is true
          return i
    ```

  + Answer: [GCDArray](src/e00-gcdArray.go)


### 0.5.2 Exercises Part 2: More Number Types, and Mathematical Conjectures

#### Perfect numbers

+ Perfect number
  + __Definition:__ a perfect number is an integer $n$ that is equal to the sum of its proper divisors
  + e.g, $6 = 1 + 2 + 3$, $27 = 1 + 2 + 4 + 7 + 14$
  + Pattern:

    \[ \begin{align*}
      6 &= 2^1(2^2 - 1) \\ 28 &= 2^2(2^3 - 1) \\ 496 &= 2^4(2^5 - 1) \\ 8128 &= 2^5(2^6 -1)
    \end{align*} \]

+ Exercise: `IsPerfect`
  + Write and implement a function `IsPerfect` that takes an integer $n$ as input and return "true" if $n$ is perfect and "false" otherwise. Recalling out first attempt at `IsPrime`, do you see any ways of making your function more efficient?
  + pseudocode

    ```go
    IsPerfect(n)
      sum <- 0
      for an integer i from 1 to n-1
        if i is a divisor of n
          sum <- sum + i
      if sum = n
        return true
      else
        return false
    ```
  
  + Answer: [IsPerfect Go Code](./src/e00-isPerfect.go)

+ Exercise: `NextPerfectNumber`
  + Write and implement a function `NextPerfectNumber` that takes an integer $n$ as input and use `IsPerfect` as subroutine to find the smallest perfect number that is larger than $n$. The use your function to find the fifth perfect number (which was unknown to the Greeks).  Can this number be represented as a product of the above form?
  + pseudocode

    ```go
    NextPerfectNumber(n)
      nextNum <- n + 1
      while IsPerfect(nextNub) == false
        nextNum = nextNum + 1
      return n
    ```

  + [NextPerfectNumber Go Code](src/e00-nextPerfect.go)

+ Mersenne primes
  + numbers of the form $2^m -1$ are more likely than others to be prime
  + eg., $m = 2 \to 2^2 - 1 = 3, \quad m = 5 \to 2^5 - 1 = 31$
  + counter example: $m = 4 \to 2^4 - 1 = 15$

+ Euclid-Euler Theorem
  + __Theorem:__ every even perfect number must be of the form $2^{m-1} \cdot (2^m -1)$
  + __Theorem:__ $2^m - 1$ is a Mersenne prime $\to 2^{m-1} \cdot (2^m - 1)$ is perfect
  + $\therefore \exists $ infinitely many Mersenne prime $\to$ infinitely many perfect number
  + infinite Mersenne prime? $\to$ Unknown



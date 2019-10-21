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
  + Top-Down Programming and Modeling a Self-Replicating Automaton
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

+ Algorithms are everywhere
  + __Algorithm__: a sequence of steps used to solve a problem
  + __Program__: converting an algorithm into code

+ First computational problem
  + __Computational problem__: _input_ data along with a specified _output_ involving the input data that cn be interpreted in _only one way_
  + GCD Problem
    + Input: integers $a$ and $$
    + output: the greatest common divisor of $a$ and $b$, denoted GCD(a, b)
  + Variables: $a$ and $b$, they can change depending on what values we want them to have
  + STOP: does this substitution change the computational problem?

+ Trivial algorithm for computing a GCD
  + a = 378 and b = 273
  + divisors of 378: 1, 2, 3, 6, 7, 9, 14, 18, 21, 27, 42, 54, 63, 126, 189, 378
  + divisors of 273: 1, 3, 7, 13, 21, 39, 91, 273
  + GCD(378, 273) = 1, 3, 7, 21
  + A trivial (obvious) algorithm solving the GCD problem
    1. Start our largest common divisors at 1
    2. for every integer $n$ between 1 and min(a, b)
      + is $n$ a divisor of $a$?
      + is $n$ a divisor of $b$?
      + if the answer to both of these questions is "yes", update out largest common divisor found to be equal to $n$
    3. after ranging through all these integers, the largest common divisor found must be GCD(a, b)
  + STOP: why might we want a faster approach?

+ A painless intro to pseudocode/control flow
  + programming languages are plentiful
  + pseudocode: a way of describing algorithms by emphasizing ideas that is "just right"
    + not too vague, like human language
    + not too precise, like a specific programming language
  + Illustrating pseudocode with a simple problem
    + Minimum of two number problem
      + input: numbers a and b
      + output: the minimum value of a and b
    + seminal idea in computer science: being able to branch based on testing a condition

+ Algorithms just like functions
  + Input $\to$ Algorithm (computer science) $\to$ output
  + input $\to$ Function (Math) $\to$ output

### Flow Control

+ `Min2` function
  + pseudocode

    ```coffee
    Min2(a, b)
      if a > b
        return b
      else
        return a
    ```

  + `Min2`: name of the function
  + `a`, `b`: input "argument"/"parameter" variables
  + `if a > b`: if statement (allows us to branch)
    + if block: if the "if statement" is true, entering the code block
  + `return b`: return statement (provides output)
  + `else`: indicating where to go when if statement is false
  + STOP: does Min2 still return the desired answer if $a$ and $b$ are equal?

+ General form of if statements

  ```coffee
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

    ```coffee
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

    ```coffee
    Min3(a, b, c)
      if a > b
        return Min2(b, c)
      else
        Min2(a, c)
    ```

  + Exercise: write pseudocode for a function `Min4(a, b, c, d)` that compute the minimum for four numbers
  + Multiple approaches for solving even a simple problem

    ```coffee
    Min4(a, b, c, d)
      if a > b
        return Min3(b, c, d)
      else
        return Min3(a, c, d)

    Min4(a, b, c, d)
      return Min2(Mini2(a, b), Min2(c, d))
    ```

    + STOP: which of these do you prefer?

+ The Doomsday algorithm
  + The doomsdays occur on Thursdays in 2019: 1/3, 2/28, 3/0, 4/4, 5, 9, 6/6, 7/11, 8/8, 9/5, 10/10, 11/7, 12/12
  + STOP: how can we use this information to quickly find the day of the week for any given date in 2019?

  ```coffee
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

    ```coffee
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

  ```coffee
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

### Loops and and Trivial GCD algorithm

+ How to convert to Pseudocode?
  + GCD of 378 and 273
  + A trivial (obvious) algorithm solving the GCD problem
    1. start th elargest common divisor at 1
    2. for every integer n between 1 and min(a, b):
      + is `n` a divisor of `a`?
      + is `n` a divisor of `b`?
      + if the answer of both of these questions is "yes", update the largest common divisor found to be equal to `n`
    3. after ranging through all these integers, the largest common divisor found must be `GCD(a, b)`
  + Key point: how can we do something "for every integer" in a range?

+ A simple problem: factorial
  + Factorial problem
    + input: an integer `n`
    + output: $n! = n \times (n-1) \times (n-2) \times \cdots \times 2 \time 1$
  





### 0.4.3 Streaming Link for Lecture 1





## 0.5 Homework 0: Working with Integers and Arrays





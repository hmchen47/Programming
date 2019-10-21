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





## 0.4 Prologue: Ancient Greek Math and the Origins of Computational Thinking





### 0.4.1 Streaming Link for Lecture 0





### 0.4.2 Lecture 0 Slides





### 0.4.3 Streaming Link for Lecture 1





## 0.5 Homework 0: Working with Integers and Arrays




# A Short Introduction to Makefiles

Author: Zhiliang Xu

Date: 2012-02-15

[Original](https://www3.nd.edu/~zxu2/acms60212-40212/Makefile.pdf)


- Make utility and Makefile
  - make utility
    - a software tool for managing and maintaining computer programs
    - automatically determining which pieces of a large program need to be recompiled
    - issuing commands to recompile them
    - reading instruction from Makefile by default
  - Makefile
    - setting a set of rules to 
      - determine which parts of a program need to recompile
      - isssue command to to recompile them
    - a way of automating software building procedure and other complex tasks w/ dependencies
    - containing: **dependency rules**, **macros**, and **suffix** (or **implicit**) **rules**


- Example: command line compile
  - demo files
    - [`functions.h`](src/gc06/functions.h)
    - [`main.cpp`](src/gc06/main.cpp)
    - [`print_hello.cpp`](src/gc06/hello.cpp)
    - [`factorial.cpp`](src/gc06/factorial.cpp)
  - command line approach to compile

    ```sh
    $ g++ -c hello.cpp main.cpp factorial.cpp
    $ ls *.o
    factorial.o*  hello.o*  main.o*
    $ g++ -o prog factorial.0 hello.o main.o
    /usr/bin/ld: cannot find factorial.0: No such file or directory
    collect2: error: ld returned 1 exit status
    $ g++ -o prog factorial.o hello.o main.o
    $ ./prog
    Hello World!
    The factorial of 5 is 120
    ```

  - modifying `hello.cpp` $\to$ recompiling and link again

    ```sh
    $ g++ -c hello.cpp main.cpp factorial.cpp
    $ g++ -o prog factorial.0 hello.o main.o
    ```




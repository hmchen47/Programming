# Using make and writing Makefiles

Author: Tia Newhall

Date: 2023-03

[Original](https://www.cs.swarthmore.edu/~newhall/unixhelp/howto_makefiles.html)


## Using make

- Unix tools to build program
  - [`make`](http://www.gnu.org/software/make/manual/)
    - reading in rules from a user created Makefile
    - re-building things that need to be re-built
  - [`makedenpend`](hhttps://linux.die.net/man/1/makedepend)
    - autogenerating compilation dependencies of files in a Makefile
    - processing all source files to determine these
    - useful for larger Makefile
  - [`Cmake`](http://www.cmake.org/)
    - a cross platform build systems
    - generating makefiles
    - useful for large projects, for builds using lots of libs, and for dealing w/ platform specific compilation issues
    - Andy Danner, [Cmake doc](https://www.cs.swarthmore.edu/~adanner/tips/cmake.php)


- How to use `make`?
  - create `Makefile` listing the rules for building the executable
  - filename: `Makefile` or `makefile`
  - rebuilding the executable by typing `make`
  - a specific target in the Makefile can be executed by typing `make target_label`
  - example: to execute the rm command in the example makefile below, type `make clean`


## Writing a Makefile

- Creating a `makefile`
  - typical structure
    - starting w/ some variable definitions
    - then a set of target entries for building a specific targets
    - followed by executing a set of commands associated w/ a target label
  - generic target entry form

    ```makefile
    # comment
    # (note: the <tab> in the command line is necessary for make to work)
    target: dependency1 dependency2 ...
        <tab> command
    ```

  - example: `Makefile`

    ```makefile
    #
    # target entry to build program executable from program and mylib object files
    program: program.o mylib.o
        gcc -o program program.o mylib.o
    ```


## Example simple C (or C++) makefile

- Example: simple Makefile for a C (or C++)
  - most simple `Makefile` for compiling a single `.c` file

  ```makefile
  # build an executable named myprog from myprog.C
  all: myprog.c
    gcc -g -Wall -o myprog prog.C

  clean:
    $(RM) myprog
  ```


## Example more advanced C Makefile




## Example simple Java makefile





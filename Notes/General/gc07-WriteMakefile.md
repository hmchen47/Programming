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


- Example: a slightly more generic simple makefile

  ```makefile
  # the compiler: gcc for C program, define as g++ for C++
  CC = g++

  # compiler flags:
  #   -g    add debugging info to the executable file
  #   -Wall turns on most, but not all, compiler earnings
  CFLACKS = -g -Wall

  # the build target executable
  TARGET = myprog

  all: $(TARGET)

  $(TARGET): $(TARGET).c 
    $(CC) $(CFLAGS) -o $(TARGET) $(TARGET).c 

  clean:
    $(RM) $(TARGET)
  ```


- Example: building an executable from multiple `.o` files

  ```makefile
  #
  # This is an example Makefile for a countwords program.  This
  # program uses both the scanner module and a counter module.
  # Typing 'make' or 'make count' will create the executable file.
  #

  # define some Makefile variables for the compiler and compiler flags
  # to use Makefile variables later in the Makefile: $()
  #
  #  -g    adds debugging information to the executable file
  #  -Wall turns on most, but not all, compiler warnings
  #
  # for C++ define  CC = g++
  CC = gcc
  CFLAGS  = -g -Wall

  # typing 'make' will invoke the first target entry in the file 
  # (in this case the default target entry)
  # you can name this target entry anything, but "default" or "all"
  # are the most commonly used names by convention
  #
  default: count

  # To create the executable file count we need the object files
  # countwords.o, counter.o, and scanner.o:
  #
  count:  countwords.o counter.o scanner.o 
    $(CC) $(CFLAGS) -o count countwords.o counter.o scanner.o

  # To create the object file countwords.o, we need the source
  # files countwords.c, scanner.h, and counter.h:
  #
  countwords.o:  countwords.c scanner.h counter.h 
    $(CC) $(CFLAGS) -c countwords.c

  # To create the object file counter.o, we need the source files
  # counter.c and counter.h:
  #
  counter.o:  counter.c counter.h 
    $(CC) $(CFLAGS) -c counter.c

  # To create the object file scanner.o, we need the source files
  # scanner.c and scanner.h:
  #
  scanner.o:  scanner.c scanner.h 
    $(CC) $(CFLAGS) -c scanner.c

  # To start over from scratch, type 'make clean'.  This
  # removes the executable file, as well as old .o object
  # files and *~ backup files:
  #
  clean: 
    $(RM) count *.o *~
  ```



## Example more advanced C Makefile




## Example simple Java makefile





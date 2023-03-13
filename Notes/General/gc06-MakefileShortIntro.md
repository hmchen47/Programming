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


- Example: [Makefile](src/gc06/Makefile)

  ```makefile
  # This is a comment line
  CC = g++
  # CFLAGS will be thee optionns passed to the compiler.
  CFLAGS = -c -Wall

  all: prog

  prog: main.o factorial.o hello.o
    $(CC) main.o factorial.o hello.o -o prog

  main.o: main.cpp
    $(CC) $(CFLAGS) main.cpp

  factorial.o: factorial.cpp
    $(CC) $(CFLAGS) factorial.cpp

  hello.o: hello.cpp
    $(CC) $(CFLAGS) hello.cpp

  clean:
    rm -rf *.o
  ```


- Basic Makefile structure
  - **dependency rules**: consisting of 3 parts
    - one or more targets
    - zero or more dependencies
    - zero or more command
  - format

    ```text
    target: dependencies
    <tab>commands to make target
    ```

    - `<tab>`: character MUST NOT be replaced by spaces
    - `target`:
      - usually the name of a file, e.g., executable or object files
      - name of an action, e.g., `clean`
    - `dependencies`: files used as input to create the `target`
    - `command`: interpreted by a shell to be executed
  - phone targets
    - not really the name of a file
    - a list of commands and no dependencies


- Make utility
  - using `/bin/shell` by default
  - procedure to execute `make target`
    - ensure all the dependencies up to date
    - target older than any dependency $\implies$ recreate it using the specified commands
  - typing `make`: create first target in `Makefile` by default
  - example: the above `Makefile`
    - `prog` depending on `main.o factorial.o hello.o`
    - ensuring all object files existing and up-to-date
    - checking for them and recreating them if necessary






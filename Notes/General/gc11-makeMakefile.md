# The "make" Command and "Makefiles"

Author: Ram Naraian

Date: 2015-02-11

[original](https://www.hackerearth.com/practice/notes/the-make-command-and-makefiles/)


- The `make` and `Makefiles`
  - `make` w/ a lot of built-in knowledge
  - `makefile`: telling `make` how an app constructed
  - able to use separate makefiles for different parts of a large project
  - capabilities
    - controlling the compilation of source code
    - preparing manual pages
    - installing the app int a target dir
    - etc.


- The syntax of `Makefiles`
  - consisting of a set of dependencies and rules
    - **dependency:** a target and a set of source files
    - **rule:** a single executable file
  - `make` determining 
    - the order in which the targets have to be made
    - the correct sequence of rules to invoke


- Useful options of `make` utility
  - `-k`: continue even an error found
  - `-n`: print out what irt would be done w/o doing it
  - `-f`: tell which file to use as its makefile


- Dependency and target
  - **dependencies** specifying how each file in the final app  related to the source files
  - **target**: usually an executable file created
  - example:
    - source files: `main.c`, `2.c`, `3.c`, `a.h`, `b.h` and `c.h`
    - the dependency list of the above progeam as follows

      ```makefile
      myapp: main.o 2.o 3.o
      main.o: man.c a.h
      2.o: 2.c a.h b.h
      3.o: 3.c a.h b.h c.h
      ```

    - the set of dependencies providing a hierarchy showing how the source files related to one other


- Rules
  - describing how to create a target
  - syntax
    - MUST be on lines starting w/ a **tab**
    - a space at the end of the kine probably causing an error


- Example of rules
  - [Makefile](src/gc11/Makefile1)
    - `myapp`: 1st target, the file wonts to create

    ```makefile
    myapp: main.o 2.o 3.o
      gcc -o myapp main.o 2.o 3.o
    main.o: main.c a.h
      gcc -c main.c
    2.o: 2.c a.h b.h
      gcc -c 2.c
    3.o: 3.c b.h c.h
      gcc -c 3.c
    ```

  - output 1

    ```sh
    $ make -f Makefile1
    make: *** No rule to make target ‘main.c’, needed by ‘main.o’. Stop.
    ```

  - source files
    - [`main.c`](src/gc11/main.c): call `function_two` and `function_three`
    - [`2.c`](src/gc11/2.c): `function_two`
    - [`3.c`](src/gc11/3.c): `function_three`
  - header files: `touch a.h`, `touch b.h` and `touch c.h`
  - output 2

    ```sh
    $ make -f Makefile1
    gcc -c main.c
    gcc -c 2.c
    gcc -c 3.c
    gcc -o myapp main.o 2.o 3.o
    ```








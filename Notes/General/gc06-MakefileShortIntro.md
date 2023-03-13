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


- Example: [Makefile](src/gc06/Makefile.1)

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


- Marcos
  - preventing from repeating text entries
  - easier to modify ``Makefile`
  - format: `NAME = text string`
  - example: `CC = g++`
  - referred to by placing the name in wither parentheses `()` or curly braces `{}` and preceding w/ `$` sign
  - example: `$(CC) main.o factorial.o hello.o -o prog`
  - internal macros
    - predefined in `make`
    - `make -p`: displaying a list of all macros, suffix rules amd targets
  - special macros
    - macro `@`: evaluating the name of the current target
    - example

      ```makefile
      prog1: $(objs)
        $(CXX) -o $@ $(objs)

      # equivalent to
      prog1: $(objs)
        $(CXX) -o prog $(objs)
      ```

  - command line macro
    - defined on the command line
    - example: `make DEBUG_FLAG=-g`


- Suffix rules
  - a way to define rules or implicit rules
  - `make` used to build a program
  - obsolete and supported for compatibility
  - using pattern rules (a rule containing character `%`) if possible
  - types: double-suffix and single-suffix
  - **double-suffix**
    - defined by the source suffix and target suffix
    - example
      - telling `make` that `.o` files are made from `.cpp` files
      - `$<`: special marco that stands for a `.cpp` files used to produce a `.o` file

      ```makefile
      .cpp.o:
        $(CC) $(CFLAG) -c $<
      ```

  - equivalent to pattern rule `%.o: %.cpp`

    ```makefile
    %.o: %.cpp
      $(CC) $(CFLAGS) -c $<
    ```


- How does `make` work?
  - comparing the modification time of the target file w/ the modification times of the dependencies files
  - recreated when any dependency file w/ a more recent modification time than its target file
  - the 1st target file built by default
  - other targets checked only if they are dependencies for the 1st target
  - the order of the target no matter except for the 1st target
  - `make` utility building them in the order required


- Final example: Makefile w/ special macros
  - [Reference](https://www.gnu.org/software/make/manual/html_node/)

  ```makefile
  # This is a comment line
  CC = g++
  # CFLAGS will be the option passed to the compiler.
  CFLAGS = -c -Wall
  OBJECTS = main.o hello.o factial.o

  all: prog

  prog: $(OBJECTS)
    $(CC) $(OBJECTS) -o prog

  %.o: %.cpp
    $(CC) $(CFLAGS) $<

  clean:
    rm -f *.o
  ```




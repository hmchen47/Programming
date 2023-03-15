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


- Example of rules and execution
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

  - how it works
    - processing the dependencies section of the makefile
    - determining the files that need to be created an din which order
    - invoking the appropriate commands in the rule section for creating the files
  - changing a file
    - reading makefile
    - determining the minimum number of commands
    - carrying them out in the correct order

    ```sh
    $ touch b.h
    $ make -f Makefile1
    gcc -c 2.c
    gcc -c 3.c
    gcc -o myapp main.o 2.o 3.o
    ```


- Comments in a Makefile
  - starting w/ `#`
  - continue to the end of the lines


- Macros in a Makefile
  - used to 
    - define source files in a more generalized form
    - control different version of UNIX, compiler used on system, 
  - syntax: `MACRONAME = value`
  - able to set the value of a macro to blank by leaving the reset of line after the `=` blank
  - accessing the value of MACRONAME: `$(MACRONAME)` or `${MACRONAME}`
  - a good way to collect system dependent parts
  - usually defined within makefile
  - able to be specified by calling `make` w/ the macro definition
    - override defines in makefile
    - passed as a single argument, i.e., no spaces or quotes
    - example: `make CC=c89`, but not `CC = c89`
  - example: [Makefile](src/gc11/Makefile2)

    ```makefile
    //A makefile with macro:-
    //Here’s a revised version of the makefile, Makefile2 , using some macros:

    all: myapp

    # Which compiler
    CC = gcc

    # Where are include files kept
    INCLUDE = .

    # Options for development
    CFLAGS = -g -Wall -std=c89

    # Options for release
    # CFLAGS = -O -Wall (–ansi = -std=c89 )
    myapp: main.o 2.o 3.o
      $(CC) -o myapp main.o 2.o 3.o
    main.o: main.c a.h
      $(CC) -I$(INCLUDE) $(CFLAGS) -c main.c
    2.o: 2.c a.h b.h
      $(CC) -I$(INCLUDE) $(CFLAGS) -c 2.c
    3.o: 3.c b.h c.h
      $(CC) -I$(INCLUDE) $(CFLAGS) -c 3.c
    ```

  - output

    ```sh
    $ make -f Makefile2
    gcc -I. -g -Wall -std=c89 -c main.c
    gcc -I. -g -Wall -std=c89 -c 2.c
    gcc -I. -g -Wall -std=c89 -c 3.c
    gcc -o myapp main.o 2.o 3.o
    ```


- Special buil-in macros
  - `$?`: list of reprequisites changed more recently than the current target
  - `$@`: name of the current target
  - `$<`: name of the current prerequisite
  - `$^`: name of the current prerequisites, w/o any suffix


- Multiple targets
  - useful to make more tha a single target file
  - useful to collect several groups of commands into a single place
  - special target `all`: default target; specifying only `myapp` as a target
  - `clean` target:
    - using the `rm` command to remove the objects
    - starting w/ `-` to ignore the result of the command
  - `install` target
    - dependent on `myapp`
    - creating `myapp` before carrying out other commands before making install
    - consisting of shell script commands
  - shell script
    - `make` utility invoking a shell for executing rules
    - adding backslashes (`\`) to
      - make the script commands on the same logical line 
      - pass together to a single invocation of the shell for execution
    - starting w/ `@` sign by not printing the command on the standard output before execcuting the rule
  - example [Makefile](src/gc11/Makefile3)

    ```makefile
    # Which compiler
    CC = gcc
    # Where to install
    INSTDIR = /usr/local/bin

    # Where are include files kept
    INCLUDE = .
    # Options for development
    CFLAGS = -g -Wall -std=c89

    # Options for release
    # CFLAGS = -O -Wall –ansi
    myapp: main.o 2.o 3.o
      $(CC) -o myapp main.o 2.o 3.o
    main.o: main.c a.h
      $(CC) -I$(INCLUDE) $(CFLAGS) -c main.c
    2.o: 2.c a.h b.h
      $(CC) -I$(INCLUDE) $(CFLAGS) -c 2.c
    3.o: 3.c b.h c.h
      $(CC) -I$(INCLUDE) $(CFLAGS) -c 3.c
    clean:
      -rm main.o 2.o 3.o
    install: myapp
    @if [ -d $(INSTDIR) ]; \
      then \
      cp myapp $(INSTDIR);\
      chmod a+x $(INSTDIR)/myapp;\
      chmod og-w $(INSTDIR)/myapp;\
      echo “Installed in $(INSTDIR)“;\
    else \
      echo “Sorry, $(INSTDIR) does not exist”;\
    fi
    ```

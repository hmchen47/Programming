# What is a Makefile and how does it work?

Author: Sachin Patil

Date: 2018-08-22

[Original](https://opensource.com/article/18/8/what-how-makefile)


## Basic Examples

- Rules of Makefile
  - syntax of typical rule

    ```makefile
    target: prerequisites
    <TAB< recipe
    ```

  - example

    ```makefile
    final_target: sub_target final_target.C
      Recipe_to_create_final_target

    sub_target: sub_target.c
      Recipe_to_create_sub_target
    ```


- Example: simple Makefile
  - basic Makefile
    - target: `say_hello`
    - prerequisites or dependencies: empty string as follwing `target` 
    - recipe: `echo "Hello World"`

    ```makefile
    say_hello:
      echo "Hello World"
    ```

  - executing `make` utility

    ```sh
    $ make
    echo "Hello World"
    Hello World
    ```


- Suppressing echo
  - starting `echo` w/ `@`
  - example

    ```makefile
    say_hello:
      @echo "Hello World"
    ```

  - executing `make` utility

    ```sh
    $ make
    Hello World
    ```


- Phony targets
  - target just a name of recipe
  - add more phony targets: `generate` and `clean`
  - example: Makefile

    ```makefile
    say_hello:
      @echo "Hello World"

    generate:
      @echo "Creating empty text files ..."
      touch file-{1..10}.tet 

    clean:
      @echo "Clean up..."
      rm *.txt
    ```


- Default target
  - the first target in the makefile
  - a.k.a. **default goal**
  - usually `all` as the first target in most projects
  - `all` responsible for calling other targets
  - `.DEFAULT_GOAL`:
    - special phony target to override the behavior
    - executing only one target at a time
    - most makefile including `all` as the target to call as many target as needed
  - example: `.DEFAULT_GOAL := generate`

    ```sh
    $ make
    Creating empty text file...
    touch file-{1..10}.txt
    ```


- Special phony target
  - `.PHONY`:
    - define all the targets that are not files
    - executing its recipe regardless of whether a file w/ that name exists or what its modification time is
  - example

    ```makefile
    .PHONY: all say_hello generate clean

    all: say_hello generate

    say_hello:
      @echo "Hello World"

    generate:
      @echo "Creating empty text files..."
      touch file-{1..10}.txt

    clean:
      @echo "Cleaning up..."
      rm *.txt
    ```

  - executing `make` utility

    ```sh
    $ make
    Hello World
    Creating empty text files...
    touch file-{1..10}.txt

    $ make clean
    Clean up...
    rm *.txt
    ```


## Advanced Examples

- Variables
  - replacing hard-coded targets and prerequisite values w/ variables and patterns
  - `=` operator: simplest way to define a variable in the makefile
  - example: assign the command `gcc` to a variable `CC` $\to$ `CC - gcc`
  - recursive expanded variable
    - assigned w/ `=` operator
    - example:
      - assigning variable: `CC = gcc`
      - recipe: `${CC} hello.c -o hello`
      - recipe expanding as `gcc -o hello`
  - simply expanded variable
    - assigned w/ `:=` operator
    - example: `CC := gcc`


- Reference variables
  - both `${CC}` and `$(CC)` valid reference to call `gcc`
  - verifying by reassigning a variable

    ```makefile
    CC = gcc
    CC = ${CC}

    all:
      @echo ${CC}
    ```

  - execcuting `make`

    ```sh
    $ make
    Makefile:8: *** Recursive variable 'CC' references itself (eventually).  Stop.
    ```


## Patterns and Functions

- Makefile w/ patterns and functions
  - `%`: matching any target name
  - `$<`: pattern to match prerequisites
  - `$@`: pattern to match target
  - `#`: comments
  - `.PHONY = all clean`: define phony targets `all` and `clean`
  - `LINKERFLAG`: variable defines flags to be used w/ `gcc` in a recipe
  - `SRCS := $(wildcard *.c): $(wildcard pattern)`:
    - one of the functions for filenames
    - all files w/ the `.c` extension stored in a variable `SRCS`
  - `BINS := $(SRCS:%.c=%)`
    - substitution reference
    - `SRCS` w/ values `foo.c bar.c` $\to$ `BINS` w/ `foo bar`
  - `all: ${BINS}`: phony target `all` calling values in `${BINS}` as individual targets
  - rule to link all object files
    - `foo`: one of the values in `${BINS}`
    - `%` replaced by `foo`
    - `$<` called for every value in `${BINS}`

    ```makefile
    %: %.o
      @echo "Checking.."
      ${CC} ${LINKERFLAG} $< -o $@

    # expand as
    foo: foo.o
      @echo "Checking.."
      gcc -lm foo.o -o foo
    ```

  - rule to compile `.c` files

    ```makefile
    %.o: %.c
      @echo "Creating object.."
      ${CC} -c $&lt;

    # expand as
    foo.o: foo.c
      @echo "Creating object.."
      gcc -c foo.c
    ```

  - `clean`: target to remove all binaries and object files

  - example

    ```makefile
    # Usage:
    # make        # compile all binary
    # make clean  # remove ALL binaries and objects

    .PHONY = all clean

    CC = gcc      # compiler to use

    LINKERFLAG = -lm

    SRCS := $(wildcard *.c)
    BINS := $(SRCS:%.c=%)

    all: ${BINS}

    %: %.o
      @echo "Checking.."
      ${CC} ${LINKERFLAG} $< -o $@

    %.o: %.c
      @echo "Creating object.."
      ${CC} -c $<

    clean:
      @echo "Cleaning up..."
      rm -rvf *.o ${BINS}
    ```



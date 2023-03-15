# C Makefile cheatsheet

Author: Chang-Ning Tsai

Date: 2022-07-28

[Original](https://cppcheatsheet.com/notes/c_make.html)


- Automatic variables
  - `$@`: filename of the target
  - `$<`: name of the first prerequisite
  - `$^`: name of all the prerequisites
  - `$+`: prerequisites listed more than one are duplicated in the order
  - example: [Makefile](src/gc10/Makefile.01)

    ```makefile
    .PHONY: all

    all: hello world

    hello world: foo foo foo bar bar
      @echo "== target: $@ =="
      @echo $<
      @echo $^
      @echo $+

    foo:
      @echo "Hello foo"

    bar:
      @echo "Hello Bar"
    ```

  - output

    ```sh
    $ make
    Hello foo
    Hello Bar
    == target: hello ==
    foo
    foo bar
    foo foo foo bar bar
    == target: world ==
    foo
    foo bar
    foo foo foo bar bar
    ```


- Makefile warning message
  - using `$(warning text)` to check make rules
  - useful debuging message
  - example: [Makefile](src/gc10/Makefile.02)

    ```makefile
    $(warning Top level warning)

    FOO := $(warning FOO variable)foo
    BAR  = $(warning BAR variable)bar

    $(warning target)target: $(warning prerequisite list)Makefile $(BAR)
      $(warning tagrget script)
      @ls
    $(BAR):
    ```
    
  - output

    ```sh
    $ make
    Makefile:1: Top level warning
    Makefile:3: FOO variable
    Makefile:6: target
    Makefile:6: prerequisite list
    Makefile:6: BAR variable
    Makefile:9: BAR variable
    Makefile:7: target script
    Makefile
    ```


- String functions
  - typical string functions: substitute, filter, find string, word counts, word, and word list
  - example: [Makefile](src/gc10/Makefile.03)

    ```makefile
    SRC      = hello_foo.c hello_bar.c foo_world.c bar_world.c

    SUBST    = $(subst .c,,$(SRC))

    SRCST    = $(SRC:.c=.o)
    PATSRCST = $(SRC:%.c=%.o)
    PATSUBST = $(patsubst %.c, %.o, $(SRC))

    .PHONY: all

    all: sub filter findstring words word wordlist

    sub:
      @echo "== sub example =="
      @echo "SUBST: " $(SUBST)
      @echo "SRCST: " $(SRCST)
      @echo "PATSRCST: " $(PATSRCST)
      @echo "PATSUBST: " $(PATSUBST)
      @echo ""

    filter:
      @echo "== filter example =="
      @echo "filter: " $(filter hello_%, $(SRC))
      @echo "filter-out: $(filter-out hello_%, $(SRC))"
      @echo ""

    findstring:
      @echo "== findstring example =="
      @echo "Res: " $(findstring hello, hello world)
      @echo "Res: " $(findstring hello, ker)
      @echo "Res: " $(findstring world, worl)
      @echo ""

    words:
      @echo "== words example =="
      @echo "num of words: "$(words $(SRC))
      @echo ""


    word:
      @echo "== word example =="
      @echo "1st word: " $(word 1,$(SRC))
      @echo "2nd word: " $(word 2,$(SRC))
      @echo "3th word: " $(word 3,$(SRC))
      @echo ""


    wordlist:
      @echo "== wordlist example =="
      @echo "[1:3]:"$(wordlist 1,3,$(SRC))
      @echo ""
    ```

  - output

    ```sh
    $ make
    == sub example ==
    SUBST:  hello_foo hello_bar foo_world bar_world
    SRCST:  hello_foo.o hello_bar.o foo_world.o bar_world.o
    PATSRCST:  hello_foo.o hello_bar.o foo_world.o bar_world.o
    PATSUBST:  hello_foo.o hello_bar.o foo_world.o bar_world.o

    == filter example ==
    filter:  hello_foo.c hello_bar.c
    filter-out: foo_world.c bar_world.c

    == findstring example ==
    Res:  hello
    Res: 
    Res: 

    == words example ==
    num of words: 4

    == word example ==
    1st word:  hello_foo.c
    2nd word:  hello_bar.c
    3th word:  foo_world.c

    == wordlist example ==
    [1:3]:hello_foo.c hello_bar.c foo_world.c
    ```


- Makefile w/ sorting and removing duplicates
  - using `sort`, `suffix` string functions
  - example: [Makefile](src/gc10/Makefile.04)

    ```makefile
    SRC = foo.c bar.c ker.c foo.h bar.h ker.h

    .PHONY: all

    all:
      @echo $(suffix $(SRC))
      @echo $(sort $(suffix $(SRC)))
    ```

  - output

    ```sh
    $ make
    .c .c .c .h .h .h
    .c .h
    ```


- Single and double dollar sign in Makefile
  - `$`: reference a make variable
  - `$$`: reference a shell variable
  - example: [Makefile](src/gc10/Makefile.05)

    ```makefile
    LIST = one two three

    .PHONY: all single_dollar double_dollar

    all: single_dollar double_dollar

    double_dollar:
      @echo "=== double dollar sign example ==="
      @for i in $(LIST); do \
        echo $$i;     \
      done

    single_dollar:
      @echo "=== single dollar sign example ==="
      @for i in $(LIST); do  \
        echo $i;     \
      done
    ```

  - output

    ```shell
    $ make
    === single dollar sign example ===



    === double dollar sign example ===
    one
    two
    three
    ```


- Building executable files
  - files in current dir: `foo.h`, `foo.c`, `bar.h`, and `bar.h`
  - example: [Makefile](src/gc10/Makefile.06)

    ```makefile
    # CFLAGS: Extra flags to give to the C compiler
    CFLAGS   += -Werror -Wall -O2 -g
    SRC       = $(wildcard *.c)
    OBJ       = $(SRC:.c=.o)
    EXE       = $(subst .c,,$(SRC))

    .PHONY: all clean

    all: $(OBJ) $(EXE)

    clean:
      rm -rf *.o *.so *.a *.la $(EXE)
    ```

  - output

    ```sh
    $ make
    cc -Werror -Wall -O2 -g   -c -o bar.o bar.c
    cc -Werror -Wall -O2 -g   -c -o foo.o foo.c
    cc   bar.o   -o bar
    cc   foo.o   -o foo
    ```


- Predefine variables w/ `$(eval)`
  - example: [Makefile](src/gc10/Makefile.07) w/o `$(eval)`

    ```makefile
    SRC = $(wildcard *.c)
    EXE = $(subst .c,,$(SRC))

    define PROGRAM_template
    $1_SHARED = lib$(strip $1).so
    endef

    .PHONY: all

    $(foreach exe, $(EXE), $(call PROGRAM_template, $(exe)))

    all:
      @echo $(foo_SHARED)
      @echo $(bar_SHARED)
    ```

  - output of `make`: `Makefile:10: *** missing separator.  Stop.`
  - example: [Makefile](src/gc10/Makefile.08)

    ```makefile
    ...
    $(foreach exe, $(EXE), $(eval $(call PROGRAM_template, $(exe))))
    ...
    ```

  - output

    ```sh
    $ make
    libfoo.so
    libbar.so
    ```


# C Makefile cheatsheet

Author: Chang-Ning Tsai

Date: 2022-07-28

[Original](https://cppcheatsheet.com/notes/c_make.html)


- Automatic variables
  - `$@`: filename of the target
  - `$<`: name of the first prerequisite
  - `$^`: name of all the prerequisites
  - `$+`: prerequisites listed more than one are duplicated in the order
  - example: [Makefile](src/Makefile.1)

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
  - example: [Makefile](src/gc10/Makefile.2)

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
  - example: [src/gc10/Makefile.3]

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



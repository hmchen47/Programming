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
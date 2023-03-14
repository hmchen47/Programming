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


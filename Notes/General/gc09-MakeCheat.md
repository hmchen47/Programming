# GNU make cheat sheet

Author: Nasser M. Abbasi

Date: 2020-05-23

[Original](https://www.12000.org/my_notes/cheat_sheets/make_notes/index.htm)


- Recursive make
  - used to build everything in the tree
  - tree structure: `A` as top dir w/ `B` and `C` as sub-dirs
  - `$HOME` containing the `common.mk` file

    ```makefile
    all::
      @for d in $(DIRS); \
      do                 \
        $(MAKE) --directory=$$d;   \
      done
    ```

  - executing `make -I$(HOME)`

    ```sh
    $ make
    make[1]: Entering directory `/tmp/B'
    make[1]: Leaving directory `/tmp/B'
    make[1]: Entering directory `/tmp/C'
    make[1]: Leaving directory `/tmp/C'
    ```


- Using `common.mk` in recursive make
  - `Makefile` in subfolders starting by defining its own specific variables
  - `common.mk` residing in common locaton such as `$HOME`
  - each makefile including this file
  - syntax: `include filenames…`
  - example:
    - Makefile in the `A` folder

      ```makefile
      DIRS := B C
      include common.mk
      all::
      ```

  - each subfolder including similar makefile
    - starting by listing the dirs below it
    - then including `common.mk`
  - actions performed by makefile
    - done at the bottom most directories first
    - followed by the higher level up
    - acting like as a stack


- Building in local directory w/o traversing
  - `-B`: unconditional make all targets
  - example:
    - building `index.htm` from `index.tex`
    - `make -I$HOME -B index.htm` 





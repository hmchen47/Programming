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





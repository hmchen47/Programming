# Argparse Tutorial

Author: Tshepang Lekhonkhobe

Date: 2023

[Original](https://docs.python.org/3/howto/argparse.html)


## Concepts

- Concepts of command line
  - `ls` cmd:
    - useful when run w/o any options at all
    - default to current directory
  - `ls <dir>`
    - displaying a different directory
    - `<dir>`: **positional argument**
    - program knowing what to do w/ the value
    - solely based on where it appears on the cmd line
    - e.g.: `cp SRC DST` - `SRC` $\to$ what you want copied, `DST` $\to$ where you want it copied to
  - `ls -l`
    - changing the behavior of the program
    - displayiing more info for each file
    - `-l`: **optional argument**
  - `ls --help`
    - a snippet of the help text
    - useful when a program is never used before
    - able to figure out how it works simply by reading its help text


## The Basics

- Embedded option of `argparse`
  - simple code snippet
    - `argparse.ArgumentParser()`: initiating an instance
    - `parser.parse_args`: retrieving the arguments from the cmd line

    ```python
    # src/argparse/prog01.py
    import argparse

    parser = argparse.ArgumentParser()
    parser.parse_args()
    ```

  - results
    - running w/o any options: nothing displayed in stdout
    - `--help` option:
      - displaying the usefullness of `argparse` module
      - the only option not required to specify
      - specifying anything else results in an error
      - `-h` as shortened option

    ```sh
    $ ./prog01.py
    $ ./prog01.py --help
    usage: prog01.py [-h]

    options:
      -h, --help  show this help message and exit
    $ ./prog01.py --verbose
    usage: prog01.py [-h]
    prog01.py: error: unrecognized arguments: --verbose
    $ ./prog01.py foo
    usage: prog01.py [-h]
    prog01.py: error: unrecognized arguments: foo
    ```



## Introducing Positional Arguments

- Positional argument overview
  - code snippet
    - option required to call
    - `parse-args` method: returning some data from the options specified
    - variable (`-h`) w/ some form of 'magic' embedded in `argparse` to perform for free
    - no need to specify which variable that value is stored in 

    ```python
    # src/argparse/prog02.py
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("echo")
    args = parser.parse_args()
    print(args.echo)
    ```

  - result

    ```sh
    $ python prog02.py
    usage: prog02.py [-h] echo
    prog02.py: error: the following arguments are required: echo

    $ python prog02.py -h
    usage: prog02.py [-h] echo

    positional arguments:
      echo

    options:
      -h, --help  show this help message and exit
    
    $ python prog02.py foo
    foo
    ```


- Adding help text
  - code snippet

    ```python
    # src/argparse/prog03.py
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("echo", help="echo the string you use here")
    args = parser.parse_args()
    print(args.echo)
    ```

  - result

    ```sh
    $ ./prog03.py -h
    usage: prog03.py [-h] echo

    positional arguments:
      echo        echo the string you use here

    options:
      -h, --help  show this help message and exit
    ```


- Arguments w/ other datatype
  - error code snippet
    - treating options as string
    - required option datatype: `int`

    ```python
    # src/argparse/prog04.py
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("square", help="display a square of a given number")
    args = parser.parse_args()
    print(args.square**2)
    ```

  - result

    ```sh
    $ ./prog04.py 4
    Traceback (most recent call last):
      File "/home/hmchen/Projects/Programming/Notes/src/argparse/./prog04.py", line 8, in <module>
        print(args.square**2)
    TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
    ```

  - code snippet
    - argument w/ datatype `int`

    ```python
    # src/argparse/prog05.py
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("square", help="display a square of a given number", type=int)
    args = parser.parse_args()
    print(args.square**2)
    ```

  - results

    ```sh
    $ ./prog05.py 4
    16

    $ ./prog05.py four
    usage: prog05.py [-h] square
    prog05.py: error: argument square: invalid int value: 'four'
    ```



## Introducing Optional arguments

- Optional argument w/ `--verbosity` option
  - code snippet
    - displaying somethion when `--verbosity` specified
    - displaying notthing when not
    - optional option: no error when running the program w/o it
    - relevant variable value if not present: `args.verbosity = None`

    ```python
    # src/argparse/prog06.py
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--verbosity", help="increase output verbosity")
    args = parser.parse_args()
    if args.verbosity:
      print("verbosity turned on")
    ```

  - results

    ```sh
    $ ./prog06.py

    $ ./prog06.py --help
    usage: prog06.py [-h] [--verbosity VERBOSITY]

    options:
      -h, --help            show this help message and exit
      --verbosity VERBOSITY
                            increase output verbosity

    $ ./prog06.py --verbosity
    usage: prog06.py [-h] [--verbosity VERBOSITY]
    prog06.py: error: argument --verbosity: expected one argument
    ```


- Assigning boolean values for optional arguments
  - option: `action = <store_true | store_false>`
  - code snippet

    ```python
    # src/argparse/prog07.py
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", help="increase output verbosity", action="store_true")
    parser.parse_args()
    ```

  - results

    ```python
    $ ./prog07.py -v
    usage: prog07.py [-h] [--verbose]
    prog07.py: error: unrecognized arguments: -v

    $ ./prog07.py --help
    usage: prog07.py [-h] [--verbose]

    options:
      -h, --help  show this help message and exit
      --verbose   increase output verbosity
    ```


- Short options
  - code snippet

    ```python
    # src/argparse/prog08.py
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
      "-v", "--verbose", help="increase output verbosity", action="store_true"
    )
    parser.parse_args()
    if args.verbose:
      print("verbosity turned on")
    ```

  - result

    ```sh
    $ ./prog08.py -v
    verbosity turned on

    $ ./prog08.py --help
    usage: prog08.py [-h] [-v]

    options:
      -h, --help     show this help message and exit
      -v, --verbose  increase output verbosity
    ```


## Combining Positional and Optional arguments

- Combining positional and optional arguments
  - order not matter
  - code snippet

    ```python
    # src/argparse/prog09.py
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("square", type=int, help="display a square of a given number")
    parser.add_argument(
      "-v", "--verbose", action="store_true", help="increase output verbosity"
    )
    args = parser.parse_args()
    answer = args.square**2
    if args.verbose:
        print(f'the square of {args.square} equals to {answer}')
    else:
      print(answer)
    ```

  - result

    ```sh
    $ ./prog09.py
    usage: prog09.py [-h] [-v] square
    prog09.py: error: the following arguments are required: square
    $ ./prog09.py 4
    16
    $ ./prog09.py 4 --verbose
    the square of 4 equals to 16
    $ ./prog09.py 4 -v
    the square of 4 equals to 16
    ```


- Multiple values of an optional argument
  - code snippet

    ```python
    # stc/argparse/prog10.py
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("square", type=int, help="display a square of a given number")
    parser.add_argument("-v", "--verbose", type=int, help="increase output verbosity")
    args = parser.parse_args()
    answer = args.square**2
    if args.verbose == 2:
      print(f"the square of {args.square} equals to {answer}")
    elif args.verbose == 1:
      print(f"{args.square}^2 = {answer}")
    else:
      print(answer)
    ```

  - results+

    ```sh
    $ ./prog10.py 4
    16

    $ ./prog10.py 4 -v
    usage: prog10.py [-h] [-v VERBOSE] square
    prog10.py: error: argument -v/--verbose: expected one argument

    $ ./prog10.py 4 -v 1
    4^2 = 16

    $ ./prog10.py 4 -v 2
    the square of 4 equals to 16

    $ ./prog10.py 4 -v 3
    16
    ```

  
- Restricting values of optional arguments
  - option: `choices=<list>`
  - code snippet

    ```python
    # src/argparse/prog11.py
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("square", type=int, help="display a square of a given number")
    parser.add_argument(
      "-v", "--verbose", type=int, choices=[0, 1, 2], help="increase output verbosity"
    )
    args = parser.parse_args()
    answer = args.square**2
    if args.verbose == 2:
      print(f"the square of {args.square} equals to {answer}")
    elif args.verbose == 1:
      print(f"{args.square}^2 = {answer}")
    else:
      print(answer)
    ```

  - result

    ```sh
    $ ./prog11.py 4 -v 3
    usage: prog11.py [-h] [-v {0,1,2}] square
    prog11.py: error: argument -v/--verbose: invalid choice: 3 (choose from 0, 1, 2)

    $ ./prog11.py 4 -h
    usage: prog11.py [-h] [-v {0,1,2}] square

    positional arguments:
      square                display a square of a given number

    options:
      -h, --help            show this help message and exit
      -v {0,1,2}, --verbose {0,1,2}
                            increase output verbosity
    ```


- Multiple same optional arguments
  - specifying duplicated arguments w/ `action="count"`
  - code snippet
    - more of a flag to explain the complain
    - similar to `store_true` action
    - demonstrating what the `count` acction gives
    - no `-v` flag specified $\to$ `None` value for the flag
    - specifying the long form of the flag $\to$ same output 
    - help output not very informative but always fixed by improving the documentation for the script
    - `-vvv` exposing a bug, expecting same as `-vv`

    ```python
    # src/argparse/prog12.py
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("square", type=int, help="display a square of a given number")
    parser.add_argument("-v", "--verbose", action="count", help="increase output verbosity")
    args = parser.parse_args()
    answer = args.square**2
    if args.verbose == 2:
        print(f"the square of {args.square} equals to {answer}")
    elif args.verbose == 1:
        print(f"{args.square}^2 = {answer}")
    else:
        print(answer)
    ```

  - result

    ```sh
    $ ./prog12.py 4
    16

    $ ./prog12.py 4 -v
    4^2 = 16

    $ ./prog12.py 4 -vv
    the square of 4 equals to 16

    $ ./prog12.py 4 --verbose --verbose
    the square of 4 equals to 16

    $ ./prog12.py 4 -v 1
    usage: prog12.py [-h] [-v] square
    prog12.py: error: unrecognized arguments: 1

    $ ./prog12.py 4 -h
    usage: prog12.py [-h] [-v] square

    positional arguments:
      square         display a square of a given number

    options:
      -h, --help     show this help message and exit
      -v, --verbose  increase output verbosity

    $ ./prog12.py 4 -vvv
    16
    ```


- Fixing the verbose bug
  - code snippet
    - behaving multiple same flags w/ the same result

    ```python
    # src/argparse/prog13.py
    ...
    if args.verbose >= 2:
        print(f"the square of {args.square} equals to {answer}")
    elif args.verbose >= 1:
      print(f"{args.square}^2 = {answer}")
    ...
    ```

  - result
    - 2nd output resulting error

    ```sh
    $ ./prog13.py 4 -vvvv
    the square of 4 equals to 16

    $ ./prog13.py 4 
    Traceback (most recent call last):
      File "/home/hmchen/Projects/Programming/Notes/src/argparse/./prog13.py", line 10, in <module>
        if args.verbose >= 2:
    TypeError: '>=' not supported between instances of 'NoneType' and 'int'
    ```


- Assigning default value
  - adding default value to prevent from error
  - code snippet

    ```python
    # src/argparse/prog14.py
    ...
    parser.add_argument(
        "-v", "--verbose", action="count", default=0, help="increase output verbosity"
    )
    ...
    ```

  - result

    ```sh
    $ ./prog14.py 4 
    16
    ```


## Getting a Little More Advanced

- Multiple positional arguments
  - computing value w/ 2 positional arguments
  - code snippet

    ```python
    # src/argparse/prog15.py
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("x", type=int, help="the base")
    parser.add_argument("y", type=int, help="the exponent")
    parser.add_argument("-v", "--verbose", action="count", default=0)
    args = parser.parse_args()
    answer = args.x**args.y
    if args.verbose >= 2:
        print(f"{args.square} to the power {args.y} equals to {answer}")
    elif args.verbose >= 1:
        print(f"{args.x}^{args.y} == {answer}")
    else:
        print(answer)
    ```

- result

  ```sh
  $ ./prog15.py
  usage: prog15.py [-h] [-v] x y
  prog15.py: error: the following arguments are required: x, y

  $ ./prog15.py -h
  usage: prog15.py [-h] [-v] x y

  positional arguments:
    x              the base
    y              the exponent

  options:
    -h, --help     show this help message and exit
    -v, --verbose

  $ ./prog15.py 4 2 -v
  4^2 == 16
  ```


- Verbose levels
  - using verbosity level to change the displayed text
  - code snippet

    ```python
    #src/argparse/prog16.py
    ...
    if args.verbose >= 2:
        print(f"Running '{__file__}'")
    elif args.verbose >= 1:
        print(f"{args.x}^{args.y} == {answer}", end="")
    print(answer)
    ```

  - result

    ```sh
    $ ./prog16.py 4 2
    16

    $ ./prog16.py 4 2 -v
    4^2 == 1616

    $ ./prog16.py 4 2 -vv
    Running '.../argparse/./prog16.py'
    16

    $ python prog16.py 4 2 -vv
    Running '.../argparse/prog16.py'
    16
    ```


- Conflict Options
  - `add_mutually_exclusive_group` method: specifying options that conflict w/ each other
  - example: `--quiet` and `--verbose` opposite each other
  - code snippet

    ```python
    # src/argparse/prog17.py
    import argparse

    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quiet", action="store_true")
    parser.add_argument("x", type=int, help="the base")
    parser.add_argument("y", type=int, help="the exponent")
    args = parser.parse_args()
    answer = args.x**args.y
    if args.quiet:
        print(answer)
    elif args.verbose:
        print(f"{args.x} to the power {args.y} equals {answer}")
    else:
        print(f"{args.x}^{args.y} == {answer}")
    ```

  - result

    ```sh
    $ ./prog17.py 4 2
    4^2 == 16
    $ ./prog17.py 4 2 -q
    16
    $ ./prog17.py 4 2 -v
    4 to the power 2 equals 16
    $ ./prog17.py 4 2 -vq
    usage: prog17.py [-h] [-v | -q] x y
    prog17.py: error: argument -q/--quiet: not allowed with argument -v/--verbose
    $ ./prog17.py 4 2 -v --quiet
    usage: prog17.py [-h] [-v | -q] x y
    prog17.py: error: argument -q/--quiet: not allowed with argument -v/--verbose
    ```


- Adding main purpose of the program
  - code snippet

    ```python
    # src/argparse/prog18.py
    import argparse

    parser = argparse.ArgumentParser(description="calculate X to the power of Y")
    ...
    ```

  - result

    ```sh
    $ ./prog18.py --help
    usage: prog18.py [-h] [-v | -q] x y

    calculate X to the power of Y

    positional arguments:
      x              the base
      y              the exponent

    options:
      -h, --help     show this help message and exit
      -v, --verbose
      -q, --quiet
    ```




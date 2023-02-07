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




## Getting a Little More Advanced





### Conflict Options





## Conclusion




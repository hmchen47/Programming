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





## Introducing Optional arguments




### Short options





## Combining Positional and Optional arguments





## Getting a Little More Advanced





### Conflict Options





## Conclusion




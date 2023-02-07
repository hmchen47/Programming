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




## Introducing Positional arguments




## Introducing Optional arguments




### Short options





## Combining Positional and Optional arguments





## Getting a Little More Advanced





### Conflict Options





## Conclusion




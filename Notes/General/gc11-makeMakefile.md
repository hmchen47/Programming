# The "make" Command and "Makefiles"

Author: Ram Naraian

Date: 2015-02-11

[original](https://www.hackerearth.com/practice/notes/the-make-command-and-makefiles/)


- The `make` and `Makefiles`
  - `make` w/ a lot of built-in knowledge
  - `makefile`: telling `make` how an app constructed
  - able to use separate makefiles for different parts of a large project
  - capabilities
    - controlling the compilation of source code
    - preparing manual pages
    - installing the app int a target dir
    - etc.


- The syntax of `Makefiles`
  - consisting of a set of dependencies and rules
    - **dependency:** a target and a set of source files
    - **rule:** a single executable file
  - `make` determining 
    - the order in which the targets have to be made
    - the correct sequence of rules to invoke


- Useful options of `make` utility
  - `-k`: continue even an error found
  - `-n`: print out what irt would be done w/o doing it
  - `-f`: tell which file to use as its makefile









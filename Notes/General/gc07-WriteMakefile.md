# Using make and writing Makefiles

Author: Tia Newhall

Date: 2023-03

[Original](https://www.cs.swarthmore.edu/~newhall/unixhelp/howto_makefiles.html)


## Using make

- Unix tools to build program
  - [`make`](http://www.gnu.org/software/make/manual/)
    - reading in rules from a user created Makefile
    - re-building things that need to be re-built
  - [`makedenpend`](hhttps://linux.die.net/man/1/makedepend)
    - autogenerating compilation dependencies of files in a Makefile
    - processing all source files to determine these
    - useful for larger Makefile
  - [`Cmake`](http://www.cmake.org/)
    - a cross platform build systems
    - generating makefiles
    - useful for large projects, for builds using lots of libs, and for dealing w/ platform specific compilation issues
    - Andy Danner, [Cmake doc](https://www.cs.swarthmore.edu/~adanner/tips/cmake.php)


## Writing a Makefile




## Example simple C (or C++) makefile




## Example more advanced C Makefile




## Example simple Java makefile





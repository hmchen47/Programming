# Appendix B. Go Programming and Examples


<video src="https://youtu.be/JMN0UewLQXE" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width=180>
  <track src="subtitle" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video><br/>

## B.1 Basic Go Syntax

### B.1.1 Variables

+ Comments
  + `//`: comment out for the line
  + `/*` & `*/`: comment out the block between

+ Six variable types covered
  + `int`: integer
  + `uint`: unsigned integer
  + `bool`: Boolean variable w/ `true` or `false`
  + `float64`: decimal number
  + `byte`: single symbol
  + `string`: contiguous collections if symbols (words)

+ Variable declaration
  + declaration w/ default value
    + Syntax: `var varName varType`
    + example: `var count int`, `var xVal float74`
    + default values: int(0), uint(0), float64(0.0), byte(''), string(""), bool(false)
  + declaration w/ assigned value
    + Syntax: `var varName varType = value`
    + eg. `var count int = 10`, `var index uint = uint(len(array))`, `var symbol byte = 'H'`, `var hello string = "Hello"`, `var statement bool = true`
  + shorthand declaration:
    + Syntax: `varName := value`
    + eg. int: `i := 0`; float64: `x := -2.3`; byte: `char := 'D'`; string: `hello := "Hello"`, bool: `statement := true`
    + using `int` instead of `unit` for integer
  + arithmetic allowed for variable declaration

+ Type conversion
  + operations w/ different types of variables NOT allowed
  + type conversion functions: `int(x)`, `float64(i)`, `uint(j)`
  + integer overflow:
    + unsigned integer (`uint`) about double the max value of `int`
    + max value of `uint`: return value of a variable w/ value (-1)
  + No constant type conversion allowed
  + No integer to boolean type conversion allowed


### B.1.2 Functions

+ Function
  + Syntax: [Ref](https://www.tutorialspoint.com/go/go_functions.htm)

    ```js
    func function_name( [parameter list] ) [return_types]
    {
      body of the function
    }
    ```
  
    + `func`: declaration of a function
    + `function_name`: actual name of the function
    + parameters:
      + a placeholder
      + when a function invoked, pass a value to the parameter
      + value referred to as actual parameter or argument
      + `parameter list`: the type, order, and number of parameter of a function
      + optional
    + return type:
      + return a list of values
      + `return_type`: the list of data types of the values the function returns
      + optional
    + function body: a collection of statements defining what the function does
  + calling a function: simply pass the required parameters along w/ its function name
  + function arguments
    + formal parameters:
      + declared variables that accept the values of the arguments
      + behaving like other local variables inside the function and created upon entry point into the function and destroyed upon exit
    + ways to pass arguments to a function
      + call by value: copy the actual value of an argument into the formal parameters of the function
      + call by reference: 
        + copy the address of an argument into the formal parameter
        + the address used to access the actual argument used in the call
        + changing made to the parameter affect the argument
  + function usage:
    + function as value: created on the fly and used as values
    + function closure: anonymous functions and used in dynamic programming
    + method: special functions w/ a receiver

+ [Demo file for Go Basic Syntax](src/GoP4L/goSyntax.go)


### B.1.3 Conditionals

+ variable re-declaration not allowed

+ variable scope & if statement

+ conditions: `>`, `<`, `>=`, `<=`, `==`, `!=`, `!`(NOT), `&&`(AND), `||`(OR)

+ [Demo for Conditionals](src/GoP4L/conditionals.go)


### B.1.4 Loops

+ Loops
  + Go lang w/o `while` keyword
  + using `for` for while loop
  + Syntax for while loop: `for condition { expression9s)}`
  + eg. `for i < n { i++ }`

+ Sum-first-n-integer problem
  + write a function in Go using a while loop that takes an integer n and return the sum of the first n positive integer
  + pseudocode

    ```js
    SumFirstNIntegers(n)
      sum = 0
      i = 1
      while i = n
        sum = sum + i
        i = i + 1
      return sum
    ```

+ Sum-even-numbers problem
  + Input: an integer n
  + Output: return the sum of all even numbers up to n and possibly include n
  + pseudocode:

    ```js
    SumEven(n)
      sum = 0
      for i from 2 to n step every 2
        sum = sum + i
      return sum
    ```

+ [Demo for Loops](src/GoP4L/loops.go)


### B.1.5 Arrays




### B.1.6 Slices




## B.2 Trivial and Euclid's Theorem of GCD Computation

+ Exercise: `TrivialGCD`
  + pseudocode

    ```js 
    TrivialGCD(a, b)
	    d = 1
	    a = Min2(a, b)
	    for every integer p from 1 to n
	    	if p is a divisor of a and b
	    		d = p
      return d
    ```
  
+ Exercise: `EuclidGCD`
  + Pseudocode

    ```js
    TrivialGCD(a, b)
      d = 1
      a = Min2(a, b)
      for every integer p from 1 to n
        if p is a divisor of a and b
          d = p
      return d
    ```

+ Timing functions
  + import `time`  and `log` packages
  + starting timestamp by `start := time.Now()`
  + measuring duration by `elapsed := time.Since(start)`
  + print the log info for the duration by `log.Print(funcName took %s", elapsed)`

+ [Demo for GCD](src/GoP4L/gcd.go)


## B.3 Eratosthenes Theorem for Finding Primes

+ Array declaration
  + fixed sized
  + Declaration w/ default values
    + assigning default value as variable declaration w/ the predefined size
    + Syntax: `var list [num]varType`
  + eg. `var list [6]float64`

+ Slice declaration
  + variable size array
  + Syntax: `var list []varType`; eg. `var list []int`
  + nothing reserved for the slice and `nil`
  + required to initial length: `list := make([]listType, len)`

+ Array indexing
  + 0-based indexing
  + the size of the array: `len(list)`
  + index from `0` to `len(list) -1`
  + NO negative index allowed
  + No index with `len(list)` allowed, beyond the predefined array size

+ Exercise: `TrivialPrimeFinder`
  + Input: an integer
  + Output: an array w/ boolean values to indicate the element is prime or not
  + pseudocode

    ```js
    TrivialPrimeFinder(n)
      primeArray = an array of false values w/ length of (n+1)
      for an integer p from 2 to n
        if p is prime
          primeArray[p] = true
      return primeArray

    IsPrime(p)
      for an integer k from 2 to square root of p
        if k is a divisor of k
          return false
      return true
    ```

+ Exercise: `SieveOfEratosthenes`
  + Input: an integer n
  + Output: am slice of n+1 booleans primeArray where primeArray[p] is true if p is prime and false otherwise
  + pseudocode

    ```js
    SieveOfEratosthenes(n)
      primeArray = an array of boolean true w/ size of (n+1)
      for an integer p from 2 to square root of n
        if primeArray[p] is true
          primeArray[k] = false w/ k is multiple of p
      return primeArray

    CrossOffMultiples(primeArray, n)
      for an integer k from 2*p to n with step p
        primeArray[k] = false
      return primeArray
    ```

+ [Demo for Primes](src/GoP4L/prime.go)




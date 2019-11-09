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


### B.1.5 Arrays and Slices

+ Arrays
  + a data structure 
  + store a __fixed-size__ sequential collection of elements of the same type
  + contiguous memory locations

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="https://www.tutorialspoint.com/go/go_arrays.htm" ismap target="_blank">
      <img src="https://www.tutorialspoint.com/go/images/arrays.jpg" style="margin: 0.1em;" alt="Illustration of array and its elements" title="Array and its indices" width=350>
    </a>
  </div>

+ Array declaration
  + Syntax(single-dimensional): `var variable_name [SIZE] variable_type`
    + eg, `var balance [10] float32`; `var balance = [5]float32{1000.0, 2.0, 3.4, 7.0, 50.0}`
  + Syntax(multiple-dimensional): `var variable_name [SIZE1][SIZE2]...[SIZEN] variable_type`
    + two-dime array: `var arrayName [ x ][ y ] variable_type`
    + eg, `var threedim [5][10][4]int`;

      ```go
      a = [3][4]int{  
          {0, 1, 2, 3} ,   /*  initializers for row indexed by 0 */
          {4, 5, 6, 7} ,   /*  initializers for row indexed by 1 */
          {8, 9, 10, 11}   /*  initializers for row indexed by 2 */
      }
      ```

  + The number of values between braces `{ }` can not be larger than the number of elements that we declare for the array between square brackets `[ ]`

+ Array element accessing
  + done by placing the index of the element within square brackets after the name of the array
  + eg, `salary := balance[9]`, `val := a[2][3]`


+ Slices declaration
  + able to increase its size dynamically or get a sub-array of its own
  + declaration
    + declaring it as an array without specifying its size
    + (MUST) using `make` function to create a slice
    + eg, 

      ```go
      var numbers []int // a slice of unspecified size
      // numbers == []int{0,0,0,0,0}
      numbers = make([]int,5,5) // a slice of length 5 and capacity
      ```

  + nil slice:
    + a slice declared w/o inputs, then by default, it is initialized as nil
    + zero length & capacity

+ Subslicing
  + obtain subslice w/ given lower and upper bounds
  + Syntax: `[lower-bound:upper-bound]`
  + missing `lower-bound`: from the beginning of the slice to the `upper-bound`
  + missing `upper-bound`: from the `lower-bound` to the end of the slice
  + eg, `numbers := []int{0,1,2,3,4,5,6,7,8}` & `numbers[1:4] = [1 2 3]`, `numbers[5:] = [5 6 7 8]`, `numbers[:4] = [0 1 2 3]`

+ Slice utilities
  + `len()`: the elements presents in the slice; eg, `lena) = 3`
  + `cap()`: the capacity of the slice (i.e., how many elements it can be accommodate); eg, `cap(a) = 5`
  + `append()`: increase the capacity of a slice; eg, `append(numbers, 1)`, `append(numbers, 2, 3, 4)`
  + `copy()`: copy the contents of a source slice to a destination slice; eg, `copy(numbers1,numbers)`

+ Passing and return array w/ function
  + passing argument
    + sized array argument
    + unsized array argument

    ```go
    void myFunction(param [10]int)  // sized

    void myFunction(param []int)    // unsize
    ```

  + return array/slice

    ```go
    void myFunction(...) [10]int {...} // sized

    void myFunction(...) []int {...}   // unsize
    ```

  + Comparison:
    + Array argument: call by value; ie, changing in function won't affect the variable in caller
    + Slice argument: call by reference; ie, changing in function will change on the variable in caller

+ Shortcut w/ for loop
  + `range` keyword iterate over an expression that evaluates to an array, slice, map, string, or channel
  + Syntax: `for idx, val := range list {...}`
    + retrieve the index and value of an element simultaneously
    + `_` if one of them not required


+ [Demo for arrays & slides](src/GoP4L/arrays.go)


### B.1.6 Strings

+ Strings declaration
  + strings are slices
  + declaration example: `var greeting = "Hello world!"`, `str1 := ""`
  + access an element of a string as slice does

+ Access elements of strings
  + same as the slices w `:` for a range
  + Syntax: `str[lower-bound:upper-bound`]
  + missing `upper-bound` & `upper-bound` usage same as slices
  + concatenate strings with `+` while slice using `append` function

+ utilities
  + `len(str)`: method returns the number of bytes contained in the string literal
  + `strings.Join(str, "text")`: concatenating multiple strings
  + `+`: concatenation of two strings
  + `string()`: convert integer/byte to string
  + `strconv`: Package strconv implements conversions to and from string representations of basic data types
    + `strconv.Itoa(i int) string`: equivalent to FormatInt(int64(i), 10)
    + `strconv.Atoi(s string) (int, error)`: equivalent to ParseInt(s, 10, 0), converted to type int.
    + `strconv.ParseFloat(s string, bitSize int) (float64, error)`: convert the string s to a floating-point number with the precision specified by bitSize

+ [Demo for Strings](src/GoP4L/string.go)


### B.1.7 Maps

+ map 
  + mapping unique keys to values
  + key: an object used to retrieve a value at a later date
  + given a key and a value to store the value in a Map object

+ map declaration
  + initializing variable w/ default as `nil`
  + Syntax: `var map_variable map[key_data_type]value_data_type`
  + __MUST__ use `mak()` function to create a map

    ```go
    /* declare a variable, by default map will be nil*/
    var map_variable map[key_data_type]value_data_type

    /* define the map as nil map can not be assigned any value*/
    map_variable = make(map[key_data_type]value_data_type)
    ```

  + Shortcut declaration: `mapVar :=make(map[keyDataType]valueDataType)`

    ```go
    mapVar := make(map[keyDataType]valueDataType)
    ```

+ Access elements
  + using keys to access the value
  + Syntax: `mapVar[key]`

+ For loop
  + able to retrieve key and value simultaneously
  
    ```go
    for key, value := range varMap {
      ...
    }
    ```

  + using `_` (underscore) to substitute unnecessary key or value

+ Existence of key
  + checking existence of a key: 

    ```go
    _, existed = varMap[key]
    ```

  + shortcut for incremental counter

    ```go
    valMap[key]++
    ```

    + if key existed, simply increase one
    + if key not existed, create the key w/ default value (0) and then add one

+ [Demo for maps](src/GoP4L/maps.go)


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


## B.3 Monte Carlo Simulation

### B.3.1 Craps simulation

+ Random number generators
  + `math/rand`: package required to import
  + three mainly used functions
    1. `rand.Int()`: pseudorandom integer
	  2. `rand.Float64()`: pseudorandom decimal in $[0, 1]$
	  3. `rand.Intn()`: pseudorandom integer $[0, n-1] \in \mathbb{N}$
  + `rand.Seed()`: providing seed for PRNG
    + `rand.Seed(1)` called, if the seed not specified
    + good practice: using `rand.Seed(time.Now().UnixNano())` to get internal clock tick as the seed

+ [Demo](src/GoP4L/craps.go)


## B.3.2 A U.S. Presidential Election Simulation

+ Reading & Parsing CSV files
  + `ioutil`: package required for IO
  + `strings`: package required to process strings
  + `ioutil.ReadFile(string)`: open & read text file
  + `strings.Split()`: separate data with provided deliminator, such as `"\n"`, `","`
  + convert split items from string to designated data type, such as `strconv.ParseFloat()`, `uint()`

+ Adding noise for Margin of Error
  + generating a value with normal distribution 
  + obtaining 95 percentile range by dividing the value with 2 (2 standard deviation)
  + applying margin of error to obtain the adjustment

+ Demo files
  + [Monte Carlo Simulation](src/GoP4L/election.go)
  + [IO and Parsing](src/GoP4L/io.go)



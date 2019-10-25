# A Short Introduction to Programming in Go

## A.1 Getting Started in Go (Mac OS)

<video src="https://youtu.be/I5XCvYs0tGo" preload="none" loop="loop" c0.5 Getting Started in Go (MacOS)ontrols="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width=180>
  <track src="subtitle" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video><br/>

+ Installation Go
  1. download Go from official website
  2. install Go by following the instruction
  3. expose the PATH for `go` if required
  4. create `go` directory and sub-folders: `src`, `pkg`, and `bin`

+ First program: print 'Hello World!' with filename `hello.go`

  ```go
  package main

  import "fmt"

  func main() {
    fmt.Println("Hello World!")
  }
  ```

  + `package main`: what you see below is going to include something runnable
  + `import "fmt"`: read from and write to files/console
  + [Demo file - Hello, World!](src/GoIntro/hello.go)

+ Build & Run
  + Compile
    1. `go build hello.go`
    2. debug if required
  + Scripting way: `go run hello.go`


## A.2 Getting Started in Go (Windows)

<video src="https://youtu.be/p3FjbqT1cko" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width=180>
  <track src="subtitle" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video><br/>

+ Installation
  1. download from official website
  2. install as instruction

+ Build & Run program
  + Open command prompt
  + navigate to the folder with the go file
  + build & run go program as described in Mac OX/Linux


## A.3 Basics of Variables in Go

<video src="https://youtu.be/3I_J1HtLmNw" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width=180>
  <track src="subtitle" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video><br/>

+ [The Go Playground](https://play.golang.org/): online Go editor

+ Variable declaration
  + variable types: int, uint, float64, symbol, string, bool
  + formal declaration
    + format: var varName varType = value
    + e.g., `var x float64 = -3.4`, `var k int = 3`, `var chr symbol = 'D'`, `var str string = "Hello"`, `var statement bool = true`
  + declaration w/o value
    + default value: int $\to$ 0, float64 $\to$ 0.0, symbol $\to$ 0, bool $\to$ flase
    + e.g., `var x int`, `var y float64`
  + multiple variable declaration

    ```go
    var (
      x int = 1
      y float64 = -3.4
      z string = "Yes"
    )
    var int i, j, k int = 1, -2, 3
  ```

  + shortcut declaration w/ `:=`: `i := 1`; `x = -4.5`, `sym := 'D'`
  + declaration w/ standard arithmetic: `x := 4.2 + 3.5`
  + __NO re-declaration__ allowed
  + string concatenation with `+`: `str1+str2`

+ Type conversion
  + arithmetic type mismatch: `int(a) + float64(b)`
  + type casting; `float64(a)`, `int(y)`
  + __No constant__ type casting allowed
  + __No boolean__ type casting from integer allowed
  + type casting with negative integer to unsigned integer
    + e.g. `i := -1`, `var u unit = unit(i)` $\to$ u = 18446744073709551615 (the value depends on the computer used)
    + integer overflow: 9223372036854775807 + 1 $\to$ -9223372036854775808

+ [Demo file for Variable Declaration](src/GoIntro/variables.go)


## A.4 Functions and Conditionals in Go

#### A.4.1 Functions

<video src="https://youtu.be/5JBiiQoLxuA" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width=180>
  <track src="subtitle" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video><br/>

+ Function Syntax

  ```go
  func square(x int) int {
    return x*x
  }
  ```

  + `func`: function keyword
  + `square`: function name
  + `x`: parameter
  + `int` within (): type of the input parameter
  + `int` after (): the type pf the value returned by the function
  + `return`: keyword for function return value(s)
  + `{}`: used for grouping related statements

+ Functions: paragraphs of programming
  + As with paragraphs, function should be well written
    1. each one should cover one (short) idea
    2. function name + parameters $\approx$ "topic sentence"
    3. function should 'lie in nicely" with the rest of your program
  + your program will typically consist of a long sequence of cuntions that call each other
  + __modularity__: the principle
  + __top-down design:__ starting w/ large task and breaking them into small pieces

+ Top-Down programming in `FrequentWords`

  ```go
  FrequentWords(Text, k)
    FrequentPatterns <- an empty list
    c <- empty array of length |Text| - k
    for i <- 0 to |Text| - k
      Pattern <- substring(Text, i, k)
      c[i] <- Count(Text, Pattern)
    macCount <- Max(a)
    for i <- o to |Text| - k
      if a[i] = macCount
        add Substring(Text, i, k) to FrequentPatterns
    FrequentPatterns <- RemoveDuplicates(FrequentPatterns)
    return FrequentPatterns
  ```

  + `Substring`: take a "substring" of Text starting at position $i$ of length $k$
  + `Count`: "count" number of matches of Pattern in Text
  + `Max`: take maximum value  in an array a
  + `RemoveDuplicates`: remove duplicates from list FrequentPatterns

+ Focus on Style: Variable/Function Names
  + use descriptive names: `numOfPeople` is better tha `n`
  + variable names are case sensitive:
    + `n` is different than `N`
    + `numOfPeople` is not the same as `numOfpeople`
  + use single letter (i, j, k) for integer that don't last log in your program
  + use __camelCases__ to connect words together
  + good function names usually involve __verbs__: `PrintFullName`, `EncodeSingleRead`, `WriteCounts`, `ListBuckets`
  + start __variable__ names with _lowercase_ letter
  + start __function__ names with _uppercase_ letter (exception latter)
  + don't use abbreviations (Bad: nerr, ptf_name, etc.)

+ [Demo file for Functions](src/GoIntro/function.go)


#### A.4.2 Conditionals

+ Computing GCD
  + GCD problem: compute the greatest common divisor of two integers
    + Input: two integer `a` and `b`
    + Output: the greatest common divisor of `a` and `b`
  + Exercise: design an algorithm in pseudocode solving this problem
 
+ A simple algorithm computing GCD
  +Idea: it isn't possible for the GCD of a and b to be larger than `min(a, b)`, so we can try every number less than `min(a, b)` and take the greatest common divisor
  + pseudocode

    ```go
    GCD(a, b)
      gcd = 1
      m = min(a, b)
      for every number p <= m
        if a/p and b/p are both integers
          gcd = p
      return gcd
    ```

+ A quicker algorithm computing GCD
  + Idea: start with `min(a, b)` and move downward, returning the first common factor of a and b that we find
  + pseudocode

    ```go
    AnotherGCD(a, b)
      m = min(a, b)
      for every number p from m to 1 (decreasing)
        if a/p and b/p are both integers
          return p
    ```

+ The world's first nontrivial algorithm (~300 BC): Euclid
  + Theorem: if $a > b$, then $gcs(a, b) = gcd(a-b, b)$
  + Example: $gcd(378, 273) = gcd(105, 273) = gcd(105, 168) = gcd(107, 63) = gcd(42, 21) = gcd(21, 21) = 21$
  + Exercise: implement Euclid's algorithm in pseudocode

+ Recall: Recursive Gauss

  ```go
  RecursiveGauss(n)
    if n = 0
      return 0
    else
    return n + RecursiveGauss(n-1)
  ```

+ Recursive Euclid's algorithm

  ```go
  RecursiveEuclid(a, b)
    if a = b
      return a
    else if a > b
      return RecursiveEuclid(a-b, b)
    else
      return RecursiveEuclid(b-a, a)
  ```

+ Be aware of scope of variables

+ Additional conditions
  + Boolean Operator: `>`, `<`, `>=`, `<=`, `==`, `!=`, `!`(NOT), `&&`(AND), `||`(OR)
  + Boolean expressions to evaluate to true or false; eg.
    + `a > 10 * b + c`: depend on value of a
    + `10 == 10`: true
    + `square(10) < 101 - 1 + 2`: true
    + `!(x*y < 33)`: inverse of `(x*y < 33)`

+ Order of operator precedence (left to right in expression w/ same level)

  | Precedence |  Operator |
  |------------|:---------:|
  |   5        |    * &nbsp;&nbsp; / &nbsp;&nbsp; % &nbsp;&nbsp; << &nbsp;&nbsp; >> &nbsp;&nbsp; & &nbsp;&nbsp; &^ |
  |   4        |    + &nbsp;&nbsp; - &nbsp;&nbsp; \| &nbsp;&nbsp; ^ |
  |   3        |    == &nbsp;&nbsp; != &nbsp;&nbsp; < &nbsp;&nbsp; <= &nbsp;&nbsp; > &nbsp;&nbsp; >= |
  |   2        |    && |
  |   1        |    \|\| |

  + Example:

  \[\underbrace{\underbrace{\underbrace{\underbrace{\underbrace{2*a}_{5} + b}_{4} \; !=\; 3}_{3}}_{2} \;\&\&\; \underbrace{\underbrace{\underbrace{\underbrace{a*c}_{5} - \underbrace{3/z}_{5}}_{4} < -5\;}_{3}}_{2}}_{1} ||\; \underbrace{\underbrace{\underbrace{\underbrace{c + \underbrace{a/2}_{5}}_{4} >= 15}_{3}}_{2}}_{1} \]

  + like in math, use parentheses to force a different order

+ True/False Quiz: `a = 10` & `b = 50`
  1. `a > 10 && b > 20`
  2. `a==10 && b < 100 && a*b > 1000`
  3. `a > 20 || b < 51 || b-a*b > 0`
  4. `a=10 && b=50`
  5. `a==10 && b >= 100 || b == 50`
  6. `b==50 || a==10 && b >= 100`
  7. `a>5 && b<20 || a==0 && b==0`
  8. `a>5 || b>20 && a==0 || b==0`
  9. `a>5 || (b>20 &7 a==0) || b==0`

  Ans: 1. false, 2. false, 3. true, 4. syntax error, 5. true, 6. true, 7. false, 8. true, 9. true

+ Nested if statement & switch operator
  + nested if statement

    ```go
    if logicalExp1 {
      statements2
    } else if logicalExp2 {
      statements2
    } else if logicalExp3 {
      statements3
    }
    ...
    } else {
      statementn
    }
    ```
  + switch operator used as in C

    ```go
    switch key {
    case key1:
      expressions
    case key2:
      expressions
    ...
    default:
      expressions
    }

+ [Demo file for conditionals]()


## A.5 A Short Lesson on Debugging

<video src="https://youtu.be/rKFU6BgX7gA" preload="none" loop="loop" controls="controls" style="margin-left: 2em;" muted="" poster="http://www.multipelife.com/wp-content/uploads/2016/08/video-converter-software.png" width=180>
  <track src="subtitle" kind="captions" srclang="en" label="English" default>
  Your browser does not support the HTML5 video element.
</video><br/>



## A.6 Loops in Go




## A.7 Nested Loops in Go




## A.8 Timing Functions in Go




## A.9 Arrays in Go




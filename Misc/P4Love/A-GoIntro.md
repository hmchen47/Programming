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


## A.4 Functions and Conditionals in Go




## A.5 A Short Lesson on Debugging




## A.6 Loops in Go




## A.7 Nested Loops in Go




## A.8 Timing Functions in Go




## A.9 Arrays in Go




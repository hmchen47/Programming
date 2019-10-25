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



## A.3 Basics of Variables in Go




## A.4 Functions and Conditionals in Go




## A.5 A Short Lesson on Debugging




## A.6 Loops in Go




## A.7 Nested Loops in Go




## A.8 Timing Functions in Go




## A.9 Arrays in Go




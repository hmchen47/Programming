package main

// VARIABLES

import (
	"fmt"
)

/*
Common types in Go
int: positive and negative integers
unit: non-negative integers only
float64: decimal number
byte: symbol/character
string: contiguous sequence of symbols
bool: boolean variable, true or false
*/

func main() {
	// Go won't be able to read a = 28
	// variable declaration formate: "var variableName variableType = value"
	var a int = 28
	fmt.Println(a)

	// change the value of a
	a = a + 14
	fmt.Println(a) // result: 42
	fmt.Println()

	// declaraction examples
	var x float64 = -2.6
	var sym byte = 'C'          // using single quotes to indicate a symbol
	var hello string = "Hello!" // using double quotes to indicate a string
	var statement bool = true

	fmt.Println("variable declaration w/ value:")
	fmt.Println(x, sym, hello, statement) // result: -2.6 67 Hello! true
	fmt.Println()

	// omitting values of variables
	var y float64       // default of 0.0
	var z int           // default of 0
	var sym1 byte       // default of 0 (another number ...)
	var hello1 string   // default of ""
	var statement1 bool // default of false

	fmt.Println("variable declaration w/o assigning value:")
	fmt.Println(y, z, sym1, hello1, statement1) // result: 0 0 0  false
	fmt.Println()

	// multiple variable declaration
	var (
		i     int     = -1
		world string  = "No"
		k     float64 = 45.67
	)

	fmt.Println("Multiple variable declaration:")
	fmt.Println(i, world, k)
	fmt.Println()

	// multiple variable declaration w/ same type
	var m, n, p int = 34, -45, 56

	fmt.Println("Multiple variable declaration w/ same type:")
	fmt.Println(m, n, p)
	fmt.Println()

	// shortcut declaration s ... done w/ :=
	x2 := -32   // same as 'var x2 int = -32'
	y2 := 4     // same as 'var y2 int = 4'
	sym2 := 'D' // same as 'var sym2 symbol = 'D''

	fmt.Println("Shortcut declaration w/ :=")
	fmt.Println(x2, y2, sym2)
	fmt.Println()

	// declaration w/ standard arithmetic
	cat := 2 + 30
	fmt.Println("Declaration w/ standard arithemetic:", cat, "\n")

	// Go not allow redeclaring a variable
	/*
		cat := 3
		fmt.Println(cat, "\n")
	*/

	// arithmetic w/ variables
	a3 := 3.2
	b3 := -2.6

	a3 = 2*b3 + 6*a3
	fmt.Println("Variable arithmetic:", a, "\n")

}

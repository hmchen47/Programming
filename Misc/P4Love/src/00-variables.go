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
	fmt.Println(a)

	// declaraction examples
	var x float64 = -2.6
	var sym byte = 'C'          // using single quotes to indicate a symbol
	var hello string = "Hello!" // using double quotes to indicate a string
	var statement bool = true

	fmt.Println(x, sym, hello, statement)

}

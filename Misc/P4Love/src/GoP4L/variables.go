package main

import (
	"fmt"
)

// Go won't read this line

/*
Everything here won't be read either (multi-line comment)

Today: we'll cover four variable types

int: integer
uint: unsigned integer
bool: Boolean variable w/ `true` or `false`
float64: decimal number

Next Time:
byte: single symbol
string: contiguous collections if symbols (words)
*/

func main() {
	fmt.Println("\n\nLet's get started!")

	// decalartion w/ default value
	var j1 int // j is an integer variable
	var x1 float64
	var u1 uint
	var y1 string
	var sym1 byte
	var statement1 bool

	fmt.Println("\nDecalartion w/ default value: (int)", j1, "(float64)", x1, "(uint)", u1, "(string)", y1, "(byte)", sym1, "(bool)", statement1)

	// decalartion w/ assigned value
	var j2 int = 14
	var x2 float64 = -2.3
	var u2 uint = 15
	var y2 string = "Hi "
	var sym2 byte = 'H' // print symbol value than the character
	var statement2 bool = true

	fmt.Println("\nDecalartion w/ default value: (int)", j2, "(float64)", x2, "(uint)", u2, "(string)", y2, "(byte)", sym2, "(bool)", statement2)

	// decalartion w/ assigned value
	j3 := 17
	x3 := -4.5
	u3 := 15 // automatically as an integer
	y3 := "Good"
	sym3 := 'H' // print symbol value than the character
	statement3 := true

	fmt.Println("\nShothand decalartion: (int)", j3, "(float64)", x3, "(no uint but int)", u3, "(string)", y3, "(byte)", sym3, "(bool)", statement3)

	// do arithmetic on numeric variable
	fmt.Println("\narithmetic operation on variables:")
	fmt.Println("integer arithmetic:", j1+j3*j2*u3)
	fmt.Println("floating point arithmetic:", 2*x1-4.5)
	fmt.Println("concate string w/ '+':", y2+y3)
	fmt.Println("int division (truncated):", j3/j2)

	// type conversion
	fmt.Println("int to float64:", float64(j3)*x2)

	// int cannot convert to bool
	// var ok int = 1
	// fmt.Println("bool & int:", bool(ok))
	fmt.Println("\nint to bool conversion not allowed!")

	var p int = -1
	fmt.Println("\n    -1 to uint:", uint(p))
	var s int = -22197
	fmt.Println("-22197 to uint:", uint(s))

	// functions
	fmt.Println("\nVarious function usage:")
	n := SumTwoInts(j1, j2)
	fmt.Println("SumTwoInts:", n)

	a1, a2 := DoubleAndDuplicate(x2)
	fmt.Println("DoubleAnDuplicate:", a1, a2)

	m := 10
	fmt.Println("call by value:", m, AddOne(m), m)
}

// examples of functions
// SumTwoInts takes 2 integers and returns their sum
func SumTwoInts(a int, b int) int {
	return a + b
}

func DoubleAndDuplicate(x float64) (float64, float64) {
	return 2.0 * x, 2.0 * x
}

func Pi() float64 { // no input
	return 3.14159
}

// function w/o return anything
func printHi() {
	fmt.Println("Hi")
}

// called by value
func AddOne(m int) int {
	m++
	return m
}

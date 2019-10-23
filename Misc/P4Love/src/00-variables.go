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

	fmt.Println("\nVariable declaration...\n")
	// Go won't be able to read a = 28
	// variable declaration formate: "var variableName variableType = value"
	var a int = 28
	fmt.Println("formal declaration, var varName varType = value")
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

	fmt.Println("variable declaration w/ value, eg. 'var x float64 = -2.3':")
	fmt.Println(x, sym, hello, statement) // result: -2.6 67 Hello! true
	fmt.Println()

	// omitting values of variables
	var y float64       // default of 0.0
	var z int           // default of 0
	var sym1 byte       // default of 0 (another number ...)
	var hello1 string   // default of ""
	var statement1 bool // default of false

	fmt.Println("variable declaration w/o assigning value, eg. 'var y symbol':")
	fmt.Println(y, z, sym1, hello1, statement1) // result: 0 0 0  false
	fmt.Println()

	// multiple variable declaration
	var (
		i     int     = -1
		world string  = "No"
		k     float64 = 45.67
	)

	fmt.Println("Multiple variable declaration, eg. 'var ( i int = -1 <cr> str string = \"No\"'):")
	fmt.Println(i, world, k)
	fmt.Println()

	// multiple variable declaration w/ same type
	var m, n, p int = 34, -45, 56

	fmt.Println("Multiple variable declaration w/ same type, eg. 'var int a, b int = 12, -23':", m, n, p, "\n")

	// shortcut declarations ... done w/ :=
	x2 := -32   // same as 'var x2 int = -32'
	y2 := 4     // same as 'var y2 int = 4'
	sym2 := 'D' // same as 'var sym2 symbol = 'D''eg. 2147483647 + 1 in demo becomes -2147483648 but failed in ver 1.10.4

	fmt.Println("Shortcut declaration w/ ':=', eg. 'x := 3':", x2, y2, sym2, "\n")

	// declaration w/ standard arithmetic
	cat := 2 + 30
	fmt.Println("Declaration w/ standard arithemetic:", cat, "\n")

	// Go not allow redeclaring a variable
	/*
		cat := 3
		fmt.Println(cat, "\n")
	*/
	fmt.Println("Re-declaring not allowed \n")

	// arithmetic w/ variables
	a3 := 3.2
	b3 := -2.6

	a3 = 2*b3 + 6*a3
	fmt.Println("Variable arithmetic, eg. x = 3*a + 6*b:", a3, "\n")

	// string concatenation
	a4 := "Hello"
	b4 := "World"

	fmt.Println("String concatenation w/ '+', eg. str1 + str2:", a4, b4, a4+b4, "\n")

	// type mismatch in arithmetic
	a5 := 3.2
	b5 := 2
	fmt.Println("Type casting, eg. float64(<int>):", a5+float64(b5), "\n")

	// Type conversion
	fmt.Print("\n\nType cating ...\n\n")

	// type casting from float64 to int: discard decimal part
	p1 := 3.4
	q1 := -5.6
	fmt.Println("Type cast from float64 to int, eg., int(4.5):", p1, "->", int(p1), "\t", q1, "->", int(q1), "\n")

	a6 := 7
	b6 := -4
	fmt.Println("Type cast from int to float64:", a6, "->", float64(a6), "\t", b6, "->", float64(b6), "\n")

	// integer division
	fmt.Println("Integer division:", a6, "/", b6, "=", a6/b6)
	fmt.Println("floating result:", float64(a6)/float64(b6), "\n")

	// type casting a constant
	// var g1 int = int(3.4)
	var g2 int = int(p1)
	fmt.Println("Type casting w/ constant, eg. 'var g int = int(3.2)': not allowed")
	fmt.Println("Type casting w/ a variable in declaration, eg. var g int = int(x):", p1, "->", g2, "\n")

	// type casting from int to bool, not allowed
	// p2 := 1
	// var q2 bool = bool(p2)
	fmt.Println("Type casting from int to bool: not allowed\n")

	// type casting from uint to int w/ negative value
	var u1 int = -1
	var u2 uint = uint(u1)
	fmt.Println("Type casting from int to uint:", u1, "->", u2, "\n")

	// integer overflow
	var u3 int = (18446744073709551615) / 2
	fmt.Println("Integer overflow (depend on the computer used):", u3, "+ 1  ->  ", u3+1, "\n")
}

package main

import (
	"fmt"
)

func main() {
	fmt.Println("\nDemo for conditionals:")
}

func SimpleFunction(x, y int) int {
	if x == y { // ==: testing whether two parameters are equal
		return 0
	} else if x > y {
		return 1
	} else { // infer x < y
		return -1
	}
}

func SameSign(x, y int) bool {
	if x*y >= 0 {
		return true
	} else {
		return false
	}
}

func PositiveDifference(a, b int) int {

	/* variable scope issue
	if a == b {
		return 0
	} else if a > b {
		var c in t= a-b // c only exist within the {expression(s)} block
	} else {
		c = b-a
	}
	return c
	*/

	var c int
	if a == b {
		c = 0
	} else if a > b {
		c = a - b
	} else {
		c = b - a
	}
	return c
}

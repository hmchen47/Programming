package main

import (
	"fmt"
)

func main() {
	fmt.Println("Factorial w/ array")

	var fact [21]uint
	fact[0] = 1

	for idx := 1; idx < len(fact); idx++ {
		fact[idx] = fact[idx-1] * uint(idx)
	}

	// print the result
	fmt.Println(fact)
}

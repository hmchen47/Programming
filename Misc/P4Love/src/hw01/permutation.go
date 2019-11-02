package main

import (
	"fmt"
)

// Exercise Part1

func main() {
	fmt.Println("Permutation:")
	fmt.Println("   5, 3 ->", Permutation(5, 3))
	fmt.Println("  10, 5 ->", Permutation(10, 5))
	fmt.Println("  15, 5 ->", Permutation(15, 5))
	fmt.Println("  20, 10 ->", Permutation(20, 10))
}

func Permutation(n, k int) uint {
	return Factorial(n) / Factorial(n-k)
}

func Factorial(n int) uint {
	if n == 1 {
		return 1
	} else {
		return uint(n) * Factorial(n-1)
	}
}

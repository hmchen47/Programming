package main

import (
	"fmt"
)

// Exercise Part1

func main() {
	fmt.Println("Combination:")
	fmt.Println("   5, 3 ->", Combination(5, 3))
	fmt.Println("  10, 5 ->", Combination(10, 5))
	fmt.Println("  15, 5 ->", Combination(15, 5))
	fmt.Println("  20, 10 ->", Combination(20, 10))
}

func Combination(n, k int) uint {
	return (Factorial(n) / Factorial(n-k)) / Factorial(k)
}

func Factorial(n int) uint {
	if n == 1 {
		return 1
	} else {
		return uint(n) * Factorial(n-1)
	}
}

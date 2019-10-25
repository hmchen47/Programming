package main

import (
	"fmt"
)

// # of ways to arrange n objects is n * (n-1) * ... * 2 * 1 = n!

func Factorial(n int) int {
	if n == 1 {
		return 1
	} else if n > 1 {
		return n * Factorial(n-1)
	}
	return -1
}

// # of ways to arrange k out of n objects, or permutation (k <= n):
//	n * (n-1) * ... * (n-k+1) = n! / (n-k)!

// # of ways to choose k of the n objects, or combination:
//	n!/((n-k)!k! )

// exercise: write and implement functions Perm(n, k) and Comb(n, k) computing these

func Perm(n, k int) int {
	return Factorial(n) / Factorial(n-k)
}

func Comb(n, k int) int {
	return Factorial(n) / (Factorial(n-k) * Factorial(k))
	// return Perm(n, k) / Factorial(k)
}

func main() {
	// fmt.Println(Comb(101, 2))
	// 101~/(99! * 2!) = (101 * 100 * 99!)/(99! * 2!) = 101 * 100/2 = 5050

	// trying Factorial itself due to the error msg:
	// 	runtime error: integer divide by zero
	fmt.Println(Factorial(2))
	fmt.Println(Factorial(99))

	// using loop to test Factorial due to Factorial(99) =
	for i := 1; i < 90; i++ {
		fmt.Println("Factorial of", i, "is", Factorial(i))
	}
}

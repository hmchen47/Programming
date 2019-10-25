package main

// Theorem: if a > b, the gcd(a, b) = gcd(a-b, b)

import (
	"fmt"
)

// recursive implementation

func Gcd(a, b int) int {
	if a > b {
		return Gcd(a-b, b)
	} else if a < b {
		return Gcd(b-1, a)
	} else { // base case a==b
		return a // or b
	}
}

/*
non-recursive GCD function
Another Gcd(a, b)
	while a != b
		if a > b
			a = a - b
		else
			b = b - a
	return a // or b
*/

// In Go, use the keyword "for" to mean "while"

func AnotherGcd(a, b uint) uint {
	for a != b {
		if a > b {
			a = a - b
		} else {
			b = b - a
		}
	}
	return a
}

/*
Gauss(n): computer the sum of the first n positive integer
	sum = 0
	i = 1
	while i <= n
		sum = sum + i
		i+=
	return sum
*/

func Gauss(n int) int {
	if n == 0 {
		// display error msg and exit
		panic("Input to Gauss() must be positive")
	}
	var sum int = 0
	i := 1
	for i <= n {
		sum = sum + i
		i++
	}
	// variable i still exists here
	return sum
}

/*
AnotherGauss(n)
	sum = 0
	for 1 = 1 to n
		sum = sum + i
	return sum
*/

func AnotherGauss(n int) int {
	sum := 0
	for i := 1; i <= n; i++ {
		// sum = sum + i
		sum += i
	}
	// variable i no longer exist here
	return sum
}

/*
Fibonacci(n)
	a, b, c = 1, 1, 1
	for i = 3 to n
		c = a + b
		a = b
		b = c
*/

func main() {
	fmt.Println("Non-recursive GCD: ", AnotherGcd(9, 6))
	fmt.Println("Gauss function:", Gauss(100))
	fmt.Println("Another Gauss:", AnotherGauss(100))
}

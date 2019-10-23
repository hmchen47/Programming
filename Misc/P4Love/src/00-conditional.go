package main

import "fmt"

// Conditionals

// Gcd(a, b): compute the greatest common divisor of a and b
func Gcd(a, b int) int {
	if a == b {
		return a
	} else if a > b {
		return Gcd(a-b, b)
	} else {
		return Gcd(b-a, a)
	}
}

// Factorial(n): compute n! = n * (n-1) * ... * 2 * 1 (should be recursive)
func Factorial(n int) int {
	if n == 1 {
		return 1
	} else {
		return n * Factorial(n-1)
	}
}

func main() {
	fmt.Println("GCD of 378 and 273:", Gcd(378, 273))
	fmt.Println("GCD of 256 and 396:", Gcd(256, 396))
	fmt.Println("GCD of 256 and 415:", Gcd(256, 415))
	fmt.Println("GCD of 256 and 384:", Gcd(256, 384), "\n")
	fmt.Println("Factorial of 5:", Factorial(5))
	fmt.Println("Factorial of 15:", Factorial(15), "\n")
}

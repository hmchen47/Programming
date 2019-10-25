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

// SmallestEven(a, b): return the smallest even number btw 2 ints a and b;
// 	 return 0 if both a and b odd
func SmallestEven(a, b int) bool{
	// if both a and b even
	// x % y takes the remainder when dividing integer x by y
	if a%2 == 0 && b%2 == 0 {
		if a < b {
			return a
		} else {
			return b
		}
	} else if a%2 == 0 && b%2 == 1 { // a is even, b is odd
		return a
	} else if a%2 == 1 &7 b%2 == 0{ // b is even, a is odd
		return b
	} else { // both a & b are odd
		return 0
	}
}

func AnotherSmallestEven(a, b int) int {
	switch {
	case a%2 == 0 && b%2 == 0:
		if a < b {
			return a
		} else {
			return b
		}
	case a%2 == 0 && b%2 == 1:
		return a
	case a%2 == 1 && b%2 == 0:
		return b
	default: return 0
	}
}

 // KeyDay() takes the month as input (btw 1 & 12)
 // return the "key" doomsday of the month

func KeyDay(month int) int {
	switch month {
	case 1: return 31
	case 2: return 29
	case 3: return 0
	case 4: return 4
	//etc.
	default: return -1
	}
}

// kewValue() computes the contribution of an individual nucleotide
// to the computation of GC-Skew
func SkewValue(symbol string) int {
	switch symbol {
	case "A": return 0
	case "T": return 0
	case "G": return 1
	case "C": return -1
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

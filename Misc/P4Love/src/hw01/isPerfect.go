package main

import "fmt"

func main() {
	fmt.Println("   9 is a perfect number:", IsPerfect(9))
	fmt.Println("   6 is a perfect number:", IsPerfect(6))
	fmt.Println("  28 is a perfect number:", IsPerfect(28))
	fmt.Println(" 496 is a perfect number:", IsPerfect(496))
	fmt.Println("  18 is a perfect number:", IsPerfect(18))
	fmt.Println("8128 is a perfect number:", IsPerfect(8128))
}

func IsPerfect(n int) bool {
	total := 0
	for i := 1; i < n; i++ {
		if IsDivisible(n, i) {
			total = total + i
		}
	}
	if total == n {
		return true
	} else {
		return false
	}
}

func IsDivisible(dividend, divisor int) bool {
	quotient := dividend / divisor
	return (dividend == divisor*quotient)
}

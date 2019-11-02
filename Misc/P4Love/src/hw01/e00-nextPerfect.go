package main

import "fmt"

func main() {
	fmt.Println("next perfect number of    9:", NextPerfectNumber(9))
	fmt.Println("next perfect number of    6:", NextPerfectNumber(6))
	fmt.Println("next perfect number of   28:", NextPerfectNumber(28))
	fmt.Println("next perfect number of  496:", NextPerfectNumber(496))
	fmt.Println("next perfect number of   18:", NextPerfectNumber(18))
	fmt.Println("next perfect number of 8128:", NextPerfectNumber(8128))
}

func NextPerfectNumber(n int) int {
	nextNum := n + 1
	for ok := true; ok; ok = !IsPerfect(nextNum) {
		nextNum++
	}

	return nextNum
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

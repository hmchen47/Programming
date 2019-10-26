package main

import (
	"log"
	"time"
)

func BasicGcd(a, b int) int {
	gcd := 1
	// range over all numbers less than or equal to min(a, b), and update gcd if we
	// find a divisor
	for p := 1; p <= Min(a, b); p++ {
		if a%p == 0 && b%p == 0 {
			// p is a common divisor
			gcd = p
		}
	}
	return gcd
}

func Min(a, b int) int {
	if a > b {
		return b
	} else {
		return a
	}
}

func EuclidGcd(a, b int) int {
	if a == b {
		return a
	} else if a < b {
		return EuclidGcd(b-a, a)
	} else { // a > b
		return EuclidGcd(a-b, b)
	}
}

func main() {
	a := 1298134236
	b := 142762444

	// start the stopwatch
	start1 := time.Now()
	BasicGcd(a, b) // storing result slows us down
	elapsed1 := time.Since(start1)
	log.Printf("BasicGcd took %s", elapsed1)

	start2 := time.Now()
	BasicGcd(a, b) // storing result slows us down
	elapsed2 := time.Since(start2)
	log.Printf("EuclidGcd took %s", elapsed2)
}

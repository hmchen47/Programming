package main

import (
	"log"
	"time"
)

func main() {
	x := 378202875
	y := 273147834

	start1 := time.Now()
	d1 := TrivialGCD(x, y)
	elapsed1 := time.Since(start1)
	log.Printf("TrivialGCD took %s to get %d\n", elapsed1, d1)

	start2 := time.Now()
	d2 := TrivialGCD(x, y)
	elapsed2 := time.Since(start2)
	log.Printf("EculidGCD took %s to get %d\n", elapsed2, d2)

}

/*
TrivialGCD(a, b)
	d <- 1
	a <- Min2(a, b)
	for every integer p from 1 to n
		if p is a divisor of a and b
			d <- p
	return d
*/

func TrivialGCD(a, b int) int {
	d := 1
	m := Min2(a, b)
	for p := 1; p <= m; p++ {
		if a%p == 0 && b%p == 0 {
			d = p
		}
	}
	return d
}

/*
EuclidGCD(a, b)
	while a not equal to b
		if a > b
			a = a-b
		else
			b = b - a
	return a
*/

func EuclidGCD(a, b int) int {
	for a != b {
		if a > b {
			a = a - b
		} else {
			b = b - a
		}
	}
	return a
}

func Min2(a, b int) int {
	if a > b {
		return b
	} else {
		return a
	}
}

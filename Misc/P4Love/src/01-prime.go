package main

import (
	"fmt"
	"log"
	"math"
	"time"
)

func main() {
	fmt.Println("\nPrimes and arrays...")

	// arrays in Go have a fixed, constant size.
	var list [6]int // give 6 default values
	fmt.Println("\nArray w/ default values:", list)

	// array indexing: from 0 to len(list)-1
	list[0] = -8
	i := 3
	list[2*i-4] = 17
	list[len(list)-1] = 43
	fmt.Println("Array values w/ indexing:", list)

	fmt.Println("\n\nFinding Primes ...")
	fmt.Println("\nTrivialPrimeFinder(12):\n  ", TrivialPrimeFinder(12))
	fmt.Println("\nSieveOfEratosthenes(12):\n  ", SieveOfEratosthenes(12))

	fmt.Println("\nPrimes finding algorithm time measurements...")
	n := 1000000
	start1 := time.Now()
	TrivialPrimeFinder(n)
	elapsed1 := time.Since(start1)
	log.Printf("TrivialPrimeFinder took %s\n", elapsed1)

	start2 := time.Now()
	SieveOfEratosthenes(n)
	elapsed2 := time.Since(start2)
	log.Printf("SieveOfEratosthenes took %s\n", elapsed2)

}

func TrivialPrimeFinder(n int) []bool {
	// var primeArray []bool
	primeArray := make([]bool, n+1)

	for p := 2; p <= n; p++ {
		if IsPrime(p) == true {
			primeArray[p] = true
		}
	}
	return primeArray
}

func IsPrime(p int) bool {
	for k := 2; float64(k) <= math.Sqrt(float64(p)); k++ {
		if p%k == 0 {
			return false
		}
	}
	return true
}

func SieveOfEratosthenes(n int) []bool {
	primeArray := make([]bool, n+1)

	// set all elements true
	for k := 2; k <= n; k++ {
		primeArray[k] = true
	}

	// range over primeArray and cross of multiples of first prime
	for p := 2; float64(p) <= math.Sqrt(float64(n)); p++ {
		if primeArray[p] == true {
			primeArray = CrossOffMultiples(primeArray, p)
		}
	}
	return primeArray
}

func CrossOffMultiples(primeArray []bool, p int) []bool {
	for k := 2 * p; k < len(primeArray); k += p {
		primeArray[k] = false
	}
	return primeArray
}

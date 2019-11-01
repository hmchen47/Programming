package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println("\nMore on arrays/slices...")

	// comparison of changing array and slice values in function
	a := make([]int, 3)
	var b [3]int
	fmt.Println("\ndeclare w/ 'var := make([]varDataType, size)':", a)
	fmt.Println("declare w/ 'var [size]varDataType':", b)
	c := [3]int{3, -2, 1}
	fmt.Println("declae array w/ assigned values 'var := [size]varDataType{val1, val2, ..., vlaN}':", c)

	ChangeFirst1Slice(a)
	ChangeFirst1Array(b)
	fmt.Println("\nComparison of changeing element values in functions:")
	fmt.Println("  ChangeFirst1Slice:", a) // called by reference
	fmt.Println("  ChangeFirst1Array:", b) // called by value

	a = append(a, 5) // add an element to right side of the slice
	fmt.Println("\nAdd more element to slide w/ append:", a)

	// get list of primes w/ slide
	fmt.Println("\nGet list primes w/ slice:")
	fmt.Println("  list of primes (<= 31):", ListPrimes(31))
	fmt.Println("  list of primes (<= 30):", ListPrimes(30))

	// access a range of array & slice - same as string
	fmt.Println("\nAccess a subarray and subslice ...")
	slice1 := make([]int, 6)
	for i := 0; i < len(slice1); i++ {
		slice1[i] = -2*i + 3
	}
	fmt.Println(" the original slices:", slice1)
	fmt.Println(" access a range ([3:5]):", slice1[3:5])
	fmt.Println(" access from a given position to end ([3:]):", slice1[3:])
	fmt.Println(" access from start to a given position ([:5]):", slice1[:5])

	fmt.Println(" delete idx=4 [append(slice[:idx], slice[idx+1:]...)]:", append(slice1[:4], slice1[5:]...))
	// replaceing element at index 1 w/ index 3 and remove index 3

}

func Max(list []int) int {
	if len(list) == 0 {
		panic("Error: empty list passed to Max()!")
	}
	var m int // default value = 0

	// range over list, updating m if we find bigger value
	for i, val := range list { // equivalent to 'for i:=0; i<len(list); i++ {'
		if i == 0 || val > m { // val equivalent to list[i]
			m = val
		}
	}

	return m
}

/*
Sum takes slice of integer and return the sum of values in the slice
*/
func Sum(a []int) int {
	var s int

	for _, value := range a { // _ means	 that the variable is not required
		s += value
	}

	return s
}

// passing a slice as a parameter
func ChangeFirst1Slice(list []int) {
	list[0] = 1 // list is the passed parameter of the caller
}

func ChangeFirst1Array(list [3]int) {
	list[0] = 1 // list is a copy of the passed parameter
}

/*
ListPrimes takes an integer and returns a list of all prime numbers up to
and including n
*/

func ListPrimes(n int) []int {
	primes := make([]int, 0) // create the slice w/0 knowing the length

	primeBooleans := SieveOfEratosthenes(n)
	// return a slice of boolean variables whose p-th element is true if p is a prime

	for p, isPrime := range primeBooleans {
		// when encountered a prime, append to the slice
		if isPrime == true {
			primes = append(primes, p)
		}
	}
	return primes
}

/*
SieveOfEratosthenes takes an integer n and returns a slice of n+1 booleans
primaeArray where primeArray[k] is true if p is a prime and false otherwise.

Implement the Sieve Of Eratosthenes approach
*/

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

/*
CrossOfMultiples takes a boolean slice and an integer p.  It cross off
multiples of p, meansing turning these multiples to false in the slice.
It return the slice obtained as a result.
*/
func CrossOffMultiples(primeArray []bool, p int) []bool {
	for k := 2 * p; k < len(primeArray); k += p {
		primeArray[k] = false
	}
	return primeArray
}

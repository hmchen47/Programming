package main

import (
	"fmt"
	"os"
)

// Variadic function use "..." to indicate an arbitrary number of variables
func Sum(numbers ...int) int {
	if len(numbers) == 0 {
		fmt.Println("Error: number of integers passed to Sum() must be positive")
		os.Exit(1) // raise flag 1
		// exiting normally os.Exit(0)
	}
	s := 0
	// numbers gets stored as an array
	for i := 0; i < len(numbers); i++ {
		s += numbers[i]
	}
	return s
}

func main() {
	// declaration of arrays
	var a1 [5]int
	var b1 [3]string
	var c1 [4]float64
	var d1 [2]bool

	// what would a1, b1, & c1 look like?
	fmt.Println("\nDecalaration w/ default value:")
	fmt.Println("  int array:    ", a1)
	fmt.Println("  string array: ", b1)
	fmt.Println("  float64 array:", c1)
	fmt.Println("  boolean array:", d1)

	// assigning value to array element
	a1[0] = 3
	b1[2] = "Hi there"
	i := 2
	c1[2*i-3] = 2.75
	d1[1] = true

	// what would a1, b1, & c1 look like?
	fmt.Println("\nAssigning value w/ index:")
	fmt.Println("  int array:    ", a1)
	fmt.Println("  string array: ", b1)
	fmt.Println("  float64 array:", c1)
	fmt.Println("  boolean array:", d1)

	a1[len(a1)-1] = -14
	fmt.Println("\nget array length w/ len() - be aware the 0-based indexing system:", len(a1))

	// using variadic function
	fmt.Println("\nvaradic function w/ '...':")
	fmt.Println(Sum(1, -4))
	fmt.Println(Sum(15, 6, 0))

	// to access command line parameters, we need the package "os"
	// in praticular, os.Args is an array containing command line
	// parameters as strings
	fmt.Println("\nCommand line argument w/ os.Args:")
	fmt.Println(os.Args)

	/*
		if len(os.Args) < 2 {
			panic("number of arguments should be at least one!")
		}
		//convert string to integer
		x := int(os.Args[1])
		y := int(os.Args[2])
		z := int(os.Args[3])
	*/
	fmt.Println("\nFunction arguments check and exit w/ os.Exit(1):")
	fmt.Println(Sum())
}

package main

import (
	"fmt"
)

func main() {
	fmt.Println("\n\nLoops...")

	fmt.Println("\nFactorial(5):", Factorial(5))
	// fmt.Println("Factorial(-120):", Factorial(-100))

	fmt.Println("\nAdd First positive n (10):", SumFirstNIntegers(10))
	fmt.Println("\nSum the even numbers till n (1):", SumEven(1))
	fmt.Println("Sum the even numbers till n (2):", SumEven(2))
	fmt.Println("\nSum the even numbers till n (10):", SumEven(10))
	fmt.Println("Sum the even numbers till n (11):", SumEven(11))

	// infinity loop
	var i uint = 10

	for ; i >= 0; i-- {
		fmt.Println(i)
	}
}

// first, a factorial function

func Factorial(n int) int {
	// handle negative input
	if n < 0 {
		// panic: print an error msg and immediately end program
		panic("Error: Negative input given to Factorial()!")
	}
	p := 1
	i := 1
	// go does not have a 'while' keyword, use 'for' instead
	// while i <= n
	for i <= n {
		p = p * i
		i = i + 1 // missing will cause infinity loop
	}

	// i exist here

	return p
}

func AnotherFactorial(n int) int {
	if n < 0 {
		panic("Error: negative input given to Factorial()!")
	}
	p := 1

	// for every integer i between 1 and n p = p*i

	// for i := n; i >= 1; i++ { <- same as the expression below
	for i := 1; i <= n; i++ {
		p *= i
	}
	// i not existed here
	return p
}

// Exercise: add first n positive integers with while loop

func SumFirstNIntegers(n int) int {
	sum := 0
	i := 1
	for i <= n {
		sum += i
		i++
	}
	return sum
}

func AnotherSum(n int) int {
	sum := 0
	for i := 1; i <= n; i++ {
		sum += i
	}
	return sum
}

// Exercise: write  function SumEven that sums all even numbers uo to and
// possibley including n

func SumEven(n int) int {
	sum := 0
	for i := 2; i <= n; i += 2 {
		sum += i
	}
	return sum
}

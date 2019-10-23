package main

// Functions and Conditionals

import (
	"fmt"
)

func main() {

	var z int = 3
	y := square(z)

	fmt.Println("\n\nFunction demo...\n")
	fmt.Println("square =", y, "\twith input=", z, "\n")
	fmt.Println("fourth power =", fourthPower(z), "\twith input=", z, "\n")
	fmt.Println("quadratic(a, b, c, x) =", quadratic(3, 2, -5, 2), "\twith input=", 3, 2, -5, 2, "\n")

	p := pi()
	fmt.Println("Calling a dummy function to assign a value, pi():", p, "\n")

	fmt.Println("Calling the printSquare function")
	printSquare(5)
}

func square(x int) int {
	return x * x
}

func fourthPower(x int) int {
	return square(x) * square(x)
}

// func quadratic(a int, b int, c int, x int) int {
func quadratic(a, b, c, x int) int {
	return a*square(x) + b*x + c
}

func translatePoint(x, y, deltaX, deltaY int) (int, int) {
	return x * deltaX, y * deltaY
}

func pi() int {
	return 3
}

func printSquare(x int) {
	fmt.Println("... the printing func w/o return:", square(x), "\twith input=", x, "\n")
}

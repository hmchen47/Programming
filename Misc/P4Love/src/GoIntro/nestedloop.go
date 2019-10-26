package main

import (
	"fmt"
	"math"
)

/*
Print rectangleproblem: drew a rectangle of symbols
Input: Integer r and c
Output: a rectangle of "#"" symbols. w/ r rows and c column

#######
#######
#######
*/

// PrintRect(r, c) prints r x c rectagle of "#" symbols

func PrintRect(r, c int) {
	// check r & c are positive
	// range over the number of rows
	for i := 0; i < r; i++ {
		// in each row, print c symbols
		/*
			for j := 0; j < c; j++ {
				fmt.Print("#")
			}
		*/
		PrintRow(c)
		// fmt.Print("\n")
		fmt.Println()
	}
}

// PrintRow(c) print c "#" symbols in a row
func PrintRow(c int) {
	for j := 0; j < c; j++ {
		fmt.Print("#")
	}
}

/*
Print Diamond problem: draw a diamond of "#" symbols
	Input: an odd integer n
	Output: print diamond of for below having height n

    #
   ###
  #####
 #######
  #####
   ###
	#

Key: think top-down
*/

// PrintDiamond(n): print a diamond of '#' symbold w/ height n (odd)

func PrintDiamond(n int) {
	if n%2 == 0 {
		panic("n shout be an odd integer!")
	}
	PrintTriangle(n - n/2)
	PrintInvertedTriangle(n / 2)
}

// PrintTriangle(r): print an upright triangle of "#" symbols w/ r rows
func PrintTriangle(r int) {
	// range over rows, print the appropriate " " and "#" each triangle
	for i := 1; i <= r; i++ {
		numSpaces := r - i
		numSymbols := 2*i - 1
		PrintRow2(numSpaces, numSymbols)
	}
}

// PrintInvertedTriangle(r): print an inverted triangle of "#" symbols w/ r rows
func PrintInvertedTriangle(r int) {
	// range over rows, print each row of spaces and symbols
	for i := 1; i <= r; i++ {
		numSpaces := i
		numSymbols := (r-i)*2 + 1
		PrintRow2(numSpaces, numSymbols)
	}
}

func PrintRow2(numSpaces, numSymbols int) {
	// first print number of spaces
	for i := 1; i <= numSpaces; i++ {
		fmt.Print(" ")
	}

	// next, print number of symbols
	for i := 1; i <= numSymbols; i++ {
		fmt.Print("#")
	}

	// finally, print a new line
	fmt.Println()
}

/*
AnotherPrintDiamond(n)
	middle = integer integer of (n/2)
    for an integer row from 0 to (n-1)
      	numSymbols = n - |middle - row| * 2
      	for an integer col from 0 to() n-1)
      	  	if |middle - col| <= integer part of (numSymbols/2)
      	    	print "#"
      	  	else
      	    	print " "   // a whitespace
*/

//AnotherPrintDiamond(n):

func AnotherPrintDiamond(n int) {
	if n%2 == 0 {
		panic("n must be odd integer!")
	}
	middle := n / 2
	for row := 0; row < n; row++ {
		numSymbols := n - int(math.Abs(float64(middle-row)))*2
		for col := 0; col < n; col++ {
			if int(math.Abs(float64(middle-col))) <= numSymbols/2 {
				fmt.Print("#")
			} else {
				fmt.Print(" ")
			}
		}
		fmt.Println()
	}
	fmt.Println()
}

func main() {
	fmt.Println("\nPrint rectangle w/ #:")
	PrintRect(3, 6)

	fmt.Println("\nDraw a diamond shape w/ symbol '#':")
	PrintDiamond(11)

	fmt.Println("\nDraw a diamond shape w/ AnotherPrintDiamond:")
	AnotherPrintDiamond(21)
}

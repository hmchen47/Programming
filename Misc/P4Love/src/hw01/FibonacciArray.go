package main

import (
	"fmt"
)

func main() {
	fmt.Println("Fibonacci Array")

	var fibArray [50]uint

	fibArray[0] = 0
	fibArray[1] = 1

	for i := 2; i < len(fibArray); i++ {
		fibArray[i] = fibArray[i-2] + fibArray[i-1]
	}

	fmt.Println(fibArray)
}

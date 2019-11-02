package main

import "fmt"

func main() {
	ary := [7]int{12, -7, 9, 11, -27, 8, 12}

	min := (18446744073709551615 / 2)

	for i := 0; i < len(ary); i++ {
		if ary[i] < min {
			min = ary[i]
		}
	}

	fmt.Println("Input:", ary)
	fmt.Println("  the minimum is", min)
}

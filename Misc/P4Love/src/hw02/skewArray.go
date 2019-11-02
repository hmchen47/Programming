package main

import (
	"fmt"
)

func main() {
	fmt.Println("\nSkew Array Problem ...")

	genome1 := "CATGGGCATCGGCCATACGCC"
	// 0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2

	genome2 := ""
	// 0

	genome3 := "C"
	// 0 -1

	genome4 := "A"
	// 0 0

	genome5 := "G"
	// 0 1

	genome6 := "T"
	// 0 0

	fmt.Println("SkewArray [0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2]:  ", SkewArray(genome1))
	fmt.Println("SkewArray [0]:  ", SkewArray(genome2))
	fmt.Println("SkewArray [0 -1]:  ", SkewArray(genome3))
	fmt.Println("SkewArray [0 0]:  ", SkewArray(genome4))
	fmt.Println("SkewArray [0 1]:  ", SkewArray(genome5))
	fmt.Println("SkewArray [0 0]:  ", SkewArray(genome6))
}

func SkewArray(genome string) []int {
	cntArray := make([]int, 1)

	for i := 0; i < len(genome); i++ {
		// fmt.Println(i, cntArray[i])
		if genome[i] == 'G' {
			cntArray = append(cntArray, cntArray[i]+1)
		} else if genome[i] == 'C' {
			cntArray = append(cntArray, cntArray[i]-1)
		} else {
			cntArray = append(cntArray, cntArray[i])
		}
	}

	return cntArray
}

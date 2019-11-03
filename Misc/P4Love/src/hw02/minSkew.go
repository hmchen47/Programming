package main

import (
	"fmt"
)

func main() {
	fmt.Println("\nMinimum Skew Problem ...")

	genome1 := "TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"
	// 11 24

	genome2 := "ACCG"
	// 3

	genome3 := "ACCC"
	// 4

	genome4 := "CCGGGT"
	// 2

	genome5 := "CCGGCCGG"
	// 2 6

	fmt.Println(" Minimum Skew [11 24]:  ", MinimumSkew(genome1))
	fmt.Println(" Minimum Skew [3]:  ", MinimumSkew(genome2))
	fmt.Println(" Minimum Skew [4]:  ", MinimumSkew(genome3))
	fmt.Println(" Minimum Skew [2]:  ", MinimumSkew(genome4))
	fmt.Println(" Minimum Skew [2 6]:  ", MinimumSkew(genome5))
}

/*
MinimumSkew()
	Input: a string genome
	Output: a list of position with skewness
*/
func MinimumSkew(genome string) []int {
	skewAry := SkewArray(genome)

	return MinPositions(skewAry)
}

func SkewArray(genome string) []int {
	cntArray := make([]int, 1)

	for i := 0; i < len(genome); i++ {
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

func MinPositions(skew []int) []int {
	minVal := MinimumSkewValue(skew)
	positions := make([]int, 0)

	for idx := range skew {
		if skew[idx] == minVal {
			positions = append(positions, idx)
		}
	}

	return positions
}

func MinimumSkewValue(skew []int) int {
	min := skew[0]
	for i := 1; i < len(skew); i++ {
		if min > skew[i] {
			min = skew[i]
		}
	}
	return min
}

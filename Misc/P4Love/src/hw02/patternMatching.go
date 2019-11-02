package main

import (
	"fmt"
)

func main() {
	fmt.Println("Pattern Matching Problem ...")

	pattern1 := "ATAT"
	text1 := "GATATATGCATATACTT"
	// 1 3 9

	pattern2 := "ACAC"
	text2 := "TTTTACACTTTTTTGTGTAAAAA"
	// 4

	pattern3 := "AAA"
	text3 := "AAAGAGTGTCTGATAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAATTAAATTTTATTGACTTAGGTCACTAAATACTTTAACCAATATAGGCATAGCGCACAGACAGATAATAATTACAGAGTACACAACATCCAT"
	// 0 46 51 74

	pattern4 := "TTT"
	text4 := "AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT"
	// 88 92 98 132

	pattern5 := "ATA"
	text5 := "ATATATA"
	// 0 2 4

	fmt.Println(" Pattern match [1 3 9]:", PatternMatching(pattern1, text1))
	fmt.Println(" Pattern match [4]:", PatternMatching(pattern2, text2))
	fmt.Println(" Pattern match [0 46 51 74]:", PatternMatching(pattern3, text3))
	fmt.Println(" Pattern match [88 92 98 132]:", PatternMatching(pattern4, text4))
	fmt.Println(" Pattern match [0 2 4]:", PatternMatching(pattern5, text5))
}

func PatternMatching(pattern, text string) []int {
	idxList := make([]int, 0)
	for i := 0; i < len(text)-len(pattern)+1; i++ {
		if text[i:i+len(pattern)] == pattern {
			idxList = append(idxList, i)
		}
	}
	return idxList
}

package main

import (
	"fmt"
)

func main() {
	fmt.Println("Pattern Count problem...")

	pattern1 := "GCG"
	text1 := "GCGCG"
	fmt.Println("\nTest set 1:\n  ", pattern1, "\n  ", text1)
	fmt.Println("  output (2):", PatternCount(pattern1, text1))

	pattern2 := "CG"
	text2 := "ACGTACGTACGT"
	fmt.Println("\nTest set 2:\n  ", pattern2, "\n  ", text1)
	fmt.Println("  output (2):", PatternCount(pattern2, text2))

	pattern3 := "AAA"
	text3 := "AAAGAGTGTCTGATAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAATTAAATTTTATTGACTTAGGTCACTAAATACTTTAACCAATATAGGCATAGCGCACAGACAGATAATAATTACAGAGTACACAACATCCAT"
	fmt.Println("\nTest set 3:\n  ", pattern3, "\n  ", text3)
	fmt.Println("  output (4):", PatternCount(pattern3, text3))

	pattern4 := "TTT"
	text4 := "AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT"
	fmt.Println("\nTest set 4:\n  ", pattern4, "\n  ", text4)
	fmt.Println("  output (4):", PatternCount(pattern4, text4))

	pattern5 := "ACT"
	text5 := "GGACTTACTGACGTACG"
	fmt.Println("\nTest set 5:\n  ", pattern5, "\n  ", text5)
	fmt.Println("  output (2):", PatternCount(pattern5, text5))

	pattern6 := "CC"
	text6 := "ATCCGATCCCATGCCCATG"
	fmt.Println("\nTest set 6:\n  ", pattern6, "\n  ", text6)
	fmt.Println("  output (5):", PatternCount(pattern6, text6))

	pattern7 := "CTC"
	text7 := "CTGTTTTTGATCCATGATATGTTATCTCTCCGTCATCAGAAGAACAGTGACGGATCGCCCTCTCTCTTGGTCAGGCGACCGTTTGCCATAATGCCCATGCTTTCCAGCCAGCTCTCAAACTCCGGTGACTCGCGCAGGTTGAGTA"
	fmt.Println("\nTest set 7:\n  ", pattern7, "\n  ", text7)
	fmt.Println("  output (9):", PatternCount(pattern7, text7))
}

// PatternCount()
//	Input: a pattern and a text w/ string
//	Output: return number of the pattern appearing in text w/ overlapping
func PatternCount(pattern, text string) int {
	count := 0

	for i := 0; i < len(text)-len(pattern)+1; i++ {
		if text[i:i+len(pattern)] == pattern {
			count++
		}
	}

	return count
}

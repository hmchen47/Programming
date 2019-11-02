package main

import (
	"fmt"
)

func main() {
	fmt.Println("Reverse Complement problem ...")

	txt1 := "AAAACCCGGT"
	// ACCGGGTTTT

	txt2 := "ACACAC"
	// GTGTGT

	txt3 := "GCTCAGCCACAACACGAGGGATACTATTATCACGGTCAGTACAACAACGCATTTGTGATCAGCAACGCACTAAGCTTGCCCAGGGTAGAACACGAGACGCACTCTGTAGCCGTTGTTATCCGACCCTTTAGGACCTTGCGCTGGGCTAGGATGGATAAACCTCGTGGTGCGGCTGTCTTTAGATGATGCTTCCAGGCGAG"
	// CTCGCCTGGAAGCATCATCTAAAGACAGCCGCACCACGAGGTTTATCCATCCTAGCCCAGCGCAAGGTCCTAAAGGGTCGGATAACAACGGCTACAGAGTGCGTCTCGTGTTCTACCCTGGGCAAGCTTAGTGCGTTGCTGATCACAAATGCGTTGTTGTACTGACCGTGATAATAGTATCCCTCGTGTTGTGGCTGAGC

	fmt.Println("Reverse complement [ACCGGGTTTT]:", ReverseComplement(txt1))
	fmt.Println("Reverse complement [GTGTGT]:", ReverseComplement(txt2))
	fmt.Println("Reverse complement [CTCGCC...AGC]:", ReverseComplement(txt3))

}

func ReverseComplement(pattern string) string {
	return Reverse(Complement(pattern))
}

/*
Reverse()
	Input: a string text
	Output: reverse the text order
*/
func Reverse(text string) string {
	n := len(text)
	reverse := ""
	for i := 0; i < n; i++ {
		reverse += string(text[n-i-1])
	}
	return reverse
}

/*
Complement()
	Input: a string text
	Output: convert A<->T, C<->G
*/
func Complement(text string) string {
	comp := ""
	for i := 0; i < len(text); i++ {
		switch text[i] {
		case 'A':
			comp += "T"
		case 'T':
			comp += "A"
		case 'C':
			comp += "G"
		case 'G':
			comp += "C"
		default:
			panic("Error: byte not w/ ATCG!")
		}
	}
	return comp
}

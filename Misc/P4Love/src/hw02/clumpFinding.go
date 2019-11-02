package main

import (
	"fmt"
)

func main() {
	fmt.Println("Clump Dinding Problem ...")

	genome1 := "CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"
	k1, L1, t1 := 5, 50, 4
	// CGACA GAAGA

	genome2 := "AAAACGTCGAAAAA"
	k2, L2, t2 := 2, 4, 2
	// AA

	genome3 := "ACGTACGT"
	k3, L3, t3 := 1, 5, 2
	// A C G T

	genome4 := "CCACGCGGTGTACGCTGCAAAAAGCCTTGCTGAATCAAATAAGGTTCCAGCACATCCTCAATGGTTTCACGTTCTTCGCCAATGGCTGCCGCCAGGTTATCCAGACCTACAGGTCCACCAAAGAACTTATCGATTACCGCCAGCAACAATTTGCGGTCCATATAATCGAAACCTTCAGCATCGACATTCAACATATCCAGCG"
	k4, L4, t4 := 3, 25, 3
	// AAA CAG CAT CCA GCC TTC

	fmt.Println(" 5-mers forming (50, 4)-clumps [CGACA GAAGA]:  ", ClumpFinding(genome1, k1, L1, t1))
	fmt.Println(" 2-mers forming (4, 2)-clumps [AA]:  ", ClumpFinding(genome2, k2, L2, t2))
	fmt.Println(" 1-mers forming (5, 2)-clumps [A C G T]:  ", ClumpFinding(genome3, k3, L3, t3))
	fmt.Println(" 3-mers forming (25, 3)-clumps [AAA CAG CAT CCA GCC TTC]:  ", ClumpFinding(genome4, k4, L4, t4))
}

/*
ClumpFinding()
	Input: a string genome,  k integer for k-mer, L integer for interval, and t integer for occurrences
	Output: finding clumps of k-

pseudo code:

FindClumps(text, k, L, t)
    patterns ← an array of strings of length 0
    n ← len(text)
    for every integer i between 0 and n − L
        window ← text[i, i + L]
        freqMap ← FrequencyTable(window, k)
        for every key s in freqMap
            if freqMap[s] ≥ t and Contains(patterns, s) = false
                patterns ← append(patterns, s)
	return patterns
*/
func ClumpFinding(genome string, k, L, t int) []string {
	clumps := make([]string, 0)
	freqMap := make(map[string]int, 0)
	// fmt.Println("\n  0. genome size:", len(genome), "k:", k, "L:", L, "t", t)

	// divide genome into intervals w/ size L, process and add to map
	for i := 0; i <= len(genome)-L; i++ {
		window := genome[i : i+L]
		freqMap = FrequencyMap(window, k)
		for key, val := range freqMap {
			if val >= t && !IsContained(clumps, key) {
				clumps = append(clumps, key)
			}
		}
	}

	return clumps
}

/*
 FrequencyMap()
	Input: a string text and an integer k
	Output: a map w/ string keys and integer values
*/
func FrequencyMap(text string, k int) map[string]int {
	freqMap := make(map[string]int)

	for i := 0; i < len(text)-k+1; i++ {
		freqMap[text[i:i+k]]++
	}

	return freqMap
}

/*
ISContained()
	Input: a patterns string array and a str string
	Output: return true if str in patterns, false otherwise
*/
func IsContained(patterns []string, str string) bool {
	for _, val := range patterns {
		if val == str {
			return true
		}
	}
	return false
}

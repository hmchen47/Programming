package main

import (
	"fmt"
)

func main() {
	fmt.Println("Frequency Map problem...")

	text1 := "ATATA"
	k1 := 3
	text2 := "mamaliga"
	k2 := 2

	fmt.Println("Frequency map (text, k-mer):", text1, k1, FrequencyMap(text1, k1))
	fmt.Println("Frequency map (text, k-mer):", text2, k2, FrequencyMap(text2, k2))

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

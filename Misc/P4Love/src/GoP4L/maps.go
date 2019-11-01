package main

import (
	"fmt"
)

func main() {
	fmt.Println("\n\nMap/Dictionary and frequent words ...")

	// one example of a map: keys are strings (words), values are number of
	// times a given word occurs in a text
	// Another example: a map whose keys are states names and whose values
	// are polling precentages (0 to 1) for each candidate

	var a []int
	a = make([]int, 6)
	fmt.Println("\nMap decalartion (created by initial varian and make function):", a)
	b := make(map[string]float64)
	fmt.Println("Map decalartion w/ valuse (created w/ shortcut & make):", b)
	c := map[string]uint{
		"txta": 20,
		"txtb": 11,
		"txtc": 38,
	}
	fmt.Println("Map declare 'var := map[keyType]valType {key:val, ...}':", c)

	// maps generalize the slice declaration
	fmt.Println("\n\nMap example w/ presidential election ...")
	var pools map[string]float64
	// just like slices, maps need to be make
	pools = make(map[string]float64) // no length required

	// add elements, no need to append
	pools["PA"] = 0.517
	pools["NY"] = 0.789
	pools["NE"] = 0.401
	pools["FL"] = 0.500
	pools["Mars"] = 0.012
	pools["Venus"] = 0.43

	fmt.Println(" list map contain:", pools)
	fmt.Println(" get size of map [len()]:", len(pools))

	// remove an element
	delete(pools, "Mars")
	delete(pools, "Venus")
	fmt.Println(" remove element [delete(mapVar, key)]:", pools)

	fmt.Println(" list of states and their polls:")
	for state, percentage := range pools {
		fmt.Println("    The polling percentags of", state, "is", percentage)
	}

	// assign keys & values from arrays and slices
	// fmt.Println("\nAssign keys & values from arrays and slices ...")
	// ary1 := [4]float64{3.1, 0.0, -78.93, 21.22}
	// primes := []int{2, 3, 5, 7, 11}

	// map function argument
	fmt.Println("\nMap passed as function arguments ...")
	dict := make(map[string]int)
	dict["Love"] = 0
	fmt.Println(" before function:", dict)
	BoostLove(dict)
	fmt.Println(" func arg declare 'funcName(var map[keytype]valType)':", dict)

	// Example for frequent words
	fmt.Println("\n\nExample for frequent words ..")
	txt4 := "ACGTTTTGAGACGACGTTT"
	k := 3
	fmt.Println("  find (text, k-mer):", txt4, k)
	fmt.Println("  the frequent words:", FindFrequentWords(txt4, k))

}

func FindFrequentWords(text string, k int) []string {
	freqPatterns := make([]string, 0)
	freqMap := FrequencyMap(text, k)
	// will give a map of k-mers in text to their number of occurrences
	max := MaxValue(freqMap)

	// range over frequency map, looking for strings (keys) achieving the
	// maximum number of values
	for pattern, val := range freqMap {
		if val == max {
			freqPatterns = append(freqPatterns, pattern)
		}
	}
	return freqPatterns
}

func MaxValue(freqMap map[string]int) int {
	m := 0
	firstTimeThrough := true

	for _, value := range freqMap {
		if firstTimeThrough == true || value > m {
			m = value
			firstTimeThrough = false
		}
	}

	return m
}

// FrequenceMap takes a string text and an integer k
// returns the map pf each k-mer substrings of test to its number of
// occurrences in text, including overlaps
func FrequencyMap(text string, k int) map[string]int {
	freq := make(map[string]int)
	// range voer all k-mer substrings of text
	for j := 0; j < len(text)-k+1; j++ {
		pattern := text[j : j+k]
		/*
			// method 1: elaborated one
			// does freq[pattern] exist?
			_, exists := freq[pattern]
			// exists is boolean = false if freq[pattern] doesn't exists
			// and true if it does
			if !exists {
				freq[pattern] = 1
			} else {
				freq[pattern]++
			}
		*/

		// method 2: shortcut
		freq[pattern]++
		// if freq[pattern] doesn't exist, Go creates the ket w/ default
		// value and then add one.  If existed, add one
	}

	return freq
}

func BoostLove(dict map[string]int) {
	dict["Love"] = 100
}

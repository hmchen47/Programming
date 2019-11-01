package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	fmt.Println("\nDemo for strings ...")

	fmt.Println("\nConvert char (byte) to string ('A'):", 'A', string('A'))
	fmt.Println("Convert int to string (45):", string(45))

	// Go think of this is for 45th symbol according to ASCII chart
	fmt.Println("\nstrconv methods ...")
	fmt.Println("  strconv class w/ Itoa() [strconv.Itoa(45)]:", strconv.Itoa(45))

	msg1, err1 := strconv.Atoi("37")
	if err1 != nil {
		fmt.Println("  rtn value & error w/ strconv.Atoi(\"37\"):", msg1, "\t", err1)
	} else {
		fmt.Println("  error & rtn value w/ strconv.Atoi(\"37\"):", err1, "\t", msg1)
	}
	msg2, err2 := strconv.Atoi("Hi")
	if err2 != nil {
		fmt.Println("  rtn value & error w/ strconv.Atoi(\"Hi\"):", msg2, "\t", err2)
	} else {
		fmt.Println("  error & rtn value w/ strconv.Atoi(\"Hi\"):", err2, "\t", msg2)
	}

	msg3, err3 := strconv.ParseFloat("3.14", 64)
	if err2 != nil {
		fmt.Println("  rtn value & error w/ strconv.ParseFloat(\"3.14\", 64):", msg3, "\t", err3)
	} else {
		fmt.Println("  error & rtn value w/ strconv.ParseFloat(\"3.14\", 64):", err3, "\t", msg3)
	}

	fmt.Println("\nstring conacteation w/ + (\"Hello\"+\"Worold!\")", "Hello"+"World!")

	str1 := "Hi this is demo of Go in P4L!"
	fmt.Println("\nstring as array (first char):", string(str1[0]), str1[0])
	fmt.Println("string as array (last char):", string(str1[len(str1)-1]), str1[len(str1)-1])

	fmt.Println("\n\nFunctions for Bacteria Replicatin of Origin ...")
	dna := "ACCGAT"

	fmt.Println("Complement(ACCGAT):", Complement(dna))
	fmt.Println("Reverse(ACCGAT):", Reverse(dna))
	fmt.Println("ReverseComplement(ACCGAT):", ReverseComplement(dna))

	// string w/ range of indices
	fmt.Println("\nAccess string elements w/ indices ...")
	str3 := "Hello Lovers!"
	fmt.Println("Access string w/ original string:", str3)
	fmt.Println("Access string range w/ ':' ([2:7]):", str3[2:7])
	fmt.Println("Access string from a given position to end ([2:]):", str3[4:])
	fmt.Println("Access string from start to a given end ([:5]):", str3[:5])

	// brainteaser: given a string, how could we delete an element at a given index?0
	fmt.Println("Delete index=4 (str[:4]+str[5:]):", str3[:4]+str3[5:])

	pattern1 := "ATA"
	text1 := "ATATA"
	fmt.Println("\nOccurrence for (text. pattern):", text1, pattern1)
	fmt.Println(" Occurrence of the pattern [string.Count(text. pattern)]:", strings.Count(text1, pattern1))
	fmt.Println(" Occurrence of the pattern [CountPattern(pattern, text)]:", CountPattern(pattern1, text1))
	fmt.Println(" Occurrence of the pattern [CountPattern2(pattern, text)]:", CountPattern2(pattern1, text1))

}

// ReverseComplement takes a DNA string and returns its reverse complement
// (corresponding to opposite strand)
func ReverseComplement(dna string) string {
	return Reverse(Complement(dna))
}

func Complement(dna string) string {
	complementDNA := ""
	for i := range dna {
		/* the following code won't change dna[i] due to array
		switch dna[i] {
		case 'A': dna[i] = 'T'
		case 'T': dna[i] = 'A'
		case 'C': dna[i] = 'G'
		case 'G': dna[i] = 'C'
		default:
			panic("Unknown symbol existed!")
		}
		*/

		// inefficient way to work on
		switch dna[i] {
		case 'A':
			complementDNA += "T"
		case 'T':
			complementDNA += "A"
		case 'C':
			complementDNA += "G"
		case 'G':
			complementDNA += "C"
		}
	}

	return complementDNA
}

// Reverse() takes string and reverse its symbols to produce a new string
func Reverse(str string) string {
	newStr := ""
	for idx := 0; idx < len(str); idx++ {
		newStr += string(str[len(str)-idx-1])
	}
	return newStr
}

// count the number of occurrences of a pattern in a text as a substring
func CountPattern(pattern, text string) int {
	count := 0
	k := len(pattern)
	n := len(text)

	// range over all substrings of text, and increment count if er found a match
	for i := 0; i < n-k+1; i++ {
		// does substring of text of length k starting at position i match patter?
		if text[i:i+k] == pattern {
			count++
		}
	}
	return count
}

func CountPattern2(pattern, text string) int {
	hits := StartingIndices(pattern, text)
	return len(hits)
}

// StartingIndices finds all starting positions of pattern in text
func StartingIndices(pattern, text string) []int {
	positions := make([]int, 0)

	k := len(pattern)
	n := len(text)

	// range over all substrings of text, and increment count if er found a match
	for i := 0; i < n-k+1; i++ {
		// does substring of text of length k starting at position i match patter?
		if text[i:i+k] == pattern {
			positions = append(positions, i)
		}
	}
	return positions
}

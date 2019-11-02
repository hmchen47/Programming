package main

import (
	"fmt"
)

func main() {
	fmt.Println("Maximum Map Value (Strings to Ints) Problem ...")

	dict1 := map[string]int{"ACT": 3, "GTGA": 6, "TA": 2}
	dict2 := map[string]int{"x1213y": 12}
	dict3 := map[string]int{"adkfdjk": -4, "adskf": -3, "fjdk": -7}
	dict4 := map[string]int{"hi": 4, "hello": 5, "world": -3, "ok": 5}

	fmt.Println("The max value of", dict1, "is", MaxDict(dict1))
	fmt.Println("The max value of", dict2, "is", MaxDict(dict2))
	fmt.Println("The max value of", dict3, "is", MaxDict(dict3))
	fmt.Println("The max value of", dict4, "is", MaxDict(dict4))
}

// MaxDict()
//	Input: a dictionary w/ string key and integer value
// 	Output: the maximum value of the values in dictionary
func MaxDict(dict map[string]int) int {
	max := 0
	firstIter := true
	for _, val := range dict {
		if firstIter == true {
			max = val
			firstIter = false
		}
		if val > max {
			max = val
		}
	}
	return max
}

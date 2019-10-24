package main

import "fmt"

func main() {
	fmt.Println("Combination w/ large number:")
	fmt.Println("  1000, 2 ->", CombinationBig(1000, 2))
	fmt.Println("  2000, 3 ->", CombinationBig(2000, 3))
	fmt.Println("  1000, 5 ->", CombinationBig(1000, 5))
}

func CombinationBig(n, k int) uint {
	var comb uint = PermutationBig(n, max(n-k, k))

	for idx := 1; idx <= min(n-k, k); idx++ {
		comb = comb / uint(idx)
	}
	return comb
}

func PermutationBig(n, k int) uint {
	var perm uint = 1
	for idx := k + 1; idx <= n; idx++ {
		perm = uint(idx) * perm
	}
	return perm
}

func min(i, j int) int {
	if i > j {
		return j
	} else {
		return i
	}
}

func max(i, j int) int {
	if i > j {
		return i
	} else {
		return j
	}
}

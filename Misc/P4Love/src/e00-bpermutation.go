package main

import "fmt"

func main() {
	fmt.Println("Permutation w/ large number:")
	fmt.Println("  1000, 2 ->", PermutationBig(1000, 2))
	fmt.Println("  2000, 3 ->", PermutationBig(2000, 3))
	fmt.Println("  1000, 5 ->", PermutationBig(1000, 5))
}

func PermutationBig(n, k int) uint {
	var perm uint = 1
	for idx := (n - k + 1); idx <= n; idx++ {
		perm = uint(idx) * perm
	}
	return perm
}

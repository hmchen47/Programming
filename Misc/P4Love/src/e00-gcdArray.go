package main

import "fmt"

func main() {
	array1 := []int{81, 63, 27, 243, 99, 135, 198}
	array2 := []int{256, 64, 1024, 512, 4096, 128, 7168, 160}
	array3 := []int{100, 76, 1234, 62, 88, 1456, 32, 78, 100, 42}

	fmt.Println("Expect:  9 \t result =", GCDArray(array1))
	fmt.Println("Expect: 32 \t result =", GCDArray(array2))
	fmt.Println("Expect:  2 \t result =", GCDArray(array3))

}

func GCDArray(array []int) int {
	min := MinArray(array)
	for i := min; i > 0; i-- {
		isCommonDivisor := true
		for j := 0; j < len(array); j++ {
			isCommonDivisor = isCommonDivisor && (IsDivisible(i, array[j]))
		}
		if isCommonDivisor == true {
			return i
		}
	}
	return 1
}

func MinArray(ary []int) int {

	min := (18446744073709551615 / 2)

	for i := 0; i < len(ary); i++ {
		if ary[i] < min {
			min = ary[i]
		}
	}
	return min
}

func IsDivisible(divisor, dividend int) bool {
	quotient := (dividend / divisor)
	return (dividend == (divisor * quotient))
}

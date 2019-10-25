package main

import "fmt"

func main() {

	prime1, prime2 := 0, 0

	prime1, prime2 = NextTwinPrimes(1)
	fmt.Println("next pair twin primes of 1:", prime1, prime2)
	prime1, prime2 = NextTwinPrimes(5)
	fmt.Println("next pair twin primes of 5:", prime1, prime2)
	prime1, prime2 = NextTwinPrimes(22)
	fmt.Println("next pair twin primes of 11:", prime1, prime2)
	prime1, prime2 = NextTwinPrimes(30)
	fmt.Println("next pair twin primes of 30:", prime1, prime2)
	prime1, prime2 = NextTwinPrimes(50)
	fmt.Println("next pair twin primes of 50:", prime1, prime2)
	prime1, prime2 = NextTwinPrimes(60)
	fmt.Println("next pair twin primes of 60:", prime1, prime2)
	prime1, prime2 = NextTwinPrimes(100)
	fmt.Println("next pair twin primes of 100:", prime1, prime2)
	prime1, prime2 = NextTwinPrimes(1000)
	fmt.Println("next pair twin primes of 1000:", prime1, prime2)
}

func NextTwinPrimes(n int) (int, int) {
	var odd int = 0
	if n == 1 {
		n++
	}
	if n == (n/2)*2 {
		odd = n + 1
	} else {
		odd = n
	}

	for !(IsPrime(odd) && IsPrime(odd+2)) {
		odd = odd + 2
	}

	return odd, odd + 2
}

func IsPrime(n int) bool {
	if n == 1 {
		return false
	}

	for i := 2; i < n; i++ {
		quotient := n / i
		if n == quotient*i {
			return false
		}
	}
	return true
}

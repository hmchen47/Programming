package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	fmt.Println("\n\nMonte Carlo Simulation w/ Craps ...")

	// Rolling a die
	fmt.Println("\nRolling die 7 times ..")
	// rand.Seed(100)
	rand.Seed(time.Now().UnixNano())
	for i := 0; i < 7; i++ {
		fmt.Print("\t", RollDie())
	}
	fmt.Print("\n")

	// Simulate Craps
	fmt.Println("\nPlay Craps w/ Monte Carlo Simulation ...")
	win := PlayCrapsOnce()
	if win {
		fmt.Println("\n Hurray! We win!!! :-)")
	} else {
		fmt.Println("\n OOps! we lost. :-(")
	}

	// Compute the house of edge
	fmt.Println("\nCompute House of Edge w/ Craps or binary games ...")
	fmt.Println(" the house of edge:", ComputeHouseOfEdge(10000))

}

/*
math/rand has three built-in functions that will use a lot
	1. rand.Int: pseudorandom integer
	2. rand.Float64: pseudorandom decimal in [0, 1]
	3. rand.Intn: pseudorandom interger [0, n-1] \in \N
*/

func RollDie() int {
	return rand.Intn(6) + 1
	// return 9rand.Int()%6) + 1
}

/*
SunTwoDie()
	Input: none
	Output: the sum of two simulated dice
*/
func SumTwoDice() int {
	return RollDie() + RollDie()
}

/*
PlayCrapsOnce()
	Input: none
	Output: true or false depending on outcome of a string simulated game of craps
*/
func PlayCrapsOnce() bool {
	firstRoll := SumTwoDice()
	// fmt.Println(" New Game w/ first roll:", firstRoll)
	if firstRoll == 7 || firstRoll == 11 {
		return true
	} else if firstRoll == 2 || firstRoll == 3 || firstRoll == 12 {
		return false
	} else {
		// fmt.Print(" New Roll(s):")

		for true {
			newRoll := SumTwoDice()
			// fmt.Print("  ", newRoll)
			if newRoll == firstRoll {
				return true
			} else if newRoll == 7 {
				return false
			}
		}
	}
	panic("We shouldn't be here!")
	return false
}

/*
ComputeHouseOfEdge()
	Input: an integer numTrials
	Output: an estimate of the house of edge of craps (or whatever  binary game)
		played over numTrials simulated games
*/
func ComputeHouseOfEdge(numTrials int) float64 {
	// use count to keep track of money won/lost
	count := 0
	for i := 0; i < numTrials; i++ {
		var outcome bool
		outcome = PlayCrapsOnce()

		if outcome == true {
			count++
		} else {
			count--
		}
	}
	return float64(count) / float64(numTrials)
}

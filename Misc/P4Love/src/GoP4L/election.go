package main

import (
	"fmt"
	"math/rand"
	"time"
)

// running these two files: election.go & io.go
// w/ "rgo run election.go io.go"

func main() {
	fmt.Println("U.S. Presidential Election simulation...")

	// first, make seed for PRNG
	rand.Seed(time.Now().UnixNano())

	// next, read in the electoral votes
	electoralVotes := ReadElectoralVotes("data/electoralVotes.txt")

	// read in polls
	filename := "data/earlyPolls.txt"
	// filename := "data/debates.txt"
	polls := ReadPollingData(filename)

	numTrials := 10000
	marginOfError := 0.05

	probability1, probability2, tieProbability := SimulateMultipleElections(polls, electoralVotes, numTrials, marginOfError)

	fmt.Println("\n\nEstimated probability of a candidate 1 win is", probability1)
	fmt.Println("Estimated probability of a candidate 2 win is", probability2)
	fmt.Println("Estimated probability of a tie is", tieProbability)
}

/*
SimulateMultipleElections
	Input: polling data as a map of statenames to floats (for candidate 1),
		along w/ a map of state names to electoral votes, a number of trials, and a margin of error in th epoll
	Output: the estimated probability of candidate 1 wining, candidate 2 wining, and a tie
*/
func SimulateMultipleElections(polls map[string]float64, electoralVotes map[string]uint, numTrials int, marginOfError float64) (float64, float64, float64) {
	// keep track of number of simulated elections won by each candidate (and tie)
	winCount1 := 0
	winCount2 := 0
	tieCount := 0

	// simulate an election n times update counts each time
	for i := 0; i < numTrials; i++ {
		// call SimulateOneElection as a subroutine
		votes1, votes2 := SimulateOneElection(polls, electoralVotes, marginOfError)

		// did candiaate1 or candidate 2 win?
		if votes1 > votes2 {
			winCount1++
		} else if votes2 > votes1 {
			winCount2++
		} else {
			tieCount++
		}
	}

	probability1 := float64(winCount1) / float64(numTrials)
	probability2 := float64(winCount2) / float64(numTrials)
	tieProbability := float64(tieCount) / float64(numTrials)

	return probability1, probability2, tieProbability
}

/*
SimulateOneElection()
	Input: a map of state names to polling percentage along with a map of state names to
		electoral college votes and a margin of error
	Output: the number of EC votes for each of the two candidates in one simulated election

*/
func SimulateOneElection(polls map[string]float64, electoralVotes map[string]uint, marginOfError float64) (uint, uint) {
	var collegeVotes1 uint = 0
	var collegeVotes2 uint = 0

	// range over all the states, and simulate the election in each state
	for state := range polls {
		poll := polls[state] // current polling value in he state for candidate1
		numVotes := electoralVotes[state]

		// adjust polling value w/ some randomized "noise"
		adjustedPoll := AddNoise(poll, marginOfError)

		// check who won state based on the adjusted poll ...
		if adjustedPoll >= 0.5 {
			// candidate 1 wins! give them the EX votes for the state
			collegeVotes1 += numVotes
		} else {
			// candidate 2 wins!
			collegeVotes2 += numVotes
		}
	}

	return collegeVotes1, collegeVotes2
}

/*
AddNoise()
	Input: a polling value for candidate 1 and a margin of error
	Output: an adjusted polling value for candidate 1 after adding tandom noise
*/
func AddNoise(poll float64, marginOfError float64) float64 {
	// random number from standard normal distribution
	x := rand.NormFloat64()
	x /= 2             // x has ~95% chance of being between -1 an +1
	x *= marginOfError // x has 95% chance of begin -marginOfError and +marginOfError

	return x + poll
}

package main

import (
	"io/ioutil"
	"strconv"
	"strings"
)

//ReadElectoralVotes takes in a filename from which to read electoral votes.
//It returns a map of state names to number of Electoral College Votes.
func ReadElectoralVotes(filename string) map[string]uint {
	data, err := ioutil.ReadFile(filename)
	Check(err)
	// each line of the datadata is stored in the format:
	// stateName, votes where votes = number of Electoral College votes.
	lines := strings.Split(string(data), "\n")

	//we create a map of strings to unsigned integers.
	electoralVotes := make(map[string]uint)

	//now, parse out data on each line and add to electoralVotes map
	for j := range lines {
		var line = strings.Split(lines[j], ",")
		stateName := line[0]
		votes, err := strconv.Atoi(line[1])
		electoralVotes[stateName] = uint(votes)
		Check(err)
	}

	return electoralVotes
}

//ReadPollingData takes in a filename from which to read data.
//It returns a map of state names to polling percentage for candidate 1.
func ReadPollingData(filename string) map[string]float64 {
	data, err := ioutil.ReadFile(filename)
	Check(err)

	// each line of the datadata is stored in the format:
	// stateName, x, y where x = candidate 1 percentage,
	// y = candidate 2 percentage
	lines := strings.Split(string(data), "\n")

	candidate1Percentages := make(map[string]float64)

	//now, parse out data on each line and add data to map.
	for j := range lines {
		var line = strings.Split(lines[j], ",")
		stateName := line[0]
		percentage1, err := strconv.ParseFloat(line[1], 64)
		// normalize percentages between 0 and 1
		candidate1Percentages[stateName] = percentage1 / 100.0
		Check(err)
	}

	return candidate1Percentages
}

func Check(e error) {
	if e != nil {
		panic(e)
	}
}

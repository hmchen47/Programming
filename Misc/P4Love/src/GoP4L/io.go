package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

/*
ReadElectoralVotes()
	Input: a filename from which to read electoral votes
	Output: a map of state names to number of Electoral College Votes
*/
func ReadElectoralVotes(filename string) map[string]uint {
	data, err := ioutil.ReadFile(filename)
	Check(err)
	// each line of the datadata is store is stored in the format:
	//	stateName, votes where votes = number of Electoral votes
	lines := strings.Split(string(data), "\n")

	// create a map of string to unsigned integers
	electoralVotes := make(map[string]uint)

	// now parse out data on each line and add to electoralVotes map
	for j := range lines {
		var line = strings.Split(lines[j], ",")
		stateName := line[0]
		fmt.Println(line[0], len(line))
		votes, err := strconv.Atoi(line[1])
		electoralVotes[stateName] = uint(votes)
		Check(err)
	}
	return electoralVotes
}

/*
ReadPollingData()
	Input: a string filename from which to read data
	Output: a map of state names to polling percentage for candate 1
*/
func ReadPollingData(filename string) map[string]float64 {
	data, err := ioutil.ReadFile(filename)
	Check(err)

	// each line of the datadata is stored in the format:
	//	stateName, x, y
	// where x = canadate 1 percentage, y = canadate 2 percentage
	lines := strings.Split(string(data), "\n")

	candidate1Percentages := make(map[string]float64)

	//now, parse out data on each line and add data to map
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

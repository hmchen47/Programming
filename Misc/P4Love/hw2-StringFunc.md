+ # Homework 2: String Functions

## 1. Welcome

Welcome to Homework 2!

Please read this page carefully before starting, especially if you are new to Stepik.

Like Homework 1, this assignment is divided into a sequence of functions for you to write.  All of these functions derive from our material on finding replication origins in bacterial genomes and relate to operations on strings.  Consult the slides provided from this chapter at the course website as needed for definitions, pseudocode, etc.

Each function is assigned to its own "step" (page).  You should create a folder called "hw2" under "go/src" and create a .go file in that folder.  You should write your functions locally, and upload your code here to test them.  A note on how the testing works here.

+ If you need any subroutines, provide those as well.
+ Behind the scenes, we grade your code on a collection of test datasets (that we provide).  You either pass all the tests (congrats!) or we let you know the first test that your code failed on.  We provide a link to test datasets beneath each problem so that you can test your code before submitting your function.  We also provide a "sample and output" so that you can see a single example of the correct answer for a given sample input.
+ You don't have to worry about formatting your answer to meet the sample output -- we handle all this behind the scenes.  Just write your Go function(s)!
+ We import any packages that you need; you won't need to import or be able to import any additional ones.
+ All code should be in Go.
+ Some of the problems have "Debug Datasets" describing each of the test datasets.  In other places we just provide the sample datasets on the same page as the problem.

Happy coding!


## 2. Substring Counting Problem

+ Substring Counting Problem
  + Input: A string pattern and a longer string text.
  + Output: The number of times that pattern appears as a substring of text.  (Remember to include overlaps.)

+ Test sets
  + Sample 1:
    + Input: GCG, GCGCG
    + Output: 2
  + Sample 2:
    + Input: CG, ACGTACGTACGT
    + Output: 3
  + Sample 3:
    + Input: AAA, AAAGAGTGTCTGATAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAATTAAATTTTATTGACTTAGGTCACTAAATACTTTAACCAATATAGGCATAGCGCACAGACAGATAATAATTACAGAGTACACAACATCCAT
    + Output: 4
  + Sample 4:
    + Input: TTT, AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT
    + Output: 4
  + Sample 5:
    + Input: ACT, GGACTTACTGACGTACG
    + Output: 2
  + Sample 6:
    + Input: CC, ATCCGATCCCATGCCCATG
    + Output: 5
  + Sample 7:
    + Input; CTC, CTGTTTTTGATCCATGATATGTTATCTCTCCGTCATCAGAAGAACAGTGACGGATCGCCCTCTCTCTTGGTCAGGCGACCGTTTGCCATAATGCCCATGCTTTCCAGCCAGCTCTCAAACTCCGGTGACTCGCGCAGGTTGAGTA
    + Output: 9

+ Write a program, test using stdin → stdout

  ```go 
  // write your PatternCount() function here along with any subroutines that you need.
  func PatternCount(pattern, text string) int {

  }
  ```

+ [Answer](src/hw02/PatternCount.go)


## 3. Maximum Map Value Problem

+ Maximum Map Value (Strings to Ints) Problem
  + Input: A map freq of strings to integers.
  + Output: The maximum value in freq.

+ Implement a function MaxDict that solves the Maximum Map Value Problem. Note: your function should still work if the values are all negative.

+ Test sets
  + Sample 1: 
    + Input: ACT 3; GTGA 6; TA 2
    + Output: 6
  + Sample 2:
    + Input: x1213y 12; Sample Output 2
    + Output: 12
  + Sample 3:
    +Input: adkfdjk -4; adskf -3; fjdk -7
    + Output: -3
  + Sample 4:
    + Input: hi 4; hello 5; world -3; ok 5
    + Output: 5

+ Write a program, test using stdin → stdout

  ```go
  // Insert your MaxDict() function here, along with any subroutines that you need.
  func MaxDict(dict map[string]int) int {

  }
  ```

  + [Answer](src/hw02/maxDict.go)


## 4. Frequency Map Problem

+ Frequency Map Problem
  + Input: A string text and an integer k.
  + Output: The "frequency map" of all k-mers appearing as substrings of text﻿, as a map of strings to integers.
  
+ Write a function FrequencyMap that takes a string text and an integer k as and returns the frequency map of all k-mers appearing in text.

+ test sets
  + Sample 1:
    + Input: ATATA; 3
    + Output: ATA 2; TAT 1
  + Sample 2:
    + Input: mamaliga; 2
    + Output:  al 1; am 1; ga 1; ig 1; li 1; ma 2

+ Write a program, test using stdin → stdout

```go
// Insert your FrequencyMap() function here, along with any subroutines that you need.
func FrequencyMap(text string, k int) map[string]int {

}
```

+ [Answer](src/hw02/frequencyMap.go)

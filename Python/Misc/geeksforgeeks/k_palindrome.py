#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
Find if string is K-Palindrome or not

Given a string, find out if the string is K-Palindrome or not. A 
    k-palindrome string transforms into a palindrome on removing at most k 
    characters from it.


Examples :
Input : String - abcdecba, k = 1
Output : Yes
String can become palindrome by removing 1 character i.e. either d or e)


Input  : String - abcdeca, K = 2
Output : Yes
Can become palindrome by removing 2 characters b and e.

Input : String - acdcb, K = 1
Output : No
String can not become palindrome by removing only one character.

If we carefully analyze the problem, the task is to transform the given 
    string into its reverse by removing at most K characters from it. The 
    problem is basically a variation of 
    [Edit Distance](http://goo.gl/OT7Jiz). We can modify the Edit Distance 
    problem to consider given string and its reverse as input and only 
    operation allowed is deletion. Since given string is compared with its 
    reverse, we will do at most N deletions from first string and N 
    deletions from second string to make them equal. Therefore, for a string 
    to be k-palindrome, 2*N <= 2*K should hold true. Below are the detailed 
    steps of algorithm - Process all characters one by one staring from 
    either from left or right sides of both strings. Let us traverse from 
    the right corner, there are two possibilities for every pair of 
    character being traversed.

If last characters of two strings are same, we ignore last characters and 
    get count for remaining strings. So we recur for lengths m-1 and n-1 
    where m is length of str1 and n is length of str2.

If last characters are not same, we consider remove operation on last 
    character of first string and last character of second string, 
    recursively compute minimum cost for the operations and take minimum of 
    two values.

Remove last char from str1: Recur for m-1 and n.
Remove last char from str2: Recur for m and n-1.

URL: http://www.geeksforgeeks.org/find-if-string-is-k-palindrome-or-not/
"""

import sys
import math

class EditDistance(object):
    def __init__(self, strA, strB):
        """
        args:
            strA: string
            strB: string
        """
        self.strA = strA
        self.strB = strB
        self.Dmx  = None

        self.misMatchCnt = 0

        self.DmxGenerateMod()

    def DmxGenerateMod(self):
        self.Dmx = [[0 for i in range(len(self.strA) + 1)] \
            for j in range(len(self.strB) + 1)]

        for j in range(len(self.strA) + 1):
            self.Dmx[0][j] = j
        for i in range(len(self.strB) + 1):
            self.Dmx[i][0] = i

        # print(self.Dmx)

        for j in range(1, len(self.strA) + 1):
            for i in range(1, len(self.strB) + 1):
                insertion = self.Dmx[i][j - 1] + 1
                deletion  = self.Dmx[i - 1][j] + 1
                match     = self.Dmx[i - 1][j - 1]
                mismatch  = self.Dmx[i - 1][j - 1] + 1

                if self.strA[j - 1] == self.strB[i - 1]:
                    self.Dmx[i][j] = min(insertion, deletion, match)
                else:
                    self.Dmx[i][j] = min(insertion, deletion, mismatch)

                if i == j and self.strA[j - 1] != self.strB[i - 1]:
                    self.misMatchCnt += 1


    def DmxGenerate(self):
        """
        compute the edit distance of the two given strings

        Pseudo Code:
        for all i:
            D(i, 0) <- 0
        for all j:
            D(0, j) <- 0
        
        for j from 1 to m (strB length):
            for i from 1 to n (strA length):
                insertion = D(i, j - 1) + 1
                deletion  = D(i - 1, j) + 1
                match     = D(i - 1, j - 1)
                mismatch  = D(i - 1, j - 1) + 1

                if A[i] == B[j]:
                    D(i, j) = min(insertion, deletion, match)
                else:
                    D(i, j) = min(insertion, deletion, unmatch)
        """
        # initialize the distance matrix
        # print("len(strA)= {} len(strB)= {}".format(len(self.strA), len(self.strB)))
        self.Dmx = [[0 for i in range(len(self.strA) + 1)] \
            for j in range(len(self.strB) + 1)]

        for j in range(len(self.strA) + 1):
            self.Dmx[0][j] = j
        for i in range(len(self.strB) + 1):
            self.Dmx[i][0] = i

        # print(self.Dmx)

        for j in range(1, len(self.strA) + 1):
            for i in range(1, len(self.strB) + 1):
                insertion = self.Dmx[i][j - 1] + 1
                deletion  = self.Dmx[i - 1][j] + 1
                match     = self.Dmx[i - 1][j - 1]
                mismatch  = self.Dmx[i - 1][j - 1] + 1

                if self.strA[j - 1] == self.strB[i - 1]:
                    self.Dmx[i][j] = min(insertion, deletion, match)
                else:
                    self.Dmx[i][j] = min(insertion, deletion, mismatch)
                    self.misMatchCnt += 1

    def __str__(self):
        # print(self.Dmx)
        rtnStr = "       "
        for i in range(len(self.strA)):
            rtnStr += "{:3s}".format(self.strA[i])

        rtnStr += "\n"

        for j in range(len(self.strB) + 1):
            if j == 0:
                rtnStr += "  "
            else:
                rtnStr += "{:s} ".format(self.strB[j - 1])

            for i in range(len(self.strA) + 1):
                # print("i= {} j= {}".format(i, j), end = "    ")
                rtnStr += "{:3d}".format(self.Dmx[j][i])

            rtnStr += "\n"

        rtnStr += "\nmisMatch cnt= {}\n".format(self.misMatchCnt)

        return rtnStr

def processing(strA, k):

    if strA[0] != strA[-1]:
        strB = strA[:-2:-1]
        if k > 0:
            k -= 1
    else:
        strB = strA[::-1]

    maxDist = EditDistance(strA, strB)

    print(maxDist)


if __name__ == "__main__":
    A = "DISTANCE"
    B = "EDITING"

    A = "abcdecba"
    k = 1

    # A ="abcdeca"
    # k = 2

    # A = "acdcb"
    # k = 1

    processing(A, 1)


"""
Examples :
Input : String - abcdecba, k = 1
Output : Yes
String can become palindrome by removing 1 character i.e. either d or e)


Input  : String - abcdeca, K = 2
Output : Yes
Can become palindrome by removing 2 characters b and e.

Input : String - acdcb, K = 1
Output : No
String can not become palindrome by removing only one character.
"""
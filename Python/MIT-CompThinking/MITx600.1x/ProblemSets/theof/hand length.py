#!/usr/bin/env python
# _*_ coding = UTF-8 _*_

def calculateHandlen(hand):
    """
   Returns the length (number of letters) in the current hand.
   
   hand: dictionary (string int)
   returns: integer
   """
    return sum(hand.values())
#!/usr/bin/env python2
# _*_ coding: utf-8 _*_

def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list 
    """
    # Your Code Here

    if start.getBefore() == None:
        return start

    return findFront(start.getBefore())

    
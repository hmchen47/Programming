#!/usr/bin/python
# _*_ coding = UTF-8 _*_

class Queue(object):

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def remove(self):
        try:
            return self.vals.pop(0)
        except:
            raise ValueError("Emty List") 
#!/usr/bin/python
# _*_ coding = UTF-8 _*_

import math

def sq(x):
    return x*x


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "<"+self.x+","+self.y+">"
    def distance(self,other):
        return math.sqrt(sq(self.x - other.x)
                         + sq(self.y - other.y))

c = Coordinate(3,4)
Origin = Coordinate(0,0)
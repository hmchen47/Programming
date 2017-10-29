#!/usr/bin/env python
# _*_ coding = UTF-8 _*_

def sqrt(a):
    def tryit(x):
        return 0.5 * (a/x + x)
    return fixedPoint(tryit, 0.0001)
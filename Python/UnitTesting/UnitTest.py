# UnitTesting/UnitTest.py
#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

# The basic unit testing class

class UnitTest:
    testID = ""
    errors = []
    # Override cleanup() if test object creation allocates non-memory
    # resources that must be cleaned up:
    def cleanup(self): pass
    # Verify a condition is true:
    def affirm(condition):
        if(!condition)
            UnitTest.errors.append("failed: " + UnitTest.testID)

#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import unittest
from ex_fibonacci import fib

class FibonacciTest(unittest.TestCase):

    def testCalculation(self):
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(5), 5)
        self.assertEqual(fib(10), 55)
        self.assertEqual(fib(20), 6765)

    def testCalculationErr(self):
        self.assertEqual(fibErr(0), 0)
        self.assertEqual(fibErr(1), 1)
        self.assertEqual(fibErr(5), 5)
        self.assertEqual(fibErr(10), 55)
        self.assertEqual(fibErr(20), 6765)

if __name__ == "__main__":
    unittest.main()

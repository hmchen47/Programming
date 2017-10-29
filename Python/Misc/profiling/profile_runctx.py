#!/usr/bin/env python2
# _*_ coding: utf-8 _*_

# URL: https://pymotw.com/2/profile/index.html

# usage: python profile_runctx.py

import profile
from profile_fibonacci_memoized import fib, fib_seq

if __name__ == '__main__':
    profile.runctx('print fib_seq(n); print', globals(), {'n':20})
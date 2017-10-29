#!/usr/bin/env python2
# _*_ coding: utf-8 _*_

# URL: https://pymotw.com/2/profile/index.html

# usage: python profile_stats_restricted.py

import profile
import pstats
from profile_fibonacci_memoized import fib, fib_seq

# Read all 5 stats files into a single object
stats = pstats.Stats('profile_stats_0.stats')
for i in range(1, 5):
    stats.add('profile_stats_%d.stats' % i)
stats.strip_dirs()
stats.sort_stats('cumulative')

# limit output to lines with "(fib" in them
stats.print_stats('\(fib')


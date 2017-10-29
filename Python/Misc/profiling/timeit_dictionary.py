#!/usr/bin/env python2
# _*_ coding: utf-8 _*_

# URL: https://pymotw.com/2/timeit/index.html

# usage: python timeit_dictionary.py

# {{{cog include('timeit/timeit_dictionary.py', 'header')}}}
import timeit
import sys

# A few constants
range_size=1000
count=1000
setup_statement="l = [ (str(x), x) for x in range(%d) ]; d = {}" % range_size
# {{{end}}}


# {{{cog include('timeit/timeit_dictionary.py', 'show_results')}}}
def show_results(result):
    "Print results in terms of microseconds per pass and per item."
    global count, range_size
    per_pass = 1000000 * (result / count)
    print '%.2f usec/pass' % per_pass,
    per_item = per_pass / range_size
    print '%.2f usec/item' % per_item

print "%d items" % range_size
print "%d iterations" % count
print
# {{{end}}}


# {{{cog include('timeit/timeit_dictionary.py', 'setitem')}}}
# Using __setitem__ without checking for existing values first
print '__setitem__:\t',
sys.stdout.flush()
# using setitem
t = timeit.Timer("""
for s, i in l:
    d[s] = i
""",
setup_statement)
show_results(t.timeit(number=count))
# {{{end}}}


# {{{cog include('timeit/timeit_dictionary.py', 'setdefault')}}}
# Using setdefault
print 'setdefault:\t',
sys.stdout.flush()
t = timeit.Timer("""
for s, i in l:
    d.setdefault(s, i)
""",
setup_statement)
show_results(t.timeit(number=count))
# {{{end}}}

# {{{cog include('timeit/timeit_dictionary.py', 'has_key')}}}
# Using has_key
print 'has_key:\t',
sys.stdout.flush()
# using setitem
t = timeit.Timer("""
for s, i in l:
    if not d.has_key(s):
        d[s] = i
""",
setup_statement)
show_results(t.timeit(number=count))
# {{{end}}}

# {{{cog include('timeit/timeit_dictionary.py', 'exception')}}}
# Using exceptions
print 'KeyError:\t',
sys.stdout.flush()
# using setitem
t = timeit.Timer("""
for s, i in l:
    try:
        existing = d[s]
    except KeyError:
        d[s] = i
""",
setup_statement)
show_results(t.timeit(number=count))
# {{{end}}}

# {{{cog include('timeit/timeit_dictionary.py', 'in')}}}
# Using "in"
print '"not in":\t',
sys.stdout.flush()
# using setitem
t = timeit.Timer("""
for s, i in l:
    if s not in d:
        d[s] = i
""",
setup_statement)
show_results(t.timeit(number=count))
# {{{end}}}


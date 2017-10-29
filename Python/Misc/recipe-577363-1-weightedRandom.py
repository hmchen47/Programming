#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
'''http://code.activestate.com/recipes/577363-weighted-random-choice/'''
import bisect
import random
import unittest

try:
    xrange
except NameError:
    # Python 3.x
    xrange = range


def weighted_random_choice(seq, weight):
    """Returns a random element from ``seq``. The probability for each element
    ``elem`` in ``seq`` to be selected is weighted by ``weight(elem)``.

    ``seq`` must be an iterable containing more than one element.

    ``weight`` must be a callable accepting one argument, and returning a
    non-negative number. If ``weight(elem)`` is zero, ``elem`` will not be
    considered. 
        
    """ 
    weights = 0
    elems = [] 
    for elem in seq:
        w = weight(elem)     
        try:
            is_neg = w < 0
        except TypeError:    
            raise ValueError("Weight of element '%s' is not a number (%s)" %
                             (elem, w))
        if is_neg:
            raise ValueError("Weight of element '%s' is negative (%s)" %
                             (elem, w))
        if w != 0:               
            try:
                weights += w
            except TypeError:
                raise ValueError("Weight of element '%s' is not a number "
                                 "(%s)" % (elem, w))
            elems.append((weights, elem))
    if not elems:
        raise ValueError("Empty sequence")
    ix = bisect.bisect(elems, (random.uniform(0, weights), None))
    return elems[ix][1]


class TestCase(unittest.TestCase):

    def test_empty(self):
        """Empty sequences raise ``ValueError``.

        """
        self.assertRaises(ValueError,
                          weighted_random_choice, [], lambda x: 0)
        self.assertRaises(ValueError,
                          weighted_random_choice, [1, 2, 3], lambda x: 0)

    def test_invalid_weight(self):
        """Invalid weight values are detected.

        """
        self.assertRaises(ValueError,
                          weighted_random_choice, [1, 2, 3], lambda x: "foo")

        class Oops(Exception):
            pass

        def weight(elem):
            raise Oops()

        self.assertRaises(Oops, weighted_random_choice, [1, 2, 3], weight)

    def test_spread(self):
        """Results are consistent with weight function.

        """
        seq = range(0, 100)
        odds, evens = [], []

        bias = 10.0

        def weight(elem):
            if elem % 2:
                return bias
            else:
                return 1

        for _ in xrange(0, 5000):
            elem = weighted_random_choice(seq, weight)
            if elem % 2:
                odds.append(elem)
            else:
                evens.append(elem)

        delta = abs(bias - float(len(odds) / float(len(evens))))
        self.assertTrue(delta < 1)


if __name__ == "__main__":
    random.seed()
    unittest.main()


'''
Another algorithm
http://rosettacode.org/wiki/Probabilistic_choice#Python
'''
def probchoice(items, probs):
    '''\
    Splits the interval 0.0-1.0 in proportion to probs
    then finds where each random.random() choice lies
    '''
 
    prob_accumulator = 0
    accumulator = []
    for p in probs:
        prob_accumulator += p
        accumulator.append(prob_accumulator)
 
    while True:
        r = random.random()
        yield items[bisect.bisect(accumulator, r)]
 
def probchoice2(items, probs, bincount=10000):
    '''\
    Puts items in bins in proportion to probs
    then uses random.choice() to select items.
 
    Larger bincount for more memory use but
    higher accuracy (on avarage).
    '''
 
    bins = []
    for item,prob in zip(items, probs):
        bins += [item]*int(bincount*prob)
    while True:
        yield random.choice(bins)
 
def tester(func=probchoice, items='good bad ugly'.split(),
                    probs=[0.5, 0.3, 0.2],
                    trials = 100000
                    ):
    def problist2string(probs):
        '''\
        Turns a list of probabilities into a string
        Also rounds FP values
        '''
        return ",".join('%8.6f' % (p,) for p in probs)
 
    from collections import defaultdict
 
    counter = defaultdict(int)
    it = func(items, probs)
    for dummy in xrange(trials):
        counter[it.next()] += 1
    print "\n##\n## %s\n##" % func.func_name.upper()  
    print "Trials:              ", trials
    print "Items:               ", ' '.join(items)
    print "Target probability:  ", problist2string(probs)
    print "Attained probability:", problist2string(
        counter[x]/float(trials) for x in items)

if __name__ == '__main__':
    items = 'aleph beth gimel daleth he waw zayin heth'.split()
    probs = [1/(float(n)+5) for n in range(len(items))]
    probs[-1] = 1-sum(probs[:-1])
    tester(probchoice, items, probs, 1000000)
    tester(probchoice2, items, probs, 1000000)



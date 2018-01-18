#!/use.bin/env python3
# _*_ coding: utf-8 _*_

def kwargsDemo(**kwargs):
    ''' Demo of using kwargs '''
    print("{}".format(kwargs))
    if kwargs is not None:
        for key, val in kwargs.items():
            print("Arguments: key({}) = {}".format(key, val))

    return 0

if __name__ == "__main__":
    kwargsDemo(name="kwargsDemo", test1="Test 1", test2="test 2")
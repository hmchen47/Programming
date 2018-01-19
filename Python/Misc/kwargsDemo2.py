#!/use.bin/env python3
# _*_ coding: utf-8 _*_


def test_args_kwargs(arg1, arg2, arg3):
    print("arg1: {}".format(arg1))
    print("arg2: {}".format(arg2))
    print("arg3: {}".format(arg3))

if __name__ == "__main__":
    print("The demo should be conducted in IDLE - see usage in file")


'''
Usage: with IDLE

args = ("two", 3, 5)
test_args_kwargs(*args) 

kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
test_args_kwargs(**kwargs)
'''
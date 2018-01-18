#!/use.bin/env python3
# _*_ coding: utf-8 _*_

def test_var_args(f_arg, *argv):
    ''' demo to *args and f_arg '''
    
    print("First normal arg: {}".format(f_arg))

    for arg in argv:
        print("Another arg through *argv: {}".format(arg))

    return 0

test_var_args("ArgsDemo-f_arg", "python-argv1", "test=argv2", "eggs-argv3")

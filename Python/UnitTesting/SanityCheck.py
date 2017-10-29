# SanityCheck.py
#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

'''
Python3 Patterns, Recipes and Idioms
URL: http://python-3-patterns-idioms-test.readthedocs.org/en/latest/    UnitTesting.html

Just run this from the root directory of the code listings for the book; it 
will descend into each subdirectory and run the program there. An easy way 
to check things is to redirect standard output to a file, then if there are 
any errors they will be the only thing that appears at the console during 
program execution.
'''

import string, glob, os
# Do not include the following in the automatic tests:
exclude = ("SanityCheck.py", "BoxObserver.py",)

def visitor(arg, dirname, names):
    dir = os.getcwd()
    os.chdir(dirname)
    try:
        pyprogs = [p for p in glob.glob('*.py') if p not in exclude ]
        if not pyprogs: return
        print('[' + os.getcwd() + ']')
        for program in pyprogs:
            print('\t', program)
            os.system("python %s > tmp".format(program))
            file = open(program).read()
            output = open('tmp').read()

            # Append program output if it's not already there:
            if file.find("output = '''") == -1 and len(output) > 0:
                divider = '#' * 50 + '\n'
                file = file.replace('#' + ':~', '#<hr>\n')
                file += "output = '''\n" + open('tmp').read() + "'''\n"
                open(program,'w').write(file)
    finally:
        os.chdir(dir)

if __name__ == "__main__":
    os.path.walk('.', visitor, None)

    
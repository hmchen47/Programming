"""
Common Pythin Programming Mistakes to Avoid

URL: http://www.techbeamers.com/python-programming-mistakes/
"""

# 1. Ignorant of Pythin Scoping Rules (LEGS)
token = 'global'

def access_local():
    token = 'local'
    if 'token' in locals() and 'token' in globals():
        print("Yes, token is in both local and global scope.")
    print("But value of token used is = (" + token + ")\n")

def access_global():
    if 'token' in globals():
        print("Yes, token is in global scope.")
    print("Value of token used is = (" + token + ")\n")

def access_enclosed():
    test = 1
    for test in range(5):
        token = 'enclosed'
        pass
    if 'token' in globals():
        print("Though, token is in global scope.")
    print("But value of token used is = (" + token + ")\n")

def id(token):
    return 1

access_local()
access_enclosed()
access_global()
print("%s = %d\n" % ("token length", id(token)))
print(token1)

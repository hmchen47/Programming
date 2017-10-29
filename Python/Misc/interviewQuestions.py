
# fucntion as first-order object
def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123, [])
list3 = extendList('a')

print("list1 = %s with %d" % (list1, id(list1)))
print("list2 = %s with %d" % (list2, id(list2)))
print("list3 = %s with %d" % (list3, id(list3)))
# Ans:  [10, 'a']
#       [123]
#       [10, 'a']

def extendList(val, list=None):
    if list == None:
        list = []
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123, [])
list3 = extendList('a')

print("list1 = %s with %d" % (list1, id(list1)))
print("list2 = %s with %d" % (list2, id(list2)))
print("list3 = %s with %d" % (list3, id(list3)))
# Ans:  [10]
#       [123]
#       ['a']


letter = "hai sethuraman"
for i in letter:
    if i == 'a':
        pass
        print("pass statement is execute ............")
    else:
        print(i)

# using ~ for home directory
import os
print(os.path.expanduser('~'))


# Reg Expression
import re
print(re.search(r"[0-9a-zA-Z.]+@[a-zA-Z]+\.(com|co\.in)$", "michael.pages@mp.com"))

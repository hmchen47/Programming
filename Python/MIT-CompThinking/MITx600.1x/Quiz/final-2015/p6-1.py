#!/usr/bin/env python2
# _*_ coding: utf-8 _*_

class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name

def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """
    curFrob = atMe
    # if double link list empty, insert the newFrob accordingly
    if (curFrob.getAfter() == None) and (curFrob.getBefore() == None):
        if curFrob.myName() > newFrob.myName():
            curFrob.setBefore(newFrob)
            newFrob.setAfter(curFrob)
            return None
        else:
            curFrob.setAfter(newFrob)
            newFrob.setBefore(curFrob)
            return None

    # move the current Frob to head of the double linked list
    #print 'search head'
    while curFrob.getBefore() != None:
        curFrob = curFrob.getBefore()
        #print '11', curFrob.myName()

    # search for appropriate position to insert the new element
    # head of the list
    if newFrob.myName() < curFrob.myName() and curFrob.getBefore() == None:
        # insert into the head of the list
        #print 'head insertion'
        newFrob.setAfter(curFrob)
        curFrob.setBefore(newFrob)
        return None
    else:
        # search for the position that current Frob is less than new Frob
        # the next Frob is greter than the new Frob, then insert the new Frob
        # if current Frob hits the end of the list, then append to the end of 
        # the list
        while curFrob.getAfter() != None:
            nextFrob = curFrob.getAfter()
            #print 'search position, cur =', curFrob.myName(), 'next =', nextFrob.myName(), 'new =', newFrob.myName()
            #print 'comaprison:', curFrob.myName() <= newFrob.myName(), nextFrob.myName() > newFrob.myName()
            if curFrob.myName() <= newFrob.myName() and \
                nextFrob.myName() > newFrob.myName():
                newFrob.setBefore(curFrob)
                newFrob.setAfter(nextFrob)
                curFrob.setAfter(newFrob)
                nextFrob.setBefore(newFrob)
                return None
            curFrob = curFrob.getAfter()

        # append to the end of the list
        #print 'end of list'
        curFrob.setAfter(newFrob)
        newFrob.setBefore(curFrob)
        return None


def prnDL(atMe):
    # move to the head
    curFrob = atMe
    print curFrob.getBefore()
    while curFrob.getBefore() != None:
        curFrob = curFrob.getBefore()

    print '1 DL head = ', curFrob.myName()

    while curFrob.getAfter() != None:
        curFrob = curFrob.getAfter()
        print '2 DL cur name', curFrob.myName()
    print


def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list 
    """
    # Your Code Here

    if start.getBefore() == None:
        return start

    return findFront(start.getBefore())


eric = Frob('eric')
andrew = Frob('andrew')
ruth = Frob('ruth')
fred = Frob('fred')
martha = Frob('martha')

insert(eric, andrew)
#prnDL(eric)
insert(eric, ruth)
#prnDL(eric)
insert(eric, fred)
#prnDL(eric)
insert(ruth, martha)
#prnDL(eric)
insert(eric, Frob('martha'))
#prnDL(eric)

print findFront(martha)
print findFront(ruth)
print findFront(eric)
'''
insert(Frob("gabby"), Frob("allison"))
#   allison, gabby
insert(Frob("gabby"), Frob("allison"))
#   gabby, allison
insert(Frob("gabby"), Frob("zara"))
#   gabby, zara
insert(Frob("gabby"), Frob("zara"))
#   zara, gabby
insert(test_list, Frob("xander"))
insert(test_list, Frob("beto"))
#   abby, beto, xander
insert(test_list, Frob("xander"))
insert(test_list, Frob("beto"))
#   xander, beto, abby
insert(Frob("alvin"), Frob("alvin"))
#   alvin, alvin
insert(test_list, Frob("lyla"))
insert(test_list, Frob("christina"))
insert(test_list, Frob("ben"))
#   allison, ben, christina, lyla
#   lyla, christina, ben, allison

test_list = Frob('zsa zsa')
a = sm.Frob('ashley')
m = sm.Frob('marcella')
v = sm.Frob('victor')
insert(test_list, m)
insert(m, a)
insert(a, v)
#   ashley, marcella, victor, zsa zsa

test_list = Frob('mark')
c = Frob('craig')
insert(test_list, Frob("sam"))
insert(test_list, Frob("nick"))
insert(test_list, c)
insert(c, Frob("xanthi"))
insert(test_list, Frob("jayne"))
insert(c, Frob("martha"))
#   craig, jayne, mark, martha, nick, sam, xanthi

test_list = Frob('leonid')
a = Frob('amara')
j1 = Frob('jennifer')
j2 = Frob('jennifer')
s = Frob('scott')
insert(test_list, s)
insert(s, j1)
insert(s, j2)
insert(j1, a)
#   amara, jennifer, jennifer, leonid, scott

test_list = Frob('eric')
insert(test_list, Frob("eric"))
insert(test_list, Frob("chris"))
insert(test_list, Frob("john"))
insert(test_list, Frob("john"))
insert(test_list, Frob("chris"))
insert(test_list, Frob("eric"))
insert(test_list, Frob("john"))
insert(test_list, Frob("chris"))
#   chris, chris, chris, eric, eric, eric, john, john, john
'''



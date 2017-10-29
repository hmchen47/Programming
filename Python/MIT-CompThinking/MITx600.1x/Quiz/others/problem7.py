#!/usr/bin/env python
# _*_ coding = UTF-8 _*_

packages = (6, 9, 20)

def McNuggets(n):
      a = packages[0]
      b = packages[1]
      c = packages[2]
      for x in range(0, n):
          for y in range(0, n):
              for z in range(0, n):
                  if a*x + b*y + c*z == n:
                      return True
      return False
      
def McNuggets2(n):
   
    if n == 0:
        return True
    for i in (6, 9, 20):
        if n >= i and McNuggets2(n - i):
            return True
    return False      
# UnitTesting/TooMuchAccess.py
#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

class TooMuchAccess(UnitTest):
    Testable tst = Testable()
    def test1(self):
        tst.f2() # Oops!
        tst.f3() # Oops!
        tst.f4() # OK


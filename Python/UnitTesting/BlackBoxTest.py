# UnitTesting/BlackBoxTest.py
#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

class BlackBoxTest(UnitTest):
    Testable tst = Testable()
    def test1(self):
        #! tst.f2() # Nope!
        #! tst.f3() # Nope!
        tst.f4() # Only public methods available


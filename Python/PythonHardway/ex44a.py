#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# Exercise 44: Inheritance Versus Composition

class Parent(object):

    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()


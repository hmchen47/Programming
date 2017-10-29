#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# Exercise 44: Inheritance Versus Composition

class Parent(object):

    def override(self):
        print("PARENT override()")

class Child(Parent):

    def override(self):
        print("CHILD override()")


dad = Parent()
son = Child()

dad.override()
son.override()


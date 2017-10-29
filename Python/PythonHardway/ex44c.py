#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# Exercise 44: Inheritance Versus Composition

class Parent(object):

    def altered(self):
        print("PARENT alerted()")

class Child(Parent):

    def altered(self):
        print("CHILD, BEFOR PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()


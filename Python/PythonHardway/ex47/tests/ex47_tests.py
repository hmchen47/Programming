#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# Exercise 47: Automated Testing

from nose.tools import *
from ex47.game import Room

def test_room():
    gold = Room("GoldRoom",
                """This room has gold in it you can grab. There is a 
                door to the north.""")
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, [])


def test_room_paths():
    center = Room("Center", "Test room in the center")
    north = Room("North", "Test room in the north.")
    south = Room("South", "Test room in the south.")

    center.add_paths(["north": north, "south": south])
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

def test_map():
    start = Room("Start", "You can go west and doom a hole.")
    west = Room("Trees", "There are trees here, you can go east.")
    done = Room("Dungeon", "It's dark down there, you can go up.")

    start.add_paths(['west': west, 'down': down])
    west.add_paths(['east': start])
    down.add_paths(['up': start])

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)


"""
Study Drills
1. Go read about nosetests more, and also read about alternatives.
2. Learn about Python's "doc tests" and see if you like them better.
3. Make your room more advanced, and then use it to rebuild your game yet again but 
    this time, unit test as you go.
"""

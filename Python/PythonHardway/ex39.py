#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# Exercise 39: Dictionaries, Oh Lovely Dictionaries

# create a mapping of state to abbreviation
states = {
    'Oregan': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
    }

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("NY stat has %s" % cities['NY'])
print("OR stat has %s" % cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbrevation is: %s" % states['Michigan'])
print("Florida's abbrevation is: %s" % states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
print("Michigan has: %s" % cities[states['Michigan']])
print("Florida has: %s" % cities[states['Florida']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in states.items():
    print("%s is abbreviated %s" % (state, abbrev))

# print every city in state
print('-' * 10)
for abbrev, city in cities.items():
    print("%s has city %s" % (abbrev, city))

# now do both at the same time
print('-' * 10)
for state, abbrev in states.items():
    print("%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev]))

print('-' * 10)
# safely get an abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
    print("Sorry no Texas.")

# get a city with a default value
city = cities.get('TX', "Does Not Exist")
print("The city for the state 'TX' is: %s" % city)


"""
Study Drills
1. Do this same kind of mapping with cities and states/regions in your country or some 
    other country.
2. Find the Python documentation for dictionaries and try to do even more things to 
    them.
3. Find out what you can't do with dictionaries. A big one is that they do not have 
    order, so try playing with that.
4. Read about Python's assert feature and then take the hashmap code and add assertions 
    for each of the tests I've done instead of print. For example, you can assert that 
    the first get operation returns "New York" instead of just printing that out.
5. Did you notice that the list function listed the items I added in a different order 
    than they were added? This is an example of how dictionaries don't maintain order, 
    and if you analyze the code you'll understand why.
6. Create a dump function that is like list but which dumps the full contents of every 
    bucket so you can debug it.
7. Make sure you know what the hash function does in that code. It's a special function 
    that converts strings to a consistent integer. Find the documentation for it 
    online. Read about what a "hash function" is in programming.
"""

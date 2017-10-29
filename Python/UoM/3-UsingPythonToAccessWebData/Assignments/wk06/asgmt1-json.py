#!/usr/bin/env python2
# _*_ coding: utf-8 _*_
'''
    The program is for the assignment to extract JSON data and parse the 
    counts and then sums the counts.
'''

import json
import urllib
import xml.etree.ElementTree as ET

input = '''
{
    "note": "This file contains the sample data for testing</note>",
    "comments": [
        {
            "count": 97,
            "name": "Romina"
        },
        {
            "count": 97,
            "name": "Laurie"
        },
        {
            "count": 90,
            "name": "Bayli"
        },
        {
            "count": 90,
            "name": "Siyona"
        },
        {
            "count": 88,
            "name": "Taisha"
        },
        {
            "count": 87,
            "name": "Ameelia"
        },
        {
            "count": 87,
            "name": "Alanda"
        },
        {
            "count": 80,
            "name": "Prasheeta"
        },
        {
            "count": 79,
            "name": "Risa"
        },
        {
            "count": 79,
            "name": "Asif"
        },
        {
            "count": 78,
            "name": "Zi"
        },
        {
            "count": 76,
            "name": "Ediomi"
        },
        {
            "count": 76,
            "name": "Danyil"
        },
        {
            "count": 72,
            "name": "Barry"
        },
        {
            "count": 72,
            "name": "Lance"
        },
        {
            "count": 66,
            "name": "Hattie"
        },
        {
            "count": 66,
            "name": "Mathu"
        },
        {
            "count": 65,
            "name": "Bowie"
        },
        {
            "count": 65,
            "name": "Samara"
        },
        {
            "count": 64,
            "name": "Uchenna"
        },
        {
            "count": 61,
            "name": "Shauni"
        },
        {
            "count": 61,
            "name": "Georgia"
        },
        {
            "count": 59,
            "name": "Rivan"
        },
        {
            "count": 58,
            "name": "Kenan"
        },
        {
            "count": 57,
            "name": "Isma"
        },
        {
            "count": 57,
            "name": "Hassan"
        },
        {
            "count": 54,
            "name": "Samanthalee"
        },
        {
            "count": 51,
            "name": "Alexa"
        },
        {
            "count": 49,
            "name": "Caine"
        },
        {
            "count": 47,
            "name": "Grady"
        },
        {
            "count": 40,
            "name": "Anne"
        },
        {
            "count": 38,
            "name": "Rihan"
        },
        {
            "count": 37,
            "name": "Alexei"
        },
        {
            "count": 36,
            "name": "Indie"
        },
        {
            "count": 36,
            "name": "Rhuairidh"
        },
        {
            "count": 32,
            "name": "Annoushka"
        },
        {
            "count": 25,
            "name": "Kenzi"
        },
        {
            "count": 24,
            "name": "Shahd"
        },
        {
            "count": 22,
            "name": "Irvine"
        },
        {
            "count": 21,
            "name": "Carys"
        },
        {
            "count": 19,
            "name": "Skye"
        },
        {
            "count": 18,
            "name": "Atiya"
        },
        {
            "count": 18,
            "name": "Rohan"
        },
        {
            "count": 14,
            "name": "Nuala"
        },
        {
            "count": 12,
            "name": "Carlo"
        },
        {
            "count": 12,
            "name": "Maram"
        },
        {
            "count": 9,
            "name": "Japleen"
        },
        {
            "count": 7,
            "name": "Breeanna"
        },
        {
            "count": 3,
            "name": "Zaaine"
        },
        {
            "count": 2,
            "name": "Inika"
        }
    ]
}
'''

# ask for URL input
url = raw_input('Enter location: ')
#url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_42.json'
print 'Retrieving', url

# open url and parsing the data
try: 
    data = urllib.urlopen(url).read()
except IOError as e:
    print "IOError({0}): {1}".format(e.errno, e.strerror)
    exit()

# retrieve data from the provide URL
print 'Retrieved', len(data), 'characters'

#info = json.loads(input)
info = json.loads(data)

#print json.dumps(info, indent = 4)

print 'Count:', len(info['comments'])

sum = 0
for idx in range(len(info['comments'])):
    #print 'Name:', info['comments'][idx]['name']
    #print 'Count:', info['comments'][idx]['count']

    sum += info['comments'][idx]['count']

print 'Sum:', sum


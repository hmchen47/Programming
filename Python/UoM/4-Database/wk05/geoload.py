#!/usr/bin/env python2
# _*_ coding: utf-8 _*_

import urllib
import sqlite3
import json
import time
import ssl

serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"

# Deal with SSL certificate anomalies Python > 2.7
# scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
scontext = None

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

# create database table if not existed
cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

# retrieve data from where.data
fh = open("where.data")
count = 0
for line in fh:
    if count > 200 : break
    address = line.strip()
    print ''
    cur.execute("SELECT geodata FROM Locations WHERE address= ?", (buffer(address), ))
    # placeholder: ? -> (buffer(address), )

    try:
        data = cur.fetchone()[0]            # geodata in the first column
        print "Found in database ",address
        continue
    except:
        pass

    # get URL and crawl down the URL
    print 'Resolving', address
    url = serviceurl + urllib.urlencode({"sensor":"false", "address": address})
    print 'Retrieving', url
    uh = urllib.urlopen(url, context=scontext)
    data = uh.read()
    print 'Retrieved',len(data),'characters',data[:20].replace('\n',' ')
    count = count + 1

    # check for good data?
    try: 
        js = json.loads(str(data))
        # print js  # We print in case unicode causes an error
    except: 
        continue

    # if something wrong, print and exit the program
    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') : 
        print '==== Failure To Retrieve ===='
        print data
        break

    # write retrieve data into database
    cur.execute('''INSERT INTO Locations (address, geodata) 
            VALUES ( ?, ? )''', ( buffer(address),buffer(data) ) )
    # complete the transaction
    conn.commit() 
    time.sleep(1)

# zoom through the data has been store in database

print "Run geodump.py to read the data from the database so you can vizualize it on a map."

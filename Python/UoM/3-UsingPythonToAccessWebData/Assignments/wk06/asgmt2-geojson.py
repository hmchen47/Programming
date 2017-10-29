#!/usr/bin/env python2
# _*_ coding: utf-8 _*_
'''
    The program is for the assignment to extract JSON data from Google 
    and parse the location.
'''

import urllib
import json

#serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
#serviceurl = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/geojson?'

while True:
    address = raw_input('Enter location: ')
    #address = 'South Federal University'
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'

    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data
        #break
        continue

    print json.dumps(js, indent=4)

    #lat = js["results"][0]["geometry"]["location"]["lat"]
    #lng = js["results"][0]["geometry"]["location"]["lng"]
    #print 'lat',lat,'lng',lng
    location = js['results'][0]['place_id']
    print 'Place id', location

    #break

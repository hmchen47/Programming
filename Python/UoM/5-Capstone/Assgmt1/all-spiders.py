# spider.py
#!/usr/bin/env python2
# _*_ coding: utf-8 _*_

import sqlite3
import urllib
import ssl 
import time

from urlparse import urljoin
from urlparse import urlparse
from BeautifulSoup import *

# Deal with SSL certificate anomalies Python > 2.7
# scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
scontext = None

# open database
conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

# create tables if not existed
#
# Pages table: store records of web pages retrieved/unrestrieved
#   id: identifier
#   url: the webpage url to visit or to be visited
#   html: the content of a visted web page, default=NULL
#   error: indicator tha the web page unretievable 
#   old_rank:
#   new_rank: 
cur.execute('''CREATE TABLE IF NOT EXISTS Pages 
    (id INTEGER PRIMARY KEY, url TEXT UNIQUE, html TEXT, 
     error INTEGER, old_rank REAL, new_rank REAL)''')

# Links table: records of web page referenced
#   from_id: the web page id that the link initiaed
#   to_id: the web page id that the link ended
cur.execute('''CREATE TABLE IF NOT EXISTS Links 
    (from_id INTEGER, to_id INTEGER)''')

# Webs table: records of the visited web site
#   ur: the url of a web site
cur.execute('''CREATE TABLE IF NOT EXISTS Webs (url TEXT UNIQUE)''')

# Check to see if we are already in progress...
cur.execute('SELECT id,url FROM Pages WHERE html is NULL and error is NULL ORDER BY RANDOM() LIMIT 1')
row = cur.fetchone()

if row is not None:
    # pages existed for retrieving
    print "Restarting existing crawl.  Remove spider.sqlite to start a fresh crawl."
else:
    # ask for new web page url to process or use the default url
    starturl = raw_input('Enter web url or enter: ')
    if ( len(starturl) < 1 ) : 
        starturl = 'http://python-data.dr-chuck.net/'

    # process to remove end '/'
    if (starturl.endswith('/') ): 
        starturl = starturl[:-1]
    
    # process to get the website url only
    web = starturl
    if (starturl.endswith('.htm') or starturl.endswith('.html')) :
        pos = starturl.rfind('/')
        web = starturl[:pos]

    # write the processed record into database, (web, ) <- singlton tuple
    if (len(web) > 1):
        cur.execute('INSERT OR IGNORE INTO Webs (url) VALUES (?)', (web, )) 
        cur.execute('INSERT OR IGNORE INTO Pages (url, html, new_rank) VALUES ( ?, NULL, 1.0 )', ( starturl, )) 
        conn.commit()

# Get the current webs
cur.execute('''SELECT url FROM Webs''')
webs = list()
for row in cur:
    webs.append(str(row[0]))

print webs

many = 0

# infinite while loop
while True:
    # ask for how many pages to process
    if ( many < 1 ) :
        sval = raw_input('How many pages:')
        if ( len(sval) < 1 ) : break
        many = int(sval)
    many = many - 1

    # retrieve a record from Pages table to process w/o page contents
    cur.execute('SELECT id,url FROM Pages WHERE html is NULL and error is NULL ORDER BY RANDOM() LIMIT 1')
    try:
        row = cur.fetchone()
        # print row
        fromid = row[0]
        url = row[1]
    except:
        # every thing processed
        print 'No unretrieved HTML pages found'
        many = 0
        break

    print fromid, url, 

    # If we are retrieving this page, there should be no links from it
    cur.execute('DELETE from Links WHERE from_id=?', (fromid, ) )
    try:
        # delay the retrieve with sleep to prevent abuse
        # time.sleep(0.2)

        # # Deal with SSL certificate anomalies Python > 2.7
        # scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        # document = urllib.urlopen(url, context=scontext)

        # Normal Unless you encounter certificate problems
        # open the requested url
        document = urllib.urlopen(url)

        # get the contents of the page
        html = document.read()

        # unable to retriev the web page -> update Pages record with code
        if document.getcode() != 200 :
            print "Error on page: ",document.getcode()
            cur.execute('UPDATE Pages SET error=? WHERE url=?', (document.getcode(), url))

        # ignore the uon test/html page and set the page to error = -1
        if 'text/html' != document.info().gettype() :
            print "Ignore non text/html page"
            cur.execute('UPDATE Pages SET error = -1 WHERE url=?', (url, ))
            conn.commit()
            continue

        # print the url to be retrieved
        print '('+str(len(html))+')',

        # process the contents with BeautifulSoup
        soup = BeautifulSoup(html)

    except KeyboardInterrupt:
        # catch the keyboard interrupt
        print ''
        print 'Program interrupted by user...'
        break
    except:
        # catch BeautifulSoup error 
        print "Unable to retrieve or parse page"
        cur.execute('UPDATE Pages SET error=-1 WHERE url=?', (url, ))
        conn.commit()
        continue

    # store Pages record
    cur.execute('INSERT OR IGNORE INTO Pages (url, html, new_rank) VALUES (?, NULL, 1.0)', ( url, )) 
    cur.execute('UPDATE Pages SET html=? WHERE url=?', (buffer(html), url ))
    conn.commit()

    # Retrieve all of the anchor tags -> parsing them
    tags = soup('a')
    count = 0
    for tag in tags:
        # empty href link
        href = tag.get('href', None)
        if ( href is None ) : continue

        # Resolve relative references like href="/contact" to the full url
        up = urlparse(href)
        if (len(up.scheme) < 1):
            href = urljoin(url, href)

        # ignore php or related query
        ipos = href.find('#')
        if (ipos > 1): href = href[:ipos]

        # ignore href link with image files
        if (href.endswith('.png') or href.endswith('.jpg') or href.endswith('.gif')): continue

        # process the href link end with /
        if (href.endswith('/') ) : href = href[:-1]
        # print href
        if (len(href) < 1 ): continue

        # Check if the URL is in any of the webs -> leaving web sites
        found = False
        for web in webs:
            if ( href.startswith(web) ) :
                found = True
                break
        if not found : continue

        # store record for new page to work with
        cur.execute('INSERT OR IGNORE INTO Pages (url, html, new_rank) VALUES ( ?, NULL, 1.0 )', ( href, ) ) 
        count = count + 1
        conn.commit()

        # retrieve the id of the href link from Page database 
        cur.execute('SELECT id FROM Pages WHERE url=? LIMIT 1', (href, ))
        try:
            row = cur.fetchone()
            toid = row[0]
        except:
            print 'Could not retrieve id'
            continue

        # print fromid, toid
        # insert the link int Links table with from_id and to_id
        cur.execute('INSERT OR IGNORE INTO Links (from_id, to_id) VALUES (?, ? )', ( fromid, toid)) 

    print count

# end of infinite while loop

cur.close()

# end of spider.py












# sprank.py
#!/usr/bin/env python2
# _*_ coding: utf-8 _*_

import sqlite3

# access the database
conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

# Find the ids that send out page rank - we only are interested
# in pages in the SCC that have in and out links
cur.execute('''SELECT DISTINCT from_id FROM Links''')

# convert the database output into list for processsing
from_ids = list()
for row in cur: 
    from_ids.append(row[0])

# Find the ids that receive page rank 
cur.execute('''SELECT DISTINCT from_id, to_id FROM Links''')

# process to get the outbound ids
to_ids = list()
links = list()
for row in cur:
    from_id = row[0]
    to_id = row[1]

    # ignore self reference
    if from_id == to_id : continue
    # ignore from_id not in the processing list
    if from_id not in from_ids : continue
    # ignore to_id not in the processing list
    if to_id not in from_ids : continue

    # add the record into link list
    links.append(row)

    # add the the to_id if not duplicated
    if to_id not in to_ids : to_ids.append(to_id)

# Get latest page ranks for strongly connected component
prev_ranks = dict()
for node in from_ids:
    # retrieve record of the processing node from Pages table
    cur.execute('''SELECT new_rank FROM Pages WHERE id = ?''', (node, ))
    row = cur.fetchone()
    # store the rank for futher uase (old_rank)
    prev_ranks[node] = row[0]

# ask for the number of iterations 
sval = raw_input('How many iterations:')
many = 1
if ( len(sval) > 0 ) : many = int(sval)

# Sanity check -> no rank to process
if len(prev_ranks) < 1 : 
    print "Nothing to page rank.  Check data."
    quit()

# Lets do Page Rank in memory so it is really fast
for i in range(many):
    # print prev_ranks.items()[:5]

    # store the result with dictionary
    next_ranks = dict();
    total = 0.0
    for (node, old_rank) in prev_ranks.items():
        total = total + old_rank
        next_ranks[node] = 0.0
    # print total

    # Find the number of outbound links and sent the page rank down each
    for (node, old_rank) in prev_ranks.items():
        # print node, old_rank
        give_ids = list()
        for (from_id, to_id) in links:
            if from_id != node : continue
           #  print '   ',from_id,to_id

            if to_id not in to_ids: continue
            give_ids.append(to_id)
        if ( len(give_ids) < 1 ) : continue
        amount = old_rank / len(give_ids)
        # print node, old_rank,amount, give_ids
    
        for id in give_ids:
            next_ranks[id] = next_ranks[id] + amount
    
    newtot = 0
    for (node, next_rank) in next_ranks.items():
        newtot = newtot + next_rank
    evap = (total - newtot) / len(next_ranks)

    # print newtot, evap
    for node in next_ranks:
        next_ranks[node] = next_ranks[node] + evap

    newtot = 0
    for (node, next_rank) in next_ranks.items():
        newtot = newtot + next_rank

    # Compute the per-page average change from old rank to new rank
    # As indication of convergence of the algorithm
    totdiff = 0
    for (node, old_rank) in prev_ranks.items():
        new_rank = next_ranks[node]
        diff = abs(old_rank-new_rank)
        totdiff = totdiff + diff

    avediff = totdiff / len(prev_ranks)
    print i+1, avediff

    # rotate
    prev_ranks = next_ranks

# Put the final ranks back into the database
print next_ranks.items()[:5]
cur.execute('''UPDATE Pages SET old_rank=new_rank''')
for (id, new_rank) in next_ranks.items() :
    cur.execute('''UPDATE Pages SET new_rank=? WHERE id=?''', (new_rank, id))
conn.commit()
cur.close()












# spdump.py
#!/usr/bin/env python2
# _*_ coding: utf-8 _*_

import sqlite3

# access datbase
conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

# retrieve records with their counts of the incoming links
cur.execute(
    ''' SELECT COUNT(from_id) AS inbound, old_rank, new_rank, id, url 
        FROM Pages JOIN Links ON Pages.id = Links.to_id
        WHERE html IS NOT NULL
        GROUP BY id ORDER BY inbound DESC'''
)

# print the records of the ids and ranks 
count = 0
for row in cur :
    if count < 50: print row
    count = count + 1

print count, 'rows.'

cur.close()












# spreset.py
#!/usr/bin/env python2
# _*_ coding: utf-8 _*_

import sqlite3

# access database
conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

# reset the ranks for all records
cur.execute('''UPDATE Pages SET new_rank=1.0, old_rank=0.0''')
conn.commit()

cur.close()

print "All pages set to a rank of 1.0"










# spjson.py
#!/usr/bin/env python2
# _*_ coding: utf-8 _*_

import sqlite3

# access database
conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()


print "Creating JSON output on spider.js..."
howmany = int(raw_input("How many nodes? "))

# retrieve records 
cur.execute('''
    SELECT COUNT(from_id) AS inbound, old_rank, new_rank, id, url 
    FROM Pages JOIN Links ON Pages.id = Links.to_id
    WHERE html IS NOT NULL AND ERROR IS NULL
    GROUP BY id ORDER BY id,inbound
''')

# loop through record to generate javascript
fhand = open('spider.js','w')
nodes = list()
maxrank = None
minrank = None
for row in cur :
    nodes.append(row)
    rank = row[2]
    if maxrank < rank or maxrank is None: maxrank = rank
    if minrank > rank or minrank is None: minrank = rank
    if len(nodes) > howmany: break

# sanity check
if maxrank == minrank or maxrank is None or minrank is None:
    print "Error - please run sprank.py to compute page rank"
    quit()

# write to javascript file with JSON format for nodes
fhand.write('spiderJson = {"nodes":[\n')
count = 0
map = dict()
ranks = dict()
for row in nodes :
    if count > 0 : fhand.write(',\n')
    # print row
    rank = row[2]
    rank = 19 * ( (rank - minrank) / (maxrank - minrank) ) 
    fhand.write('{'+'"weight":'+str(row[0])+',"rank":'+str(rank)+',')
    fhand.write(' "id":'+str(row[3])+', "url":"'+row[4]+'"}')
    map[row[3]] = count
    ranks[row[3]] = rank
    count = count + 1
fhand.write('],\n')

# retrieve records for links
cur.execute('''SELECT DISTINCT from_id, to_id FROM Links''')
fhand.write('"links":[\n')

count = 0
for row in cur :
    # print row
    if row[0] not in map or row[1] not in map : continue
    if count > 0 : fhand.write(',\n')
    rank = ranks[row[0]]
    srank = 19 * ( (rank - minrank) / (maxrank - minrank) ) 
    fhand.write('{"source":'+str(map[row[0]])+',"target":'+str(map[row[1]])+',"value":3}')
    count = count + 1
fhand.write(']};')
fhand.close()
cur.close()

print "Open force.html in a browser to view the visualization"

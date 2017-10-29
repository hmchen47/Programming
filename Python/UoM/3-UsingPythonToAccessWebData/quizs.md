
Quizs - Regular Expression
--------------------------
Q1. Which of the following regular expressions would extract 'uct.ac.za' from this string using re.findall?
    From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
A. @(\S+)
B. F.+:
C. @\S+
D. ..@\S+..

Ans: A

Q2. What will the '\$' regular expression match?
A. A dollar sign
B. A new line at the end of a line
C. An empty line
D. The end of a line
E. The beginning of a line

Ans: A

Q3. What would the following mean in a regular expression? [a-z0-9]
A. Match any text that is surrounded by square braces
B. Match anything but a lowercase letter or digit
C. Match a lowercase letter or a digit
D. Match an entire line as long as it is lowercase letters or digits
E. Match any number of lowercase letters followed by any number of digits

Ans: C

Q4. What is the type of the return value of the re.findall() method?
A. A list of strings
B. A string
C. A single character
D. An integer
E. A boolean

Ans: A

Q5. What is the "wild card" character in a regular expression (i.e., the character that matches any character)?
A. +
B. .
C. *
D. ^
E. ?
F. $

Ans: B

Q6. What is the difference between the "+" and "*" character in regular expressions?
A. The "+" matches at least one character and the "*" matches zero or more characters
B. The "+" matches upper case characters and the "*" matches lowercase characters
C. The "+" matches the beginning of a line and the "*" matches the end of a line
D. The "+" matches the actual plus character and the "*" matches any character
E. The "+" indicates "start of extraction" and the "*" indicates the "end of extraction"

Ans: A

Q7. What does the "[0-9]+" match in a regular expression?
A. Several digits followed by a plus sign
B. One or more digits
C. Any number of digits at the beginning of a line
D. Zero or more digits
E. Any mathematical expression

Ans: B

Q8. What does the following Python sequence print out?
    x = 'From: Using the : character'
    y = re.findall('^F.+:', x)
    print y
A. :
B. ['From:']
C. From:
D. ^F.+:
E. ['From: Using the :']

Ans: E

Q9. What character do you add to the "+" or "*" to indicate that the match is to be done in a non-greedy manner?
A. ++
B. ?
C. \g
D. **
E. $
F. ^

Ans: B

Q10. Given the following line of text:
    From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
What would the regular expression '\S+?@\S+' match?
A. \@\
B. marquard@uct
C. stephen.marquard@uct.ac.za
D. From
E. d@u

Ans: C

Q11. Which of the following best describes "Regular Expressions"?
A. The way Python handles and recovers from errors that would otherwise cause a traceback
B. A way to calculate mathematical values paying attention to operator precedence
C. A small programming language unto itself
D. A way to solve Algebra formulas for the unknown value

Ans: C

Q12. Which of the following is the way we match the "start of a line" in a regular expression?
A. ^
B. str.startswith()
C. \linestart
D. String.startsWith()
E. variable[0:1]

Ans: A


Quiz - Networks and Sockets
---------------------------
Q1. What do we call it when a browser uses the HTTP protocol to load a file or page from a server and display it in the browser?
A. The Request/Response Cycle
B. IMAP
C. DECNET
D. SMTP
E. Internet Protocol (IP)

Ans: A

Q2. Which of the following is most similar to a TCP port number?
A. A telephone extension
B. A street number in an address
C. The GPS coordinates of a building
D. The distance between two locations
E. A telephone number

Ans: A

Q3. What must you do in Python before opening a socket?
A. import socket
B. _socket = true
C. import tcp
D. open socket
E. import tcp-socket

Ans: A

Q4. Which of the following TCP sockets is most commonly used for the web protocol (HTTP)?
A. 22
B. 119
C. 25
D. 80
E. 23

Ans: D

Q5. Which of the following is most like an open socket in an application?
A. An "in-progress" phone conversation
B. Fiber optic cables
C. The wheels on an automobile
D. The chain on a bicycle
E. The ringer on a telephone

Ans: A

Q6. What does the "H" of HTTP stand for?
A. Hypertext
B. Hyperspeed
C. Simple
D. Manual
E. wHolsitic

Ans: A

Q7. What is an important aspect of an Application Layer protocol like HTTP?
A. Which application talks first? The client or server?
B. What is the IP address for a domain like www.dr-chuck.com?
C. How much memory does the server need to serve requests?
E. How long do we wait before packets are retransmitted?

Ans: A

Q8. What are the three parts of this URL (Uniform Resource Locator)?
    http://www.dr-chuck.com/page1.htm
A. Protocol, document, and offset
B. Host, offset, and page
C. Page, offset, and count
D. Document, page, and protocol
E. Protocol, host, and document

Ans: E

Q9. When you click on an anchor tag in a web page like below, what HTTP request is sent to the server?
    <p>Please click <a href="page1.htm">here</a>.</p>
A. GET
B. POST
C. PUT
D. DELETE
E. INFO

Ans: A

Q10. Which organization publishes Internet Protocol Standards?
A. SIFA
B. IMS
C. LDAP
D. IETF
E. SCORM

Ans: D

Q11. What separates the HTTP headers from the body of the HTTP document?
A. X-End-Header: true
B. Four dashes
C. A less-than sign indicating the start of an HTML tag
D. A blank line

Ans: D


Q12. In a client-server application on the web using sockets, which must come up first?
A. server
B. client
C. it does not matter

Ans: A


Quiz - Reading Web Data From Python
-----------------------------------
Q1. Which of the following Python data structures is most similar to the value returned in this line of Python:
    x = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
A. list
B. file handle
C. regular expression
D. dictionary
E. socket

Ans: B

Q2. In this Python code, which line actually reads the data?
    import socket
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('www.py4inf.com', 80))
    mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')
    while True:
        data = mysock.recv(512)
        if ( len(data) < 1 ) :
            break
        print data
    mysock.close()
A. mysock.recv()
B. socket.socket()
C. mysock.close()
D. mysock.connect()
E. mysock.send()

Ans: A

Q3. Which of the following regular expressions would extract the URL from this line of HTML:
    <p>Please click <a href="http://www.dr-chuck.com">here</a></p>
A. href="(.+)"
B. href=".+"
C. http://.*
D. <.*>

Ans: A

Q4. In this Python code, which line is most like the open() call to read a file:
    import socket
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('www.py4inf.com', 80))
    mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')
    while True:
        data = mysock.recv(512)
        if ( len(data) < 1 ) :
            break
        print data
    mysock.close()
A. mysock.connect()
B. import socket
C. mysock.recv()
D. mysock.send()
E. socket.socket()

Ans: A

Q5. Which HTTP header tells the browser the kind of document that is being returned?
A. Content-Type:
B. HTML-Document:
C. Document-Type:
D. ETag:
E. Metadata:

Ans: A

Q6. What should you check before scraping a web site?
A. That the web site supports the HTTP GET command
B. That the web site allows scraping
C. That the web site only has links within the same site
D. That the web site returns HTML for all pages

Ans: B


Q7. What is the purpose of the BeautifulSoup Python library?
A. It optimizes files that are retrieved many times
B. It repairs and parses HTML to make it easier for a program to understand
C. It animates web operations to make them more attractive
D. It builds word clouds from web pages
E.It allows a web site to choose an attractive skin

Ans: B


Q8. What ends up in the "x" variable in the following code:
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    x = soup('a')
A. A list of all the anchor tags (<a..) in the HTML from the URL
B. True if there were any anchor tags in the HTML from the URL
C. All of the externally linked CSS files in the HTML from the URL
D. All of the paragraphs of the HTML from the URL

Ans: A

Quiz - eXtensible Markup Language
---------------------------------
Q1. What is the name of the Python 2.x library to parse XML data?
A. xml.json
B. xml.etree.ElementTree
C. xml-misc
D. xml2

Ans: B

Q2. Which of the following are not commonly used serialization formats?
A. JSON
B. Dictionaries
C. TCP
D. HTTP
E. XML

Ans: B, C, D

Q3. In this XML, which are the "complex elements"?
    <people>
        <person>
           <name>Chuck</name>
           <phone>303 4456</phone>
        </person>
        <person>
           <name>Noah</name>
           <phone>622 7421</phone>
        </person>
    </people>
A. people
B. person
C. name
D. phone
E. Noah

Ans: A, B

Q4. In the following XML, which are attributes?
    <person>
      <name>Chuck</name>
      <phone type="intl">
         +1 734 303 4456
       </phone>
       <email hide="yes" />
    </person>
A. hide
B. email
C. name
D. type
E. person

Ans: A, D

Q5. In the following XML, which node is the parent node of node e
    <a>
      <b>X</b>
        <c>
          <d>Y</d>
          <e>Z</e>
        </c>
    </a>
A. b
B. e
C. a
D. c

Ans: D

Q6. Looking at the following XML, what text value would we find at path "/a/b/c/e"
    <a>
      <b>X</b>
        <c>
          <d>Y</d>
          <e>Z</e>
        </c>
    </a>
A. a
B. e
C. Z
D. Y
E. b

Ans: C

Q7. What is the purpose of XML Schema?
A. A Python program to tranform XML files
B. To compute SHA1 checksums on data to make sure it is not modified in transit
C. To transfer XML data reliably during network outages
D. To establish a contract as to what is valid XML

Ans: D

Q8. If you were building an XML Schema and wanted to limit the values allowed in an xs:string field to only those in a particular list, what XML tag would you use in your XML Schema definition?
A. maxOccurs
B. xs:element
C. xs:sequence
D. xs:complexType
E. xs:enumeration

Ans: E

Q9. What does the "Z" mean in this representation of a time:
    2002-05-30T09:30:10Z
A. This time is in the UTC timezone
B. The hours value is in the range 0-12
C. The local timezone for this time is New Zealand
D. This time is Daylight Savings Time

Ans: A

Q10. Which of the following dates is in ISO8601 format?
A. 05/30/2002
B. May 30, 2002
C. 2002-05-30T09:30:10Z
D. 2002-May-30

Ans: C

Q11. What is the method to cause Python to parse XML that is stored in a string?
A. fromstring()
B. parse()
C. readall()
D. extract()
E. xpath()

Ans: A

Q12. What is a good time zone to use when computers are exchanging data over APIs?
A. The local time zone of the sending computer without daylight savings time
B. Universal Time / GMT
C. The local time zone of the receiving computer
D. The local time zone of the sending computer

Ans: B


Quiz - REST, JSON, and APIs
---------------------------
Q1. Who is credited with getting the JSON movement started?
A. Douglas Crockford
B. Bjarne Stroustrup
C. Pooja Sankar
D. Mitchell Baker

Ans: A

Q2. What Python library do you have to import to parse and handle JSON?
A. BeautifulSoup
B. import re
C. import json
D. ElementTree

Ans: C

Q3. Which of the following is a web services approach used by the Twitter API?
A. SOAP
B. REST
C. XML-RPC
D. CORBA

Ans: B

Q4. What kind of variable will you get in Python when the following JSON is parsed:
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  }
A. A list with six items
B. A tuple with three items
C. A list with three items
D. A dictionary with three key / value pairs
E. A list of tuples

Ans: D

Q5. Which of the following is __not__ true about the service-oriented approach?
A. An application runs together all in one place
B. Standards are developed where many pairs of applications must work together
C. Web services and APIs are used to transfer data between applications
D. An application makes use of the services provided by other applications

Ans: A

Q6. If the following JSON were parsed and put into the variable x,
  {
      "users": [
          {
              "status": {
                  "text": "@jazzychad I just bought one .__.",
               },
               "location": "San Francisco, California",
               "screen_name": "leahculver",
               "name": "Leah Culver",
           },
     ...
what Python code would extract "Leah Culver" form the JSON?
A. x->name
B. x["name"]
C. x[0]["name"]
D. x["users"][0]["name"]
E. x["users"]["name"]

Ans: D

Q7. What library call do you make to append properly encoded parameters to the end of a URL like the following:
  http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address=Ann+Arbor%2C+MI
A. urllib.urlencode()
B. re.match()
C. urllib.urlcat()
D. re.encode()

Ans: A

Q8. What happens when you exceed the Google geocoding API rate limit?
A. You canot use the API until you respond to an email that contains a survey question
B. You cannot use the API for 24 hours
C. Your application starts to perform very slowly
D. The API starts to perform very slowly

Ans: B

Q9. What protocol does Twittter use to protect its API?
A. Java Web Tokens
B. SOAP
C. PKI-HMAC
D. WS*Security
E. OAuth
F. SHA1-MD5

Ans: E

Q10. What header does Twitter use to tell you how many more API requests you can make before you will be rate limited?
A. x-request-count-down
B. x-max-requests
C. content-type
D. x-rate-limit-remaining

Ans: D
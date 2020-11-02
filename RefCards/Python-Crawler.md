# Web Scrape Related Python Modules

## Requests library

### Request APIs

  <table style="font-family: Arial,Helvetica,Sans-Serif; margin: 0 auto; width: 60vw;" cellspacing="0" cellpadding="5" border="1">
    <caption style="font-size: 1.5em; margin: 0.2em;"><a href="https://tinyurl.com/y22zaby4">Request APIs</a></caption>
    <thead>
    <tr style="font-size: 1.2em;">
      <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:30%;">Function</th>
      <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">Description</th>
      <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Return</th>
      <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:5%;">Link</th>
    </tr>
    </thead>
    <tbody>
    <tr>
      <td><code style="color: cyan;">request(method, url, **kwargs)</code></td>
      <td>Constructs and sends a Request</td>
      <td>requests.Response</td>
      <td style="text-align: center;"><a href="https://requests.readthedocs.io/en/latest/api/#requests.Request">API</a></td>
    </tr>
    <tr>
      <td><code style="color: cyan;">delete(url, **kwargs)</code></td>
      <td>Sends a DELETE request</td>
      <td>requests.Response object</td>
      <td style="text-align: center;"><a href="https://tinyurl.com/yy27nkp2">API</a></td>
    </tr>
    <tr>
      <td><code style="color: cyan;">get(url, params=None, **kwargs)</code></td>
      <td>Sends a GET request</td>
      <td>requests.Response</td>
      <td style="text-align: center;"><a href="https://requests.readthedocs.io/en/latest/api/#requests.get">API</a></td>
    </tr>
    <tr>
      <td><code style="color: cyan;">head(url, **kwargs)</code></td>
      <td>Sends a HEAD request</td>
      <td>requests.Response</td>
      <td style="text-align: center;"><a href="https://requests.readthedocs.io/en/latest/api/#requests.head">API</a></td>
    </tr>
    <tr>
      <td><code style="color: cyan;">options(url, **kwargs)</code></td>
      <td>Sends an OPTIONS request</td>
      <td>requests.Response</td>
      <td style="text-align: center;"><a href="https://requests.readthedocs.io/en/latest/api/#requests.Session.options">API</a></td>
    </tr>
    <tr>
      <td><code style="color: cyan;">patch(url, data=None, **kwargs)</code></td>
      <td>Sends a PATCH request</td>
      <td>requests.Response</td>
      <td style="text-align: center;"><a href="https://requests.readthedocs.io/en/latest/api/#requests.patch">API</a></td>
    </tr>
    <tr>
      <td><code style="color: cyan;">post(url, data=None, json=None, **kwargs)</code></td>
      <td>Sends a POST request</td>
      <td>requests.Response</td>
      <td style="text-align: center;"><a href="https://requests.readthedocs.io/en/latest/api/#requests.post">API</a></td>
    </tr>
    <tr>
      <td><code style="color: cyan;">put(url, data=None, **kwargs)</code></td>
      <td>Sends a PUT request</td>
      <td>requests.Response</td>
      <td style="text-align: center;"><a href="">API</a></td>
    </tr>
    </tbody>
  </table> 


### Request Response Class

  <table style="font-family: Arial,Helvetica,Sans-Serif; width: 60vw;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
    <caption style="font-size: 1.5em; margin: 0.2em;"><a href="https://requests.readthedocs.io/en/latest/api/#requests.Response">Request APIs</a></caption>
    <thead>
    <tr style="font-size: 1.2em;">
      <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Attribute / Function</th>
      <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:30%;">Description</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <tr>
      <td><code style="color: cyan;">status_code = None</code></td>
      <td>Integer Code of responded HTTP Status, e.g. 404 or 200</td>
    </tr>
    <tr>
      <td><code style="color: cyan;">text</code></td>
      <td><p>Content of the response, in unicode.</p>
        <p>If Response.encoding is None, encoding will be guessed using chardet.</p>
        <p>The encoding of the response content is determined based solely on HTTP headers, following RFC 2616 to the letter. If you can take advantage of non-HTTP knowledge to make a better guess at the encoding, you should set r.encoding appropriately before accessing this property.</p>
      </td>
    </tr>
      <td><code style="color: cyan;">apparent_encoding</code></td>
      <td>The apparent encoding, provided by the chardet library.</td>
    </tr>
    <tr>
      <td><code style="color: cyan;">close()</code></td>
      <td>Releases the connection back to the pool. Once this method has been called the underlying raw object must not be accessed again.</td>
    </tr>
    <tr>
      <td><code style="color: cyan;">get(url, params=None, **kwargs)</code></td>
      <td>Sends a GET request</td>
    </tr>
    <tr>
      <td><code style="color: cyan;">content</code></td>
      <td>Content of the response, in bytes.</td>
    </tr>
    <tr>
      <td><code style="color: cyan;">cookies = None</code></td>
      <td>A CookieJar of Cookies the server sent back.</td>
    </tr>
    <tr>
      <td><code style="color: cyan;">elapsed = None</code></td>
      <td>The amount of time elapsed between sending the request and the arrival of the response (as a timedelta). This property specifically measures the time taken between sending the first byte of the request and finishing parsing the headers. It is therefore unaffected by consuming the response content or the value of the stream keyword argument.</td>
    </tr>
    <tr>
      <td><code style="color: cyan;">encoding = None</code></td>
      <td>Encoding to decode with when accessing r.text.</td>
    </tr>
    <tr>
      <td><code style="color: cyan;">headers = None</code></td>
      <td>Case-insensitive Dictionary of Response Headers. For example, headers['content-encoding'] will return the value of a 'Content-Encoding' response header.</td>
    </tr>
    <tr>
      <td><code style="color: cyan;">history = None</code></td>
      <td>A list of Response objects from the history of the Request. Any redirect responses will end up here. The list is sorted from the oldest to the most recent request.</td>
    </tr>
    <tr>
      <td><code style="color: cyan;">is_permanent_redirect</code></td>
      <td>True if this Response one of the permanent versions of redirect</td>
    </tr>
    <tr>
      <td><code style="color: cyan;">is_redirect</code></td>
      <td>True if this Response is a well-formed HTTP redirect that could have been processed automatically (by <code>Session.resolve_redirects</code>).</td>
    </tr>
    <tr>
      <td><code style="color: cyan;">iter_content(chunk_size=1, decode_unicode=False)</code></td>
      <td>
        <p>Iterates over the response data. When stream=True is set on the request, this avoids reading the content at once into memory for large responses. The chunk size is the number of bytes it should read into memory. This is not necessarily the length of each item returned as decoding can take place.</p>
        <p>chunk_size must be of type int or None. A value of None will function differently depending on the value of stream. stream=True will read data as it arrives in whatever size the chunks are received. If stream=False, data is returned as a single chunk.</p>
        <p>If decode_unicode is True, content will be decoded using the best available encoding based on the response.</p>
      </td>
    </tr>
    <tr>
      <td><code style="color: cyan;">iter_lines(chunk_size=512, decode_unicode=False, delimiter=None)</code></td>
      <td>Iterates over the response data, one line at a time. When stream=True is set on the request, this avoids reading the content at once into memory for large responses.</td>
    </tr>
    <tr>
      <td><code style="color: cyan;">json(**kwargs)</code></td>
      <td>Returns the json-encoded content of a response, if any</td>
    </tr>
    <tr>
      <td><code style="color: cyan;">links</code></td>
      <td>Returns the parsed header links of the response, if any</td>
    </tr>
    <tr>
      <td><code style="color: cyan;">next</code></td>
      <td>Returns a PreparedRequest for the next request in a redirect chain, if there is one</td>
    </tr>
    <tr>
      <td><code style="color: cyan;">ok</code></td>
      <td>
        <p>Returns True if status_code is less than 400, False if not.</p>
        <p>This attribute checks if the status code of the response is between 400 and 600 to see if there was a client error or a server error. If the status code is between 200 and 400, this will return True. This is not a check to see if the response code is 200 OK.</p>
      </td>
    </tr>
    <tr>
      <td><code style="color: cyan;">raise_for_status()</code></td>
      <td>Raises HTTPError, if one occurred</td>
    </tr>
    <tr>
      <td><code style="color: cyan;">reason = None</code></td>
      <td>Textual reason of responded HTTP Status, e.g. “Not Found” or “OK”.</td>
    </tr>
    <tr>
      <td><code style="color: cyan;">request = None</code></td>
      <td>The <strong>PreparedRequest</strong> object to which this is a response</td>
    </tr>
    <tr>
      <td><code style="color: cyan;">url = None</code></td>
      <td>Final URL location of Response.</td>
    </tr>
    </tbody>
  </table> 



## BeautifulSoup library

### [Making the soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#making-the-soup)

To parse a document, pass it into the BeautifulSoup constructor. You can pass in a string or an open filehandle:

```python
from bs4 import BeautifulSoup

with open("index.html") as fp:
    soup = BeautifulSoup(fp)

soup = BeautifulSoup("<html>a web page</html>")
```


### Kinds of Objects

Beautiful Soup transforms a complex HTML document into a complex tree of Python objects.  

kinds of objects: Tag, NavigableString, BeautifulSoup, and Comment.

<table style="font-family: Arial,Helvetica,Sans-Serif; width: 60vw;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
  <caption style="font-size: 1.5em; margin: 0.2em;"><a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/#kinds-of-objects">Objects</a></caption>
  <thead>
  <tr style="font-size: 1.2em;">
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:5%;">Name</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:30%;">Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td style="text-align: center;">Tag</td>
    <td>Corresponding to an XML or HTML tag in the original document.  Tags have a lot of attributes and methods, and I’ll cover most of them in "Navigating the tree" and "Searching" the tree.</td>
  </tr>
  <tr>
    <td style="text-align: center;">NavigableString</td>
    <td><p>A string corresponds to a bit of text within a tag. Beautiful Soup uses the NavigableString class to contain these bits of text.</p><p>A NavigableString is just like a Python Unicode string, except that it also supports some of the features described in Navigating the tree and Searching the tree.</p></td>
  </tr>
  <tr>
    <td style="text-align: center;">BeautifulSoup</td>
    <td>The BeautifulSoup object represents the parsed document as a whole.</td>
  </tr>
  <tr>
    <td style="text-align: center;">Name</td>
    <td>Every tag has a name, accessible as <code>.name</code></td>
  </tr>
  <tr>
    <td style="text-align: center;">Attributes</td>
    <td><p>A tag may have any number of attributes. The tag &lt;b id="boldest"&gt; has an attribute “id” whose value is “boldest”.</p><p>access that dictionary directly as <code>.attrs</code></p></td>
  </tr>
  <tr>
    <td style="text-align: center;">Multi-valued attributes</td>
    <td>The most common multi-valued attribute is class (that is, a tag can have more than one CSS class). Others include rel, rev, accept-charset, headers, and accesskey. Beautiful Soup presents the value(s) of a multi-valued attribute as a list.</td>
  </tr>
  </tbody>
</table>



### Parsing BeautifulSoup

<table style="font-family: Arial,Helvetica,Sans-Serif; width: 60vw;" cellspacing="0" cellpadding="5" border="1">
  <caption style="font-size: 1.5em; margin: 0.2em;"><a href="url">Parser Library</a></caption>
  <thead>
  <tr style="font-size: 1.2em;">
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:5%;">Parser</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:30%;">Typical Usage</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:30%;">Advantages</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:30%;">Disadvantages</th>
  </tr>
  </thead>
  <tbody>
  <tr><td><p>Python’s html.parser</p></td>
  <td><p>BeautifulSoup(markup,"html.parser")</code></p></td>
  <td><ul>
    <li><p>Batteries included</p></li>
    <li><p>Decent speed</p></li>
    <li><p>Lenient (As of Python 2.7.3 and 3.2.)</p></li>
  </ul>
  </td>
  <td><ul>
  <li><p>Not as fast as lxml, less lenient than html5lib.</p></li>
  </ul>
  </td>
  </tr>
  <tr><td><p>lxml’s HTML parser</p></td>
  <td><p><code><span>BeautifulSoup(markup,"lxml")</code></p></td>
  <td><ul>
  <li><p>Very fast</p></li>
  <li><p>Lenient</p></li>
  </ul>
  </td>
  <td><ul> <li><p>External C dependency</p></li>  </ul>
  </td>
  </tr>
  <tr><td><p>lxml’s XML parser</p></td>
  <td><p><code><span>BeautifulSoup(markup,"lxml-xml")</code>
  <code><span>BeautifulSoup(markup,"xml")</code></p></td>
  <td><ul>
  <li><p>Very fast</p></li>
  <li><p>The only currently supported XML parser</p></li>
  </ul>
  </td>
  <td><ul>
  <li><p>External C dependency</p></li>
  </ul>
  </td>
  </tr>
  <tr><td><p>html5lib</p></td>
  <td><p><code><span>BeautifulSoup(markup,"html5lib")</code></p></td>
  <td><ul>
  <li><p>Extremely lenient</p></li>
  <li><p>Parses pages the same way a web browser does</p></li>
  <li><p>Creates valid HTML5</p></li>
  </ul>
  </td>
  <td><ul>
  <li><p>Very slow</p></li>
  <li><p>External Python dependency</p></li>
  </ul>
  </td>
  </tr>
  </tbody>
</table>


### Navigating the tree
  
+ Navigating using tag names
  + navigating the parse tree is to say the name of the tag you want
    + e.g., `soup.head     # <head><title>The Dormouse's story</title></head>`
  + applied again and again to zoom in on a certain part of the parse tree

<table style="font-family: Arial,Helvetica,Sans-Serif; width: 60vw;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
  <caption style="font-size: 1.5em; margin: 0.2em;"><a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/#navigating-using-tag-names">Attributes to Navigate Tree </a></caption>
  <thead>
  <tr style="font-size: 1.2em;">
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:5%;">Attributes</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">Usage</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:50%;">Examples</th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td style="color: cyan;"><code>soup.tagname</code></td>
    <td>the name of the tag to navigate the parse tree</td>
    <td style="font-family: monospace;">soup.head<br/><span style="color: grey;"># &lt;head&gt;&lt;title&gt;The Dormouse's story&gtl&lt;/title&gt;&lt;/head&gt;<br/><br/>soup.title<br/><span style="color: grey;"># &lt;title&gt;The Dormouse's story&lt;/title&gt;<br/><br/>soup.body.b<br/><span style="color: grey;"># &lt;b&gt;The Dormouse's story&lt;/b&gt;</td>
  </tr>
  <tr>
    <td style="color: cyan;"><code>.contents</code></td>
    <td>a list of a tag's children</td>
    <td style="font-family: monospace;">head_tag = soup.head<br/><span style="color: grey;"># &lt;head&gt;&lt;title&gt;The Dormouse's story&lt;/title&gt;&lt;/head&gt;<br/><br/>head_tag.contents>br/><span style="color: grey;"># [&lt;title&gt;The Dormouse's story&lt;/title&gt;]</td>
  </tr>
  <tr>
    <td style="color: cyan;"><code>.children</code></td>
    <td>iterate over a tag’s children for a string</td>
    <td style="font-family: monospace;">text = title_tag.contents[0]<br/>text.contents<br/><span style="color: grey;"># AttributeError: 'NavigableString' object has no attribute 'contents'<br/><br/>for child in title_tag.children:<br/>&nbsp;&nbsp;&nbsp;&nbsp;print(child)<br/><span style="color: grey;"># The Dormouse's story>/span></td>
  </tr>
  <tr>
    <td style="color: cyan;"><code>.descendants</code></td>
    <td>iterate over all of a tag’s children, recursively</td>
    <td style="font-family: monospace;">for child in head_tag.descendants:<br/>&nbsp;&nbsp;&nbsp;&nbsp;print(child)<br/><span style="color: grey;"># &lt;title&gt;The Dormouse's story&lt;/title&gt;<br/># The Dormouse's story<span></td>
  </tr>
  <tr>
    <td style="color: cyan;"><code>.string</code></td>
    <td><p>If a tag has only one child, and that child is a NavigableString.</p><p>If a tag’s only child is another tag, and that tag has a .string, then the parent tag is considered to have the same .string as its child</p><p>If there’s more than one thing inside a tag, you can still look at just the strings.</p></td>
    <td style="font-family: monospace;">title_tag.string<br/><span style="color: grey;"># u'The Dormouse's story'<br/><br/>head_tag.contents<br/><span style="color: grey;"># [&lt;title&gt;The Dormouse's story&lt;/title&gt;]<br/>head_tag.string<br/><span style="color: grey;"># u'The Dormouse's story'<br/><br/>for string in soup.strings:<br/>&nbsp;&nbsp;&nbsp;&nbsp;print(repr(string))<br/><span style="color: grey;"># u"The Dormouse's story"<br/># u'\n\n'<br/># u"The Dormouse's story"<br/># u'\n\n'</td>
  </tr>
  <tr>
    <td style="color: cyan;"><code>.stripped_strings</code></td>
    <td>the <code>.strings</code> generator provides extra white spaces. <.stripped_strings</code> removes them</td>
    <td style="font-family: monospace;">for string in soup.strings:<br/>&nbsp;&nbsp;&nbsp;&nbsp;print(repr(string))<br/><span style="color: grey;"># u"The Dormouse's story"<br/># u"The Dormouse's story"</td>
  </tr>
  <tr>
    <td style="color: cyan;"><code>.parent</code></td>
    <td>access an element’s parent</td>
    <td style="font-family: monospace;">title_tag = soup.title<br/>title_tag<br/><span style="color: grey;"># &lt;title&gt;The Dormouse's story&lt;/title&gt;<br/>title_tag.parent<br/><span style="color: grey;"># &lt;head&gt;&lt;title&gt;The Dormouse's story&lt;/title&gt;&lt;/head&gt;</td>
  </tr>
  <tr>
    <td style="color: cyan;"><code>.parents</code></td>
    <td>iterate over all of an element’s parents with .parents</td>
    <td style="font-family: monospace;">link = soup.a<br/>link<br/><span style="color: grey;"># &lt;a class="sister" href="http://example.com/elsie" id="link1"&gt;Elsie&lt;/a&gt;<br/>for parent in link.parents:<br/>&nbsp;&nbsp;&nbsp;&nbsp;if parent is None:<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(parent)<br/>&nbsp;&nbsp;&nbsp;&nbsp;else:<<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(parent.name)<br/><span style="color: grey;"># p<br/># body<br/># html<br/># [document]<br/># None</td>
  </tr>
  <tr>
    <td style="color: cyan;"><code>.next_sibling<br/><br/>.previous_sibling</code></td>
    <td>navigate between page elements that are on the same level of the parse tree</td>
    <td style="font-family: monospace;">sibling_soup.b.next_sibling<br/><span style="color: grey;"># &lt;c&gt;text2&lt;/c&gt;<br/><br/>sibling_soup.c.previous_sibling<br/><span style="color: grey;"># &lt;b&gt;text1&lt;/b&gt;<br/><br/>sibling_soup.b.string<br/><span style="color: grey;"># u'text1'</td>
  </tr>
  <tr>
    <td style="color: cyan;"><code>.next_siblings<br/><br/>.previous_siblings</code></td>
    <td>iterate over a tag’s siblings</td>
    <td style="font-family: monospace;">for sibling in soup.a.next_siblings:<br/>&nbsp;&nbsp;&nbsp;&nbsp;print(repr(sibling))<br/><span style="color: grey;"># u',\n'<br/># &lt;a class="sister" href="http://example.com/lacie" id="link2"&gt;Lacie&lt;/a&gt;<br/># u' and\n'<br/># &lt;a class="sister" href="http://example.com/tillie" id="link3"&gt;Tillie&lt;/a&gt;<br/># u'; and they lived at the bottom of a well.'<br/># None<span style="color: grey;"></td>
  </tr>
  <tr>
    <td style="color: cyan;"><code>.next_element</code></td>
    <td>point to whatever was parsed immediately afterwards</td>
    <td style="font-family: monospace;">last_a_tag.next_element<br/><span style="color: grey;"># u'Tillie'</td>
  </tr>
  <tr>
    <td style="color: cyan;"><code>.previous_element</code></td>
    <td>point to whatever element was parsed immediately before this one</td>
    <td style="font-family: monospace;">last_a_tag.previous_element<br/><span style="color: grey;"># u' and\n'</td>
  </tr>
  <tr>
    <td style="color: cyan;"><code>.next_elements<br/><br/>.previous_elements</code></td>
    <td>iterators to move forward or backward in the document as it was parsed</td>
    <td style="font-family: monospace;">for element in last_a_tag.next_elements:<br/>&nbsp;&nbsp;&nbsp;&nbsp;print(repr(element))<br/><span style="color: grey;"># u'Tillie'<br/># u';\nand they lived at the bottom of a well.'</td>
  </tr>
  </tbody>
</table>


### Searching the tree

+ Filters
  + a string
    + passing a string to a search method and Beautiful Soup
    + performing a match against that exact string
    + e.g., `soup.find_all('b') # [<b>The Dormouse's story</b>]`
  + a regular expression
    + passing in a regular expression object
    + filtering against that regular expression using `search()` method
    + e.g., 

      ```python
      for tag in soup.find_all(re.compile("^b")):
        print(tag.name)

      # body
      # b
      ```

    + a list
      + allowING a string match against any item in that lisT
      + example:

        ```python
        soup.find_all(["a", "b"])
        # [<b>The Dormouse's story</b>,
        #  <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
        #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
        #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
        ```

    + `True`
      + matching everything it can
      + example

        ```python
        for tag in soup.find_all(True):
            print(tag.name)
        # html
        # head
        # title
        # body
        # p
        # b
        # p
        # a
        # a
        # a
        # p
        ```

    + a function
      + define a function that takes an element as its only argument
      + return True if the argument matches, and False otherwise
      + example

        ```python
        def has_class_but_no_id(tag):
            return tag.has_attr('class') and not tag.has_attr('id')

        soup.find_all(has_class_but_no_id)
        # [<p class="title"><b>The Dormouse's story</b></p>,
        #  <p class="story">Once upon a time there were…bottom of a well.</p>,
        #  <p class="story">...</p>]

        from bs4 import NavigableString

        def surrounded_by_strings(tag):
            return (isinstance(tag.next_element, NavigableString)
                    and isinstance(tag.previous_element, NavigableString))

        for tag in soup.find_all(surrounded_by_strings):
            print tag.name
        # p
        # a
        # a
        # a
        # p
        ```


### BeautifulSoup Searching Methods

<table style="font-family: Arial,Helvetica,Sans-Serif; width: 60vw;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
  <caption style="font-size: 1.5em; margin: 0.2em;"><a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/#a-function">Searching Methods </a></caption>
  <thead>
  <tr style="font-size: 1.2em;">
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Method / Argument</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:30%;">Description</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:30%;">Examples</th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td style="color: cyan;">find_all( name, attrs, recursive, string, limit, **kwargs)</td>
    <td>look through a tag’s descendants and retrieves all descendants that match your filters<br/><br/>the most popular method in the Beautiful Soup search API</td>
    <td colspan="2" style="font-family: monospace;">
      soup.find_all("title")<br/>
      <span style="color: grey;"># [&lt;title&gt;The Dormouse's story&lt;/title&gt;]</span><br/><br/>
      soup.find_all("p", "title")<br/>
      <span style="color: grey;"># [&lt;p class="title"&gt;&lt;b&gt;The Dormouse's story&lt;/b&gt;&lt;/p&gt;]</span><br/><br/>
      soup.find_all("a")<br/>
      <span style="color: grey;"># [&lt;a class="sister" href="http://example.com/elsie" id="link1"&gt;Elsie&lt;/a&gt;,</span><br/>
      <span style="color: grey;">#  &lt;a class="sister" href="http://example.com/lacie" id="link2"&gt;Lacie&lt;/a&gt;,</span><br/>
      <span style="color: grey;">#  &lt;a class="sister" href="http://example.com/tillie" id="link3"&gt;Tillie&lt;/a&gt;]</span><br/><br/>
      soup.find_all(id="link2")<br/>
      <span style="color: grey;"># [&lt;a class="sister" href="http://example.com/lacie" id="link2"&gt;Lacie&lt;/a&gt;]</span><br/><br/>
      import re<br/>
      soup.find(string=re.compile("sisters"))<br/>
      <span style="color: grey;"># u'Once upon a time there were three little sisters; and their names were\n'</span><br/><br/>
      soup.find_all("a")<br/>
      soup("a")<br/><br/>
      soup.title.find_all(string=True)<br/>
      soup.title(string=True)
    </td>
  </tr>
    <td style="color: cyan;"><code>name</code></td>
    <td>tell Beautiful Soup to only consider tags with certain names<br/><br/>Text strings ignored</td>
    <td style="font-family: monospace;">soup.find_all("title")<br/><span style="color: grey;"># [&lt;title&gt;The Dormouse's story&lt;/title&gt;]</td>
  </tr>
  <tr>
    <td style="color: cyan;"><code>keyword</code></td>
    <td>
      any argument not recognized to turn into a filter on one of a tag’s attributes
      filter an attribute based on a string, a regular expression, a list, a function, or the value True<br/><br/>
      filter multiple attributes at once by passing in more than one keyword argument<br/><br/>
      attributes names unable to be used as the names of keyword arguments<br/><br/>
      unable to use a keyword argument to search for HTML’s ‘name’ element, because Beautiful Soup uses the name argument to contain the name of the tag itself
    </td>
    <td style="font-family: monospace;">
      soup.find_all(href=re.compile("elsie"), id='link1')<br/>
      <span style="color: grey;"># [&lt;a class="sister" href="http://example.com/elsie" id="link1"&gt;three&lt;/a&gt;]</span><br/><br/>
      soup.find_all(href=re.compile("elsie"),id='link1')<br/>
      <span style="color: grey;"># [&lt;a class="sister" href="http://example.com/elsie" id="link1"&gt;three&lt;/a&gt;]</span><br/><br/>
      data_soup = BeautifulSoup('&lt;div data-foo="value"&gt;foo!&lt;/div&gt;')<br/>
      data_soup.find_all(data-foo="value")<br/>
      <span style="color: grey;"># SyntaxError: keyword can't be an expression</span><br/><br/>
      name_soup = BeautifulSoup('&lt;input name="email"/&gt;')<br/>
      name_soup.find_all(name="email")<br/>
      <span style="color: grey;"># []</span><br/>
      name_soup.find_all(attrs={"name": "email"})<br/>
      <span style="color: grey;"># [&lt;input name="email"/&gt;]</span>
    </td>
  </tr>
  <tr>
    <td style="color: cyan;"><code>id</code></td>
    <td>
      pass in a value for an argument called id, Beautiful Soup will filter against each tag’s ‘id’ attribute<br/><br/>
    </td>
    <td style="font-family: monospace;">
      soup.find_all(id='link2')<br/>
      <span style="color: grey;"># [&lt;a class="sister" href="http://example.com/lacie" id="link2"&gt;Lacie&lt;/a&gt;]</span><br/><br/>
      soup.find_all(id=True)<br/>
      <span style="color: grey;"># [&lt;a class="sister" href="http://example.com/elsie" id="link1"&gt;Elsie&lt;/a&gt;,<br/>
      #  &lt;a class="sister" href="http://example.com/lacie" id="link2"&gt;Lacie&lt;/a&gt;,<br/>
      #  &lt;a class="sister" href="http://example.com/tillie" id="link3"&gt;Tillie&lt;/a&gt;]</span>
    </td>
  </tr>
  <tr>
    <td style="color: cyan;"><code>href</code></td>
    <td>pass in a value for href, Beautiful Soup will filter against each tag’s ‘href’ attribute</td>
    <td style="font-family: monospace;">soup.find_all(href=re.compile("elsie"))<br/><span style="color: grey;"># [&lt;a class="sister" href="http://example.com/elsie" id="link1"&gt;Elsie&lt;/a&gt;]</span>
    </td>
  </tr>
  <tr>
    <td style="color: cyan;"><code>attrs</code></td>
    <td>
      using these attributes in searches by putting them into a dictionary and passing the dictionary as the attrs argument
    </td>
    <td style="font-family: monospace;">
      data_soup.find_all(attrs={"data-foo": "value"})</span><br/>
      <span style="color: grey;"># [&lt;div data-foo="value"&gt;foo!&lt;/div&gt;]</span>
    </td>
  </tr>
  <tr>
    <td style="color: cyan;"><code>class_</code></td>
    <td>
      “class”, is a reserved word in Python<br/><br/>
      pass <code>class_</code> a string, a regular expression, a function, or True<br/><br/>
      multiple values for its “class” attribute<br/><br/>
      search for the exact string value<br/><br/>
      no searching for variants of the string value<br/><br/>
      search for tags that match two or more CSS classes
    </td>
    <td style="font-family: monospace;">
      soup.find_all(class_=re.compile(<span class="s2">"itl"))<br/><span style="color: grey;"># [&lt;p class="title"&gt;&lt;b&gt;The Dormouse's story&lt;/b&gt;&lt;/p&gt;]</span><br/><br/>
      def <span class="nf">has_six_characters(css_class):<br/>
      &nbsp;&nbsp;&nbsp;&nbsp;return css_class >is >not None >and len(css_class) <span class="o">== 6<br/><br/>
      soup.find_all(class_=has_six_characters)<br/>
      <span style="color: grey;"># [&lt;a class="sister" href="http://example.com/elsie" id="link1"&gt;Elsie&lt;/a&gt;,<br/>
      #  &lt;a class="sister" href="http://example.com/lacie" id="link2"&gt;Lacie&lt;/a&gt;,<br/>
      #  &lt;a class="sister" href="http://example.com/tillie" id="link3"&gt;Tillie&lt;/a&gt;]</span><br/><br/>
      css_soup=</span> BeautifulSoup('&lt;p class="body strikeout"&gt;&lt;/p&gt;')<br/>
      css_soup.find_all(<span class="s2">"p", class_=<span class="s2">"strikeout")<br/>
      <span style="color: grey;"># [&lt;p class="body strikeout"&gt;&lt;/p&gt;]</span><br/><br/>
      css_soup.find_all(<span class="s2">"p", class_=<span class="s2">"body")<br/>
      <span style="color: grey;"># [&lt;p class="body strikeout"&gt;&lt;/p&gt;]</span><br/><br/>
      css_soup.find_all(<span class="s2">"p", class_=<span class="s2">"body strikeout")<br/>
      <span style="color: grey;"># [&lt;p class="body strikeout"&gt;&lt;/p&gt;]</span><br/>
      css_soup.select(<span class="s2">"p.strikeout.body")
      <span style="color: grey;"># [&lt;p class="body strikeout"&gt;&lt;/p&gt;]</span>
    </td>
  </tr>
  <tr>
    <td style="color: cyan;"><code>string</code></td>
    <td>pass in a string, a regular expression, a list, a function, or the value True<br/><br/>combine it with arguments that find tags: Beautiful Soup will find all tags whose .string matches your value for string</td>
    <td style="font-family: monospace;">
      soup.find_all(string="Elsie")<br/>
      <span style="color: grey;"># [u'Elsie']</span><br/><br/>
      soup.find_all(string=["Tillie","Elsie","Lacie"])<br/>
      <span style="color: grey;"># [u'Elsie', u'Lacie', u'Tillie']</span><br/><br/>
      soup.find_all(string=re.compile("Dormouse"))<br/>
      [u"The Dormouse's story", u"The Dormouse's story"]<br/><br/>
      def is_the_only_string_within_a_tag(s):<br/>
      &nbsp;&nbsp;&nbsp;&nbsp;"""Return True if this string is the only child of its parent tag."""<br/>
      &nbsp;&nbsp;&nbsp;&nbsp;return (s== s.parent.string)<br/><br/>
      soup.find_all(string=is_the_only_string_within_a_tag)</span><br/>
      <span style="color: grey;"># [u"The Dormouse's story", u"The Dormouse's story", u'Elsie', u'Lacie', u'Tillie', u'...']</span><br/><br/>
      soup.find_all("a", string="Elsie")<br/>
      <span style="color: grey;"># [&lt;a href="http://example.com/elsie" class="sister" id="link1"&gt;Elsie&lt;/a&gt;]</span>
    </td>
  </tr>
  <tr>
    <td style="color: cyan;"><code>limit</code></td>
    <td>pass in a number for limit to tell Beautiful Soup to stop gathering results after it’s found a certain number</td>
    <td style="font-family: monospace;">
      soup.find_all("a",</span> <span style="color: grey;">limit=</span><span class="mi">2)</span><br/>
      <span style="color: grey;"># [&lt;a class="sister" href="http://example.com/elsie" id="link1"&gt;Elsie&lt;/a&gt;,</span><br/>
      <span style="color: grey;">#  &lt;a class="sister" href="http://example.com/lacie" id="link2"&gt;Lacie&lt;/a&gt;]</span>
    </td>
  </tr>
  <tr>
    <td style="color: cyan;"><code>recursive </code></td>
    <td>consider direct children<br/>call <code>mytag.find_all()</code>, Beautiful Soup examining all the descendants of mytag: its children, its children’s children, and so on</td>
    <td style="font-family: monospace;">
    soup.html.find_all("title")</span><br/>
    <span style="color: grey;"># [&lt;title&gt;The Dormouse's story&lt;/title&gt;]</span><br/><br/>
    soup.html.find_all("title", recursive=False)<br/>
    <span style="color: grey;"># []</span>
    </td>
  </tr>
  <tr>
    <td style="color: cyan;"><code>find()</code></td>
    <td>same as <code>find_all()</code> passing in <code>limit=1</code><br/><br/>just returns the result while <code>find_all()</code> returns a list containing the single result</td>
    <td style="font-family: monospace;">
      soup.find_all('title', limit=1)<br/>
      <span style="color: grey;"># [&lt;title&gt;The Dormouse's story&lt;/title&gt;]</span><br/><br/>
      soup.find('title')<br/>
      <span style="color: grey;"># &lt;title&gt;The Dormouse's story&lt;/title&gt;</span><br/>
      print(soup.find("nosuchtag"))</span><br/>
      <span style="color: grey;"># None</span><br/><br/>
      soup.head.title<br/>
      <span style="color: grey;"># &lt;title&gt;The Dormouse's story&lt;/title&gt;</span><br/><br/>
      soup.find>("head">).find>("title">)<br/>
      <span style="color: grey;"># &lt;title&gt;The Dormouse's story&lt;/title&gt;</span>
    </td>
  </tr>
  <tr>
    <td style="color: cyan;"><code>find_parents()<br/><br/>find_parent()</code></td>
    <td>work way up the tree, looking at a tag’s (or a string’s) parents</td>
    <td style="font-family: monospace;">
      a_string=soup.find>(string="Lacie">)<br/>
      a_string</span><br/>
      <span style="color: grey;"># u'Lacie'</span><br/><br/>
      a_string.find_parents>("a">)<br/>
      <span style="color: grey;"># [&lt;a class="sister" href="http://example.com/lacie" id="link2"&gt;Lacie&lt;/a&gt;]</span><br/><br/>
      a_string.find_parent>("p">)<br/>
      <span style="color: grey;"># &lt;p class="story"&gt;Once upon a time there were three little sisters; and their names were</span><br/>
      <span style="color: grey;">#  &lt;a class="sister" href="http://example.com/elsie" id="link1"&gt;Elsie&lt;/a&gt;,</span><br/>
      <span style="color: grey;">#  &lt;a class="sister" href="http://example.com/lacie" id="link2"&gt;Lacie&lt;/a&gt; and</span><br/>
      <span style="color: grey;">#  &lt;a class="sister" href="http://example.com/tillie" id="link3"&gt;Tillie&lt;/a&gt;;</span><br/>
      <span style="color: grey;">#  and they lived at the bottom of a well.&lt;/p&gt;</span><br/><br/>
      a_string.find_parents>("p">,</span> class="title">)<br/>
      <span style="color: grey;"># []</span>
    </td>
  </tr>
  <tr>
    <td style="color: cyan;"><code>find_next_siblings()<br/><br/>find_next_sibling()</code></td>
    <td><code>find_next_siblings()</code> method returns all the siblings that match, and <code>find_next_sibling()</code> only returns the first one</td>
    <td style="font-family: monospace;">
      first_link=soup.a<br/>
      first_link<br/>
      <span style="color: grey;"># &lt;a class="sister" href="http://example.com/elsie" id="link1"&gt;Elsie&lt;/a&gt;</span><br/><br/>
      first_link.find_next_siblings>("a">)<br/>
      <span style="color: grey;"># [&lt;a class="sister" href="http://example.com/lacie" id="link2"&gt;Lacie&lt;/a&gt;,</span><br/>
      <span style="color: grey;">#  &lt;a class="sister" href="http://example.com/tillie" id="link3"&gt;Tillie&lt;/a&gt;]</span><br/><br/>
      first_story_paragraph= soup.find>("p">,>"story">)<br/>
      first_story_paragraph.find_next_sibling>("p">)<br/>
      <span style="color: grey;"># &lt;p class="story"&gt;...&lt;/p&gt;</span>
    </td>
  </tr>
  <tr>
    <td style="color: cyan;"><code>find_previous_siblings()<br/><br/>find_previous_sibling()</code></td>
    <td><code>find_previous_siblings()</code> method returns all the siblings that match, and <code>find_previous_sibling()</code> only returns the first one</td>
    <td style="font-family: monospace;">
      last_link= soup.find>("a">, id="link3">)<br/>
      last_link<br/>
      <span style="color: grey;"># &lt;a class="sister" href="http://example.com/tillie" id="link3"&gt;Tillie&lt;/a&gt;</span><br/><br/>
      last_link.find_previous_siblings>("a">)<br/>
      <span style="color: grey;"># [&lt;a class="sister" href="http://example.com/lacie" id="link2"&gt;Lacie&lt;/a&gt;,</span><br/>
      <span style="color: grey;">#  &lt;a class="sister" href="http://example.com/elsie" id="link1"&gt;Elsie&lt;/a&gt;]</span><br/><br/>
      first_story_paragraph=</span> soup.find>("p">,>"story">)<br/>
      first_story_paragraph.find_previous_sibling>("p">)<br/>
      <span style="color: grey;"># &lt;p class="title"&gt;&lt;b&gt;The Dormouse's story&lt;/b&gt;&lt;/p&gt;</span><br/><br/>
    </td>
  </tr>
  <tr>
    <td style="color: cyan;"><code>find_all_next()<br/><br/>find_next()</code></td>
    <td><code>find_all_next()</code> method returns all matches, and f<code>ind_next()</code> only returns the first match</td>
    <td style="font-family: monospace;">
      first_link = soup.a<br/>
      first_link<br/>
      <span style="color: grey;"># &lt;a class="sister" href="http://example.com/elsie" id="link1"&gt;Elsie&lt;/a&gt;</span><br/><br/>
      first_link.find_all_next>(string=</span><span class="kc">True>)<br/>
      <span style="color: grey;"># [u'Elsie', u',\n', u'Lacie', u' and\n', u'Tillie',</span><br/>
      <span style="color: grey;">#  u';\nand they lived at the bottom of a well.', u'\n\n', u'...', u'\n']</span><br/><br/>
      first_link.find_next>("p">)<br/>
      <span style="color: grey;"># &lt;p class="story"&gt;...&lt;/p&gt;</span>
    </td>
  </tr>
  <tr>
    <td style="color: cyan;"><code>find_all_previous()<br/><br/>find_previous()</code></td>
    <td><code>find_all_previous()</code> method returns all matches, and <code>find_previous()</code> only returns the first match</td>
    <td style="font-family: monospace;">
      first_link = soup.a<br/>
      first_link<br/>
      <span style="color: grey;"># &lt;a class="sister" href="http://example.com/elsie" id="link1"&gt;Elsie&lt;/a&gt;</span><br/><br/>
      first_link.find_all_previous("p")<br/>
      <span style="color: grey;"># [&lt;p class="story"&gt;Once upon a time there were three little sisters; ...&lt;/p&gt;,</span><br/>
      <span style="color: grey;">#  &lt;p class="title"&gt;&lt;b&gt;The Dormouse's story&lt;/b&gt;&lt;/p&gt;]</span><br/><br/>
      first_link.find_previous("title")<br/>
      <span style="color: grey;"># &lt;title&gt;The Dormouse's story&lt;/title&gt;</span>
    </td>
  </tr>
  </tbody>
</table>



  


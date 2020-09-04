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


  


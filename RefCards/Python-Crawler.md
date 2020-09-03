# Web Scrape Related Python Modules

## Requests library

  <table style="font-family: Arial,Helvetica,Sans-Serif; width: 60vw;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
    <caption style="font-size: 1.5em; margin: 0.2em;"><a href="https://tinyurl.com/y22zaby4">Request APIs</a></caption>
    <thead>
    <tr style="font-size: 1.2em;">
      <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">Function</th>
      <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:30%;">Description</th>
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


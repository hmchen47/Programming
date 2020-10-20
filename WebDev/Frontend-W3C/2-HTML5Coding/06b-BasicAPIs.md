# Week 6: HTML5 Basic APIs


## 6.2 The Web Storage API


### 6.2.0 Lecture Notes







### 6.2.1 The Web storage API

The Web storage API introduces "two related mechanisms, similar to HTTP session cookies, for storing structured data on the client side".

Indeed, Web Storage provides two interfaces - `sessionStorage` and `localStorage` - whose main difference is data longevity. This specification defines an API for persistent data storage of key-value pair data in Web clients.

<p style="border: 1px solid red; margin: 20px; padding: 20px;"><strong>With <span style="font-family: 'courier new', courier;">localStorage</span> the data will remain until it is deleted, whereas with <span style="font-family: 'courier new', courier;">sessionStorage</span> the data is erased when the tab/browser is closed.</strong></p>

For convenience, we will mainly illustrate the `localStorage` object. Just change "local" to "session" and it should work (this time with a session lifetime).key value pairs


#### Simple key-value stores, one per domain (following the same origin policy)!

`localStorage` is a simple key-value store, in which the keys and values are strings. There is only one store per domain. This functionality is exposed through the globally available `localStorage` object. The same applies to `sessionStorage`.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y6nsroaz')"
    src    ="https://tinyurl.com/y5en4w7j"
    alt    ="key value pairs"
    title  ="key value pairs"
  />
</figure>


Example:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com">// Using localStorage</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="com">// store data</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">localStorage</span><span class="pun">.</span><span class="pln">lastName </span><span class="pun">=</span><span class="pln"> </span><span class="str">"Bunny"</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">localStorage</span><span class="pun">.</span><span class="pln">firstName </span><span class="pun">=</span><span class="pln"> </span><span class="str">"Bugs"</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">localStorage</span><span class="pun">.</span><span class="pln">location </span><span class="pun">=</span><span class="pln"> </span><span class="str">"Earth"</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="com">// retrieve data</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> lastName </span><span class="pun">=</span><span class="pln"> localStorage</span><span class="pun">.</span><span class="pln">lastName</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> firstName </span><span class="pun">=</span><span class="pln"> localStorage</span><span class="pun">.</span><span class="pln">firstName</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> location </span><span class="pun">=</span><span class="pln"> localStorage</span><span class="pun">.</span><span class="pln">location</span><span class="pun">;</span></li>
</ol></div>

This data is located in a store attached to the origin of the page. We created a [JSBin example in which we included the above code](https://jsbin.com/povuqa/1/edit). ([Local Example - key-value pair](src/6.2.1-example.html))

Once opened in your browser, the JavaScript code is executed. With the browser dev. tools, we can check what has been stored in the `localStorage` for this domain:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
    onclick="window.open('https://tinyurl.com/y6nsroaz')"
    src    ="https://tinyurl.com/y6gy7qzu"
    alt    ="example of localStorage"
    title  ="example of localStorage"
  />
</figure>


Here is a view of the devtools. In more recent versions of Google Chrome, the "Resources" tab is named "Applications":

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
    onclick="window.open('https://tinyurl.com/y6nsroaz')"
    src    ="https://tinyurl.com/y3hwnf95"
    alt    ="dev tools can be used to show what is in the local storage"
    title  ="dev tools can be used to show what is in the local storage"
  />
</figure>


#### Differences with cookies?

Cookies are also a popular way to store key-value pairs. Web Storage, however, is a more powerful technique than cookies. The main difference is in size limits: cookies are limited to a few KBytes whereas Web Storage may extend to several MBytes. Also cookies generate additional HTTP request traffic (whether to request a Web page, an image, a stylesheet, a JavaScript file, etc.).

Objects managed by Web Storage are no longer carried on the network and HTTP, and are easily accessible (read, change and delete) from JavaScript, using the Web Storage API.


#### External resources

+ From W3C's specification: [The W3C Web Storage API recommendation](https://tinyurl.com/mzurr3x)
+ An Interesting article on Web.dev: [Storage for the Web](https://tinyurl.com/y7zzerln)
+ From MDN's Web Docs: [Web Storage API](https://tinyurl.com/m7apsg2)







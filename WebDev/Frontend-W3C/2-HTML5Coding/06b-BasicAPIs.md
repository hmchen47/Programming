# Week 6: HTML5 Basic APIs


## 6.2 The Web Storage API


### 6.2.0 Lecture Notes

+ [Web Storage API](#621-the-web-storage-api)
  + similar to HTTP session cookies
  + two related mechanisms for storing structured data on the client side
    + `sessionStorage`:
      + erased when the tab/browser closed
      + tab specific, and scoped to the lifetime of the tab
      + useful for storing small amounts of session specific information
      + used with caution: synchronous and blocking the main thread
      + limited to about 5MB and containing only strings
      + not accessible from web workers or service workers
      + data never transferred to the server
      + storage limit larger than a cookie
    + `localStorage`:
      + data remained until deleted
      + avoided due to synchronous to block the main thread
      + limited to about 5MB and containing only strings
      + not accessible from web workers or service workers
      + stored data w/o expiration date
      + get cleared only through JavaScript, or clearing the Browser cache / Locally Stored Data
      + storage limit: the maximum amongst the three
  + main difference: data longevity
  + key-value store for `localStorage`
    + a simple key-value store
    + the keys and values: strings
    + only one store per domain
    + same applies to `sessionStorage`
    + functionality exposed through the globally available `localStorage` object
    + example

      ```js
      // store data
      localStorage.lastName = "Bunny";
      localStorage.firstName = "Bugs";
      localStorage.location = "Earth";

      // retrieve data
      var lastName = localStorage.lastName;
      var firstName = localStorage.firstName;
      var location = localStorage.location;
      ```

  + [example: save & restore form contents on the fly](#622-example-1)
    + save the first name input field's content: `oninput="localStorage.firstName=this.value;"`
    + restoring the form content on page load/reload: `if (localStorage.firstName !== undefined) document.getElementById("firstName").value = localStorage.firstName;`

+ [Cookies & Web Storage](#differences-with-cookies)
  + main difference: limits
  + cookie:
    + a popular way to store key-value pairs
    + cookies limited to a few KBytes
    + generate additional HTTP request traffic: request a Web page, an image, a stylesheet, a JavaScript file, etc.
    + not used for storage
    + sent with every HTTP request
    + storing anything more than a small amount of data
    + significantly increasing the size of every web request
    + limited to only strings
  + Web Storage: a more powerful technique than cookies
    + Web Storage extended to several MBytes
    + objects managed no longer carried on the network and HTTP
    + easily accessible (read, change and delete) from JavaScript
    + using the Web Storage API





### 6.2.1 The Web storage API

The Web storage API introduces "two related mechanisms, similar to HTTP session cookies, for storing structured data on the client side".

Indeed, Web Storage provides two interfaces - `sessionStorage` and `localStorage` - whose main difference is data longevity. This specification defines an API for persistent data storage of key-value pair data in Web clients.

<p style="border: 1px solid red; margin: 20px; padding: 20px;"><strong>With <span style="font-family: 'courier new', courier;">localStorage</span> the data will remain until it is deleted, whereas with <span style="font-family: 'courier new', courier;">sessionStorage</span> the data is erased when the tab/browser is closed.</strong></p>

For convenience, we will mainly illustrate the `localStorage` object. Just change "local" to "session" and it should work (this time with a session lifetime).key value pairs


#### Simple key-value stores, one per domain (following the same origin policy)!

`localStorage` is a simple key-value store, in which the keys and values are strings. There is only one store per domain. This functionality is exposed through the globally available `localStorage` object. The same applies to `sessionStorage`.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
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

This data is located in a store attached to the origin of the page. We created a [JSBin example in which we included the above code](https://jsbin.com/povuqa/1/edit). ([Local Example - key-value pair](src/6.2.1-example1.html))

Once opened in your browser, the JavaScript code is executed. With the browser dev. tools, we can check what has been stored in the `localStorage` for this domain:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick="window.open('https://tinyurl.com/y6nsroaz')"
    src    ="https://tinyurl.com/y6gy7qzu"
    alt    ="example of localStorage"
    title  ="example of localStorage"
  />
</figure>


Here is a view of the devtools. In more recent versions of Google Chrome, the "Resources" tab is named "Applications":

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
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


### 6.2.2 Example 1

You can start filling this form and come back another day and complete it. It doesn't matter if you closed your browser before coming back. The form never loses what you entered, even if you reload the page, or press "backspace" by mistake. __This form auto saves/restores its content.__

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick="window.open('https://tinyurl.com/y56ul3qd')"
    src    ="https://tinyurl.com/y2gfb6f7"
    alt    ="form screenshot, a form that saves/restores its content as we type"
    title  ="form screenshot, a form that saves/restores its content as we type"
  />
</figure>

In this example, we use the most simple way to use `localStorage`:

+ __Save with the localStorage.key = value syntax.__ For example, `localStorage.firstName = 'Michel'` will save the value "Michel" with the access key being 'firstName'
+ __Restore with the var value = localStorage.key syntax.__ For example, `var fn = localStorage.firstName;` will set fn with the value 'Michel' if this value has been previously saved as in the example from the line above.


#### Saving the form content on the fly

Open this [online example at JSBin](https://jsbin.com/zezudo/edit?html,output), and use F12 or cmd-alt-i (Mac OS) to look at the dev. tools. As you type in the different input fields, their content is updated in the `localStorage`. ([Local Example - Saving Contents](src/6.2.2-example1.html))

We just added input event listeners to each input field. For example, in order to save the first name input field's content, we just added:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">oninput</span><span class="pun">=</span><span class="str">"localStorage.<span style="color: #ff0000;">firstName</span>=this.value;"</span></li>
</ol></div>

Where `firstName` in red is the key and `this.value` the current value of the input field.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
    onclick="window.open('https://tinyurl.com/y56ul3qd')"
    src    ="https://tinyurl.com/yxrw28md"
    alt    ="As we are filing a form text input type, its content is saved in local storage. The image shows the httml coe of the input type, that as a oninput='localStorage.firstName = this.value". Devtools are open on the "Applications" tab and show the LocalStorage content. It has the same value as what has been typed in the form firstName field."
    title  ="As we are filing a form text input type, its content is saved in local storage. The image shows the httml coe of the input type, that as a oninput='localStorage.firstName = this.value". Devtools are open on the "Applications" tab and show the LocalStorage content. It has the same value as what has been typed in the form firstName field."
  />
</figure>


In the same way, we added an input listener to all the input fields in this example's form.


#### Restoring the form content on page load/reload

This time, we want the form content to be restored on page load/reload. We will add a `restoreFormContent()` function in the JavaScript code that will be called each time the page is loaded. In this function, we will read the saved data and set the input fields' values.

[Complete example on JSBin](https://jsbin.com/zezudo/edit?js,output): enter data and press reload at any time. The form content is restored! ([Local Example - Restore Content](src/6.2.2-example2.html))

Source code extract (only addition to the previous example):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com">// Called when the page is loaded</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">window</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> restoreFormContent</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> restoreFormContent</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"restoring form content from localStorage"</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">if</span><span class="pun">(</span><span class="pln">localStorage</span><span class="pun">.</span><span class="pln">firstName </span><span class="pun">!==</span><span class="pln"> </span><span class="kwd">undefined</span><span class="pun">)</span><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">"firstName"</span><span class="pun">).</span><span class="pln">value </span><span class="pun">=</span><span class="pln"> localStorage</span><span class="pun">.</span><span class="pln">firstName</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">if</span><span class="pun">(</span><span class="pln">localStorage</span><span class="pun">.</span><span class="pln">lastName </span><span class="pun">!==</span><span class="pln"> </span><span class="kwd">undefined</span><span class="pun">)</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">"lastName"</span><span class="pun">).</span><span class="pln">value </span><span class="pun">=</span><span class="pln"> localStorage</span><span class="pun">.</span><span class="pln">lastName</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">if</span><span class="pun">(</span><span class="pln">localStorage</span><span class="pun">.</span><span class="pln">email </span><span class="pun">!==</span><span class="pln"> </span><span class="kwd">undefined</span><span class="pun">)</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">"email"</span><span class="pun">).</span><span class="pln">value </span><span class="pun">=</span><span class="pln"> localStorage</span><span class="pun">.</span><span class="pln">email</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">if</span><span class="pun">(</span><span class="pln">localStorage</span><span class="pun">.</span><span class="pln">age </span><span class="pun">!==</span><span class="pln"> </span><span class="kwd">undefined</span><span class="pun">)</span><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">"age"</span><span class="pun">).</span><span class="pln">value </span><span class="pun">=</span><span class="pln"> localStorage</span><span class="pun">.</span><span class="pln">age</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">if</span><span class="pun">(</span><span class="pln">localStorage</span><span class="pun">.date</span><span class="pln">&nbsp;</span><span class="pun">!==</span><span class="pln"> </span><span class="kwd">undefined</span><span class="pun">)</span><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">"date"</span><span class="pun">).</span><span class="pln">value </span><span class="pun">=</span><span class="pln"> localStorage</span><span class="pun">.</span><span class="pln">date</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

The tests at _lines 7, 10, 13, etc._, verify that data has been saved, before trying to restore it. Without these tests, it would put the "undefined" string as the value of input fields with no corresponding data to restore.


### 6.2.3 localStorage and sessionStorage

This time we will look at another example that uses new methods from the API:

+ `localStorage.setItem(...),`
+ `localStorage.getItem(...),`
+ `localStorage.removeItem(...),`
+ `localStorage.clear().`


#### Getting/setting values using the getItem(key) and setItem(key, value) methods

If you want to keep a simple counter of the number of times a given user has loaded your application, you can use the following code (just to show how to use setItem/removeItem methods):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> counter </span><span class="pun">=</span><span class="pln"> localStorage</span><span class="pun">.</span><span class="pln">getItem</span><span class="pun">(</span><span class="str">"count"</span><span class="pun">)</span><span class="pln"> </span><span class="pun">||</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">counter</span><span class="pun">++;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">localStorage</span><span class="pun">.</span><span class="pln">setItem</span><span class="pun">(</span><span class="str">"count"</span><span class="pun">,</span><span class="pln"> counter</span><span class="pun">);</span></li>
</ol></div>

As you can easily guess from the above, we use `var value = getItem(key)` to retrieve a key's value and `setItem(key, value)` to set it. This is similar to what we saw in the examples of the page above, except that this time:

+ The key can contain spaces, for example we can write: `localStorage.setItem("Instructor's name", "Michel");` and `var name =  localStorage.getItem("Instructor's name");`, while `var name = localStorage.Instructor's name;` will not work!
+ In a loop or in an iterator, sometimes we need to set/get `localStorage` values using this syntax, for example: 

  <div class="source-code"><ol style="list-style-type: decimal;" class="linenums">
  <li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> inputField </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">"firstName"</span><span class="pun">);</span></li>
  <li class="L1" style="margin-bottom: 0px;"><span class="pln">saveInputFieldValue</span><span class="pun">(</span><span class="pln">inputField</span><span class="pun">);</span></li>
  <li class="L2" style="margin-bottom: 0px;">...&nbsp;</li>
  <li class="L5" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> saveInputFieldValue</span><span class="pun">(</span><span class="pln">field</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
  <li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; localStorage</span><span class="pun">.</span><span class="pln">setItem</span><span class="pun">(</span><span class="pln">field</span><span class="pun">.</span><span class="pln">id</span><span class="pun">,</span><span class="pln"> field</span><span class="pun">.</span><span class="pln">value</span><span class="pun">);</span></li>
  <li class="L7" style="margin-bottom: 0px;"><span class="pun">}</span></li>
  </ol></div>


#### Deleting a key with `removeItem(key)`, or all keys with `clear()`

Deleting a key can be performed through `removeItem()`. And if you wish to reset the entire store, simply call `localStorage.clear()`.

Note that it will probably only be the rare occasion that you will want the entire store to be cleared by the user in production software (since that effectively deletes their entire data). However, it is a rather a common operation needed during development, since bugs may store faulty data the persistence of which can break your application, since the way you store data may evolve over time, or simply because you also need to test the experience of the user when first using the application.

One way of handling this is to add a user interface button that calls `clear()` when clicked, but you must then remember to remove it when you ship! The recommended approach  to use (whenever possible) is to simply open the dev. tool's console and type `localStorage.clear()` there — it's safer and works just as well.


#### Iterating local stores

Local stores (`localStorage` or `sessionStorage`) can also be iterated through in order to list all the content that they contain. The order is not guaranteed, but this may be useful at times (if only for debugging purposes!). The following code lists everything in the current store:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">for</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> n </span><span class="pun">=</span><span class="pln"> localStorage</span><span class="pun">.</span><span class="pln">length</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> n</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> k </span><span class="pun">=</span><span class="pln"> localStorage</span><span class="pun">.</span><strong><span class="pln">key</span><span class="pun">(</span><span class="pln">i</span></strong><span class="pun"><strong>)</strong>;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="pln">k </span><span class="pun">+</span><span class="pln"> </span><span class="str">": "</span><span class="pln"> </span><span class="pun">+</span><strong><span class="pln"> localStorage</span><span class="pun">[</span><span class="pln">k</span></strong><span class="pun"><strong>]</strong>); // get the ith value, the one with a key that is in the variable k.</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

Students may note that something seems a bit off in the example above: instead of calling `localStorage.getItem(k)`, we simply access `localStorage[k]`. Why? Because keys in the local store can also be accessed as if the store were a simple JavaScript object. So instead of `localStorage.getItem("foo")` and `localStorage.setItem("foo", "bar")`, one can write `localStorage.foo` and `localStorage.foo = "bar"`. Of course there are limitations to this mapping: any string can serve as a key, so that localStorage.getItem("one two three") works, whereas that string would not be a valid identifier after the dot (but it could still work as `localStorage["one two three"])`.


#### Example that shows all the methods of the local storage API in action

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/yy9qgkwx')"
    src    ="https://tinyurl.com/y69fuwcx"
    alt    ="example with buttons that shown how to iterate on localStorage, clear it etc.Example that shows all the methods of the local storage API in action"
    title  ="example with buttons that shown how to iterate on localStorage, clear it etc.Example that shows all the methods of the local storage API in action"
  />
</figure>


[Online example at JSBin](https://jsbin.com/nedigi/edit?html,css,output), run it, then click on the first button to show all key/values in the `localStorage`. Open the URL in another tab, and see that the data is shared between tabs, as local stores are attached to an origin. ([Local Example - localStorage])

Then click on the second button to add data to the store, click on the third to remove data. Finally, the last one clears the whole data store.

Source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">utf-8</span><span class="pln"> </span><span class="tag">/&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;title&gt;</span><span class="pln">Example of localStorare API use</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;script&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Using localStorage</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> counter </span><span class="pun">=</span><span class="pln"> localStorage</span><span class="pun">.</span><span class="pln">getItem</span><span class="pun">(</span><span class="str">"count"</span><span class="pun">)</span><span class="pln"> </span><span class="pun">||</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;counter</span><span class="pun">++;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;localStorage</span><span class="pun">.</span><span class="pln">setItem</span><span class="pun">(</span><span class="str">"count"</span><span class="pun">,</span><span class="pln"> counter</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">function</span><span class="pln"> getCountValue</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// retrieve data</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#counter"</span><span class="pun">).</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> localStorage</span><span class="pun">.</span><span class="pln">count</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">function</span><span class="pln"> seeAllKeyValuePairsStored</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; </span><span class="com">// clear list first</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'#list'</span><span class="pun">).</span><span class="pln">innerHTML</span><span class="pun">=</span><span class="str">""</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">for</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> n </span><span class="pun">=</span><span class="pln"> localStorage</span><span class="pun">.</span><span class="pln">length</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> n</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> key </span><span class="pun">=</span><span class="pln"> localStorage</span><span class="pun">.</span><span class="pln">key</span><span class="pun">(</span><span class="pln">i</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> value </span><span class="pun">=</span><span class="pln"> localStorage</span><span class="pun">[</span><span class="pln">key</span><span class="pun">];</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="pln">key </span><span class="pun">+</span><span class="pln"> </span><span class="str">": "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> value</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> li </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">createElement</span><span class="pun">(</span><span class="str">'li'</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;li</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> key </span><span class="pun">+</span><span class="pln"> </span><span class="str">": "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> value</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'#list'</span><span class="pun">).</span><span class="pln">insertBefore</span><span class="pun">(</span><span class="pln">li</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">null</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">function</span><span class="pln"> resetStore</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// erase all key values from store </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; localStorage</span><span class="pun">.</span><span class="pln">clear</span><span class="pun">();</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; </span><span class="com">// reset displayed list too</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'#list'</span><span class="pun">).</span><span class="pln">innerHTML</span><span class="pun">=</span><span class="str">""</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun"></span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">function</span><span class="pln"> addSomeData</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// store data</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; localStorage</span><span class="pun">.</span><span class="pln">lastName </span><span class="pun">=</span><span class="pln"> </span><span class="str">"Buffa"</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; localStorage</span><span class="pun">.</span><span class="pln">firstName </span><span class="pun">=</span><span class="pln"> </span><span class="str">"Michel"</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// refresh display</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; seeAllKeyValuePairsStored</span><span class="pun">();</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun"></span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">function</span><span class="pln"> removeSomeData</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// store data</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; localStorage</span><span class="pun">.</span><span class="pln">removeItem</span><span class="pun">(</span><span class="str">"lastName"</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; localStorage</span><span class="pun">.</span><span class="pln">removeItem</span><span class="pun">(</span><span class="str">"firstName"</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; </span><span class="com">// refresh display</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; seeAllKeyValuePairsStored</span><span class="pun">();</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/script&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&lt;/head&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;body</span><span class="pln"> </span><span class="atn">onload</span><span class="pun">=</span><span class="atv">"</span><span class="pln">getCountValue</span><span class="pun">()</span><span class="atv">"</span><span class="tag">&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;h1&gt;</span><span class="pln">Number of times this page has been seen on this browser: </span><span class="tag">&lt;span</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"counter"</span><span class="tag">&gt;&lt;/span&gt;&lt;/h1&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">seeAllKeyValuePairsStored</span><span class="pun">()</span><span class="atv">"</span><span class="tag">&gt;</span><span class="pln">Show all key value pairs stored in localStorage</span><span class="tag">&lt;/button&gt;&lt;br/&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;output</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"list"</span><span class="tag">&gt;&lt;/output&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">addSomeData</span><span class="pun">()</span><span class="atv">"</span><span class="tag">&gt;</span><span class="pln">Add some data to the store</span><span class="tag">&lt;/button&gt;&lt;br/&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">removeSomeData</span><span class="pun">()</span><span class="atv">"</span><span class="tag">&gt;</span><span class="pln">Remove some data</span><span class="tag">&lt;/button&gt;&lt;br/&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">resetStore</span><span class="pun">()</span><span class="atv">"</span><span class="tag">&gt;</span><span class="pln">reset store (erase all key/value pairs)</span><span class="tag">&lt;/button&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>

You can check in the Chrome dev. tools user interface that the content of the localStorage changes as you click on the buttons.





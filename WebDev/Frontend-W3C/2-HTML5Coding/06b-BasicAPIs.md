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
      + storage limit: the maximum among the three
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

+ [getItem and setItem methods](#gettingsetting-values-using-the-getitemkey-and-setitemkey-value-methods)
  + using `var value = getItem(key)` to retrieve a key's value and `setItem(key, value)` to set it
  + a counter counting the number of times a given user loaded the application:

    ```js
    var counter = localStorage.getItem("count") || 0;
    counter++;
    localStorage.setItem("count", counter);
    ```

  + spaces acceptable: `localStorage.setItem("Instructor's name", "Michel");` and `var name = localStorage.getItem("Instructor's name");`
  + not acceptable: `var name = localStorage.Instructor's name; will not work!`
  + syntax to set/get `localStorage` values within loop or iterator

    ```js
    var inputField = document.getElementById("firstName");
    saveInputFieldValue(inputField);
    ... 
    function saveInputFieldValue(field) {
        localStorage.setItem(field.id, field.value);
    }
    ```

+ [removeItem and clear methods](#deleting-a-key-with-removeitemkey-or-all-keys-with-clear)
  + `removeItem(key)`: delete a key
  + `localStorage.clear()`:
    + reset the entire store
    + rare occasion to clear the entire store by the user in production software
    + a common operation needed during development
      + bugs may store faulty data the persistence of which can break your application
      + the way to store data may evolve over time
      + test the experience of the user when first using the application
  + one way of reseting the entire store
    + add a user interface button that calls `clear()` when clicked
    + remember to remove it when you ship
  + recommended approach: simply open the dev. tool's console and type `localStorage.clear()`

+ [Example for local storage API](#example-that-shows-all-the-methods-of-the-local-storage-api-in-action)
  + HTML button to activate the JS function: `<button onclick="resetStore()">reset store (erase all key/value pairs)</button>`
  + retrieve all data: `function getCountValue() { document.querySelector("#counter").innerHTML = localStorage.count; }`
  + view all stored data

    ```js
    function seeAllKeyValuePairsStored() {
      // clear list first
      document.querySelector('#list').innerHTML="";
      for (var i = 0, n = localStorage.length; i < n; i++) {
         var key = localStorage.key(i);
         var value = localStorage[key];
         console.log(key + ": " + value);
         var li = document.createElement('li');
         li.innerHTML = key + ": " + value;
         document.querySelector('#list').insertBefore(li, null);
      }
    }
    ```

  + reset all stored data: `function resetStore() { localStorage.clear(); document.querySelector('#list').innerHTML=""; }`
  + add/remove some data to local storage

    ```js
    function addSomeData() {
      // store data
      localStorage.lastName = "Buffa";
      localStorage.firstName = "Michel";
      // refresh display
      seeAllKeyValuePairsStored();
    }
    function removeSomeData() {
      // store data
      localStorage.removeItem("lastName");
      localStorage.removeItem("firstName");
      // refresh display
      seeAllKeyValuePairsStored();
    ```

+ [Example to save/restore states](#624-example-2)
  + save initial preferences

    ```js
    function initPreferences() {
      console.log("Adding input listener to all input fields");

      // add an input listener to all input fields
      var listOfInputsInForm = document.querySelectorAll("input");
      for(var i= 0; i < listOfInputsInForm.length; i++) {
          addInputListener(listOfInputsInForm[i]);
      }

      // restore preferences
      restorePreferences();
      applyGUIvalues(); // Use the input fields' values we just restored to set
                        // internal size, incX, color, lineWidth variables
    }
    ```

  + load preferences:

    ```js
    function restorePreferences() {
      console.log("restoring form content from localStorage");

      // get the list of all input elements in the form
      var listOfInputsInForm = document.querySelectorAll("input");

      // For each input element, 
      //  - get its id (that is also the key for it's saved content in the localStorage)
      //  - get the value associated with the id/key in the local storage
      //  - If the value is not undefined, restore the value of the input field
      for(var i= 0; i < listOfInputsInForm.length; i++) {
        var fieldToRestore = listOfInputsInForm[i];
        var id = fieldToRestore.id;
        var savedValue = localStorage.getItem(id);

        if(savedValue !== undefined) {
          fieldToRestore.value = savedValue;
        }
      }
    }
    ```

+ [Example for generic functions](#625-example-3)
  + calling `init()` function when the page loaded

    ```js
    function init() {
      console.log("Adding input listener to all input fields");
      // add an input listener to all input fields
      var listOfInputsInForm = document.querySelectorAll("input");

      for(var i= 0; i < listOfInputsInForm.length; i++) {
          addInputListener(listOfInputsInForm[i]);
      }
      // restore form content with previously saved values
      restoreFormContent();
    }
    ```

  + `addInputListener(inputField)` function:
    + taking an input field as parameter and attaches an `oninput` listener to it
    + saving the field's content each time a value entered

      ```js
      function addInputListener(inputField) {
          inputField.addEventListener('input', function(event) {
              localStorage.setItem(inputField.id, inputField.value);
          }, false);
      }
      ```

  + restore the last saved value for each input field, if present.
    + get the list of input fields: `document.querySelectorAll("input");`
    + iterate through the list: `for(var i= 0; i < listOfInputsInForm.length; i++) {...}`
    + get `id` of inout fields as the key in `localStorage` for the previous data saved for this field: `var fieldToRestore = listOfInputsInForm[i]; var id = fieldToRestore.id;`
    + restore by setting the value of the input field if not undefined: `if(savedValue !== undefined) { fieldToRestore.value = savedValue; }`

    ```js
    function restoreFormContent() {
      console.log("restoring form content from localStorage");

      // get the list of all input elements in the form
      var listOfInputsInForm = document.querySelectorAll("input");

      // For each input element,
      // - get its id (that is also the key for it's saved content in the localStorage)
      // - get the value associated with the id/key in the local storage
      // - If the value is not undefined, restore the value of the input field
      for(var i= 0; i < listOfInputsInForm.length; i++) {
        var fieldToRestore = listOfInputsInForm[i];
        var id = fieldToRestore.id;
        var savedValue = localStorage.getItem(id);
        if(savedValue !== undefined) {
            fieldToRestore.value = savedValue;
        }
      }
    }
    ```

+ [Size of Web storage](#626-size-limitations-etc)
  + related mechanism w/ user agents (browsers) according to Web storage specification
    + limiting the total amount of space allowed for storage areas
    + allowing the user to grant more space to a site, when reaching quotas
    + allowing users to see how much space each domain is using
    + giving at least 5Mb per origin
  + local storage required for saving/loading data on demand in many cases
  + more complex solutions:
    + processing transaction: require more available space than local storage
    + e.g., IndexedDB, a No SQL database
  + limit amount of data to prevent from storing anything anything huge
  + storage not necessarily permanent
  + serious applications
    + synchronizing existing data with the server on a regular basis
    + avoid data loss when using the same service from multiple devices at once

+ [sessionStorage key/values vs cookies](#sessionstorage-keyvalues-instead-of-cookies)
  + store session-based data in a manner more powerful than cookies
  + `sessionStorage` object working in exactly the same way as `localStorage`
  + lifetime limited to a single browser session (lifetime of your tab/window)
  + `sessionStorage` advantage: being scoped to a given browser tab (or similar execution context)
  + Cookies' security drawback
    + two tabs open to the same site $\to$ share the same cookies
    + storing information about a given operation using cookies in one tab
    + probably leaking the information to the other side
    + confusing if performing different tasks in each
  + `sessionStorage` data scoped and not leak across tabs

+ [JSON to structure key-value pairs](#626-size-limitations-etc)
  + `JSON.stringify()` and `JSON.parse() methods`: manipulate minimal record format to store complex data
  + JSON (JavaScript Object Notation)
    + a lightweight data-interchange format
    + easy for machines to parse and generate.
    + a text format completely programming language independent
    + providing a great way of encoding and decoding data
    + a really good match for JavaScript
    + careful not to use circular data structures or non-serializable objects
    + straightforward plugging yo support local store in vast majority of cases
    + two structures:
      + a collection of name/value pairs
      + an ordered list of values
  + typical usage:
    + `locaStorage.key = JSON.stringify(object);`
    + `localStorage.setItem(key, JSON.stringify(object));`
  + example:
    + store the object as a JSON String: `localStorage.setItem('testObject', JSON.stringify(personObject));`
    + retrieve the object from storage: `retrievedObject = JSON.parse(localStorage.getItem('testObject'));`

      ```js
      var contact = {};
      contact.familyName = fieldFamilyName.value;
      contact.givenName = fieldGivenName.value;
      // Add the curent contact to the array
      contacts.push(contact);
      // Save in JSON
      localStorage.contacts = JSON.stringify(contacts);


      // Read contacts from localStorage
      function getContacts() {
        var contacts = localStorage.contacts;
        if (contacts) {
          return JSON.parse(contacts);
        } else {
          return [];
        }
      } 
      ```



### 6.2.1 The Web storage API

The Web storage API introduces "two related mechanisms, similar to HTTP session cookies, for storing structured data on the client side".

Indeed, Web Storage provides two interfaces - `sessionStorage` and `localStorage` - whose main difference is data longevity. This specification defines an API for persistent data storage of key-value pair data in Web clients.

<p style="border: 1px solid red; margin: 20px; padding: 20px;"><strong>With <span style="font-family: 'courier new', courier;">localStorage the data will remain until it is deleted, whereas with <span style="font-family: 'courier new', courier;">sessionStorage the data is erased when the tab/browser is closed.</strong></p>

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

<div><ol>
<li value="1">// Using localStorage</li>
<li> </li>
<li>// store data</li>
<li>localStorage.lastName = "Bunny";</li>
<li>localStorage.firstName = "Bugs";</li>
<li>localStorage.location = "Earth";</li>
<li> </li>
<li>// retrieve data</li>
<li>var lastName = localStorage.lastName;</li>
<li>var firstName = localStorage.firstName;</li>
<li>var location = localStorage.location;</li>
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

<div><ol>
<li value="1">oninput="localStorage.<span style="color: #ff0000;">firstName=this.value;"</li>
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

<div><ol>
<li value="1">// Called when the page is loaded</li>
<li>window.onload = restoreFormContent;</li>
<li>&nbsp;</li>
<li>function restoreFormContent() {</li>
<li>&nbsp; &nbsp;console.log("restoring form content from localStorage");</li>
<li> </li>
<li>&nbsp; &nbsp;if(localStorage.firstName !== undefined) </li>
<li>&nbsp; &nbsp; &nbsp;document.getElementById("firstName").value = localStorage.firstName;</li>
<li> </li>
<li>&nbsp; &nbsp;if(localStorage.lastName !== undefined) </li>
<li>&nbsp; &nbsp; &nbsp;document.getElementById("lastName").value = localStorage.lastName;</li>
<li> </li>
<li>&nbsp; &nbsp;if(localStorage.email !== undefined) </li>
<li>&nbsp; &nbsp; &nbsp;document.getElementById("email").value = localStorage.email;</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;if(localStorage.age !== undefined) </li>
<li>&nbsp; &nbsp; &nbsp;document.getElementById("age").value = localStorage.age;</li>
<li> </li>
<li>&nbsp; &nbsp;if(localStorage.date&nbsp;!== undefined) </li>
<li>&nbsp; &nbsp; &nbsp;document.getElementById("date").value = localStorage.date;</li>
<li>}</li>
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

<div><ol>
<li value="1">var counter = localStorage.getItem("count") || 0;</li>
<li>counter++;</li>
<li>localStorage.setItem("count", counter);</li>
</ol></div>

As you can easily guess from the above, we use `var value = getItem(key)` to retrieve a key's value and `setItem(key, value)` to set it. This is similar to what we saw in the examples of the page above, except that this time:

+ The key can contain spaces, for example we can write: `localStorage.setItem("Instructor's name", "Michel");` and `var name =  localStorage.getItem("Instructor's name");`, while `var name = localStorage.Instructor's name;` will not work!
+ In a loop or in an iterator, sometimes we need to set/get `localStorage` values using this syntax, for example: 

  <div><ol style="list-style-type: decimal;">
  <li value="1">var inputField = document.getElementById("firstName");</li>
  <li>saveInputFieldValue(inputField);</li>
  <li>...&nbsp;</li>
  <li>function saveInputFieldValue(field) {</li>
  <li>&nbsp; &nbsp; localStorage.setItem(field.id, field.value);</li>
  <li>}</li>
  </ol></div>


#### Deleting a key with `removeItem(key)`, or all keys with `clear()`

Deleting a key can be performed through `removeItem()`. And if you wish to reset the entire store, simply call `localStorage.clear()`.

Note that it will probably only be the rare occasion that you will want the entire store to be cleared by the user in production software (since that effectively deletes their entire data). However, it is a rather a common operation needed during development, since bugs may store faulty data the persistence of which can break your application, since the way you store data may evolve over time, or simply because you also need to test the experience of the user when first using the application.

One way of handling this is to add a user interface button that calls `clear()` when clicked, but you must then remember to remove it when you ship! The recommended approach  to use (whenever possible) is to simply open the dev. tool's console and type `localStorage.clear()` there — it's safer and works just as well.


#### Iterating local stores

Local stores (`localStorage` or `sessionStorage`) can also be iterated through in order to list all the content that they contain. The order is not guaranteed, but this may be useful at times (if only for debugging purposes!). The following code lists everything in the current store:

<div><ol>
<li value="1">for (var i = 0, n = localStorage.length; i &lt; n; i++) {</li>
<li>&nbsp; &nbsp;&nbsp;var k = localStorage.<strong>key(i</strong><strong>)</strong>;</li>
<li>&nbsp; &nbsp; console.log(k + ": " +<strong> localStorage[k</strong><strong>]</strong>); // get the ith value, the one with a key that is in the variable k.</li>
<li>}</li>
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


[Online example at JSBin](https://jsbin.com/nedigi/edit?html,css,output), run it, then click on the first button to show all key/values in the `localStorage`. Open the URL in another tab, and see that the data is shared between tabs, as local stores are attached to an origin. ([Local Example - localStorage](src/6.2.3-example1.html))

Then click on the second button to add data to the store, click on the third to remove data. Finally, the last one clears the whole data store.

Source code:

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html lang="en"&gt;</li>
<li>&lt;head&gt;</li>
<li>&lt;meta charset=utf-8 /&gt;</li>
<li>&lt;title&gt;Example of localStorare API use&lt;/title&gt;</li>
<li> &lt;script&gt;</li>
<li>&nbsp; &nbsp;// Using localStorage</li>
<li>&nbsp; &nbsp;var counter = localStorage.getItem("count") || 0;</li>
<li>&nbsp; &nbsp;counter++;</li>
<li>&nbsp; &nbsp;localStorage.setItem("count", counter);</li>
<li> </li>
<li>&nbsp; &nbsp;function getCountValue() {</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;// retrieve data</li>
<li>&nbsp; &nbsp; &nbsp; document.querySelector("#counter").innerHTML = localStorage.count;</li>
<li>&nbsp; &nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp;function seeAllKeyValuePairsStored() {</li>
<li>&nbsp; &nbsp; &nbsp; // clear list first</li>
<li>&nbsp; &nbsp; &nbsp; document.querySelector('#list').innerHTML="";</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;for (var i = 0, n = localStorage.length; i &lt; n; i++) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;var key = localStorage.key(i);</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;var value = localStorage[key];</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;console.log(key + ": " + value);</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;var li = document.createElement('li');</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;li.innerHTML = key + ": " + value;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;document.querySelector('#list').insertBefore(li, null);</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;}</li>
<li>&nbsp; &nbsp;} </li>
<li> </li>
<li>&nbsp; &nbsp;function resetStore() { </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// erase all key values from store </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; localStorage.clear();</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; // reset displayed list too</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;document.querySelector('#list').innerHTML="";</li>
<li>&nbsp; &nbsp;}</li>
<li></li>
<li>&nbsp; &nbsp;function addSomeData() {</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;// store data</li>
<li>&nbsp; &nbsp; &nbsp; localStorage.lastName = "Buffa";</li>
<li>&nbsp; &nbsp; &nbsp; localStorage.firstName = "Michel";</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;// refresh display</li>
<li>&nbsp; &nbsp; &nbsp; seeAllKeyValuePairsStored();</li>
<li>&nbsp; &nbsp;}</li>
<li></li>
<li>&nbsp; &nbsp;function removeSomeData() {</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;// store data</li>
<li>&nbsp; &nbsp; &nbsp; localStorage.removeItem("lastName");</li>
<li>&nbsp; &nbsp; &nbsp; localStorage.removeItem("firstName");</li>
<li>&nbsp; &nbsp; &nbsp; // refresh display</li>
<li>&nbsp; &nbsp; &nbsp; seeAllKeyValuePairsStored();</li>
<li>&nbsp; &nbsp;}</li>
<li> &lt;/script&gt;</li>
<li>&lt;/head&gt;</li>
<li>&lt;body onload="getCountValue()"&gt;</li>
<li>&nbsp; &nbsp;&lt;h1&gt;Number of times this page has been seen on this browser: &lt;span id="counter"&gt;&lt;/span&gt;&lt;/h1&gt;</li>
<li> </li>
<li>&nbsp; &nbsp;&lt;button onclick="seeAllKeyValuePairsStored()"&gt;Show all key value pairs stored in localStorage&lt;/button&gt;&lt;br/&gt;</li>
<li>&nbsp; &nbsp;&lt;output id="list"&gt;&lt;/output&gt;</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;&lt;button onclick="addSomeData()"&gt;Add some data to the store&lt;/button&gt;&lt;br/&gt;</li>
<li>&nbsp; &nbsp;&lt;button onclick="removeSomeData()"&gt;Remove some data&lt;/button&gt;&lt;br/&gt;</li>
<li>&nbsp; &nbsp;&lt;button onclick="resetStore()"&gt;reset store (erase all key/value pairs)&lt;/button&gt;</li>
<li>&lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
</ol></div>

You can check in the Chrome dev. tools user interface that the content of the localStorage changes as you click on the buttons.


### 6.2.4 Example 2

Local stores are also useful for saving/restoring user preferences of Web Applications. For example, the JS Bin tool you have been using since the beginning of this course uses localStorage to store the list of tabs you open, and their width:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
    onclick="window.open('https://tinyurl.com/y6gqevet')"
    src    ="https://tinyurl.com/y2lpkt43"
    alt    ="example of preferences"
    title  ="example of preferences"
  />
</figure>


This way, the next time you come back to JSBin, "it will remember your last settings".

Another example is a guitar FX processor / amp simulator your instructor is writing with some of his students. It uses localStorage to save/restore presets values:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick="window.open('https://tinyurl.com/y6gqevet')"
    src    ="https://tinyurl.com/y5sgaxcy"
    alt    ="guitar fx processor uses localStorage"
    title  ="guitar fx processor uses localStorage"
  />
</figure>


#### Save/restore preferences

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/y6gqevet')"
    src    ="https://tinyurl.com/yyoq59w7"
    alt    ="animated rectangle with GUI"
    title  ="animated rectangle with GUI"
  />
</figure>


[Original example on JSBin](https://jsbin.com/dewagit/1/edit?html,css,output): we can change the color, size and speed of the animated rectangle. However, each time we come back to the page, default values are restored. ([Local Example - Animated Rectangle](src/6.2.4-example1.html))

We would like to save the current values and find them back as they were when we come back to the page.

[Here is a modified example that saves/restores its state, you can try it at JSBin](https://jsbin.com/cebavo/edit?html,js,console,output). In this modified version of the animated rectangle example, you can set the color, size, speed, etc. And if you reload the page, the state of the different input field is restored, but also the internal variables. Check the source code in the JS Bin example and read the following explanations. ([Local Example - Animated Rectangle w/ States](src/6.2.4-example2.html))

We used the same generic code for saving/restoring input fields' values we saw in the first example that used `localStorage`. The only difference is that we renamed the two generic functions so that they correspond better to their role here (instead of `saveFormContent` we called the function `restorePreferences`).

The function `initPreferences` is executed when the page is loaded.

Source code extract:

<div><ol>
<li value="1">function initPreferences() {</li>
<li>&nbsp; &nbsp;console.log("Adding input listener to all input fields");</li>
<li>&nbsp; &nbsp;// add an input listener to all input fields</li>
<li>&nbsp; &nbsp;var listOfInputsInForm = document.querySelectorAll("input");</li>
<li>&nbsp; &nbsp;for(var i= 0; i &lt; listOfInputsInForm.length; i++) {</li>
<li>&nbsp; &nbsp; &nbsp; addInputListener(listOfInputsInForm[i]);</li>
<li>&nbsp; &nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp;// restore preferences</li>
<li>&nbsp; &nbsp;restorePreferences();</li>
<li> </li>
<li>&nbsp; &nbsp;applyGUIvalues(); // Use the input fields' values we just restored to set internal&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// size, incX, color, lineWidth variables</li>
<li>}</li>
<li>&nbsp;</li>
<li>function addInputListener(inputField) {</li>
<li> // same as before</li>
<li>}</li>
<li>&nbsp;</li>
<li>function restorePreferences() {</li>
<li> // same as old restoreFormContent</li>
<li>}</li>
<li>&nbsp;</li>
<li>function applyGUIvalues() {</li>
<li>&nbsp; &nbsp;// Check restored input field content to set the size of the rectangle</li>
<li>&nbsp; &nbsp;var sizeWidget = document.getElementById("size");</li>
<li>&nbsp; &nbsp;size = Math.sign(incX)*parseInt(sizeWidget.value);</li>
<li><span style="line-height: 25.6000003814697px; background-color: #eeeeee;">&nbsp; &nbsp;// also update the outline element's value</li>
<li>&nbsp; &nbsp;document.getElementById("sizeValue").innerHTML = size;</li>
<li> </li>
<li><span style="color: #666600; line-height: 25.6000003814697px; background-color: #ffffff;">&nbsp; &nbsp;// Check restored input field content to set the color&nbsp;of the rectangle</li>
<li>&nbsp; &nbsp;var colorWidget = document.getElementById("color");</li>
<li>&nbsp; &nbsp;ctx.fillStyle = colorWidget.value;</li>
<li> </li>
<li><span style="color: #666600; line-height: 25.6000003814697px;">&nbsp; &nbsp;// Check restored input field content to set the speed&nbsp;of the rectangle</li>
<li>&nbsp; &nbsp;var speedWidget = document.getElementById("speed");</li>
<li>&nbsp; &nbsp;incX = Math.sign(incX)*parseInt(speedWidget.value);</li>
<li>&nbsp; &nbsp;// also update the outline element's value</li>
<li>&nbsp; &nbsp;document.getElementById("speedValue").innerHTML = Math.abs(incX);</li>
<li> </li>
<li>&nbsp; &nbsp;<span style="color: #666600; line-height: 25.6000003814697px;">// Check restored input field content to set the&nbsp;lineWidth<span style="color: #666600; line-height: 25.6000003814697px;">&nbsp;of the rectangle</li>
<li>&nbsp; &nbsp;var lineWidthWidget = document.getElementById("lineWidth");</li>
<li>&nbsp; &nbsp;ctx.lineWidth = parseInt(lineWidthWidget.value);</li>
<li>}</li>
</ol></div>


### 6.2.5 Example 3

[Online example at JSBin](https://jsbin.com/volicig/edit?html,js,console,output) ([Local Example - Save/restore Form contents](src/6.2.5-example1.html))
 
<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y3jk6lmd')"
    src    ="https://courses.edx.org/assets/courseware/v1/8240f6a10d1b1526c377ec699bb0ccb0/asset-v1:W3Cx+HTML5.1x+2T2020+type@asset+block/exampleonsteroids.png"
    alt    ="form that saves/restore its content using generic functions"
    title  ="form that saves/restore its content using generic functions"
  />
</figure>


This time, using the `setItem` and `getItem` method we saw earlier in the course, we could write some generic functions for saving/restoring input fields' content, without having advance knowledge about the number of fields in the form, their types, their ids, etc.

Furthermore, we removed all input listeners in the HTML, making it cleaner (no more `oninput="localStorage.firstName = this.value;"`...)


#### Define listeners + restore old values after the page is loaded, use generic functions

We start writing an `init()` function that is called when the page is loaded. This function will:

1. Define `input` listeners for all input fields
2. Restore the last saved value for each input field, if present.

Source code:

<div><ol>
<li value="1">// Called when the page is loaded</li>
<li>window.onload = init;</li>
<li>&nbsp;</li>
<li>function init() {</li>
<li>&nbsp; &nbsp;console.log("Adding input listener to all input fields");</li>
<li>&nbsp; &nbsp;// add an input listener to all input fields</li>
<li>&nbsp; &nbsp;var listOfInputsInForm = document.<strong>querySelectorAll</strong>("input");<br><br></li>
<li>&nbsp; &nbsp;for(var i= 0; i &lt; listOfInputsInForm.length; i++) {</li>
<li>&nbsp; &nbsp; &nbsp; addInputListener(listOfInputsInForm[i]);</li>
<li>&nbsp; &nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp;// restore form content with previously saved values</li>
<li>&nbsp; &nbsp;restoreFormContent();</li>
<li>}</li>
</ol></div> 

And here is the `addInputListener(inputField)` function. It takes an input field as parameter and attaches an `oninput` listener to it, that will save the field's content each time a value is entered. The key will be the id of the input field (_line 3_):

<div><ol>
<li value="1">function addInputListener(inputField) {</li>
<li>&nbsp; &nbsp; inputField.addEventListener('input', function(event) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; <strong>localStorage</strong><strong>.setItem(inputField.id, inputField.value);</strong></li>
<li>&nbsp; &nbsp; &nbsp;}, false);</li>
<li>}</li>
</ol></div>

Note that at _line 2_, we use `addEventListener` (that is not using the `oninput` property here). `adddEventListener` doesnot replace existing `oninput` definitions and keep all existing listeners unchanged.


#### Restore all input fields' content using a generic function

We have seen how to save all input fields' content on the fly. Now, let's see how we can restore saved values and update the form. This is done using the function `restoreFormContent()`:

<div><ol>
<li value="1">function restoreFormContent() {</li>
<li>&nbsp; &nbsp;console.log("restoring form content from localStorage");</li>
<li> </li>
<li>&nbsp; &nbsp;// get the list of all input elements in the form</li>
<li>&nbsp; &nbsp;var listOfInputsInForm = document.querySelectorAll("input");</li>
<li> </li>
<li>&nbsp; &nbsp;// For each input element, </li>
<li>&nbsp; &nbsp;// - get its id (that is also the key for it's saved content </li>
<li>&nbsp; &nbsp;// in the localStorage)</li>
<li>&nbsp; &nbsp;// - get the value associated with the id/key in the local</li>
<li>&nbsp; &nbsp;// storage</li>
<li>&nbsp; &nbsp;// - If the value is not undefined, restore the value</li>
<li>&nbsp; &nbsp;// of the input field</li>
<li>&nbsp; &nbsp;for(var i= 0; i &lt; listOfInputsInForm.length; i++) {</li>
<li>&nbsp; &nbsp; &nbsp;var fieldToRestore = listOfInputsInForm[i];</li>
<li>&nbsp; &nbsp; &nbsp;var id = fieldToRestore.id;</li>
<li>&nbsp; &nbsp; &nbsp;<strong>var savedValue = localStorage.getItem(id);</strong></li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;if(savedValue !== undefined) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; <strong>fieldToRestore</strong><strong>.value = savedValue;</strong></li>
<li>&nbsp; &nbsp; &nbsp;}</li>
<li>&nbsp; &nbsp;}</li>
<li>}</li>
</ol></div>

In this function, we first get the list of input fields (_line 5_), then iterate on it (_line 14_). For each input field, we get its `id`, which value is the key in `localStorage` for the previous data saved for this field (_lines 15-16_). Then if the value is not undefined, we restore it by setting the value of the input field (_lines 19-20_).


#### These generic functions can be used in many different projects

Indeed, if you look carefully, you will see that these functions are really useful. You may easily embed them in your own projects, or perhaps adapt them for a particular need (i.e. for saving input type="checkboxes" that work a bit differently), etc.



### 6.2.6 Size limitations, etc.

Few things to remember, from the Web storage specification:

+ User agents (browsers) should limit the total amount of space allowed for storage areas.
+ User agents may prompt the user when quotas are reached, allowing the user to grant more space to a site. This enables sites to store many user-created documents on the user's computer, for instance.
+ User agents should allow users to see how much space each domain is using.
+ A mostly arbitrary limit of five megabytes per origin is recommended (translation: give at least 5Mb per origin).

__In many cases, local storage is all that your application will need for saving/loading data on demand.__ More complex ways to do it exist, such as IndexedDB, a No SQL database, that proposes transactions and usually comes with far more available space than local storage. IndexedDB usage is for advanced users and will be covered in the W3Cx HTML5 Apps and Games.

Additionally, there will be a limit on the amount of data that you can store there. Browsers enforce quotas that will prevent you from cluttering your users' drives excessively. These quotas can vary from platform to platform, but are usually reasonably generous for simple cases (around 5MB), so __if you are careful not to store anything huge there, you should be fine__.

__Finally, keep in mind that this storage is not necessarily permanent.__ Browsers are inconsistent in how they allow for it to be wiped, but in several cases it gets deleted with cookies — which is logical when you think of how it can be used for tracking in a similar fashion.

For serious applications, you might want to synchronize existing data with the server on a regular basis, in order to avoid data loss (and in general, because users enjoy using the same service from multiple devices at once). This is a rather complex feat, and frameworks such as Firebase can help. Such techniques are beyond the scope of this course and will not be covered.


#### `sessionStorage` key/values instead of cookies?

Note that if all you need is to store session-based data in a manner that is more powerful than cookies, you can use the `sessionStorage` object which works in exactly the same way as localStorage, but the lifetime is limited to a single browser session (lifetime of your tab/window).

<strong>Also note that in addition to being more convenient and capable of storing more data than cookies, it has the advantage of <span style="color: red;">being scoped to a given browser tab (or similar execution context).</span></strong>

<span style="color: red; font-weight: bold;">Cookies' security drawback</span>: if a user has two tabs open to the same site, they will share the same cookies. Which is to say that if you are storing information about a given operation using cookies in one tab, that information will leak to the other side — this can be confusing if the user is performing different tasks in each.

<p style="border: 1px solid; magin: 20px; padding: 20px;"><span style="color: #ff0000;"><strong>By using <span style="font-family: courier new,courier;">sessionStorage</span>, the data you store will be scoped and therefore not leak across tabs!</strong></span></p>


### 6.2.7 Storing more than strings? Use JSON!

Storing strings is all well and good, but it quickly becomes limiting: you may want to store more complex data with at least a modicum of structure.

There are some simple approaches, such as creating your own minimal record format (e.g. a string with fields separated with a given character, using `join()` on store and `split()` upon retrieval) or using multiple keys (e.g. post_17_title, post_17_content, post_17_author, etc.). But these are really hacks. Thankfully, there's a better way,  `JSON.stringify()` and `JSON.parse()` methods.

[JSON](https://www.json.org/) provides a great way of encoding and decoding data that is a really good match for JavaScript. You have to be careful not to use circular data structures or non-serializable objects, but in the vast majority of cases, plugging JSON support into your local store is straightforward.


#### Typical usage

<div><ol>
<li value="1">locaStorage.key = JSON.stringify(object); // or...</li>
<li>localStorage.setItem(key, JSON.stringify(object));</li>
</ol></div>

Let's try a simple toy example ([online at JSBin](https://jsbin.com/ciricis/2/edit?html,console,output)).  The example below saves a JavaScript object in JSON, then restores it and checks that the object properties are still there! ([Local Example - Origin](src/6.2.7-example1.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
    onclick="window.open('https://tinyurl.com/y3mlad7s')"
    src    ="https://tinyurl.com/y4z3hu6q"
    alt    ="JSON save / load in localStorage"
    title  ="JSON save / load in localStorage"
  />
</figure>


Source code:

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html lang="en"&gt;</li>
<li>&lt;head&gt;</li>
<li>&lt;meta charset=utf-8 /&gt;</li>
<li>&lt;title&gt;Storing JSON Objects with Local Storage&lt;/title&gt;</li>
<li> &lt;script&gt;</li>
<li>&nbsp; &nbsp;&nbsp;var personObject= {'givenName': 'Michel', 'familyName': 'Buffa'};</li>
<li> </li>
<li>&nbsp; &nbsp; // Store the object as a JSON String</li>
<li>&nbsp; &nbsp; <strong>localStorage</strong><strong>.setItem('testObject', JSON.stringify(personObject));</strong></li>
<li> </li>
<li>&nbsp; &nbsp; // Retrieve the object from storage</li>
<li>&nbsp; &nbsp; <strong>var</strong><strong> retrievedObject = JSON.parse(localStorage.getItem('testObject'));</strong></li>
<li> </li>
<li>&nbsp; &nbsp; console.log(retrievedObject.firstName + " " + retrievedObject.lastName);</li>
<li> </li>
<li>&nbsp; &nbsp;// then you can use retrievedObject.givenName, retrievedObject.familyName...</li>
<li> &lt;/script&gt;</li>
<li>&lt;/head&gt;</li>
<li>&lt;body&gt;</li>
<li>&lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
</ol></div>


__Explanations:__

+ _Line 7_: we built a JavaScript object that contains a person.
+ _Line 10_: we store it in `localStorage` as a JSON string object, with a key equal to `testObject`.
+ _Line 13_: we restore it from `localStorage` as a string, and the `JSON.parse` methods turns it back into a JavaScript object.
+ _Line 15_: we print the values of the object properties.


#### Examples


__Example #1: showing how we can save a form's content in JSON__

[Online example on JSBin that saves in localStorage an array of contacts in JSON](https://jsbin.com/nejewiw/2/edit?html,js,console,output) ([Local Example - JSON](src/6.2.7-example2.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
    onclick="window.open('https://tinyurl.com/y3mlad7s')"
    src    ="https://tinyurl.com/yylczjo9"
    alt    ="localStorage JSON"
    title  ="localStorage JSON"
  />
</figure>


__Example #2: a form and a table that displays the contacts stored in localStorage__

[Example on JSBin](https://jsbin.com/karoboj/3/edit?html,css,console,output) ([Local Example - localStorage](src/6.2.7-example3.html))

Add contacts using the form, see how the HTML table is updated. Try to reload the page: data are persisted in `localStorage`. 

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
    onclick="window.open('https://tinyurl.com/y3mlad7s')"
    src    ="https://tinyurl.com/y6ouwfvu"
    alt    ="serverless contact manager"
    title  ="serverless contact manager"
  />
</figure>

Examine the localStorage:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
    onclick="window.open('https://tinyurl.com/y3mlad7s')"
    src    ="https://tinyurl.com/y3ub2hnz"
    alt    ="localStorage view in devtools shows the data"
    title  ="localStorage view in devtools shows the data"
  />
</figure>


The source code for this example is a bit long, and we suggest that you examine it in the JS Bin tool. We extensively commented it. It uses:

+ Well structured page with the new elements seen during Week 1 (section, article, nav, aside, etc.)
+ HTML5 form elements with builtin and custom validation (the date cannot be in the past, the firstName and lastName fields do not accept &, #, ! or $ characters),
+ `localStorage` for saving / restoring an array of contacts in JSON
+ It shows how to use the DOM API for dynamically updating the page content (build the HTML table from the array of contacts, add a new line when a new contact is submitted, etc.)


### 6.2.8 Discussion and projects

Here is the discussion forum for this part of the course. You can post your comments and share your creations here, and of course ask questions.

Let us suggest some topics of discussion and optional projects:


#### Suggested topics

+ The last example showed a contact manager that can work without a server. There are frameworks such as  Firebase that help synchronize local data and remote data. A bit like Google photos... Have you heard of them? Have you already tried to address such problems?
+ Did you try browser extensions for managing `localStorage` and `sessionStorage`?


#### Optional projects

Here are a few project ideas. Your classmates and the team who prepared the course will be glad to try them and offer feedback. Please post URLs in this discussion forum. These projects are optional, meaning that they won't be graded.

+ __Project 1 (easy):__ Try to save / load the current state of a form you used. Or if you added a GUI to a canvas animation, you could try to reproduce what has been done in an example of the course: save/restore the GUI state and preferences (color, speed, etc., of the animation).
+ __Project 2 (harder):__  Try to complete the last example presented in the course - the contact manager - with features such as: ability to delete entries in the table (and also on the `localStorage`), add a picture (and save it as `dataURL` in `localStorage`. Data URLs are strings, so it's possible to save/restore them in `localStorage`), etc.





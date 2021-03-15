# Module 5: Working with forms


## 5.5 A small application


### 5.5.1 A contact manager (part 1)

In this final part of the course, let's build together a minimal contact manager that shows how to use ES6 classes, local storage, forms and the HTML table JavaScript API.

This is a play project that you can easily improve:

+ A contact, in this application, is just a person with a name and an email. Feel free to add other properties and methods to the Contact class.
+ The contactManager is also an ES6 class with methods for adding, removing, sorting, saving and loading contacts on your hard disk. We will add new functionalities, step by step, in the next sections, but you can improve the examples provided by adding your own new features (build a better HTML table, add new sorting options, etc.)

__Let's start with a simple skeleton (no GUI), beginning with the `Contact` class__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">class</span><span class="pln"> </span><span class="typ">Contact</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;constructor</span><span class="pun">(</span><span class="pln">name</span><span class="pun">,</span><span class="pln"> email</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; this</span><span class="pun">.</span><span class="pln">name </span><span class="pun">=</span><span class="pln"> name</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; this</span><span class="pun">.</span><span class="pln">email </span><span class="pun">=</span><span class="pln"> email</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp;}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

As you can see, a contact is just a name and an email. We will use the above class like this:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> c1 </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Contact</span><span class="pun">(</span><span class="str">"Jimi Hendrix"</span><span class="pun">,</span><span class="pln"> </span><span class="str">"jimi@rip.com"</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> c2 </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Contact</span><span class="pun">(</span><span class="str">"Robert Fripp"</span><span class="pun">,</span><span class="pln"> </span><span class="str">"robert.fripp@kingcrimson.com"</span><span class="pun">);</span></li>
</ol></div>

Then you can print the properties of contact `c1` or `c2` using for example `console.log(c1.name)`, `console.log(c2.email)`, etc.


#### A minimal ContactManager class

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">class</span><span class="pln"> </span><span class="typ">ContactManager</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; constructor</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // when we build the contact manager, it</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // has an empty list of contacts</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; this</span><span class="pun">.</span><span class="pln">listOfContacts </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[];</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; }</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; add</span><span class="pun">(</span><span class="pln">contact</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; this</span><span class="pun">.</span><span class="pln">listOfContacts</span><span class="pun">.</span><span class="pln">push</span><span class="pun">(</span><span class="pln">contact</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; }</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; remove</span><span class="pun">(</span><span class="pln">contact</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; // we iterate on the list of contacts until we find the contact</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; // passed as a parameter (we say that they are equal if emails match)</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; for</span><span class="pun">(</span><span class="kwd">let</span><span class="pln"> i </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> </span><span class="kwd">this</span><span class="pun">.</span><span class="pln">listOfContacts</span><span class="pun">.</span><span class="pln">length</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; var</span><span class="pln"> c </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">this</span><span class="pun">.</span><span class="pln">listOfContacts</span><span class="pun">[</span><span class="pln">i</span><span class="pun">];</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; if</span><span class="pun">(</span><span class="pln">c</span><span class="pun">.</span><span class="pln">email </span><span class="pun">===</span><span class="pln"> contact</span><span class="pun">.</span><span class="pln">email</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // remove the contact at index i</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; this</span><span class="pun">.</span><span class="pln">listOfContacts</span><span class="pun">.</span><span class="pln">splice</span><span class="pun">(</span><span class="pln">i</span><span class="pun">,</span><span class="pln"> i</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // stop/exit the loop</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; break</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; }</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;};</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; }</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; printContactsToConsole</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; this</span><span class="pun">.</span><span class="pln">listOfContacts</span><span class="pun">.</span><span class="pln">forEach</span><span class="pun">(</span><span class="kwd">function</span><span class="pun">(</span><span class="pln">c</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="pln">c</span><span class="pun">.</span><span class="pln">name</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; });</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; };</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>


__Explanations:__

+ This is a minimal ES6 class for building a contact manager. It has only one property: the list of contacts, and a method for adding a new contact (_line 8_), one for removing a contact (_line 12_), that iterate on the list of contacts until the contact passed as a parameter is found (when email properties match), then the contact is removed using the `splice` method, and we go out from the loop using the `break` statement (_line 22_).
+ It also has a utility method for printing to the console the list of contacts (_line 27_).

We can use the contact manager like this:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> cm </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">ContactManager</span><span class="pun">();</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> c1 </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Contact</span><span class="pun">(</span><span class="str">"Jimi Hendrix"</span><span class="pun">,</span><span class="pln"> </span><span class="str">"jimi@rip.com"</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> c2 </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Contact</span><span class="pun">(</span><span class="str">"Robert Fripp"</span><span class="pun">,</span><span class="pln"> </span><span class="str">"robert.fripp@kingcrimson.com"</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> c3 </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Contact</span><span class="pun">(</span><span class="str">"Angus Young"</span><span class="pun">,</span><span class="pln"> </span><span class="str">"angus@acdc.com"</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> c4 </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Contact</span><span class="pun">(</span><span class="str">"Arnold Schwarzenneger"</span><span class="pun">,</span><span class="pln"> </span><span class="str">"T2@terminator.com"</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"--- Adding 4 contacts ---"</span><span class="pun">)</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">cm</span><span class="pun">.</span><span class="pln">add</span><span class="pun">(</span><span class="pln">c1</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">cm</span><span class="pun">.</span><span class="pln">add</span><span class="pun">(</span><span class="pln">c2</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">cm</span><span class="pun">.</span><span class="pln">add</span><span class="pun">(</span><span class="pln">c3</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">cm</span><span class="pun">.</span><span class="pln">add</span><span class="pun">(</span><span class="pln">c4</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">cm</span><span class="pun">.</span><span class="pln">printContactsToConsole</span><span class="pun">();</span></li>
</ol></div>

As you can see, this is a very minimal version. It's always a good idea to start with very simple structures/classes, and a few methods. Then type the code on CodePen or JSBin and use the devtool console. Check that there are no syntax errors, that everything runs smoothly.

Here is the CodePen of this minimal version. Click on the CodePen label on the top right, and once in CodePen, open the console:

[CodePen Demo](https://codepen.io/w3devcampus/pen/yXoXER)

[Local Demo](src/js/05e-example01.js)


#### Adding a method for sorting the list of contacts by name

Do you remember the `sort()` method you can use on arrays? We saw it in modules 2 or 3. Since our array contains objects, we must provide a callback for comparing two elements by name. Here is the code for the new sort() method we added to the ContactManager class:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">sort</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // As our array contains objects, we need to pass as argument</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // a method that can compare two contacts.</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // we use a class method, which is similar to the distance(p1, p2)</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // method we saw in the ES6 Point class in module 4</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // We always call such methods using the name of the class followed</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // by the dot operator</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp;<strong> this</strong></span><strong><span class="pun">.</span><span class="pln">listOfContacts</span><span class="pun">.</span><span class="pln">sort</span><span class="pun">(</span><span class="typ">ContactManager</span><span class="pun">.</span><span class="pln">compareByName</span><span class="pun">);</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><strong><span class="com">// class method for comparing two contacts by name</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><strong><span class="kwd">static</span><span class="pln"> compareByName</span></strong><span class="pun">(</span><span class="pln">c1</span><span class="pun">,</span><span class="pln"> c2</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // JavaScript has built in capabilities for comparing strings</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // in alphabetical order</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">c1</span><span class="pun">.</span><span class="pln">name </span><span class="pun">&lt;</span><span class="pln"> c2</span><span class="pun">.</span><span class="pln">name</span><span class="pun">)</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; return</span><span class="pln"> </span><span class="pun">-</span><span class="lit">1</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">c1</span><span class="pun">.</span><span class="pln">name </span><span class="pun">&gt;</span><span class="pln"> c2</span><span class="pun">.</span><span class="pln">name</span><span class="pun">)</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; return</span><span class="pln"> </span><span class="lit">1</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; return</span><span class="pln"> </span><span class="lit">0</span><span class="pun">; // c1.name = c2.name</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
</ol></div>

The important thing here is to notice that we declared the `compareByName` method as a class method (using the `static` keyword). This is similar to what we did in the `Point` class example from module 4, when we explained the "class properties and methods". This method compareByName does not depend on any instance of the contact manager, consequently: it's a class method.

CodePen that uses this new method:

[CodePen Demo](https://codepen.io/w3devcampus/pen/MovoBz)

[Local Demo](src/js/05e-example02.js)


#### Notes for 5.5.1 A contact manager (part 1)

+ Example: [`Contact` and `ContactManager` classes](src/js/05e-example01.js)
  + `Contact` class: a person w/ a name and an email

    ```js
    class Contact {
      constructor(name, email) {
        this.name = name;
        this.email = email;
      }
    }
    ```

  + `ContactManager` class:
    + a minimal ES6 class to build a contact manager
    + only one property: the list of contacts
    + two methods: add and remove contact

    ```js
    class ContactManager {
      constructor() {   // built the contact manager w/ empty list of contacts
        this.listOfContacts = [];
      }

      add(contact) {
        this.listOfContacts.push(contact);
      }

      remove(contact) {
        for (let i = 0; i < this.listOfContacts.length; i++) {
          var c = this.listOfContacts[i];

          if (c.email === c.email) {
            this.listOfContacts.splice(i, i);
            break;
          }
        }
      }

      printContactsToConsole() {
        this.listOfContacts.forEach(function(c) {
          console.log(c.name);
        });
      }
    }
    ```

+ Example: [`Contact` and `ContactManager` verification](/src/js/05e-example01.js)
  + create contacts: `var cm = new ContactManager(); var c1 = new Contact("Jimi Hendrix", "jimi@rip.com"); var c2 = new Contact("Robert Fripp", "robert.fripp@kingcrimson.com"); var c3 = new Contact("Angus Young", "angus@acdc.com"); var c4 = new Contact("Arnold Schwarzenneger", "T2@terminator.com");`
  + add contacts into contact manager: `cm.add(c1); cm.add(c2); cm.add(c3); cm.add(c4);`
  + display to verify: `cm.printContactsToConsole();`
  + delete a contact: `cm.remove(c2);`
  + display to verify: `cm.printContactsToConsole();`

+ Example: [sorting contacts in manager](src/js/05e-example02.js)
  + define `sort` method in `ContactManager`: `sort() { this.listOfContacts(ContactManager.compareByName); }`
  + class method for comparing two contacts by name: 
  
    ```js
    static compareName(c1, c2) {
      if (c1.name < c2.name>)
        return -1;
      
      if (c.name > c2.name)
        return 1;
      
      return 0;
    }
    ```


### 5.5.2 Persistence (part 2)

Let's use load/save methods is for loading and saving the list of contacts in Local Storage.


#### `load` and `save` methods (persistence)

This time, we add to the `ContactManager` class a `load()` and a `save()` method for loading/saving from disk (from a key/value pair database located on your hard disk, and associated to the domain of your Web application).

__Saving the list of contacts in JSON, checking the saved value using the devtools__

Here is the code we added to the ES6 class for saving the list of contacts in JSON:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="kwd">class</span><span class="pln"> </span><span class="typ">ContactManager</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; constructor</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // when we build the contact manager, it</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // has an empty list of contacts</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; this</span><span class="pun">.</span><span class="pln">listOfContacts </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[];</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; }</span></li>
<li class="L6" style="margin-bottom: 0px;"></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; ...</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>save</strong></span><strong><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // We can only save strings in local storage. So, let's convert</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // our array of contacts to JSON</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; localStorage</span><span class="pun">.</span><span class="pln">contacts </span><span class="pun">=</span><span class="pln"> JSON</span><span class="pun">.</span><span class="pln">stringify</span><span class="pun">(</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">listOfContacts</span><span class="pun">);</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="pun">&nbsp; &nbsp; &nbsp;}</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>


You write data identified by a key in localStorage like this:

localStorage.keyName = a string value
In our case, line 13 saves the list of contacts with a key named "contacts" in the local storage. In order to save the list of contacts as a string, we convert it to the JSON format using the  JSON.stringify(...) method (JSON = string based)

Try an example on CodePen, save some contacts...

[CodePen Demo](https://codepen.io/w3devcampus/pen/PjKbVP)

[Local Demo](src/js/05e-example03.js)


... then we can check in the devtools that the list has been saved.

In Google Chrome, click the Application tab, then LocalStorage:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick= "window.open('https://tinyurl.com/5huywey')"
    src    = "https://tinyurl.com/nbh6j5nh"
    alt    = "Chrome local storage inspector"
    title  = "Chrome local storage inspector"
  />
</figure>


In Firefox, you first need to activate the storage view like this:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick= "window.open('https://tinyurl.com/5huywey')"
    src    = "https://tinyurl.com/58ye47sk"
    alt    = "FF activate storage view in devtools"
    title  = "FF activate storage view in devtools"
  />
</figure>


You will see the list of contacts when you click on the newly appeared "Storage" tab:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick= "window.open('https://tinyurl.com/5huywey')"
    src    = "https://tinyurl.com/m48665xw"
    alt    = "FF storage inspector"
    title  = "FF storage inspector"
  />
</figure>



#### Restoring the list of contacts

This time, we've added a `load()` method that will check if a list of contacts has been saved. If this is the case, it will read it from LocalStorage, convert it back from JSON into a JavaScript object. In order to test this, in the following CodePen, we first save the list, then we empty the list in memory (setting the array to an empty array), print the list of contacts (that displays a message "LIST EMPTY!"), then we load the contacts from LocalStorage and print the list again: it has been restored to its previous value.

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="kwd">class</span><span class="pln"> </span><span class="typ">ContactManager</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; constructor</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // when we build the contact manager, it</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // has an empty list of contacts</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; this</span><span class="pun">.</span><span class="pln">listOfContacts </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[];</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; }</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // Will erase all contacts</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; empty</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; this</span><span class="pun">.</span><span class="pln">listOfContacts </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[];</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; }</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; ...</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; load</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; if</span><span class="pun">(</span><span class="pln">localStorage</span><span class="pun">.</span><span class="pln">contacts </span><span class="pun">!==</span><span class="pln"> </span><span class="kwd">undefined</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // the array of contacts is saved in JSON, let's convert</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // it back to a reak JavaScript object.</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; this</span><span class="pun">.</span><span class="pln">listOfContacts </span><span class="pun">=</span><span class="pln"> JSON</span><span class="pun">.</span><span class="pln">parse</span><span class="pun">(</span><span class="pln">localStorage</span><span class="pun">.</span><span class="pln">contacts</span><span class="pun">);</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; }</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="pun">&nbsp; &nbsp; }</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">...</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"--- Saving contacts to local storage ---"</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">cm</span><span class="pun">.</span><span class="pln">save</span><span class="pun">();</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"--- Emptying the list of contacts ---"</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">cm</span><span class="pun">.</span><span class="pln">empty</span><span class="pun">();</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">cm</span><span class="pun">.</span><span class="pln">printContactsToConsole</span><span class="pun">();</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"--- Loading contacts from local storage ---"</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">cm</span><span class="pun">.</span><span class="pln">load</span><span class="pun">();</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">cm</span><span class="pun">.</span><span class="pln">printContactsToConsole</span><span class="pun">();</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"Do you notice: contacts have all been restored!"</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
</ol></div>

__Explanations:__

+ At _line 16_, we check if a previous version has been saved.
+ At _line 19_, we read the string value associated to the key named "contacts", and use `JSON.parse(...)` to turn it into a JavaScript object we can work with.
+ _Lines 26-36_ test the load/save/empty functionalities. You can try this yourself live: click on the CodePen label below, on the top right corner, and once in CodePen, open the CodePen console (or the read devtool console) to see the result of the execution of these tests.


#### Notes for 5.5.2 Persistence (part 2)

+ Example: [load and save w/ Local Storage](src/js/05e-example03.js)
  + loading / saving from a key/value pair database located in hard disk
  + associated to the domain of Web application
  + add `load` and `save` methods for constructor
  + convert array of contacts to JSON and save into local storage: `save() { localStorage.contacts = JSON.stringify(this.lostOfContacts); }`
  + verify `LocalStorage` w/ devtool:
    + Chrome: devtool > Application > Local Storage (left panel) > `https://js.codepen.io` > Key/Value pair (right panel)
    + Firefox: devtool > setting icon on top-right corner > Storage (left panel)
    + Safari: devtool > Storage (top banner) > Local Storage > `https://js.codepen.io` > key/value pair
  + empty list of contacts: `empty() { this.listOfContacts = []; }`
  + load contacts from `LocalStorage` and convert JSON back into JS object: `load() { if (localStorage.contact != undefined) { this.listOfContacts = JSON.parse(localStorage.contacts); }}`
  + verify `save()`, `empty()` and `load()` w/ printing in console
    + `console.log("---Saving contacts to local storage---"); cm.save();`
    + `console.log("---Empty the list of contacts---"); cm.empty(); cm.printContactsToConsole();`
    + `console.log("---Loading contacts from local storage---); cm.load(); cm.printContactsColsole();`


### 5.5.3 Display contacts in an HTML5 table (part 3)

We're going to reuse the code from this CodePen (example taken from a previous section of the course, the one about working with remote data), and adapt it to our needs:

[CodePen Demo](https://codepen.io/w3devcampus/pen/vmLMRN)

[Local Demo](src/05e-example04.html)

This time, we will first add some HTML to the contact manager example (same as in the previous CodePen except that we've renamed "users" as "contacts"):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp; &lt;title&gt;</span><span class="pln">A contact manager, v3</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">/&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;/head&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;body&gt;</span><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &lt;p&gt;</span><span class="pln">List of contacts</span><span class="tag">&lt;/p&gt;</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; <strong>&lt;div</strong></span><strong><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"contacts"</span><span class="tag">&gt;&lt;/div&gt;</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>

The div at _line 9_ is where we're going to dynamically insert an HTML table with one row for each contact. We will keep the same minimal CSS for displaying table, row and cell borders (we encourage you to improve this):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">table </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;margin</span><span class="pun">-</span><span class="pln">top</span><span class="pun">:</span><span class="pln"> </span><span class="lit">20px</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">table</span><span class="pun">,</span><span class="pln"> tr</span><span class="pun">,</span><span class="pln"> td </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;border</span><span class="pun">:</span><span class="pln"> </span><span class="lit">1px</span><span class="pln"> solid</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">}</span><span class="pln"> </span></li>
</ol></div>

And here is the method we add in our ContactManager class; an adaptation of the function `displayUsersAsATable(users)` from the previous CodePen:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">class</span><span class="pln"> </span><span class="typ">ContactManager</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; .....</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; displayContactsAsATable</span><span class="pun">(</span><span class="pln">idOfContainer</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // to empty the container that contains the results</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; let</span><span class="pln"> container </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#"</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> idOfContainer</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; container</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> </span><span class="str">""</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; if</span><span class="pun">(</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">listOfContacts</span><span class="pun">.</span><span class="pln">length </span><span class="pun">===</span><span class="pln"> </span><span class="lit">0</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; container</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> </span><span class="str">"&lt;p&gt;No contacts to display!&lt;/p&gt;"</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // stops the execution of this method</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; return</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; }</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // creates and populates the table with users</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; let</span><span class="pln">&nbsp;table </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">createElement</span><span class="pun">(</span><span class="str">"table"</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // iterates on the array of users</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; this</span><span class="pun">.</span><span class="pln">listOfContacts</span><span class="pun">.</span><span class="pln">forEach</span><span class="pun">(</span><span class="kwd">function</span><span class="pun">(</span><span class="pln">currentContact</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // creates a row</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; let</span><span class="pln">&nbsp;row </span><span class="pun">=</span><span class="pln"> table</span><span class="pun">.</span><span class="pln">insertRow</span><span class="pun">();</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; row</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> </span><span class="str">"&lt;td&gt;"</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> currentContact</span><span class="pun">.</span><span class="pln">name </span><span class="pun">+</span><span class="pln"> </span><span class="str">"&lt;/td&gt;"</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; +</span><span class="pln"> </span><span class="str">"&lt;td&gt;"</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> currentContact</span><span class="pun">.</span><span class="pln">email </span><span class="pun">+</span><span class="pln"> </span><span class="str">"&lt;/td&gt;"</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; });</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // adds the table to the div</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; container</span><span class="pun">.</span><span class="pln">appendChild</span><span class="pun">(</span><span class="pln">table</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; }</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>


__Explanations:__

+ __Line 3:__ the method `displayContactsAsATable` takes as a parameter the id of the HTML element in which the table will be inserted after being built. This id is used by the querySelector call at _line 5_.
+ __Lines 9-13:__ if the list of contacts is empty, we just return, but first we display in the HTML container a message: "No contact to display!"
+ __Lines 16-25:__ we create a table, and for each contact we insert and fill a new row in the table. 
+ __Line 28:__ the table is inserted (appended) in the HTML container.

CodePen of this example:

[CodePen Demo](https://codepen.io/w3devcampus/pen/yXoVdp)

[Local Demo](src/05e-example05.html)

Note that we also added a method called `addTestData()` to the ContactManager class, as this is a way to make testing the class easier. The code in this method is similar to all the code we used in previous examples for testing the class by adding four contacts to it and displaying messages in the devtool console.


#### Notes for 5.5.3 Display contacts in an HTML5 table (part 3)

+ Example: [display contacts in HTML5 table w/ Xhr2](src/05e-example04.html)
  + Refer to Xhr2 of [JSON data from a REST Web Service](5-JavaScript/05d-Forms.md#examples)
  + add container to display contact table: `<div id="contacts"></div>`
  + add function to display users in table: `function displayUsersAsTable(users) {...}`
    + empty the container: `var usersDiv = document.querySelector("#users"); usersDiv.innerHTML = "";`
    + create and populate the table w/ users: `vat table = document.createElement("table");`
    + iterate to display users of array: `users.forEach(function(currentUser) {...});`
      + create a row: `var row = table.insertRow();`
      + insert cells in the row: `var nameCell = row.insertCell(); nameCell.innerHTML = currentUser.name; var cityCell = row.insertCell(); cityCell.innerHTML = currentuser.address.city;`
    + add the table tot he div: `usersDiv.appendChild(table);`


+ Example: [display contacts in HTML5 table](src/05e-example05.html)
  + implementation w/ `class ContactManager` 
  + add button element: `<button onclick="search();">Get a remote list of users' names and emails</button>`
  + add empty container for table: `<div id="users"></div>`
  + specify table styles: `table { margin-top: 20px; }` & `table, tr, td { border: 1px solid; }`
  + add method to display contacts in table: `displayContactsAsTable(idOfContainer) {...}`
    + empty the container: `let container = document.querySelector('#' + idOfContainer); container.innerHTML = "";`
    + no contact: `if (this.listOfContacts.length === 0) { container.innerHTML = "<p>No contacts to sdisplay!>/p>"; return; }`
    + create and populate the table w/ users: `let table = document.createElement("table");`
    + iterate the users of the array: `this.listOfContacts.forEach(function(currentContact) {...});`
      + create row: `let row = table.insertRow();`
      + add data of the row: `row.innerHTML = "<td>" + currentContact.name + "</td>" + "<td>" + currentComtact.email + "</td>";`
    + add table to the div: `container.appendChild(table);`
  

### 5.5.4 Use a form to enter new contacts (part 4)

In the previous example, we added a form for entering a new contact, and an "add" button.

Here is the HTML code of the form:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;form</span><span class="pln"> </span><strong><span class="atn">onsubmit</span><span class="pun">=</span><span class="atv">"</span><span class="kwd">return</span><span class="pln"> formSubmitted</span><span class="pun">();</span><span class="atv">"</span></strong><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &lt;fieldset&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &nbsp; &nbsp; &lt;legend&gt;</span><span class="pln">Personal informations</span><span class="tag">&lt;/legend&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &nbsp; &nbsp; &lt;label&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Name : </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"text"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"name"</span><span class="pln"> </span><span class="atn">required</span><span class="tag">&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &nbsp; &nbsp; &lt;/label&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &nbsp; &nbsp; &lt;label&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Email : </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"email"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"email"</span><span class="pln"> </span><span class="atn">required</span><span class="tag">&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &nbsp; &nbsp; &lt;/label&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &nbsp; &nbsp; &lt;br&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &nbsp; &nbsp; <strong>&lt;button&gt;</strong></span><strong><span class="pln">Add new Contact</span><span class="tag">&lt;/button&gt;</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &lt;/fieldset&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/form&gt;</span></li>
</ol></div>

The button at line 13 will submit the form by default (it's equivalent to an `<input type="submit">`).

The event listener at line 1:

```html
<form onsubmit="return formSubmitted();">
```

  ... will call the `formSubmitted` function when the form is submitted. It is interesting that we use `onclick="return formSubmitted();"`:

+ If the returned value is `true`, the form will be submitted by your browser (this would reload the HTML page).
+ If the returned value is `false`, the form will not be submitted (this is what we want, so we will return `false` in the `formSubmitted` function).

Here is the code of the `formSubmitted` function:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> formSubmitted</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // Get the values from input fields</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; let</span><span class="pln"> name </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#name"</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; let</span><span class="pln"> email </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#email"</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun"></span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; <strong>let</strong></span><strong><span class="pln"> newContact </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Contact</span><span class="pun">(</span><span class="pln">name</span><span class="pun">.</span><span class="pln">value</span><span class="pun">,</span><span class="pln"> email</span><span class="pun">.</span><span class="pln">value</span><span class="pun">);</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; cm</span><span class="pun">.</span><span class="pln">add</span><span class="pun">(</span><span class="pln">newContact</span><span class="pun">);</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // Empty the input fields</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; name</span><span class="pun">.</span><span class="pln">value </span><span class="pun">=</span><span class="pln"> </span><span class="str">""</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; email</span><span class="pun">.</span><span class="pln">value </span><span class="pun">=</span><span class="pln"> </span><span class="str">""</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; <strong>// refresh&nbsp;the table</strong></span></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; cm</span><span class="pun">.</span><span class="pln">displayContactsAsATable</span><span class="pun">(</span><span class="str">"contacts"</span><span class="pun">);</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // do not let your browser submit the form using HTTP</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; <strong>return</strong></span><strong><span class="pln"> </span><span class="kwd">false</span><span class="pun">;</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

__Explanations:__

+ _Lines 2-7:_ we get the values entered in the form's input fields, build a new contact and add it to the contact list
+ _Lines 10-11:_ we reset the content of the input fields (we empty them)
+ _Line 14:_ we display the HTML table with the new added contact
+ _Line 17:_ we return false so that the form will not be submitted. This will prevent the browser from reloading the HTML page.

CodePen example:

[CodePen Demo](https://codepen.io/w3devcampus/pen/awypEg)

[Local Demo](src/05e-example06.html)

Note that we've also added some buttons for playing with the load/save features we implemented in the previous page:

+ Add some new contacts to the list using the form,
+ Save them by clicking on the save button,
+ Empty the list, click the empty button,
+ Reload the list... you can see that contacts have been correctly saved and restored!


#### Notes for 5.5.4 Use a form to enter new contacts (part 4)

+ Example: [input form to add new contact](src/05e-example06.html)
  + event listener: `<form onsubmit="return formSubmitted();">...</form>`
  + grouping inputs fields and submit button: `<fieldset>...</field>`
    + legend of group: `<legend>Personal information</legend>`
    + name input form: `<label> Name : <input type="text" id="name" required> </label>`
    + email input form: `<label> Email : <input type="email" id="email" required> </label>`
    + submit butt: `<button>Add new Contact</button>`
  + add buttons for table displaying: `<div id="contacts"></div>"
    + empty button: `<button onclick="emptyList();">Empty</button>`
    + save button: `<button onclick="cm.save();">Save</button>`
    + reload button: `<button onclick="loadList();"></button>`
  + callback function once button clicked: `function formSubmitted() {...}`
    + access elements: `let name = document.querySelector("#name"); let email = document.querySelector("#email");`
    + assign values in a new contact: `let newContact = new Contact(name.value, email.value); cm.add(newContact);`
    + empty the input fields: `name.value = ""; email.value = "";`
    + refresh the table: `cm.displayContactsAsATable("contacts");`
    + prevent from submitting by the browser to reload the HTTP page: `return false;`
  + empty list: `function emptyList() { cm.empty(); cm.displayContactsAsATable("contacts"); }`
  + load list: `function loadList() { cm.load(); cm.displayContactsAsATable("contacts"); }`
  + save strings in Local Storage: `localStorage.contacts = JSON.stringify(this.listOfContacts);`


### 5.5.5 Discussion and projects

Here is the discussion forum for this part of the course. Please either post your comments/observations/questions or share your creations.


#### Optional projects

+ Improve the CSS of the contact manager table.
+ Add more complicated features to the contact manager:
  + Add an extra column with a trash bin icon in it (you can use this [trash icon](https://i.imgur.com/yHyDPio.png), do right click and "save link as"). When you click on this icon, delete the contact.

    _Hint_: find a way to get the index of the current row in the click event listener, so that you can easily delete the contact from the array. You can add a "HTML data attribute" using `trashbin.dataset.contactId = 3;` for example, when you create the `img` element of the trash bin, do something like this:

    ```js
    let trashbin = document.createElement("img");
    trashbin.src =  "http://i.imgur.com/yHyDPio.png";
    trashbin.dataset.contactId = 3; // 3 is the current row index and corresponds
                                    // to contact at index = 3 in the array of contacts
    ```

    It's like adding a `data-contactId` attribute to the HTML of the `img` element. Then in the event listener, use `evt.target.dataset.contactId` to get it back.

  + Add a search form for searching a contact by name: rebuild the table to display only contacts that match. More difficult: reduce the table as you type!
  + Improve the CSS of this ugly-looking table! ;-)
  + Add a header on the table and try to make the table sortable when you click on the header of one column (e.g., clicking on "email" will sort the table by email).
+ [ADVANCED] Using the [classList JavaScript interface](https://developer.mozilla.org/en-US/docs/Web/API/Element/classList): `elem.classList.add("name of a CSS class")`, `remove`, and `toggle` methods, allow the user to manipulate CSS classes from JavaScript. Try to make the table of contacts editable. Click on a cell and it will become editable (_tip_: use both a label and an input field). When you click, you hide the label and show the input field, and when you click outside of the input field, you do the reverse. Use the "`blur`" event to detect when clicks occur outside).



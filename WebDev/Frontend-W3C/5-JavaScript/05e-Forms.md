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
    + 

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
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://tinyurl.com/5huywey')"
    src    = "https://tinyurl.com/nbh6j5nh"
    alt    = "Chrome local storage inspector"
    title  = "Chrome local storage inspector"
  />
</figure>


In Firefox, you first need to activate the storage view like this:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://tinyurl.com/5huywey')"
    src    = "https://tinyurl.com/58ye47sk"
    alt    = "FF activate storage view in devtools"
    title  = "FF activate storage view in devtools"
  />
</figure>


You will see the list of contacts when you click on the newly appeared "Storage" tab:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://tinyurl.com/5huywey')"
    src    = "https://tinyurl.com/m48665xw"
    alt    = "FF storage inspector"
    title  = "FF storage inspector"
  />
</figure>



#### Restoring the list of 

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



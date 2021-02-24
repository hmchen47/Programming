# Module 4: Structuring data


## 4.4 Improving the game with classes


### 4.4.1 Class and constructor

First, let's look how we were handling balls previously in our game!

We have built balls in order to fill the array of balls.

#### OLD VERSION

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> createBalls</span><span class="pun">(</span><span class="pln">n</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // empty array</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; let</span><span class="pln"> ballArray </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[];</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // create n balls</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; for</span><span class="pun">(</span><span class="kwd">let</span><span class="pln"> i</span><span class="pun">=</span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> n</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{&nbsp;</span><strong>// let's build multiple times a singleton object</strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; <strong>let</strong></span><strong><span class="pln"> b </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{&nbsp;</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; x</span><span class="pun">:</span><span class="pln">w</span><span class="pun">/</span><span class="lit">2</span><span class="pun">,</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; y</span><span class="pun">:</span><span class="pln">h</span><span class="pun">/</span><span class="lit">2</span><span class="pun">,</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; radius</span><span class="pun">:</span><span class="pln"> </span><span class="lit">5</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="lit">30</span><span class="pln"> </span><span class="pun">*</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">random</span><span class="pun">(),</span><span class="pln"> </span><span class="com">// between 5 and 35</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; speedX</span><span class="pun">:</span><span class="pln"> </span><span class="pun">-</span><span class="lit">5</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="lit">10</span><span class="pln"> </span><span class="pun">*</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">random</span><span class="pun">(),</span><span class="pln"> </span><span class="com">// between -5 and + 5</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; speedY</span><span class="pun">:</span><span class="pln"> </span><span class="pun">-</span><span class="lit">5</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="lit">10</span><span class="pln"> </span><span class="pun">*</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">random</span><span class="pun">(),</span><span class="pln"> </span><span class="com">// between -5 and + 5</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; color</span><span class="pun">:</span><span class="pln">getARandomColor</span><span class="pun">(),</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; }</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // add ball b to the array</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; ballArray</span><span class="pun">.</span><span class="pln">push</span><span class="pun">(</span><span class="pln">b</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; } // end of for loop</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun"></span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // returns the array full of randomly created balls</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; return</span><span class="pln"> ballArray</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

In the code above, in order to build `n` balls, we created a singleton ball object multiple times. This worked, but if we have misspelled a property name within the code, or forgot one of the properties that had to be initialized, we would have received no warnings. We will replace these lines with something like `let b = new Ball(...);`

#### NEW VERSION

Using the `new` keyword and an ES6 class

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> createBalls2</span><span class="pun">(</span><span class="pln">n</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // empty array</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; let</span><span class="pln"> ballArray </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[];</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // create n balls</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; for</span><span class="pun">(</span><span class="kwd">let</span><span class="pln"> i</span><span class="pun">=</span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> n</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // Create some random values...</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; let</span><span class="pln"> x </span><span class="pun">=</span><span class="pln"> w</span><span class="pun">/</span><span class="lit">2</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; let</span><span class="pln"> y </span><span class="pun">=</span><span class="pln"> h</span><span class="pun">/</span><span class="lit">2</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; let</span><span class="pln"> radius </span><span class="pun">=</span><span class="pln"> </span><span class="lit">5</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="lit">30</span><span class="pln"> </span><span class="pun">*</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">random</span><span class="pun">();</span><span class="pln"> </span><span class="com">// between 5 and 35</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; let</span><span class="pln"> speedX </span><span class="pun">=</span><span class="pln"> </span><span class="pun">-</span><span class="lit">5</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="lit">10</span><span class="pln"> </span><span class="pun">*</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">random</span><span class="pun">();</span><span class="pln"> </span><span class="com">// between -5 and + 5</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; let</span><span class="pln"> speedY </span><span class="pun">=</span><span class="pln"> </span><span class="pun">-</span><span class="lit">5</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="lit">10</span><span class="pln"> </span><span class="pun">*</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">random</span><span class="pun">();</span><span class="pln"> </span><span class="com">// between -5 and + 5</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; let</span><span class="pln"> color </span><span class="pun">=</span><span class="pln"> getARandomColor</span><span class="pun">();</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; <strong>// Create the new ball b</strong></span></li>
<li class="L6" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; let</span><span class="pln"> b </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Ball</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">,</span><span class="pln"> radius</span><span class="pun">,</span><span class="pln"> color</span><span class="pun">,</span><span class="pln"> speedX</span><span class="pun">,</span><span class="pln"> speedY</span><span class="pun">);</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // add ball b to the array</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; ballArray</span><span class="pun">.</span><span class="pln">push</span><span class="pun">(</span><span class="pln">b</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; }</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // returns the array full of randomly created balls</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; return</span><span class="pln"> ballArray</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>


Ok, not a very big change here, except that we are no longer manipulating the property names one by one, and we use the `new` keyword. 

And here is the (so far, incomplete) ES6 class for Ball (continued in the next page of this course):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><strong><span class="kwd">class</span><span class="pln"> </span><span class="typ">Ball</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>constructor</strong></span><strong><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">,</span><span class="pln"> radius</span><span class="pun">,</span><span class="pln"> color</span><span class="pun">,</span><span class="pln"> speedX</span><span class="pun">,</span><span class="pln"> speedY</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; this</span><span class="pun">.</span><span class="pln">x </span><span class="pun">=</span><span class="pln"> x</span><span class="pun">; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// properties</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; this</span><span class="pun">.</span><span class="pln">y </span><span class="pun">=</span><span class="pln"> y</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; this</span><span class="pun">.</span><span class="pln">radius </span><span class="pun">=</span><span class="pln"> radius</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; this</span><span class="pun">.</span><span class="pln">color </span><span class="pun">=</span><span class="pln"> color</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; this</span><span class="pun">.</span><span class="pln">speedX </span><span class="pun">=</span><span class="pln"> speedX</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; this</span><span class="pun">.</span><span class="pln">speedY </span><span class="pun">=</span><span class="pln"> speedY</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; }</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">...</span><span class="pln"> </span><span class="com">// code to come for methods</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>


#### Notes for 4.4.1 Class and constructor

+ Example: comparisons of constructor function and class
  + constructor function: `functioncreateBalls1(n) {...}`
    + declare an empty array: `let ballArray = [];`
    + create `n` balls w/ properties by singleton object and add into array

      ```js
      for(let i=0; i < n; i++) { // let's build multiple times a singleton object
          let b = { 
              x:w/2,
              y:h/2,
              radius: 5 + 30 * Math.random(), // between 5 and 35
              speedX: -5 + 10 * Math.random(), // between -5 and + 5
              speedY: -5 + 10 * Math.random(), // between -5 and + 5
              color:getARandomColor(),
          }

        ballArray.push(b);
      }
      ```

    + return the array w/ randomly created balls: `return ballArray;`
  + constructor function w/ `new` keyword: `functioncreateBalls2(n) {...}`
    + declare an empty array: `let ballArray = [];`
    + create `n` balls w/ properties by `new` keyword and add into array

      ```js
      for(let i=0; i < n; i++) {
        let x = w/2; let y = h/2;
        let radius = 5 + 30 * Math.random(); // between 5 and 35
        let speedX = -5 + 10 * Math.random(); // between -5 and + 5
        let speedY = -5 + 10 * Math.random(); // between -5 and + 5
        let color = getARandomColor();
 
        // Create the new ball b
        let b = new Ball(x, y, radius, color, speedX, speedY);

        ballArray.push(b);
      }
      ```

    + return the array w/ randomly created balls: `return ballArray;`
  + ES5 class: `class Ball() {...}`
    + declare constructor: `constructor(x, y, radius, color, speedX, speedY) {...}`
    + declare properties:

      ```js
      this.x = x;            // properties
      this.y = y;
      this.radius = radius;
      this.color = color;
      this.speedX = speedX;
      this.speedY = speedY;
      ```

    + declare methods: `// code for methods`


### 4.4.2 Adding methods classes

Ok, we've seen how to define the Ball class: properties and constructor. Properties are the DNA for balls: they all have an x and y position, a radius, a color, a horizontal and a vertical speed.

It is time to add some behaviors: a `draw` and a `move` method. Indeed, all balls will be able to draw and move themselves.

Here's how we were drawing a ball in the previous version of the game:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> drawFilledCircle</span><span class="pun">(</span><strong>c</strong><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // GOOD practice: save the context, use 2D trasnformations</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">save</span><span class="pun">();</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // translate the coordinate system, draw relative to it</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">translate</span><span class="pun">(</span><strong><span class="pln">c</span><span class="pun">.</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> c</span><span class="pun">.</span><span class="pln">y</span></strong><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillStyle </span><span class="pun">=</span><strong><span class="pln"> c</span><span class="pun">.</span><span class="pln">color</span><span class="pun">;</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // (0, 0) is the top left corner of the monster.</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">beginPath</span><span class="pun">();</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">arc</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><strong><span class="pln"> c</span><span class="pun">.</span><span class="pln">radius</span></strong><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">*</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">PI</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fill</span><span class="pun">();</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// GOOD practice: restore the context</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">restore</span><span class="pun">();</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

And this how we were drawing and moving all the balls:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> drawAllBalls</span><span class="pun">(</span><span class="pln">ballArray</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ballArray</span><span class="pun">.</span><span class="pln">forEach</span><span class="pun">(</span><span class="kwd">function</span><span class="pun">(</span><span class="pln">b</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; drawFilledCircle</span><span class="pun">(</span><span class="pln">b</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; });</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> moveAllBalls</span><span class="pun">(</span><span class="pln">ballArray</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // iterate on all balls in array</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; balls</span><span class="pun">.</span><span class="pln">forEach</span><span class="pun">(</span><span class="kwd">function</span><span class="pun">(</span><span class="pln">b</span><span class="pun">,</span><span class="pln"> index</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // b is the current ball in the array</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; b</span><span class="pun">.</span><span class="pln">x </span><span class="pun">+=</span><span class="pln"> </span><span class="pun">(</span><span class="pln">b</span><span class="pun">.</span><span class="pln">speedX </span><span class="pun">*</span><span class="pln"> globalSpeedMutiplier</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; b</span><span class="pun">.</span><span class="pln">y </span><span class="pun">+=</span><span class="pln"> </span><span class="pun">(</span><span class="pln">b</span><span class="pun">.</span><span class="pln">speedY </span><span class="pun">*</span><span class="pln"> globalSpeedMutiplier</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; testCollisionBallWithWalls</span><span class="pun">(</span><span class="pln">b</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; testCollisionWithPlayer</span><span class="pun">(</span><span class="pln">b</span><span class="pun">,</span><span class="pln"> index</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">});</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>


#### Adding a draw and a move method to the ES6 ball class

Instead of having these behaviors as separate functions that take a ball reference as a parameter, it is always better to put this as a method inside the class. Indeed, each ball can move, can draw itself, and the content of these methods does not bring any external dependencies.

For example, if we decide to put a method named testCollisionWithWalls inside the Ball class, it would be bad, in terms of reusability, for its content to rely on external, global variables, such as the canvas size. You could have passed the canvas as a parameter, but then you create more specialization: you have a Ball class for balls that can move inside a rectangular area that is a canvas. It's better to just pass the width and the height of the zone.

Anyway, if you plan to use your balls in another game, it is recommended that you keep the class as simple as possible. It will be more reusable in other projects.

__New version__ of the ES6 Ball class with draw and move methods:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">class</span><span class="pln"> </span><span class="typ">Ball</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; constructor</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">,</span><span class="pln"> radius</span><span class="pun">,</span><span class="pln"> color</span><span class="pun">,</span><span class="pln"> speedX</span><span class="pun">,</span><span class="pln"> speedY</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;">&nbsp; &nbsp; &nbsp; &nbsp; // see previous section for the code</li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; }</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; draw</span><span class="pun">(</span><strong><span class="pln">ctx</span></strong><span class="pun">)</span><span class="pln"> </span><span class="pun">{ // Nearly the same as the old drawFilledCircle function</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // BEST practice: save the context, use 2D transformations</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">save</span><span class="pun">();</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // translate the coordinate system, draw relative to it</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">translate</span><span class="pun">(</span><strong><span class="kwd">this</span><span class="pun">.</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">this</span><span class="pun">.</span><span class="pln">y</span></strong><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillStyle </span><span class="pun">=</span><span class="pln"> </span><strong><span class="kwd">this</span><span class="pun">.</span><span class="pln">color</span><span class="pun">;</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // (0, 0) is the top left corner of the monster.</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">beginPath</span><span class="pun">();</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">arc</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><strong><span class="kwd">this</span><span class="pun">.</span><span class="pln">radius</span></strong><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">*</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">PI</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fill</span><span class="pun">();</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // BEST practice: restore the context</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">restore</span><span class="pun">();</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; }</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; move</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; this</span><span class="pun">.</span><span class="pln">x </span><span class="pun">+=</span><span class="pln"> </span><span class="kwd">this</span><span class="pun">.</span><span class="pln">speedX</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; this</span><span class="pun">.</span><span class="pln">y </span><span class="pun">+=</span><span class="pln"> </span><span class="kwd">this</span><span class="pun">.</span><span class="pln">speedY</span><span class="pun">;</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; }</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

Explanations:

+ _Line 6_: the `draw` function's content is nearly the same as the `drawFilledCircle` function we previously used. We replaced all `c.x`, `c.y` etc. by `this.x`, `this.y`, to use the properties of the current object. This means that when we create a ball with `var b = new Ball(...);` and when we draw it using `b.draw(ctx)`, then `this.x` will be the value of the x property of the ball b, etc.
+ _Line 23_: the move function takes no parameter as it will add the value of the speedX/speedY properties to the current `x` and `y` value of the current ball.

<span style="color: brown;">Notice that we did not take into account the <code>globalSpeedMultiplier</code> we had in the old moveAllBalls function, as this is not something that is individually relevant to each ball: it is more something that affect ALL balls. <b>This should raise an alert: use an ES6 class property for that!</b></span>

In other words, even if zero ball has been created, this `globalSpeedMultiplier` is set and can be modified using a slider in the graphic user interface. Consequently, it is not a ball property, __more a property of the Ball class itself.__

This setting could be created using a class property, as seen in a previous section of this course.


#### Example: draw and move balls

And here is how we can now move and draw ALL balls

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> drawAllBalls2</span><span class="pun">(</span><span class="pln">ballArray</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ballArray</span><span class="pun">.</span><span class="pln">forEach</span><span class="pun">(</span><span class="kwd">function</span><span class="pun">(</span><span class="pln">b</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;<strong> b</strong></span><strong><span class="pun">.</span><span class="pln">draw</span><span class="pun">(</span><span class="pln">ctx</span><span class="pun">);</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; });</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> moveAllBalls2</span><span class="pun">(</span><span class="pln">ballArray</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // iterate on all balls in array</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; balls</span><span class="pun">.</span><span class="pln">forEach</span><span class="pun">(</span><span class="kwd">function</span><span class="pun">(</span><span class="pln">b</span><span class="pun">,</span><span class="pln"> index</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // b is the current ball in the array</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;<strong> b</strong></span><strong><span class="pun">.</span><span class="pln">move</span><span class="pun">();</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; testCollisionBallWithWalls</span><span class="pun">(</span><span class="pln">b</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; testCollisionWithPlayer</span><span class="pun">(</span><span class="pln">b</span><span class="pun">,</span><span class="pln"> index</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">});</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>


And here is the CodePen version of the game that includes these improvements:

[CodePen Demo](https://codepen.io/w3devcampus/pen/EWzgpr)

[Local Demo](src/04d-example01.html)








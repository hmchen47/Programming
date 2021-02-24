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








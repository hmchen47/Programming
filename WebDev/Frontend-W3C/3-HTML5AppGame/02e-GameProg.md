# Module 2: Game programming with HTML5 section


## 2.5 Animating multiple objects, collision detection

### 2.5.1 Animating multiple objects

#### Live coding video: animating multiple objects

<a href="https://edx-video.net/W3CHTM52/W3CHTM52T415-V001700_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript Download](https://bit.ly/2SRKvzF)

In this section, we will see how we can animate and control not only the player but also other objects on the screen.

Let's study a simple example: animating a few balls and detecting collisions with the surrounding walls. For the sake of simplicity, we will not use time-based animation in the first examples.


#### Wall collisions with multiple balls

__Animating multiple balls which bounce off horizontal and vertical walls__

[Online example](https://jsbin.com/fikomik/edit?js,output) at JSBin:

[Local Demo](src/02e-example01.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick= "window.open("https://bit.ly/3cYKbWP")"
    src    = "https://bit.ly/35EjWAV"
    alt    = "Some circular balls that bounce agains vertical and horizontal borders of the canvas"
    title  = "Some circular balls that bounce agains vertical and horizontal borders of the canvas"
  />
</figure>

In this example, we define a constructor function for creating balls. This is a way to design JavaScript "pseudo classes" as found in other object-oriented languages like Java, C# etc. It's useful when you plan to create many objects of the same class. Using this we could animate hundreds of balls on the screen.

Each ball has an x and y position, and in this example, instead of working with angles, we defined two "speeds" - horizontal and vertical speeds - in the form of the increments we will add to the x and y positions at each frame of animation. We also added a variable for adjusting the size of the balls: the radius.

Here is the constructor function for building balls:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com">// Constructor function for balls</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> </span><span class="typ">Ball</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">,</span><span class="pln"> vx</span><span class="pun">,</span><span class="pln"> vy</span><span class="pun">,</span><span class="pln"> diameter</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">&nbsp; // property of each ball: a x and y position, speeds, radius</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">x </span><span class="pun">=</span><span class="pln"> x</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">y </span><span class="pun">=</span><span class="pln"> y</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">vx </span><span class="pun">=</span><span class="pln"> vx</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">vy </span><span class="pun">=</span><span class="pln"> vy</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">radius </span><span class="pun">=</span><span class="pln"> diameter</span><span class="pun">/</span><span class="lit">2</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; // methods</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">draw </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">beginPath</span><span class="pun">();</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">arc</span><span class="pun">(</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">this</span><span class="pun">.</span><span class="pln">y</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">this</span><span class="pun">.</span><span class="pln">radius</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">*</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">PI</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fill</span><span class="pun">();</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">};</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">move </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// add horizontal increment to the x pos</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// add vertical increment to the y pos</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">x </span><span class="pun">+=</span><span class="pln"> </span><span class="kwd">this</span><span class="pun">.</span><span class="pln">vx</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">y </span><span class="pun">+=</span><span class="pln"> </span><span class="kwd">this</span><span class="pun">.</span><span class="pln">vy</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="pun">};</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div><br>

Using a constructor function makes it easy to build new balls as follows:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> b1 </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Ball</span><span class="pun">(</span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln">&nbsp;2, 2,&nbsp;</span><span class="lit">5</span><span class="pun">);</span><span class="pln"> </span><span class="com">// x, y, vx, vy, radius</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> b1 </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Ball</span><span class="pun">(</span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">130</span><span class="pun">,</span><span class="pln">&nbsp;4, 5,&nbsp;</span><span class="lit">5</span><span class="pun">);</span><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">etc</span><span class="pun">...</span></li>
</ol></div><br>

We defined two methods in the constructor function for moving the ball and for drawing the ball as a black filled circle. Here is the syntax for moving and drawing a ball:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">b1</span><span class="pun">.</span><span class="pln">draw</span><span class="pun">();</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">b1</span><span class="pun">.</span><span class="pln">move</span><span class="pun">();</span></li>
</ol></div><br>

We will call these methods from inside the mainLoop, and as you'll see, we will create many balls. This object-oriented design makes it easier to handle large quantities.

Here is the rest of the code from this example:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> canvas</span><span class="pun">,</span><span class="pln"> ctx</span><span class="pun">,</span><span class="pln"> width</span><span class="pun">,</span><span class="pln"> height</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="com">// array of balls to animate</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="kwd">var</span><span class="pln"> ballArray </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[];</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> init</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; canvas </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#myCanvas"</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; ctx </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">getContext</span><span class="pun">(</span><span class="str">'2d'</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; width </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">width</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; height </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">height</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><strong><span class="com">// try to change this number</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; createBalls</span><span class="pun">(</span><span class="lit">16</span><span class="pun">);</span></strong><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; requestAnimationFrame</span><span class="pun">(</span><span class="pln">mainLoop</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> createBalls</span><span class="pun">(</span><span class="pln">numberOfBalls</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">for</span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i</span><span class="pun">=</span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> numberOfBalls</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><strong><span class="com">// Create a ball with random position and speed. </span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// You can change the radius</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> ball </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Ball</span><span class="pun">(</span><span class="pln">width</span><span class="pun">*</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">random</span><span class="pun">(),</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; height</span><span class="pun">*</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">random</span><span class="pun">(),</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">(</span><span class="lit">10</span><span class="pun">*</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">random</span><span class="pun">())-</span><span class="lit">5</span><span class="pun">,</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">(</span><span class="lit">10</span><span class="pun">*</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">random</span><span class="pun">())-</span><span class="lit">5</span><span class="pun">,</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="lit">30</span><span class="pun">);</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><strong><span class="pln"> </span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">//&nbsp;add the ball to the array</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>ballArray</strong></span><strong><span class="pun">[</span><span class="pln">i</span><span class="pun">]</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> ball</span><span class="pun">;</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">}</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> mainLoop</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// clear the canvas</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; ctx</span><span class="pun">.</span><span class="pln">clearRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> width</span><span class="pun">,</span><span class="pln"> height</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><strong><span class="com">// for each ball in the array</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp;&nbsp;</span><span class="kwd">for</span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i</span><span class="pun">=</span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> ballArray</span><span class="pun">.</span><span class="pln">length</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> ball </span><span class="pun">=</span><span class="pln"> ballArray</span><span class="pun">[</span><span class="pln">i</span><span class="pun">];&nbsp;</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><strong><span class="pln"> </span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// 1) move the ball</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; ball</span><span class="pun">.</span><span class="pln">move</span><span class="pun">();</span><span class="pln"> </span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="pln"> </span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// 2) test if the ball collides with a wall</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;&nbsp;testCollisionWithWalls</span><span class="pun">(</span><span class="pln">ball</span><span class="pun">);</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><strong><span class="pln"> </span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// 3) draw the ball</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; ball</span><span class="pun">.</span><span class="pln">draw</span><span class="pun">();</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp;&nbsp;</span><span class="pun">}</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// ask for a new frame of animation at 60f/s</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; window</span><span class="pun">.</span><span class="pln">requestAnimationFrame</span><span class="pun">(</span><span class="pln">mainLoop</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> testCollisionWithWalls</span><span class="pun">(</span><span class="pln">ball</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// left</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">ball</span><span class="pun">.</span><span class="pln">x </span><span class="pun">&lt;</span><span class="pln"> ball</span><span class="pun">.</span><span class="pln">radius</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{ // x and y of the ball are at the center of the circle</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ball</span><span class="pun">.</span><span class="pln">x </span><span class="pun">=</span><span class="pln"> ball</span><span class="pun">.</span><span class="pln">radius</span><span class="pun">; &nbsp; &nbsp; // if collision, we replace the ball at a position</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ball</span><span class="pun">.</span><span class="pln">vx </span><span class="pun">*=</span><span class="pln"> </span><span class="pun">-</span><span class="lit">1</span><span class="pun">; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// where it's exactly in contact with the left border</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">} &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // and we reverse the horizontal speed</span><span class="pln"></span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// right</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">ball</span><span class="pun">.</span><span class="pln">x </span><span class="pun">&gt;</span><span class="pln"> width </span><span class="pun">-</span><span class="pln"> </span><span class="pun">(</span><span class="pln">ball</span><span class="pun">.</span><span class="pln">radius</span><span class="pun">))</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ball</span><span class="pun">.</span><span class="pln">x </span><span class="pun">=</span><span class="pln"> width </span><span class="pun">-</span><span class="pln"> </span><span class="pun">(</span><span class="pln">ball</span><span class="pun">.</span><span class="pln">radius</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ball</span><span class="pun">.</span><span class="pln">vx </span><span class="pun">*=</span><span class="pln"> </span><span class="pun">-</span><span class="lit">1</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">}</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// up</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">ball</span><span class="pun">.</span><span class="pln">y </span><span class="pun">&lt;</span><span class="pln"> ball</span><span class="pun">.</span><span class="pln">radius</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ball</span><span class="pun">.</span><span class="pln">y </span><span class="pun">=</span><span class="pln"> ball</span><span class="pun">.</span><span class="pln">radius</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ball</span><span class="pun">.</span><span class="pln">vy </span><span class="pun">*=</span><span class="pln"> </span><span class="pun">-</span><span class="lit">1</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">}</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// down</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">ball</span><span class="pun">.</span><span class="pln">y </span><span class="pun">&gt;</span><span class="pln"> height </span><span class="pun">-</span><span class="pln"> </span><span class="pun">(</span><span class="pln">ball</span><span class="pun">.</span><span class="pln">radius</span><span class="pun">))</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ball</span><span class="pun">.</span><span class="pln">y </span><span class="pun">=</span><span class="pln"> height </span><span class="pun">-</span><span class="pln"> </span><span class="pun">(</span><span class="pln">ball</span><span class="pun">.</span><span class="pln">radius</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ball</span><span class="pun">.</span><span class="pln">vy </span><span class="pun">*=</span><span class="pln"> </span><span class="pun">-</span><span class="lit">1</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">}</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div><br>

Notice that:

+ All the balls are stored in an array (_line 4_),
+ We wrote a `createBalls(nb)` function that creates a given number of balls (and stores them in the array) with random values for position and speed (_lines 18-32_)
+ In the mainLoop, we iterate on the array of balls and for each ball we: 1) move it, 2) test if it collides with the boundaries of the canvas (in the function `testCollisionWithWalls`), and 3) we draw the balls (_lines 38-50_). The order of these steps is not critical and may be changed.
+ The function that tests collisions is straightforward (_lines 55-76_).  We did not use "if... else if" since a ball may sometimes touch two walls at once (in the corners). In that rare case, we need to invert both the horizontal and vertical speeds. When a ball collides with a wall, we need to replace it in a position where it is no longer against the wall (otherwise it will collide again during the next animation loop execution).


#### Direction and velocity with wall colisions

__Similar example but with the ball direction as an angle, and a single velocity variable__

Try this [example at JSBin](https://jsbin.com/begaci/edit): it behaves in the same way as the previous example.

[Local Demo](src/02e-example02.html)

Note that we just changed the way we designed the balls and computed the angles after they rebound from the walls. The changes are highlighted in bold:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> canvas</span><span class="pun">,</span><span class="pln"> ctx</span><span class="pun">,</span><span class="pln"> width</span><span class="pun">,</span><span class="pln"> height</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="com">// Array of balls to animate</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> ballArray </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[];</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> init</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;">&nbsp; ...</li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> createBalls</span><span class="pun">(</span><span class="pln">numberOfBalls</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">for</span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i</span><span class="pun">=</span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> numberOfBalls</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// Create a ball with random position and speed. </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// You can change the radius</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> ball </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Ball</span><span class="pun">(</span><span class="pln">width</span><span class="pun">*</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">random</span><span class="pun">(),</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; height</span><span class="pun">*</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">random</span><span class="pun">(),</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; </span><strong><span class="pun">(</span><span class="lit">2</span><span class="pun">*</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">PI</span><span class="pun">)*</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">random</span><span class="pun">(), // angle</span></strong><span class="pln"></span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; </span><strong><span class="pun">(</span><span class="lit">10</span><span class="pun">*</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">random</span><span class="pun">())-</span><span class="lit">5</span><span class="pun">, &nbsp; &nbsp; &nbsp;// speed</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="lit">30</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// We add it in an array<br></span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ballArray</span><span class="pun">[</span><span class="pln">i</span><span class="pun">]</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> ball</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">}</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> mainLoop</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;...</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">}</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> testCollisionWithWalls</span><span class="pun">(</span><span class="pln">ball</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// left</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">ball</span><span class="pun">.</span><span class="pln">x </span><span class="pun">&lt;</span><span class="pln"> ball</span><span class="pun">.</span><span class="pln">radius</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;ball</span><span class="pun">.</span><span class="pln">x </span><span class="pun">=</span><span class="pln"> ball</span><span class="pun">.</span><span class="pln">radius</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;<strong>ball</strong></span><strong><span class="pun">.</span><span class="pln">angle </span><span class="pun">=</span><span class="pln"> </span><span class="pun">-</span><span class="pln">ball</span><span class="pun">.</span><span class="pln">angle </span><span class="pun">+</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">PI</span><span class="pun">;</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">}</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// right</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">ball</span><span class="pun">.</span><span class="pln">x </span><span class="pun">&gt;</span><span class="pln"> width </span><span class="pun">-</span><span class="pln"> </span><span class="pun">(</span><span class="pln">ball</span><span class="pun">.</span><span class="pln">radius</span><span class="pun">))</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ball</span><span class="pun">.</span><span class="pln">x </span><span class="pun">=</span><span class="pln"> width </span><span class="pun">-</span><span class="pln"> </span><span class="pun">(</span><span class="pln">ball</span><span class="pun">.</span><span class="pln">radius</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>ball</strong></span><strong><span class="pun">.</span><span class="pln">angle </span><span class="pun">=</span><span class="pln"> </span><span class="pun">-</span><span class="pln">ball</span><span class="pun">.</span><span class="pln">angle </span><span class="pun">+</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">PI</span><span class="pun">;</span></strong><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">}</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// up</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">ball</span><span class="pun">.</span><span class="pln">y </span><span class="pun">&lt;</span><span class="pln"> ball</span><span class="pun">.</span><span class="pln">radius</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ball</span><span class="pun">.</span><span class="pln">y </span><span class="pun">=</span><span class="pln"> ball</span><span class="pun">.</span><span class="pln">radius</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>ball</strong></span><strong><span class="pun">.</span><span class="pln">angle </span><span class="pun">=</span><span class="pln"> </span><span class="pun">-</span><span class="pln">ball</span><span class="pun">.</span><span class="pln">angle</span><span class="pun">;</span></strong><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">}</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// down</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">ball</span><span class="pun">.</span><span class="pln">y </span><span class="pun">&gt;</span><span class="pln"> height </span><span class="pun">-</span><span class="pln"> </span><span class="pun">(</span><span class="pln">ball</span><span class="pun">.</span><span class="pln">radius</span><span class="pun">))</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ball</span><span class="pun">.</span><span class="pln">y </span><span class="pun">=</span><span class="pln"> height </span><span class="pun">-</span><span class="pln"> </span><span class="pun">(</span><span class="pln">ball</span><span class="pun">.</span><span class="pln">radius</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;<strong> ball</strong></span><strong><span class="pun">.</span><span class="pln">angle </span><span class="pun">=-</span><span class="pln">ball</span><span class="pun">.</span><span class="pln">angle</span><span class="pun">;</span></strong><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">}</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="com">// constructor function for balls</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> </span><span class="typ">Ball</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">,</span><span class="pln"> angle</span><span class="pun">,</span><span class="pln"> v</span><span class="pun">,</span><span class="pln"> diameter</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">x </span><span class="pun">=</span><span class="pln"> x</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">y </span><span class="pun">=</span><span class="pln"> y</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><strong><span class="kwd">this</span><span class="pun">.</span><span class="pln">angle </span><span class="pun">=</span><span class="pln"> angle</span><span class="pun">;</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp;&nbsp;</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">v </span><span class="pun">=</span><span class="pln"> v</span><span class="pun">;</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">radius </span><span class="pun">=</span><span class="pln"> diameter</span><span class="pun">/</span><span class="lit">2</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">draw </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;">&nbsp; &nbsp;...</li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">};</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">move </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// add horizontal increment to the x pos</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// add vertical increment to the y pos</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><strong><span class="kwd">this</span><span class="pun">.</span><span class="pln">x </span><span class="pun">+=</span><span class="pln"> </span><span class="kwd">this</span><span class="pun">.</span><span class="pln">v </span><span class="pun">*</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">cos</span><span class="pun">(</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">angle</span><span class="pun">);</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">y </span><span class="pun">+=</span><span class="pln"> </span><span class="kwd">this</span><span class="pun">.</span><span class="pln">v </span><span class="pun">*</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">sin</span><span class="pun">(</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">angle</span><span class="pun">);</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">};</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div><br>

Using angles or horizontal and vertical increments is equivalent. However, one method might be preferable to the other: for example, to control an object that follows the mouse, or that tracks another object in order to attack it, angles would be more practical input to the computations required.


#### Notes for 2.5.1 Animating multiple objects

+ Pseudo class
  + define a constructor function for creating objects
  + found in other object-oriented languages, such as Java, C#, etc.
  + useful to create many objects of the same classes

+ Example: direction and velocity w/ wall collisions
  + constructor function for balls w/ x & y velocity<a name="ballXY"></a>: `function Ball(x, y, vx, vy, diameter) {...}`
    + declare ball properties: `this.x = x; this.y = y; this.vx = vx; this.vy = vy; this.radius = diameters/2;`
    + draw ball: `this.draw = function() { ctx.beginPath(); ctx.arc(this.x, this.y, this.radius, 0.2*Math.PI); ctx.fill(); };`
    + move ball: `this.move = function() { this.x += this.x; this.y += this.y; };`
  + declare variables<a name="vars"></a>: `var canvas, ctx, width, height;`
  + declare array of balls<a name="ballArray"></a>: `var ballArray = [];`
  + init page after DOM ready<a name="init"></a>: `function innit() {...}`
    + access canvas and set context: `var canvas = document.querySelector("#myCanvas"); var ctx = canvas.getContext("2d");`
    + set varables: `width = canvas.width; height = canvas.height;`
    + call to create balls: `createBalls(16);`
    + start animation loop: `requestAnimationFrame(mainLoop);`
  + create balls w/ x, y velocity: `function createBalls(numberOfBalls) {...}`
    + iterate to create balls: `for (var i-0; i<numberOfBalls; i++) {...}`
    + create ball: `var ball = new Ball(width*Math.random(), height*Math.random(), (10*Math.random())-5, (10*Math.random())-5, 30);`
    + add ball to array: `ballArray[i] = ball;`
  + create animation loop<a name="animationLoop"></a>: `function mainLoop() {...}`
    + empty canvas: `ctx.clearRect(0, 0, width, height);`
    + draw balls through loop: `for (var i=0; i<ballArray.length; i++) {...}`
      + get the ball: `var ball = ballArray[i];`
      + move the ball: `ball.move();`
      + call to test collision: `textCollisionWithWalls(ball);`
      + draw the ball: `ball.draw();`
    + request for next frame: `window.requestAnimationFrame(mainLoop);`
  + text collision w/ x, y velocity: `function testCollisionWithWalls(ball) {...}`
    + (x, y): center of the circle
    + collision: replace the ball at position where it's exactly in contact w/ the border
    + test collision independently, `if...else if` not suitable
    + left colission: `if (ball.x < (ball.radius)) {ball.x = ball.radius; ball.vx *= -1;}`
    + right colission: `if (ball.x > width - ball.radius) {ball.x = width - ball.radius; ball.vx *= -1;}`
    + up colission: `if (ball.y < (ball.radius)) {ball.y = ball.radius; ball.vy *= -1;}`
    + right colission: `if (ball.y > width - ball.radius) {ball.y = width - ball.radius; ball.vy *= -1;}`

+ Example: direction and velocity with wall colissions
  + [declare variables](#vars)
  + declare [array of balls](#ballArray)
  + [init page after DOM ready](#init)
  + create balls w/ angle & speed: `function createBalls(numberOfBalls) {...}`
    + iterate to create balls: `for (var i-0; i<numberOfBalls; i++) {...}`
    + create ball: `var ball = new Ball(width*Math.random(), height*Math.random(), (2*Math.PI)*Math.random(), (10*Math.random())-5, 30);`
    + add ball to array: `ballArray[i] = ball;`
  + create [animation loop](#animationLoop)
  + text collision w/ angle & speed: `function testCollisionWithWalls(ball) {...}`
    + test collision independently, `if...else if` not suitable
    + left colission: `if (ball.x < (ball.radius)) {ball.x = ball.radius; ball.angle = -ball.angle + Math.PI;}`
    + right colission: `if (ball.x > width - ball.radius) {ball.x = width - ball.radius; ball.angle = -ball.angle + Math.PI;}`
    + up colission: `if (ball.y < (ball.radius)) {ball.y = ball.radius; ball.angle = -ball.angle;}`
    + right colission: `if (ball.y > width - ball.radius) {ball.y = width - ball.radius; ball.angle = -ball.angle;}`
  + constructor function for balls w/ speed and angle<a name="ballSA"></a>: `function Ball(x, y, angle, v, diameter) {...}`
    + declare ball properties: `this.x = x; this.y = y; this.angle = angle; this.v = v; this.radius = diameters/2;`
    + draw ball: `this.draw = function() { ctx.beginPath(); ctx.arc(this.x, this.y, this.radius, 0.2*Math.PI); ctx.fill(); };`
    + move ball: `this.move = function() { this.x += this.v * Math.cos(this.angle); this.y += this.v * Math.sin(this.angle); };`


### 2.5.2 Adding balls to the game framework

This time, let's extract the source code used to create the balls, and include it in our game framework. We are also going to use time-based animation. The distance that the player and each ball should move is computed and may vary between animation frames, depending  on the time-delta since the previous frame.

[Online example](https://jsbin.com/tehuve/edit) at JSBin.

[Local Demo](src/02e-example03.html)

Try to move the monster with arrow keys and use the mouse button while moving to change the monster's speed. Look at the source code and change the parameters controlling the creation of the balls: number, speed, radius, etc. Also, try changing the monster's default speed. See the results.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick= "window.open("https://bit.ly/3xEXEuO")"
    src    = "https://bit.ly/3gPYw8Y"
    alt    = "Monster + balls in the game framework. On the screen we see the monster + a bunch of balls"
    title  = "Monster + balls in the game framework. On the screen we see the monster + a bunch of balls"
  />
</figure>

For this version, we copied and pasted some code from the previous example and we also modified the mainLoop to make it more readable. In a next lesson, we will split the game engine into different files and clean the code-base to make it more manageable. But for the moment, jsbin.com is a good playground to try-out and test things...

The new mainLoop:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> mainLoop </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">time</span><span class="pun">){</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">//main function, called each frame </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; measureFPS</span><span class="pun">(</span><span class="pln">time</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// number of ms since last frame draw</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; delta </span><span class="pun">=</span><span class="pln"> timer</span><span class="pun">(</span><span class="pln">time</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Clear the canvas</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; clearCanvas</span><span class="pun">();</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Draw the monster</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; drawMyMonster</span><span class="pun">(</span><span class="pln">monster</span><span class="pun">.</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> monster</span><span class="pun">.</span><span class="pln">y</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Check inputs and move the monster</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; updateMonsterPosition</span><span class="pun">(</span><span class="pln">delta</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Update and draw balls</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; updateBalls</span><span class="pun">(</span><span class="pln">delta</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Call the animation loop every 1/60th of second</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; requestAnimationFrame</span><span class="pun">(</span><span class="pln">mainLoop</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">};</span></li>
</ol></div><br>

As you can see, we draw the player/monster, we update its position; and we call an `updateBalls` function to do the same  for the balls: draw and update their position.

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> updateMonsterPosition</span><span class="pun">(</span><span class="pln">delta</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; monster</span><span class="pun">.</span><span class="pln">speedX </span><span class="pun">=</span><span class="pln"> monster</span><span class="pun">.</span><span class="pln">speedY </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// check inputStates</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">inputStates</span><span class="pun">.</span><span class="pln">left</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; monster</span><span class="pun">.</span><span class="pln">speedX </span><span class="pun">=</span><span class="pln"> </span><span class="pun">-</span><span class="pln">monster</span><span class="pun">.</span><span class="pln">speed</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">inputStates</span><span class="pun">.</span><span class="pln">up</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; monster</span><span class="pun">.</span><span class="pln">speedY </span><span class="pun">=</span><span class="pln"> </span><span class="pun">-</span><span class="pln">monster</span><span class="pun">.</span><span class="pln">speed</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pun">...</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Compute the incX and incY in pixels depending</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// on the time elapsed since last redraw</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; monster</span><span class="pun">.</span><span class="pln">x </span><span class="pun">+=</span><span class="pln"> calcDistanceToMove</span><span class="pun">(</span><span class="pln">delta</span><span class="pun">,</span><span class="pln"> monster</span><span class="pun">.</span><span class="pln">speedX</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; monster</span><span class="pun">.</span><span class="pln">y </span><span class="pun">+=</span><span class="pln"> calcDistanceToMove</span><span class="pun">(</span><span class="pln">delta</span><span class="pun">,</span><span class="pln"> monster</span><span class="pun">.</span><span class="pln">speedY</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> updateBalls</span><span class="pun">(</span><span class="pln">delta</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// for each ball in the array</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">for</span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i</span><span class="pun">=</span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> ballArray</span><span class="pun">.</span><span class="pln">length</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> ball </span><span class="pun">=</span><span class="pln"> ballArray</span><span class="pun">[</span><span class="pln">i</span><span class="pun">];</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// 1) move the ball</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ball</span><span class="pun">.</span><span class="pln">move</span><span class="pun">();</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// 2) test if the ball collides with a wall</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;testCollisionWithWalls</span><span class="pun">(</span><span class="pln">ball</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// 3) draw the ball</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ball</span><span class="pun">.</span><span class="pln">draw</span><span class="pun">();</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">}</span><span class="pln"> </span></li>
</ol></div><br>

Now, in order to turn this into a game, we need to create some interactions between the player (the monster) and the obstacles/enemies (balls, walls)... It's time to take a look at collision detection.


#### Notes for 2.5.2 Adding balls to the game framework

+ Example: game framework w/ bouncing balls
  + tasks:
    + move the moster w/ arrow keys
    + accelerate monster w/ mouse button
    + animate bouncing balls
  + generate animation loop: `var mainloop = function(time) {...}`
    + call to measure FPS: `measureFPS(time);`
    + clear canvas: `clearCanvas();`
    + call to draw monster: `drawMyMonster(monster.x, monster.y);`
    + call to move monster: `updateMonsterPosition(delta);`
    + call to draw balls: `updateBalls(delta);`
    + call for next frame: `requestAnimationFrame(mainLoop);`
  + calculate the new position of monster: `function updateMonsterPosition(delta) {...}`
    + init speed: `monster.speedX = monster.speedY = 0;`
    + set left arrow key: `if (inputStates.left) {monster.speedX = -monster.speed;}`
    + set up arrow key: `if (inputStates.up) {monster.speedY = -monster.speed;}`
    + ...
    + compute the position: `monster.x += calcDistanceToMove(delta, monster.speedX); monster.y += calcDistanceToMove(delta, monster.speedY);`







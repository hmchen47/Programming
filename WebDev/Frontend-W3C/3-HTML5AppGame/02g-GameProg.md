# Module 2: Game programming with HTML5 section


## 2.7 Game states


### 2.7.1 Menus, high score tables, etc.


#### Properties of player and enemy objects

With our game framework handling the basics, we can make things more exciting by causing something to happen when a collision occurs - maybe the player 'dies', balls are removed, or we should add to your score? Usually, we add extra properties to the player and enemy objects. For example, a boolean `dead` property that will record if an object is dead or alive: if a ball is marked "dead", do not draw it! If all balls are dead: go to the next level with more balls, faster balls, etc.

Let's try adding a `dead` property to balls and consult it before drawing them. We could also test to see if all the balls are dead, in which case we recreate them and add one more ball. Let's update the score whenever the monster eats a ball. And finally, we should add a test in the `createBalls` function to ensure that no balls are created on top of the monster.

[Try this jsBin!](https://jsbin.com/jixolu/edit?js,console,output)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3xRoIXS')"
    src    = "https://bit.ly/3j69VV0"
    alt    = "Eat the ball game"
    title  = "Eat the ball game"
  />
</figure>


Source code extract:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> updateBalls</span><span class="pun">(</span><span class="pln">delta</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><strong>// for each ball in the array</strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> allBallDead </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">;</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">for</span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i</span><span class="pun">=</span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> ballArray</span><span class="pun">.</span><span class="pln">length</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> ball </span><span class="pun">=</span><span class="pln"> ballArray</span><span class="pun">[</span><span class="pln">i</span><span class="pun">];</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>&nbsp;</strong></span><strong><span class="kwd">if</span><span class="pun">(</span><span class="pln">ball</span><span class="pun">.</span><span class="pln">dead</span><span class="pun">)</span><span class="pln"> </span><span class="kwd">continue</span><span class="pun">; // do nothing if the ball is dead</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>&nbsp;</strong></span><strong>// if we are here: the ball is not dead</strong></li>
<li class="L0" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp;allBallDead </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">;</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// 1) move the ball</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;ball</span><span class="pun">.</span><span class="pln">move</span><span class="pun">();</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// 2) test if the ball collides with a wall</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;testCollisionWithWalls</span><span class="pun">(</span><span class="pln">ball</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// Test if the monster collides</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">if</span><span class="pun">(</span><span class="pln">circRectsOverlap</span><span class="pun">(</span><span class="pln">monster</span><span class="pun">.</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> monster</span><span class="pun">.</span><span class="pln">y</span><span class="pun">,</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;monster</span><span class="pun">.</span><span class="pln">width</span><span class="pun">,</span><span class="pln"> monster</span><span class="pun">.</span><span class="pln">height</span><span class="pun">,</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;ball</span><span class="pun">.</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> ball</span><span class="pun">.</span><span class="pln">y</span><span class="pun">,</span><span class="pln"> ball</span><span class="pun">.</span><span class="pln">radius</span><span class="pun">))</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">//change the color of the ball</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; ball</span><span class="pun">.</span><span class="pln">color </span><span class="pun">=</span><span class="pln"> </span><span class="str">'red'</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; <strong>ball</strong></span><strong><span class="pun">.</span><span class="pln">dead </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">;</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// Here, a sound effect would greatly improve</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// the experience!</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;<strong> currentScore</strong></span><strong><span class="pun">+=</span><span class="pln"> </span><span class="lit">1</span><span class="pun">;</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// 3) draw the ball</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;ball</span><span class="pun">.</span><span class="pln">draw</span><span class="pun">();</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">&nbsp;<strong> if</strong></span><strong><span class="pun">(</span><span class="pln">allBallDead</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// reset all balls, create more balls each time</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">//&nbsp;as a way&nbsp;of increasing the difficulty</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong>&nbsp; &nbsp; &nbsp;// in a real game: change the level, play nice music!</strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp;nbBalls</span><span class="pun">++;</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp;createBalls</span><span class="pun">(</span><span class="pln">nbBalls</span><span class="pun">);</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div><br>


#### Game states: menus, high score tables, etc.

In this example, let's make use of a global `gameState` variable for managing the life-cycle of the game. Usually, there is a main menu with a "start new game" option, then we play the game, and if we 'die' we suffer a game-over screen, etc...

Ah!... you think that the game has been too easy? Let's reverse the game: now you must survive without being touched by a ball!!!

Also, every five seconds a next level will start: the set of balls is re-created, and each level has two more than before. How long can you survive?

Try this JsBin, then look at the source code. Start from the `mainloop`!

`currentGameState = gameStates.gameOver`:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3xRoIXS')"
    src    = "https://bit.ly/35WQ2aV"
    alt    = "Game Over Screen, asking to press space to start again"
    title  = "Game Over Screen, asking to press space to start again"
  />
</figure>


`currentGameState = gameStates.gamerunning`:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3xRoIXS')"
    src    = "https://bit.ly/3gRbkxa"
    alt    = "game running, showing score, time, level"
    title  = "game running, showing score, time, level"
  />
</figure>


Game state management in the JavaScript code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="pun">...</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// game states</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> gameStates </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;mainMenu</span><span class="pun">:</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;gameRunning</span><span class="pun">:</span><span class="pln"> </span><span class="lit">1</span><span class="pun">,</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;gameOver</span><span class="pun">:</span><span class="pln"> </span><span class="lit">2</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">};</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> currentGameState </span><span class="pun">=</span><span class="pln"> gameStates</span><span class="pun">.</span><span class="pln">gameRunning</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> currentLevel </span><span class="pun">=</span><span class="pln"> </span><span class="lit">1</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> TIME_BETWEEN_LEVELS </span><span class="pun">=</span><span class="pln"> </span><span class="lit">5000</span><span class="pun">;</span><span class="pln"> </span><span class="com">// 5 seconds</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> currentLevelTime </span><span class="pun">=</span><span class="pln"> TIME_BETWEEN_LEVELS</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">...</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> mainLoop </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> </span><span class="pun">(</span><span class="pln">time</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;...</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// number of ms since last frame draw</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;delta </span><span class="pun">=</span><span class="pln"> timer</span><span class="pun">(</span><span class="pln">time</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Clear the canvas</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;clearCanvas</span><span class="pun">();</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;// monster.dead is set to true in updateBalls when there</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;// is a collision</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><strong><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">monster</span><span class="pun">.</span><span class="pln">dead</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; currentGameState </span><span class="pun">=</span><span class="pln"> gameStates</span><span class="pun">.</span><span class="pln">gameOver</span><span class="pun">;</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><strong><span class="kwd">switch</span><span class="pln"> </span><span class="pun">(</span><span class="pln">currentGameState</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">case</span><span class="pln"> gameStates</span><span class="pun">.</span><span class="pln">gameRunning</span><span class="pun">:</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// draw the monster</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; drawMyMonster</span><span class="pun">(</span><span class="pln">monster</span><span class="pun">.</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> monster</span><span class="pun">.</span><span class="pln">y</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// Check inputs and move the monster</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; updateMonsterPosition</span><span class="pun">(</span><span class="pln">delta</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// update and draw balls</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; updateBalls</span><span class="pun">(</span><span class="pln">delta</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// display Score</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; displayScore</span><span class="pun">();</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// decrease currentLevelTime. Survive 5s per level</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// When &lt; 0 go to next level</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;currentLevelTime </span><span class="pun">-=</span><span class="pln"> delta</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">currentLevelTime </span><span class="pun">&lt;</span><span class="pln"> </span><span class="lit">0</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; goToNextLevel</span><span class="pun">();</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">break</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><strong><span class="kwd">case</span><span class="pln"> gameStates</span><span class="pun">.</span><span class="pln">mainMenu</span><span class="pun">:</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com">// TO DO! We could have a main menu with high scores etc.</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">break</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><strong><span class="kwd">case</span><span class="pln"> gameStates</span><span class="pun">.</span><span class="pln">gameOver</span><span class="pun">:</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"GAME OVER"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">50</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"Press SPACE to start again"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">50</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"Move with arrow keys"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">50</span><span class="pun">,</span><span class="pln"> </span><span class="lit">200</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"Survive 5 seconds for next level"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">50</span><span class="pun">,</span><span class="pln"> </span><span class="lit">250</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">inputStates</span><span class="pun">.</span><span class="pln">space</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; startNewGame</span><span class="pun">();</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">break</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp;...</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">};</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">...&nbsp;</span></li>
</ol></div><br>

And below are the functions for starting a new level, starting a new game, and the `updateBalls` function that determines when a player loses and changes the current game-state to GameOver:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> startNewGame</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; monster</span><span class="pun">.</span><span class="pln">dead </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; currentLevelTime </span><span class="pun">=</span><span class="pln"> </span><span class="lit">5000</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; currentLevel </span><span class="pun">=</span><span class="pln"> </span><span class="lit">1</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; nbBalls </span><span class="pun">=</span><span class="pln"> </span><span class="lit">5</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; createBalls</span><span class="pun">(</span><span class="pln">nbBalls</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>currentGameState </strong></span><strong><span class="pun">=</span><span class="pln"> gameStates</span><span class="pun">.</span><span class="pln">gameRunning</span><span class="pun">;</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> goToNextLevel</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// reset time available for next level</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// 5 seconds in this example</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;currentLevelTime </span><span class="pun">=</span><span class="pln"> </span><span class="lit">5000</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;currentLevel</span><span class="pun">++;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Add two balls per level</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;nbBalls </span><span class="pun">+=</span><span class="pln"> </span><span class="lit">2</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;createBalls</span><span class="pun">(</span><span class="pln">nbBalls</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> updateBalls</span><span class="pun">(</span><span class="pln">delta</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// Move and draw each ball, test collisions, </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">for</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> ballArray</span><span class="pun">.</span><span class="pln">length</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;...</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com">// Test if the monster collides</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">circRectsOverlap</span><span class="pun">(</span><span class="pln">monster</span><span class="pun">.</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> monster</span><span class="pun">.</span><span class="pln">y</span><span class="pun">,</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; monster</span><span class="pun">.</span><span class="pln">width</span><span class="pun">,</span><span class="pln"> monster</span><span class="pun">.</span><span class="pln">height</span><span class="pun">,</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ball</span><span class="pun">.</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> ball</span><span class="pun">.</span><span class="pln">y</span><span class="pun">,</span><span class="pln"> ball</span><span class="pun">.</span><span class="pln">radius</span><span class="pun">))</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com">//change the color of the ball</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;ball</span><span class="pun">.</span><span class="pln">color </span><span class="pun">=</span><span class="pln"> </span><span class="str">'red'</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <strong>&nbsp;monster</strong></span><strong><span class="pun">.</span><span class="pln">dead </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">;</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com">// Here, a sound effect greatly improves</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com">// the experience!</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;plopSound</span><span class="pun">.</span><span class="pln">play</span><span class="pun">();</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com">// 3) draw the ball</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;ball</span><span class="pun">.</span><span class="pln">draw</span><span class="pun">();</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
</ol></div>








# Module 2: Game programming with HTML5 section


## 2.7 Game states


### 2.7.1 Menus, high score tables, etc.


#### Properties of player and enemy objects

With our game framework handling the basics, we can make things more exciting by causing something to happen when a collision occurs - maybe the player 'dies', balls are removed, or we should add to your score? Usually, we add extra properties to the player and enemy objects. For example, a boolean `dead` property that will record if an object is dead or alive: if a ball is marked "dead", do not draw it! If all balls are dead: go to the next level with more balls, faster balls, etc.

Let's try adding a `dead` property to balls and consult it before drawing them. We could also test to see if all the balls are dead, in which case we recreate them and add one more ball. Let's update the score whenever the monster eats a ball. And finally, we should add a test in the `createBalls` function to ensure that no balls are created on top of the monster.

[Try this jsBin!](https://jsbin.com/jixolu/edit?js,console,output)

[Local Demo](src/02g-example01.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 12vw;"
    onclick= "window.open('https://bit.ly/3xRoIXS')"
    src    = "https://bit.ly/3j69VV0"
    alt    = "Eat the ball game"
    title  = "Eat the ball game"
  />
</figure>


Source code extract:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> updateBalls</span><span class="pun">(</span><span class="pln">delta</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><strong style="color: red;">// for each ball in the array</strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong style="color: red;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> allBallDead </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">;</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">for</span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i</span><span class="pun">=</span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> ballArray</span><span class="pun">.</span><span class="pln">length</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> ball </span><span class="pun">=</span><span class="pln"> ballArray</span><span class="pun">[</span><span class="pln">i</span><span class="pun">];</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong style="color: red;">&nbsp;</strong></span><strong style="color: red;"><span class="kwd">if</span><span class="pun">(</span><span class="pln">ball</span><span class="pun">.</span><span class="pln">dead</span><span class="pun">)</span><span class="pln"> </span><span class="kwd">continue</span><span class="pun">; // do nothing if the ball is dead</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong style="color: red;">&nbsp;</strong></span><strong style="color: red;">// if we are here: the ball is not dead</strong></li>
<li class="L0" style="margin-bottom: 0px;"><strong style="color: red;"><span class="pln">&nbsp; &nbsp; &nbsp;allBallDead </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">;</span></strong></li>
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
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; <strong style="color: red;">ball</strong></span><strong style="color: red;"><span class="pun">.</span><span class="pln">dead </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">;</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// Here, a sound effect would greatly improve</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// the experience!</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;<strong style="color: red;"> currentScore</strong></span><strong style="color: red;"><span class="pun">+=</span><span class="pln"> </span><span class="lit">1</span><span class="pun">;</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// 3) draw the ball</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;ball</span><span class="pun">.</span><span class="pln">draw</span><span class="pun">();</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">&nbsp;<strong style="color: red;"> if</strong></span><strong style="color: red;"><span class="pun">(</span><span class="pln">allBallDead</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><strong style="color: red;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// reset all balls, create more balls each time</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong style="color: red;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">//&nbsp;as a way&nbsp;of increasing the difficulty</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong style="color: red;">&nbsp; &nbsp; &nbsp;// in a real game: change the level, play nice music!</strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong style="color: red;"><span class="pln">&nbsp; &nbsp; &nbsp;nbBalls</span><span class="pun">++;</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><strong style="color: red;"><span class="pln">&nbsp; &nbsp; &nbsp;createBalls</span><span class="pun">(</span><span class="pln">nbBalls</span><span class="pun">);</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><strong style="color: red;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div><br>


#### Game states: menus, high score tables, etc.

In this example, let's make use of a global `gameState` variable for managing the life-cycle of the game. Usually, there is a main menu with a "start new game" option, then we play the game, and if we 'die' we suffer a game-over screen, etc...

Ah!... you think that the game has been too easy? Let's reverse the game: now you must survive without being touched by a ball!!!

Also, every five seconds a next level will start: the set of balls is re-created, and each level has two more than before. How long can you survive?

Try this JsBin, then look at the source code. Start from the `mainloop`!

`currentGameState = gameStates.gameOver` & `currentGameState = gameStates.gamerunning`:

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://bit.ly/3xRoIXS" ismap target="_blank">
    <img style="margin: 0.1em;" height=200
      src   = "https://bit.ly/35WQ2aV"
      alt   = "Game Over Screen, asking to press space to start again"
      title = "Game Over Screen, asking to press space to start again"
    >
    <img style="margin: 0.1em;" height=200
      src   = "https://bit.ly/3gRbkxa"
      alt   = "game running, showing score, time, level"
      title = "game running, showing score, time, level"
    >
  </a>
</div>


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
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><strong style="color: red;"><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">monster</span><span class="pun">.</span><span class="pln">dead</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><strong style="color: red;"><span class="pln">&nbsp; &nbsp; &nbsp; currentGameState </span><span class="pun">=</span><span class="pln"> gameStates</span><span class="pun">.</span><span class="pln">gameOver</span><span class="pun">;</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><strong style="color: red;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><strong style="color: red;"><span class="kwd">switch</span><span class="pln"> </span><span class="pun">(</span><span class="pln">currentGameState</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><strong style="color: red;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">case</span><span class="pln"> gameStates</span><span class="pun">.</span><span class="pln">gameRunning</span><span class="pun">:</span></strong></li>
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
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><strong style="color: red;"><span class="kwd">case</span><span class="pln"> gameStates</span><span class="pun">.</span><span class="pln">mainMenu</span><span class="pun">:</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com">// TO DO! We could have a main menu with high scores etc.</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">break</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><strong style="color: red;"><span class="kwd">case</span><span class="pln"> gameStates</span><span class="pun">.</span><span class="pln">gameOver</span><span class="pun">:</span></strong></li>
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
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong style="color: red;">currentGameState </strong></span><strong style="color: red;"><span class="pun">=</span><span class="pln"> gameStates</span><span class="pun">.</span><span class="pln">gameRunning</span><span class="pun">;</span></strong></li>
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
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <strong style="color: red;">&nbsp;monster</strong></span><strong style="color: red;"><span class="pun">.</span><span class="pln">dead </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">;</span></strong></li>
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


#### Notes for 2.7.1 Menus, high score tables, etc.

+ Example: properties for balls
  + tasks:
    + adding a `dead` property to balls and check before drawing
    + display score and update it as monster eats ball
    + add a test to ensure no balls created on top of monster
  + update ball position: `function updateBalls(delta) {...}`
    + declare variable: `var allBallDead = true;`
    + iterate through all balls: `for (var i=0; i<ballArray.length; i++) {...}`
      + declare ball: `var ball = ballArray[i];`
      + check existence of ball: `if (ball.dead) continue;`
      + set ball existed: `allBallDead = false;`
      + set ball position: `ball.move();`
      + test collision w/ walls: `textCollisionWithWalls(ball);`
      + test collision w/ monster: `if (circRectOverlap(monster.x, monster.y, monster.with, monster.height, ball.x, ball.y)) { ball.color = 'red'; ball.dead = true; currentScore += 1; }`
      + draw ball: `ball.draw();`
    + reset to create balls: `if (allBallDead) { nbBalls++; createBalls(nbBalls); }`

+ Example: game states
  + tasks
    + using a global `gameState` variable for managing the life cycle of the game
    + start next level game for 5 seconds
  + declare game state: `var gameStates = { mainMenu: 0, gameRunning: 1, gameOver: 2 };`
  + init variable values: `var currentGameState = gameStates.gameRunning; var currentLevel = 1; var TIME_BETWEEN_LEVELS = 5000; var currentLevelTime = TIME_BETWEEN_LEVELS;`
  + generate animation loop: `var mainLoop = function (time) {...};`
    + ...
    + get time difference btw frames: `delta = timer(time);`
    + clear the canvas: `clearCanvas();`
    + check monster existence: `if (monster.dead) { currentGameState = gameStates.gameOver; }`
    + select current game state: `switch (currentGameState) {...}`
      + case for game running: `case gameStates.gameRunning:`
        + draw monster: `drawMyMonster(monster.x, monster.y);`
        + call to update monster position: `updateMonsterPosition(delta);`
        + call to update ball positions: `updateBalls(delta);`
        + call to display score: `displayScore();`
        + decrease current level time remain: `currentLevelTime -= delta;`
        + check next level: `if (currentLevelTime < 0) { goToNextLevel(); }`
        + exit case: `break;`
      + case for displaying main menu: `case gameState.mainMenu:`
        + display menu for game
        + exit case: `break;`
      + case for game over: `case gameStates.gameOver:`
        + display game instruction: `ctx.fillText("GAME OVER", 50, 100); ctx.fillText("Press SPACE to start again", 50, 150); ctx.fillText("Move with arrow keys", 50, 200); ctx.fillText("Survive 5 seconds for next level", 50, 250);`
        + check to start new game: `if (inputStates.space) { startNewGame(); }`
        + exit case: `break;`
  + start new game: `function startNewGame() {...}`
    + set values for variables: `monster.dead = false; currentLevelTime = 5000; currentLevel = 1; nbBalls = 5;`
    + call to create balls: `createBalls(nbBalls);`
    + set game state: `currentGameState = gameStates.gameRunning;`
  + move to next level: `function goToNextLevel() {...}`
    + set values for variables: `currentLevelTime = 5000; currentLevel++; nbBalls += 2;`
    + call to create balls: `createBalls(nbBalls);`
  + update balls in game: `function updateBalls(delta) {...}`
    + iterate to move all balls: `for (var i=0; i<ballArray.length; i++) {...}`
    + ...
    + test collision w/ monster: `if (circRectOverlap(monster.x, monster.y, monster.width, monster.height, ball.x, ball.y, ball.radius)) { ball.color = 'red'; monster.dead = true; plopSound.play(); }`
    + draw ball: `ball.draw;`


### 2.7.2 Splitting the game into several JS files

JSBin is a great tool for sharing code, for experimenting, etc. But as soon as the size of your project increases, you'll find that the tool is not suited for developing large systems. 

In order to keep working on this game framework, we recommend that you modularize the project and split the JavaScript code into several JavaScript files:

+ Review the different functions and isolate those that have no dependence on the framework. Obviously, the sprite utility functions, the collision detection functions, and the ball constructor function can be separated from the game framework, and could easily be reused in other projects. Key and mouse listeners also can be isolated, gamepad code too...
+ Look at what you could change to reduce dependencies: add a parameter in order to make a function independent from global variables, for example.
+ In the end, try to limit the `game.js` file to the core of the game framework (`init` function, `mainloop`, game states, score, levels), and separate the rest into functional groupings, eg `utils.js`, `sprites.js`, `collision.js`, `listeners.js`, etc.

Let's do this together!


#### Start with a simple structure

First, create a `game.html` file that contains the actual HTML code:

`game.html`:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;title&gt;</span><span class="pln">Nearly a real game</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&nbsp;<strong style="color: red;">&lt;!-- External JS libs --&gt;</strong></span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;script</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://cdnjs.cloudflare.com/ajax/libs/howler/1.1.25/howler.min.js"</span><span class="tag">&gt;&lt;/script&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span style="color: #008888;" color="#008888">&nbsp;<strong style="color: red;">&lt;!-- CSS files for your game --&gt;</strong></span></li>
<li class="L4" style="margin-bottom: 0px;"><span style="color: #008888;" color="#008888">&nbsp;&lt;link rel="stylesheet" href="css/game.css"&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><strong style="color: red;"><span class="pln"> </span><span class="com">&lt;!-- Include here all game JS files--&gt;</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><strong style="color: red;"><span class="com">&nbsp;&lt;script src="js/game.js"&gt;&lt;/script&gt;</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&lt;/head&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&lt;body&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;canvas</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myCanvas"</span><span class="pln"> </span><span class="atn">width</span><span class="pun">=</span><span class="atv">"400"</span><span class="pln"> </span><span class="atn">height</span><span class="pun">=</span><span class="atv">"400"</span><span class="tag">&gt;&lt;/canvas&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div><br>

Here is the `game.css` file (very simple):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">canvas </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;border</span><span class="pun">:</span><span class="pln"> </span><span class="lit">1px</span><span class="pln"> solid black</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div><br>

Let's take the JavaScript code from the last JSBin example, save it to a file called `game.js`, and locate it in a subdirectory `js` under the directory where the `game.html` file is located. Similarly, we'll keep the CSS file in a `css` subdirectory:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick= "window.open('https://bit.ly/3h7oqVI')"
    src    = "https://bit.ly/3vTlXUn"
    alt    = "first game structure"
    title  = "first game structure"
  />
</figure>


Try the game: open the `game.html` file in your browser. If the game does not work, open devtools, look at the console, fix the errors, try again, etc. You may have to do this several times when you split your files and encounter errors.


#### Isolate the ball function constructor

Put the Ball constructor function in a js/ball.js file, include it in the `game.html` file, and try the game: oops, it doesn't work! Let's open the console:

`Ball.js`:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com">// constructor function for balls</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> </span><span class="typ">Ball</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">,</span><span class="pln"> angle</span><span class="pun">,</span><span class="pln"> v</span><span class="pun">,</span><span class="pln"> diameter</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp;...</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">draw </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> </span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;<strong style="color: red;">ctx</strong></span><span class="pun">.</span><span class="pln">save</span><span class="pun">();</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">...</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><span class="pun">};</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">move </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> </span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; ...</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">x </span><span class="pun">+=</span><strong style="color: red;"><span class="pln"> calcDistanceToMove</span></strong><span class="pun">(</span><span class="pln">delta</span><span class="pun">,</span><span class="pln"> incX</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">y </span><span class="pun">+=</span><strong style="color: red;"><span class="pln"> calcDistanceToMove</span></strong><span class="pun">(</span><span class="pln">delta</span><span class="pun">,</span><span class="pln"> incY</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">};</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
</ol></div><br>


#### Isolate the time based animation functions into a separate file

Hmmm... the `calcDistanceToMove` function is used here, but is defined in the `game.js` file, inside the `GF` object and will certainly raise an error... Also, the `ctx` variable should be added as a parameter to the `draw` method, otherwise it won't be recognized... 

Just for fun, let's try the game without fixing this, and look at the devtools console:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3h7oqVI')"
    src    = "https://bit.ly/3xSIsdC"
    alt    = "error the function calcDistToMove not found in ball.js"
    title  = "error the function calcDistToMove not found in ball.js"
  />
</figure>


Aha! The `calcDistanceToMove` function is indeed used by the Ball constructor in `ball.js` at _line 27_ (it moves the ball using time-based animation). If you look carefully, you will see that it's also used for moving the monster, etc. In fact, there are parts in the game framework related to time-based animation. Let's move them all into a `timeBasedAnim.js` file!!

Fix: extract the utility functions related to time-based animation and add a _ctx_ parameter to the draw method of `ball.js`. Don't forget to add it in `game.js` where `ball.draw()` is called. The call should be now `ball.draw(ctx);` instead of `ball.draw()` without any parameter.

`timeBasedAnim.js`:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> delta</span><span class="pun">,</span><span class="pln"> oldTime </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> timer</span><span class="pun">(</span><span class="pln">currentTime</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> delta </span><span class="pun">=</span><span class="pln"> currentTime </span><span class="pun">-</span><span class="pln"> oldTime</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;oldTime </span><span class="pun">=</span><span class="pln"> currentTime</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">return</span><span class="pln"> delta</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> calcDistanceToMove </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> </span><span class="pun">(</span><span class="pln">delta</span><span class="pun">,</span><span class="pln"> speed</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">//console.log("#delta = " + delta + " speed = " + speed);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">return</span><span class="pln"> </span><span class="pun">(</span><span class="pln">speed </span><span class="pun">*</span><span class="pln"> delta</span><span class="pun">)</span><span class="pln"> </span><span class="pun">/</span><span class="pln"> </span><span class="lit">1000</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">};</span></li>
</ol></div><br>


#### Isolate the part that counts the number of frames per second

We need to add a small `initFPS` function for creating the `<div>` that displays the FPS value... this function will be called from the `GF.start()` method. There was code in this `start` method that has been moved into the `initFPS` function we created and added into the `fps.js` file.

`fps.js`:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="com">// vars for counting frames/s, used by the measureFPS function</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> frameCount </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> lastTime</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> fpsContainer</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> fps</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> initFPSCounter </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// adds a div for displaying the fps value</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;fpsContainer </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">createElement</span><span class="pun">(</span><span class="str">'div'</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;document</span><span class="pun">.</span><span class="pln">body</span><span class="pun">.</span><span class="pln">appendChild</span><span class="pun">(</span><span class="pln">fpsContainer</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> measureFPS </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> </span><span class="pun">(</span><span class="pln">newTime</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// test for the very first invocation</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">lastTime </span><span class="pun">===</span><span class="pln"> </span><span class="kwd">undefined</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; lastTime </span><span class="pun">=</span><span class="pln"> newTime</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">return</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">//calculate the difference between last &amp; current frame</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> diffTime </span><span class="pun">=</span><span class="pln"> newTime </span><span class="pun">-</span><span class="pln"> lastTime</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">diffTime </span><span class="pun">&gt;=</span><span class="pln"> </span><span class="lit">1000</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; fps </span><span class="pun">=</span><span class="pln"> frameCount</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; frameCount </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; lastTime </span><span class="pun">=</span><span class="pln"> newTime</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">//and display it in an element we appended to the </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// document in the start() function</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;fpsContainer</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> </span><span class="str">'FPS: '</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> fps</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;frameCount</span><span class="pun">++;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">};</span></li>
</ol></div><br>

At this stage, the structure looks like this:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick= "window.open('https://bit.ly/3h7oqVI')"
    src    = "https://bit.ly/3jcRPAM"
    alt    = "Game structure"
    title  = "Game structure"
  />
</figure>



#### Let's continue and isolate the event listeners

Now, consider the code that creates the listeners, can we move it from the `GF.start()` method into a `listeners.js` file? We'll have to pass the canvas as an extra parameter (to resolve a dependency) and we also move the `getMousePos` method into there. 

`listeners.js`:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> addListeners</span><span class="pun">(</span><span class="pln">inputStates</span><span class="pun">,</span><strong style="color: red;"><span class="pln"> canvas</span></strong><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">//add the listener to the main, window object, and update the states</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;window</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'keydown'</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">event</span><span class="pun">.</span><span class="pln">keyCode </span><span class="pun">===</span><span class="pln"> </span><span class="lit">37</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;inputStates</span><span class="pun">.</span><span class="pln">left </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">event</span><span class="pun">.</span><span class="pln">keyCode </span><span class="pun">===</span><span class="pln"> </span><span class="lit">38</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;inputStates</span><span class="pun">.</span><span class="pln">up </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">}</span><span class="pln">&nbsp;...</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">},</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">//if the key&nbsp;is released, change the states object </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;window</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'keyup'</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;...</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">},</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Mouse event listeners</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;canvas</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'mousemove'</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> </span><span class="pun">(</span><span class="pln">evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; inputStates</span><span class="pun">.</span><span class="pln">mousePos </span><span class="pun">=</span><strong style="color: red;"><span class="pln"> getMousePos</span><span class="pun">(</span><span class="pln">evt</span><span class="pun">,</span><span class="pln"> canvas</span><span class="pun">);</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">},</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;">...</li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> getMousePos</span><span class="pun">(</span><span class="pln">evt</span><span class="pun">,</span><strong style="color: red;"><span class="pln"> canvas</span></strong><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp;...</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div><br>


#### Isolate the collision tests

Following the same idea, let's put these into a `collisions.js` file:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="com">// We can add the other collision functions seen in the</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// course here...</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// Collisions between rectangle and circle</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> circRectsOverlap</span><span class="pun">(</span><span class="pln">x0</span><span class="pun">,</span><span class="pln"> y0</span><span class="pun">,</span><span class="pln"> w0</span><span class="pun">,</span><span class="pln"> h0</span><span class="pun">,</span><span class="pln"> cx</span><span class="pun">,</span><span class="pln"> cy</span><span class="pun">,</span><span class="pln"> r</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp;...</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> testCollisionWithWalls</span><span class="pun">(</span><span class="pln">ball</span><span class="pun">,</span><strong style="color: red;"><span class="pln"> w</span><span class="pun">,</span><span class="pln"> h</span></strong><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp;...</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
</ol></div><br>

We added the width and height of the canvas as parameters to the testCollisionWithWalls function to resolve dependencies. The other collision functions (circle-circle and rectangle-rectangle) presented during the course, could be put into this file as well.


#### Final downloadable version and conclusion

After all that, we reach this tidy structure:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick= "window.open('https://bit.ly/3h7oqVI')"
    src    = "https://bit.ly/3x8fK8k"
    alt    = "final game structure in files"
    title  = "final game structure in files"
  />
</figure>


Final `game.html` file:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;title&gt;</span><span class="pln">Nearly a real game</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><strong style="color: red;"><span class="tag">&lt;link</span><span class="pln"> </span><span class="atn">rel</span><span class="pun">=</span><span class="atv">"stylesheet"</span><span class="pln"> </span><span class="atn">href</span><span class="pun">=</span><span class="atv">"css/game.css"</span><span class="tag">&gt;</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;script</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://cdnjs.cloudflare.com/ajax/libs/howler/1.1.25/howler.min.js"</span><span class="tag">&gt;&lt;/script&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">&lt;!-- Include here all JS files --&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><strong style="color: red;"><span class="tag">&lt;script</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"js/game.js"</span><span class="tag">&gt;&lt;/script&gt;</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><strong style="color: red;"><span class="pln"> </span><span class="tag">&lt;script</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"js/ball.js"</span><span class="tag">&gt;&lt;/script&gt;</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><strong style="color: red;"><span class="pln"> </span><span class="tag">&lt;script</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"js/timeBasedAnim.js"</span><span class="tag">&gt;&lt;/script&gt;</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><strong style="color: red;"><span class="pln"> </span><span class="tag">&lt;script</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"js/fps.js"</span><span class="tag">&gt;&lt;/script&gt;</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong style="color: red;"><span class="pln"> </span><span class="tag">&lt;script</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"js/listeners.js"</span><span class="tag">&gt;&lt;/script&gt;</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong style="color: red;"><span class="pln"> </span><span class="tag">&lt;script</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"js/collisions.js"</span><span class="tag">&gt;&lt;/script&gt;</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;/head&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;body&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;canvas</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myCanvas"</span><span class="pln"> </span><span class="atn">width</span><span class="pun">=</span><span class="atv">"400"</span><span class="pln"> </span><span class="atn">height</span><span class="pun">=</span><span class="atv">"400"</span><span class="tag">&gt;&lt;/canvas&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div><br>

We could go further by defining a `monster.js` file, turning all the code related to the monster/player into a well-formed object, with draw and move methods, etc. There are many potential improvements you could make. JavaScript experts are welcome to make a much fancier version of this little game :-)

[Download the zip](https://bit.ly/3xIZGKm) for this version, just open the game.html file in your browser!

[Local Demo](src/02f-gameForMooc/game.html)

Our intent this week was to show you the primary techniques/approaches for dealing with animation, interactions, collisions, managing with game states, etc. 

The quizzes for this week are not so important. _We're keen to see you write your own game!_ You are welcome to freely re-use the examples presented in the lessons and modify them, improve the code structure, playability, add sounds, better graphics, more levels, etc. We like to give points for style and flair, but most especially because we've been (pleasantly) surprised!


#### Notes for 2.7.2 Splitting the game into several JS files

+ Modulizing game project
  + review and isolate functions
    + grouping functions w/o dependence on the framework
    + typical functions reused in other project
      + sprite utility functions
      + collision detection functions
      + ball constructor functions
    + typical interactive functions
      + key and mouse listener
      + gamepad code
      + ...
  + reduce dependencies:
    + change code to reduce dependencies
    + example: add a parameter to to make a function independent from global variables
  + limit main JavaScript to certain function
    + `game.js` as the core of the game framework: `init` function, `mainloop` function, game states, score, levels
    + other functional groupings: `utils.js`, `sprites.js`, `collisions.js`, `listeners.js`

+ Possible procedure of game development
  + start w/ a simple structure: `game.html` and `game.css`
  + isolate ball function constructor: `ball.js`
  + isolate time-based animation functions in a separate file: `timeBaseAnim.js`
  + isolate the part counting the number of frames per second: `fps.js`
  + isolate the event listeners: `listeners.js`
  + isolate the collision tests: `collisions.js`

+ A simple structure
  + HTML snippet `game.html`<a name="simpleGame"></a>:
    + head part: `<head> ... </head>`
      + sound script: `<script src="https://cdnjs.cloudflare.com/.../howler.min.js"></script>`
      + css style: `<link rel="stylesheet" href="css/game.css">`
      + game script: `<script src="js/game.js"></script>`
    + body part: `<canvas id="myCanvas" width=200 height=200></canvas>`
  + CSS style `game.css`: `canvas { border: 1px solid black; }`

+ Ball function constructor `ball.js`
  + ball constructor: `function Ball(x, y, angle, v, diameter) {...}`
    + ...
    + draw method: `this.draw = function() { ctx.save; ... };`
    + move method: `this.move = function() { ... this.x += calDistanceToMove(delta, incX); this.y += calcDistanceToMove(delta, incY); };`
  + `calcDistanceToMove` used here but declared in `game.js` within `GF` object
  + `ctx` variable missing $\to$ added as a parameter to the `draw` method

+ Time-based animation `timeBaseAnim,js`
  + `calcDistanceToMove` function used by the Ball constructor and moving the monster etc.
  + extract the utility functions related to time-based animation
  + add `ctx` parameter to the `draw` method of `ball.js`
  + delcare variables: `var delta, oldTime = 0;`
  + calculate time difference btw frames: `function timer(currentTime) {...}`
    + set time difference: `var delta = currentTime - oldTime;`
    + update old time: `oldTime = currentTime;`
    + return the time difference: `return delta;`
  + calculate distance: `var calcDistanceToMove = function (delta, speed) { return (speed*delta) / 1000; };`

+ Count the number of frames per second `fps.js`
  + add a small `initFPS` function for creating the `<div>` to display the FPS value
  + call `initFPS` from `GF.start()` method
  + code in `start` method moved into the `initFPS` function and added into the `fps.js`
  + declare variables: `var fameCount = 0; var lastTime; var fpsContainer; var fps;`
  + init PFS count: `var initFPSCount = function() {...}`
    + create fpd container: `fpsContainer = document.createElement('div');`
    + add container into page: `document.body.appendChild(fpsContainer);`
  + measure FPS: `var measureFPS = function(newTime) {...}`
    + test for the first invocation: `if (lastTime === undefined) ( lastTime = newTime; return; )`
    + calculate time difference btw the last and current frames: `var diffTime = newTime - lastTime;`
    + check time difference greater than 1 second: `if (diffTime < 1000) { fps = frameCount; frameCount = 0; lastTime = newTime; }`
  + display fps info: `fpsContainer.innerHTML = 'FPS: ' + fps; frameCount++;`

+ Handling event listeners `listeners.js`
  + add listenters for input states: `function addListeners(inputStates, canvas) {...}`
    + add key down listeners: `window.addEventListener('keydown', function(event) {...}, false);`
      + check left arrow key down: `if (event.keyCode === 37) { inputStates.left = true; }`
      + check right arrow key up: `else if (event.keyCode === 38) { inputStates.up = true; }`
      + ...
    + add key up listeners: `window.addEventListener('keyup', function(event) {...}, false);`
    + add mouse event listener: `canvas.addEventListener('mouseover', function(evt) {inputStates.mousePos = getMousePos(evt, canvas)}; false);`
    + ...
  + calculate mouse position: `function getMousePos(evt, canvas) {...}`

+ Collision detection `collisions.js`
  + detect collision btw rectangle and circle: `function circRectsOverlap(x0, y0, w0, h0, cx, cy, r) {...}`
  + detection collision w/ walls: `function testCollisionWithWalls(ball, w, h) {...}`

+ Final version of game fraework
  + HTML [simple structure](#simpleGame)
  + additional links for JS files
    + link JS file for ball function constructor: `<script src="js/ball.js"></script>`
    + link JS file for time-based animation functions in a separate file: `<script src="js/timeBaseAnim.js"></script>`
    + link JS file for the part counting the number of frames per second: `<script src="js/fps.js"></script>`
    + link JS file for the event listeners: `<script src="js/listeners.js"></script>`
    + link JS file for the collision tests: `<script src="js/collisions.js"></script>`


### 





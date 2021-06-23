# Module 2: Game programming with HTML5 section


## 2.6 Sprite-based animation


### 2.6.1 Introduction


#### Live coding video: sprite-based animation

<a href="https://edx-video.net/W3CHTM52/W3CHTM52T415-V001900_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript Download](https://bit.ly/3j4xlKd)


In this lesson, we learn how to animate images - which are known as "sprites". This technique uses components from a collection of animation frames. By drawing different component images, rapidly, one-after-the-other, we obtain an animation effect.

Here is an example of a spritesheet, where each line animates a woman walking in a particular direction:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick= "window.open('https://bit.ly/3gQmAIU')"
    src    = "https://bit.ly/3gKIVsy"
    alt    = "sprite sheet of a woman walking, with different postures"
    title  = "sprite sheet of a woman walking, with different postures"
  />
</figure>


The first line corresponds to the direction we called "south", the second "south west", the third "west", etc. The 8 lines cover movement in all eight cardinal directions.

Each line is composed of 13 small images which together comprise an "animated" sprite. If we draw each of the 13 animations of the first line, in turn; we will see a woman who seems to move towards the screen. And if we draw each sprite a little closer to the bottom of the screen, we obtain a woman who appears to approach the bottom of the screen, swinging her arms and legs, as she walks!

Try it yourself: here is a [quick and dirty example](https://jsbin.com/jokodod/edit?html,js,console,output) to try at JSBin working with the above sprite sheet.  Use the arrow keys and take a look! We accentuated the movement by changing the scale of the sprite as the woman moves up (further from us) or down (closer to us).

[Local Demo](src/02f-example01.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick= "window.open('https://bit.ly/3gQmAIU')"
    src    = "https://bit.ly/3gOqcMP"
    alt    = "A woman animated using sprite. Screenshot of the JsBin example that explain how to run it in standalone mode"
    title  = "A woman animated using sprite. Screenshot of the JsBin example that explain how to run it in standalone mode"
  />
</figure>


We have not yet investigated how this works, nor have we built it into the small game engine we started to build in earlier chapters. First, let's explain how to use "sprites" in JavaScript and canvas.


#### Notes for 2.6.1 Introduction

+ Sprite animation
  + using components from a collection of animation frames
  + animation effect: drawing component images, rapidly, one-after-the-other


### 2.6.2 Different sorts of sprite sheets

There are different sorts of sprite sheets. See some examples below.


#### Multiple postures on a single sprite sheet

A sprite sheet with different "sprite" sets that correspond to different "postures": this is the case for the walking woman we just saw in the previous lesson. This sprite sheet contains 8 different sets of sprites, or postures, each corresponding to a direction. In this example, each posture comprises exactly 13 sprites, aligned in a single row across the sprite sheet.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick= "window.open('https://bit.ly/3zORhXs')"
    src    = "https://bit.ly/3gKIVsy"
    alt    = "sprite sheet of a woman walking, with different postures"
    title  = "sprite sheet of a woman walking, with different postures"
  />
</figure>


#### One posture per sprite sheet

Some sprite sheets have a single sprite set, spreading over multiple lines; like this walking robot: {left diagram)}

This is an example that you will see a lot around the Internet, in many sprite sheets. For the full animation of the robot, we will need multiple sprite sheets: one for each posture.

As another example, here is the "jumping robot" sprite sheet: (right diagram)

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://bit.ly/3zORhXs" ismap target="_blank">
    <img style="margin: 0.1em;" height=250
      src   = "https://bit.ly/2TYragd"
      alt   = "a sprite sheet with a walking robot (only the posture "move to the right" is in the sprite sheet)"
      title = "a sprite sheet with a walking robot (only the posture "move to the right" is in the sprite sheet)"
    >
    <img style="margin: 0.1em;" height=250
      src   = "https://bit.ly/3j9mtuH"
      alt   = "sprite sheet for a robot jump"
      title = "sprite sheet for a robot jump"
    >
  </a>
</div>


Whereas the walking robot posture is made of 16 sprites, the jumping robot needs 26!


#### Hybrid sprite sheets

You will also find sprite sheets that contain completely different sets of sprites (this one comes from the [famous Gridrunner IOS game](https://www.youtube.com/watch?v=1tLNcj1ygFA) by Jeff Minter):

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick= "window.open('https://bit.ly/3zORhXs')"
    src    = "https://bit.ly/3gKLkU6"
    alt    = "Gridrunner spritesheet"
    title  = "Gridrunner spritesheet"
  />
</figure>

So, when we think about writing a "sprite engine", we need to consider how to support different layouts of sprite sheet.


#### Notes for 2.6.2 Different sorts of sprite sheets

+ Types of sprite sheets
  + multiple postures on a single sprite sheet
    + different sprite sets corresponding to different postures
    + example: walking woman
      + 8 different sets of sprites, or posturess, each corresponding to a direction
      + each compriseing exactly 13 sprites, aligned in a single row across the sprite sheet
  + one posture per sprite sheet
    + only a single sprite set per sheet
    + spreadign over multiple lines
    + multiple sprite sheets: one for each posture
    + example: walking robot (16 sprites) and jumping robot (26 sprites)
  + hybrid sprite sheets
    + sprite sheets containing completely different sets of sprites
    + sprite engine: considering how to support differenet layouts of sprite sheet


### 2.6.3 Sprite extraction and animation

#### Principle

Before doing anything interesting with the sprites, we need to:

1. Load the sprite sheet(s),
2. Extract the different postures and store them in an array of sprites,
3. Choose the appropriate one, and draw it within the animation loop, taking into account elapsed time. We cannot draw a different image of the woman walking at 60 updates per second. We will have to create a realistic "delay" between each change of sprite image.

In this lesson, let's construct an interactive tool to present the principles of sprite extraction and animation.


#### Example #1

In this example, we'll move the slider to extract the sprite indicated by the slider value. See the red rectangle? This is the sprite image currently selected! When you move the slider, the corresponding sprite is drawn in the small canvas. As you move the slider from one to the next, see how the animation is created?

[Try it at JSBin](https://jsbin.com/yukacep/edit?html,js,output):

[Local Demo](src/02f-example02.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3d7BPMl')"
    src    = "https://bit.ly/2SR5UJt"
    alt    = "Screenshot of the example: move a slider to select a subimage/sprite from the spritesheet"
    title  = "Screenshot of the example: move a slider to select a subimage/sprite from the spritesheet"
  />
</figure>


HTML code:

<div class="source-code" style="padding-left: 10px; padding-right: 30px; border: 1px solid black; line-height: 25.6px;"><ol class="linenums" style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">&lt;html lang</span><span class="pun" style="color: #666666;">=</span><span class="str" style="color: #008800;">"en"</span><span class="pun" style="color: #666666;">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="str" style="color: #008800;">&lt;head&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="str" style="color: #008800;">&lt;title&gt;</span><span class="typ" style="color: #aa0066;">Extract</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #008888;">and</span><span class="pln">&nbsp;draw sprite</span><span class="pun" style="color: #666666;">&lt;/</span><span class="pln">title</span><span class="pun" style="color: #666666;">&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="str" style="color: #008800;">&lt;style&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;canvas&nbsp;</span><span class="pun" style="color: #666666;">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; border</span><span class="pun" style="color: #666666;">:</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">1px</span><span class="pln">&nbsp;solid black</span><span class="pun" style="color: #666666;">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun" style="color: #666666;">}</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="pun" style="color: #666666;">&lt;/</span><span class="pln">style</span><span class="pun" style="color: #666666;">&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="pun" style="color: #666666;">&lt;/</span><span class="pln">head</span><span class="pun" style="color: #666666;">&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="str" style="color: #008800;">&lt;body&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="typ" style="color: #aa0066;">Sprite</span><span class="pln">&nbsp;width</span><span class="pun" style="color: #666666;">:</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">48</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;height</span><span class="pun" style="color: #666666;">:</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">92</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;rows</span><span class="pun" style="color: #666666;">:</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">8</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;sprites per posture</span><span class="pun" style="color: #666666;">:</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">13</span><span class="str" style="color: #008800;">&lt;p&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun" style="color: #666666;">&lt;</span><span class="pln">label&nbsp;</span><span class="kwd" style="color: #008888;">for</span><span class="pun" style="color: #666666;">=</span><span class="str" style="color: #008800;">"x"</span><span class="pun" style="color: #666666;">&gt;</span><span class="pln">x</span><span class="pun" style="color: #666666;">:</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666666;">&lt;</span><span class="pln">input id</span><span class="pun" style="color: #666666;">=</span><span class="str" style="color: #008800;">"x"</span><span class="pln">&nbsp;type</span><span class="pun" style="color: #666666;">=</span><span class="str" style="color: #008800;">"number"</span><span class="pln">&nbsp;min</span><span class="pun" style="color: #666666;">=</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666666;">&gt;&lt;</span><span class="pln">br</span><span class="pun" style="color: #666666;">/&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun" style="color: #666666;">&lt;</span><span class="pln">label&nbsp;</span><span class="kwd" style="color: #008888;">for</span><span class="pun" style="color: #666666;">=</span><span class="str" style="color: #008800;">"y"</span><span class="pun" style="color: #666666;">&gt;</span><span class="pln">y</span><span class="pun" style="color: #666666;">:</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666666;">&lt;</span><span class="pln">input id</span><span class="pun" style="color: #666666;">=</span><span class="str" style="color: #008800;">"y"</span><span class="pln">&nbsp;type</span><span class="pun" style="color: #666666;">=</span><span class="str" style="color: #008800;">"number"</span><span class="pln">&nbsp;min</span><span class="pun" style="color: #666666;">=</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666666;">&gt;&lt;</span><span class="pln">br</span><span class="pun" style="color: #666666;">/&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun" style="color: #666666;">&lt;</span><span class="pln">label&nbsp;</span><span class="kwd" style="color: #008888;">for</span><span class="pun" style="color: #666666;">=</span><span class="str" style="color: #008800;">"width"</span><span class="pun" style="color: #666666;">&gt;</span><span class="pln">width</span><span class="pun" style="color: #666666;">:</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666666;">&lt;</span><span class="pln">input id</span><span class="pun" style="color: #666666;">=</span><span class="str" style="color: #008800;">"width"</span><span class="pln">&nbsp;type</span><span class="pun" style="color: #666666;">=</span><span class="str" style="color: #008800;">"number"</span><span class="pln">&nbsp;min</span><span class="pun" style="color: #666666;">=</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666666;">&gt;&lt;</span><span class="pln">br</span><span class="pun" style="color: #666666;">/&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun" style="color: #666666;">&lt;</span><span class="pln">label&nbsp;</span><span class="kwd" style="color: #008888;">for</span><span class="pun" style="color: #666666;">=</span><span class="str" style="color: #008800;">"height"</span><span class="pun" style="color: #666666;">&gt;</span><span class="pln">height</span><span class="pun" style="color: #666666;">:</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666666;">&lt;</span><span class="pln">input id</span><span class="pun" style="color: #666666;">=</span><span class="str" style="color: #008800;">"height"</span><span class="pln">&nbsp;type</span><span class="pun" style="color: #666666;">=</span><span class="str" style="color: #008800;">"number"</span><span class="pln">&nbsp;min</span><span class="pun" style="color: #666666;">=</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666666;">&gt;&lt;</span><span class="pln">p</span><span class="pun" style="color: #666666;">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun" style="color: #666666;"></span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="typ" style="color: #aa0066;">Select</span><span class="pln">&nbsp;current sprite</span><span class="pun" style="color: #666666;">:</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666666;">&lt;</span><span class="pln">input type</span><span class="pun" style="color: #666666;">=</span><span class="pln">range id</span><span class="pun" style="color: #666666;">=</span><span class="str" style="color: #008800;">"spriteSelect"</span><span class="pln">&nbsp;value</span><span class="pun" style="color: #666666;">=</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666666;">&gt;</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666666;">&lt;</span><span class="pln">output id</span><span class="pun" style="color: #666666;">=</span><span class="str" style="color: #008800;">"spriteNumber"</span><span class="pun" style="color: #666666;">&gt;</span><span class="pln"></span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun" style="color: #666666;"></span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="pun" style="color: #666666;">&lt;</span><span class="pln">p</span><span class="pun" style="color: #666666;">/&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun" style="color: #666666;">&lt;</span><span class="pln">canvas id</span><span class="pun" style="color: #666666;">=</span><span class="str" style="color: #008800;">"canvas"</span><span class="pln">&nbsp;width</span><span class="pun" style="color: #666666;">=</span><span class="str" style="color: #008800;">"48"</span><span class="pln">&nbsp;height</span><span class="pun" style="color: #666666;">=</span><span class="str" style="color: #008800;">"92"</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666666;">/&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="pun" style="color: #666666;">&lt;/</span><span class="pln">p</span><span class="pun" style="color: #666666;">&gt;</span><span class="pln"></span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun" style="color: #666666;">&lt;</span><span class="pln">canvas id</span><span class="pun" style="color: #666666;">=</span><span class="str" style="color: #008800;">"spritesheet"</span><span class="pun" style="color: #666666;">&gt;&lt;/</span><span class="pln">canvas</span><span class="pun" style="color: #666666;">&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="pun" style="color: #666666;">&lt;/</span><span class="pln">body</span><span class="pun" style="color: #666666;">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun" style="color: #666666;">&lt;/</span><span class="pln">html</span><span class="pun" style="color: #666666;">&gt;</span></li>
</ol></div><br>

Notice that we use an `<input type="range">` to select the current sprite, and we have two canvases: a small one for displaying the currently-selected sprite, and a larger one that contains the sprite sheet and in which we draw a red square to highlight the selected sprite.

Here's an extract from the JavaScript. You don't have to understand all the details, just look at the part in bold which extracts the individual sprites:

<div class="source-code" style="padding-left: 10px; padding-right: 30px; border: 1px solid black; line-height: 25.6px;"><ol class="linenums" style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li class="L0" style="margin-bottom: 0px;" value="1"><strong style="color: red;"><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;SPRITE_WIDTH&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">48</span><span class="pun" style="color: #666666;">; &nbsp; // Characteristics of the sprites and spritesheet</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><strong style="color: red;"><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;SPRITE_HEIGHT&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">92</span><span class="pun" style="color: #666666;">;</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong style="color: red;"><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;NB_ROWS&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">8</span><span class="pun" style="color: #666666;">;</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong style="color: red;"><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;NB_FRAMES_PER_POSTURE&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">13</span><span class="pun" style="color: #666666;">;</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">// the different input and output fields</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;xField</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;yField</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;wField</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;hField</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;spriteSelect</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;spriteNumber</span><span class="pun" style="color: #666666;">;<br><br></span></li>
<li class="L6" style="margin-bottom: 0px;"><span color="#000000">// The two canvases and respective contexts</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;canvas</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;canvasSpriteSheet</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;ctx1</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;ctx2</span><span class="pun" style="color: #666666;">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">window</span><span class="pun" style="color: #666666;">.</span><span class="pln">onload&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #008888;">function</span><span class="pun" style="color: #666666;">()</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666666;">{</span><span class="pln"></span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; canvas&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;document</span><span class="pun" style="color: #666666;">.</span><span class="pln">getElementById</span><span class="pun" style="color: #666666;">(</span><span class="str" style="color: #008800;">"canvas"</span><span class="pun" style="color: #666666;">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx1&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;canvas</span><span class="pun" style="color: #666666;">.</span><span class="pln">getContext</span><span class="pun" style="color: #666666;">(</span><span class="str" style="color: #008800;">"2d"</span><span class="pun" style="color: #666666;">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; canvasSpriteSheet&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;document</span><span class="pun" style="color: #666666;">.</span><span class="pln">getElementById</span><span class="pun" style="color: #666666;">(</span><span class="str" style="color: #008800;">"spritesheet"</span><span class="pun" style="color: #666666;">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx2&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;canvasSpriteSheet</span><span class="pun" style="color: #666666;">.</span><span class="pln">getContext</span><span class="pun" style="color: #666666;">(</span><span class="str" style="color: #008800;">"2d"</span><span class="pun" style="color: #666666;">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln" style="line-height: 1.6;"></span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln" style="line-height: 1.6;">&nbsp; &nbsp; xField&nbsp;</span><span class="pun" style="line-height: 1.6;">=</span><span class="pln" style="line-height: 1.6;">&nbsp;document</span><span class="pun" style="line-height: 1.6;">.</span><span class="pln" style="line-height: 1.6;">querySelector</span><span class="pun" style="line-height: 1.6;">(</span><span class="str" style="line-height: 1.6;">"#x"</span><span class="pun" style="line-height: 1.6;">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; yField&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;document</span><span class="pun" style="color: #666666;">.</span><span class="pln">querySelector</span><span class="pun" style="color: #666666;">(</span><span class="str" style="color: #008800;">"#y"</span><span class="pun" style="color: #666666;">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; wField&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;document</span><span class="pun" style="color: #666666;">.</span><span class="pln">querySelector</span><span class="pun" style="color: #666666;">(</span><span class="str" style="color: #008800;">"#width"</span><span class="pun" style="color: #666666;">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; hField&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;document</span><span class="pun" style="color: #666666;">.</span><span class="pln">querySelector</span><span class="pun" style="color: #666666;">(</span><span class="str" style="color: #008800;">"#height"</span><span class="pun" style="color: #666666;">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; spriteSelect&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;document</span><span class="pun" style="color: #666666;">.</span><span class="pln">querySelector</span><span class="pun" style="color: #666666;">(</span><span class="str" style="color: #008800;">"#spriteSelect"</span><span class="pun" style="color: #666666;">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; spriteNumber&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;document</span><span class="pun" style="color: #666666;">.</span><span class="pln">querySelector</span><span class="pun" style="color: #666666;">(</span><span class="str" style="color: #008800;">"#spriteNumber"</span><span class="pun" style="color: #666666;">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; // Update values of the input fields in the page</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; wField</span><span class="pun" style="color: #666666;">.</span><span class="pln">value&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;SPRITE_WIDTH</span><span class="pun" style="color: #666666;">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; hField</span><span class="pun" style="color: #666666;">.</span><span class="pln">value&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;SPRITE_HEIGHT</span><span class="pun" style="color: #666666;">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; xField</span><span class="pun" style="color: #666666;">.</span><span class="pln">value&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666666;">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; yField</span><span class="pun" style="color: #666666;">.</span><span class="pln">value&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666666;">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun" style="color: #666666;">&nbsp; &nbsp; // Set attributes for the slider depending on the number of sprites on the&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun" style="color: #666666;">&nbsp; &nbsp; // sprite sheet</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; spriteSelect</span><span class="pun" style="color: #666666;">.</span><span class="pln">min&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666666;">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; spriteSelect</span><span class="pun" style="color: #666666;">.</span><span class="pln">max</span><span class="pun" style="color: #666666;">=</span><span class="pln">NB_ROWS</span><span class="pun" style="color: #666666;">*</span><span class="pln">NB_FRAMES_PER_POSTURE&nbsp;</span><span class="pun" style="color: #666666;">-</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">1</span><span class="pun" style="color: #666666;">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun" style="color: #666666;">&nbsp; &nbsp; // By default the slider is disabled until the sprite sheet is fully loaded</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln" style="line-height: 1.6;">&nbsp; &nbsp; spriteSelect</span><span class="pun" style="line-height: 1.6;">.</span><span class="pln" style="line-height: 1.6;">disabled&nbsp;</span><span class="pun" style="line-height: 1.6;">=</span><span class="pln" style="line-height: 1.6;">&nbsp;</span><span class="kwd" style="line-height: 1.6;">true</span><span class="pun" style="line-height: 1.6;">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; spriteNumber</span><span class="pun" style="color: #666666;">.</span><span class="pln">innerHTML</span><span class="pun" style="color: #666666;">=</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666666;">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com" style="color: #880000;">// Load the spritesheet</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; spritesheet&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #008888;">new</span><span class="pln">&nbsp;</span><span class="typ" style="color: #aa0066;">Image</span><span class="pun" style="color: #666666;">();</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; spritesheet</span><span class="pun" style="color: #666666;">.</span><span class="pln">src</span><span class="pun" style="color: #666666;">=</span><span class="str" style="color: #008800;">"https://i.imgur.com/3VesWqx.png"</span><span class="pun" style="color: #666666;">;</span><span class="pln"></span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;<strong style="color: red;">&nbsp;</strong></span><strong style="color: red;"><span class="com" style="color: #880000;">// Called when the spritesheet has been loaded</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; spritesheet</span><span class="pun" style="color: #666666;">.</span><span class="pln">onload&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #008888;">function</span><span class="pun" style="color: #666666;">()</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666666;">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com" style="color: #880000;">// enable slider</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; spriteSelect</span><span class="pun" style="color: #666666;">.</span><span class="pln">disabled&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #008888;">false</span><span class="pun" style="color: #666666;">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com" style="color: #880000;">// Resize big canvas to the size of the sprite sheet image</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; canvasSpriteSheet</span><span class="pun" style="color: #666666;">.</span><span class="pln">width&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;spritesheet</span><span class="pun" style="color: #666666;">.</span><span class="pln">width</span><span class="pun" style="color: #666666;">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; canvasSpriteSheet</span><span class="pun" style="color: #666666;">.</span><span class="pln">height&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;spritesheet</span><span class="pun" style="color: #666666;">.</span><span class="pln">height</span><span class="pun" style="color: #666666;">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// Draw the whole spritesheet</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;ctx2</span><span class="pun" style="color: #666666;">.</span><span class="pln">drawImage</span><span class="pun" style="color: #666666;">(</span><span class="pln">spritesheet</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666666;">);<br><br></span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// Draw the first sprite in the big&nbsp;canvas, corresponding to sprite 0</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// wireframe rectangle in the sprite sheet</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;drawWireFrameRect</span><span class="pun" style="color: #666666;">(</span><span class="pln">ctx2</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;SPRITE_WIDTH</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;SPRITE_HEIGHT</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;</span><span class="str" style="color: #008800;">'red'</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">3</span><span class="pun" style="color: #666666;">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;<br></span><span class="com" style="color: #880000;">&nbsp; &nbsp; &nbsp;// small canvas, draw sub image corresponding to sprite 0</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;ctx1</span><span class="pun" style="color: #666666;">.</span><span class="pln">drawImage</span><span class="pun" style="color: #666666;">(</span><span class="pln">spritesheet</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;SPRITE_WIDTH</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;SPRITE_HEIGHT</span><span class="pun" style="color: #666666;">,</span><span class="pln"></span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="lit" style="color: #006666;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;0</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;SPRITE_WIDTH</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;SPRITE_HEIGHT</span><span class="pun" style="color: #666666;">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun" style="color: #666666;">};</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com" style="color: #880000;">// input listener on the slider</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;spriteSelect</span><span class="pun" style="color: #666666;">.</span><span class="pln">oninput&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #008888;">function</span><span class="pun" style="color: #666666;">(</span><span class="pln">evt</span><span class="pun" style="color: #666666;">)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666666;">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// Current sprite number from 0 to NB_FRAMES_PER_POSTURE * NB_ROWS</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;index&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;spriteSelect</span><span class="pun" style="color: #666666;">.</span><span class="pln">value</span><span class="pun" style="color: #666666;">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L3" style="margin-bottom: 0px;"><strong style="color: red;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// Computation of the x and y position that corresponds to the sprite</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><strong style="color: red;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// number index as selected by the slider</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><strong style="color: red;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;x&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;index&nbsp;</span><span class="pun" style="color: #666666;">*</span><span class="pln">&nbsp;SPRITE_WIDTH&nbsp;</span><span class="pun" style="color: #666666;">%</span><span class="pln">&nbsp;spritesheet</span><span class="pun" style="color: #666666;">.</span><span class="pln">width</span><span class="pun" style="color: #666666;">;</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><strong style="color: red;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;y&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;</span><span class="typ" style="color: #aa0066;">Math</span><span class="pun" style="color: #666666;">.</span><span class="pln">floor</span><span class="pun" style="color: #666666;">(</span><span class="pln">index&nbsp;</span><span class="pun" style="color: #666666;">/</span><span class="pln">&nbsp;NB_FRAMES_PER_POSTURE</span><span class="pun" style="color: #666666;">)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666666;">*</span><span class="pln">&nbsp;SPRITE_HEIGHT</span><span class="pun" style="color: #666666;">;</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// Update fields</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;xField</span><span class="pun" style="color: #666666;">.</span><span class="pln">value&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;x</span><span class="pun" style="color: #666666;">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;yField</span><span class="pun" style="color: #666666;">.</span><span class="pln">value&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;y</span><span class="pun" style="color: #666666;">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// Clear big canvas, draw wireframe rect at x, y, redraw stylesheet</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;ctx2</span><span class="pun" style="color: #666666;">.</span><span class="pln">clearRect</span><span class="pun" style="color: #666666;">(</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;canvasSpriteSheet</span><span class="pun" style="color: #666666;">.</span><span class="pln">width</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;canvasSpriteSheet</span><span class="pun" style="color: #666666;">.</span><span class="pln">height</span><span class="pun" style="color: #666666;">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;ctx2</span><span class="pun" style="color: #666666;">.</span><span class="pln">drawImage</span><span class="pun" style="color: #666666;">(</span><span class="pln">spritesheet</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666666;">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;drawWireFrameRect</span><span class="pun" style="color: #666666;">(</span><span class="pln">ctx2</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;x&nbsp;</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;y</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;SPRITE_WIDTH</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;SPRITE_HEIGHT</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;</span><span class="str" style="color: #008800;">'red'</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">3</span><span class="pun" style="color: #666666;">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// Draw the current sprite in the small canvas</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;ctx1</span><span class="pun" style="color: #666666;">.</span><span class="pln">clearRect</span><span class="pun" style="color: #666666;">(</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;SPRITE_WIDTH</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;SPRITE_HEIGHT</span><span class="pun" style="color: #666666;">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;ctx1</span><span class="pun" style="color: #666666;">.</span><span class="pln">drawImage</span><span class="pun" style="color: #666666;">(</span><span class="pln">spritesheet</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;x</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;y</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;SPRITE_WIDTH</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;SPRITE_HEIGHT</span><span class="pun" style="color: #666666;">,</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;SPRITE_WIDTH</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;SPRITE_HEIGHT</span><span class="pun" style="color: #666666;">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// Update output elem on the right of the slider</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;spriteNumber</span><span class="pun" style="color: #666666;">.</span><span class="pln">innerHTML&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;index</span><span class="pun" style="color: #666666;">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun" style="color: #666666;">};</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun" style="color: #666666;">};</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="kwd" style="color: #008888;">function</span><span class="pln">&nbsp;drawWireFrameRect</span><span class="pun" style="color: #666666;">(</span><span class="pln">ctx</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;x</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;y</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;w</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;h</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;color</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;lineWidth</span><span class="pun" style="color: #666666;">)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666666;">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; ctx</span><span class="pun" style="color: #666666;">.</span><span class="pln">save</span><span class="pun" style="color: #666666;">();</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; ctx</span><span class="pun" style="color: #666666;">.</span><span class="pln">strokeStyle&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;color</span><span class="pun" style="color: #666666;">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; ctx</span><span class="pun" style="color: #666666;">.</span><span class="pln">lineWidth&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;lineWidth</span><span class="pun" style="color: #666666;">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; ctx</span><span class="pun" style="color: #666666;">.</span><span class="pln">strokeRect</span><span class="pun" style="color: #666666;">(</span><span class="pln">x&nbsp;</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;y</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;w</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;h</span><span class="pun" style="color: #666666;">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; ctx</span><span class="pun" style="color: #666666;">.</span><span class="pln">restore</span><span class="pun" style="color: #666666;">();</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun" style="color: #666666;">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
</ol></div><br>

__Explanations:__

+ _Lines 1-4_: characteristics of the sprite sheet. How many rows, i.e., how many sprites per row, etc.
+ _Lines 11-39_: initializations that run just after the page has been loaded. We first get the canvas and contexts. Then we set the minimum and maximum values of the slider (an `<input type=range>`) at _lines 31-32_, and disable it at _line 34_ (we cannot slide it before the sprite sheet image has been loaded). We display the current sprite number 0 in the `<output>` field to the right of the slider (_line 35_).  Finally, in _lines 37-39_, we load the sprite sheet image.
+ _Lines 42-58_: this callback is run once the sprite sheet image has been loaded. We enable the slider, set the big canvas to the size of the loaded image, and then draw it (_line 51_). We also draw the first sprite from the sprite sheet in the small canvas and draw a red wireframe rectangle around the first sprite in the sprite sheet (_lines 52-58_).
+ _Lines 61-87_: the input listener callback, called each time the slider moves. _Lines 65-68_ are the most important ones here: we compute the x and y position of the sprite selected with the slider. We take into account the number of sprites per posture, the number of rows, and the dimensions of each sprite. Then, as in the previous step, we draw the current sprite in the small canvas and highlight the current sprite with a red rectangle in the sprite sheet.

The code is generic enough to work with different kinds of sprite sheets. Adjust the global parameters in bold at _lines 1-5_ and try the extractor.


#### Example #2

This is the same application with another sprite sheet.

We just changed these parameter values: try the same code but with another sprite sheet (the one with the robot) - [see on JSBin](https://jsbin.com/jeledoq/edit?html,js,output).

[Local Demo](src/02f-example03.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick= "window.open('https://bit.ly/3d7BPMl')"
    src    = "https://bit.ly/3w0L1ZT"
    alt    = "We just changed these parameter values: try the same code but with another sprite sheet (the one with the robot) - see on JSBin."
    title  = "We just changed these parameter values: try the same code but with another sprite sheet (the one with the robot) - see on JSBin."
  />
</figure>

Now it's time to see how we can make a small sprite animation framework!


#### Notes for 2.6.3 Sprite extraction and animation

+ Procedure of sprite animation
  + loading the sprite sheet(s)
  + extracting the different postures and store them in an array of sprites
  + sprite engine
    + choosing the appropriate one
    + drawing withing the animation loop
    + taking into account elapsed time: creating a realistic "delay" btw each change of sprite image

+ Example: walking woman w/ multiple postures/sheet
  + HTML snippet
    + display default settings: `<p>Sprite width: 48, height: 92, rows: 8, sprites per posture: 13</p>`
    + row input of sprite sheet: `<label for="x">x <input id="x" type="number" min=0><br/>`
    + column input of sprite sheet: `<label for="y">y <input id="y" type="number" min=0><br/>`
    + width input of selected posture: `<label for="width">width <input id="width" type="number" min=0><br/>`
    + length input of selected posture: `<label for="height">height <input id="height" type="number" min=0><br/>`
    + slider to select sprite: `<p>Select current sprite <input type=range id="spriteSelect" value=0> <output id="spriteNumber"></output></p>`
    + selected sprite image: `<p><canvas id="canvas" width=48 height=92 /></p>`
    + display sprite sheet: `<p><canvas id="spritesheet"></canvas></p>`
  + JavaScript snippet:
    + set characteristics of sprite and sprite sheet: `var SPRITE_WIDTH = 48; var SPRITE_HEIGHT = 92; var NB_ROWS = 8; var NB_FRAMES_PER_PSOTURE = 13;`
    + declare variables: `var xFields, yField, wField, hField, spriteSheet, spriteNumber; var canvas, canvasSpriteSheet, ctx1, ctx2;`
    + init page after DOM ready: `window.onload = function() {...}`
      + access canvas and set context: `canvas = document.getElementById("canvas"); ctx1 = canvas.getContext("2d"); canvasSpriteSheet = document.getElementById("spritesheet"); ctx2 = canvasSpriteSheet.getContext("2d");`
      + access elements: `xField = document.querySelector("#x"); yField = document.querySelector("#y"); wField = document.querySelector("#width"); hField = document.querySelector("#height"); spriteSelect = document.querySelector("#spriteSelect"); spriteNumber = document.querySelector("#spriteNumber");`
      + update values of input fields: `wField.value = SPRITE_WIDTH; hField.value = SPRITE_HEIGHT; xField.value = 0; yField.value = 0;`
      + set attributes of slider and default values: `spriteSelect.value = 0; spriteSelect.min = NB_ROWS*NB_FRAMES_PER_POSTURE - 1; spriteSelect.disablked = true; spriteNumber.innerHTML = 0;`
      + load spritesheet: `spritesheet = new img(); spritesheet.src="https://i.imgur.com/3VesWqx.png";`
    + process after sprite sheet downloaded: `spritesheet.onload = function() {...}`
      + delcare variable: `var index = spriteSelect.value;`
      + compute the position of selected posture: `var x = index*SPRITE_WIDTH % spritesheet.width; var y = Math.foor(index/NB_FRAMES_PER_POSTURE) * SPRITE_HEIGHT;`
      + update fields: `xField.value = x; yField.value = y;`
      + draw red wireframe for selected sprite: `ctx2.clearRect(0, 0, canvasSpriteSheet.width, canvasSpriteSheet.height,); ctx2.drawImage(spritesheet, 0, 0); drawWireFrameRect(ctx2, x, y, SPRITE_WIDTH, SPRITE_HEIGHT, 'red'. 3);`
      + draw select sprite in small canvas: `ctx1.clearRect(0, 0, SPRITE_WIDTH, SPRITE_HEIGHT); ctx1.drawImage(spritesheet, x, y, SPRITE_WIDTH, SPRITE_HEIGHT, 0, 0, SPRITE_WIDTH, SPRITE_HEIGHT);`
      + update output element for slider: `spriteNumber.innerHTML = index;`
    + draw wireframe: `function drawWireFrameRect(ctx, x, y, w, h, color, lineWidth) {...}`
      + save ctx: `ctx.save();`
      + set and draw wireframe: `ctx.strokeStyle = color; ctx.lineWidth = lineWidth; ctx.strokeRect(x. y. w. h);`
      + restore ctx: `ctx.restore();`





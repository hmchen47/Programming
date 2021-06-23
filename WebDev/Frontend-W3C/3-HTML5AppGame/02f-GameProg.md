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
1. Extract the different postures and store them in an array of sprites,
1. Choose the appropriate one, and draw it within the animation loop, taking into account elapsed time. We cannot draw a different image of the woman walking at 60 updates per second. We will have to create a realistic "delay" between each change of sprite image.

In this lesson, let's construct an interactive tool to present the principles of sprite extraction and animation.


#### Example #1

In this example, we'll move the slider to extract the sprite indicated by the slider value. See the red rectangle? This is the sprite image currently selected! When you move the slider, the corresponding sprite is drawn in the small canvas. As you move the slider from one to the next, see how the animation is created? 

[Try it at JSBin](https://jsbin.com/yukacep/edit?html,js,output):

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3d7BPMl')"
    src    = "https://bit.ly/2SR5UJt"
    alt    = "Screenshot of the example: move a slider to select a subimage/sprite from the spritesheet"
    title  = "Screenshot of the example: move a slider to select a subimage/sprite from the spritesheet"
  />
</figure>


HTML code:

<div class="source-code" style="padding-left: 30px; padding-right: 30px; border: 1px solid black; line-height: 25.6px;"><ol class="linenums" style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln" style="color: #000000;">&lt;html lang</span><span class="pun" style="color: #666600;">=</span><span class="str" style="color: #008800;">"en"</span><span class="pun" style="color: #666600;">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp;</span><span class="str" style="color: #008800;">&lt;head&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp;</span><span class="str" style="color: #008800;">&lt;title&gt;</span><span class="typ" style="color: #660066;">Extract</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="kwd" style="color: #000088;">and</span><span class="pln" style="color: #000000;">&nbsp;draw sprite</span><span class="pun" style="color: #666600;">&lt;/</span><span class="pln" style="color: #000000;">title</span><span class="pun" style="color: #666600;">&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp;</span><span class="str" style="color: #008800;">&lt;style&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp;canvas&nbsp;</span><span class="pun" style="color: #666600;">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; &nbsp; border</span><span class="pun" style="color: #666600;">:</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="lit" style="color: #006666;">1px</span><span class="pln" style="color: #000000;">&nbsp;solid black</span><span class="pun" style="color: #666600;">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp;&nbsp;</span><span class="pun" style="color: #666600;">}</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp;</span><span class="pun" style="color: #666600;">&lt;/</span><span class="pln" style="color: #000000;">style</span><span class="pun" style="color: #666600;">&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp;</span><span class="pun" style="color: #666600;">&lt;/</span><span class="pln" style="color: #000000;">head</span><span class="pun" style="color: #666600;">&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp;</span><span class="str" style="color: #008800;">&lt;body&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp;</span><span class="typ" style="color: #660066;">Sprite</span><span class="pln" style="color: #000000;">&nbsp;width</span><span class="pun" style="color: #666600;">:</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="lit" style="color: #006666;">48</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;height</span><span class="pun" style="color: #666600;">:</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="lit" style="color: #006666;">92</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;rows</span><span class="pun" style="color: #666600;">:</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="lit" style="color: #006666;">8</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;sprites per posture</span><span class="pun" style="color: #666600;">:</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="lit" style="color: #006666;">13</span><span class="str" style="color: #008800;">&lt;p&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp;</span><span class="pun" style="color: #666600;">&lt;</span><span class="pln" style="color: #000000;">label&nbsp;</span><span class="kwd" style="color: #000088;">for</span><span class="pun" style="color: #666600;">=</span><span class="str" style="color: #008800;">"x"</span><span class="pun" style="color: #666600;">&gt;</span><span class="pln" style="color: #000000;">x</span><span class="pun" style="color: #666600;">:</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="pun" style="color: #666600;">&lt;</span><span class="pln" style="color: #000000;">input id</span><span class="pun" style="color: #666600;">=</span><span class="str" style="color: #008800;">"x"</span><span class="pln" style="color: #000000;">&nbsp;type</span><span class="pun" style="color: #666600;">=</span><span class="str" style="color: #008800;">"number"</span><span class="pln" style="color: #000000;">&nbsp;min</span><span class="pun" style="color: #666600;">=</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666600;">&gt;&lt;</span><span class="pln" style="color: #000000;">br</span><span class="pun" style="color: #666600;">/&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp;</span><span class="pun" style="color: #666600;">&lt;</span><span class="pln" style="color: #000000;">label&nbsp;</span><span class="kwd" style="color: #000088;">for</span><span class="pun" style="color: #666600;">=</span><span class="str" style="color: #008800;">"y"</span><span class="pun" style="color: #666600;">&gt;</span><span class="pln" style="color: #000000;">y</span><span class="pun" style="color: #666600;">:</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="pun" style="color: #666600;">&lt;</span><span class="pln" style="color: #000000;">input id</span><span class="pun" style="color: #666600;">=</span><span class="str" style="color: #008800;">"y"</span><span class="pln" style="color: #000000;">&nbsp;type</span><span class="pun" style="color: #666600;">=</span><span class="str" style="color: #008800;">"number"</span><span class="pln" style="color: #000000;">&nbsp;min</span><span class="pun" style="color: #666600;">=</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666600;">&gt;&lt;</span><span class="pln" style="color: #000000;">br</span><span class="pun" style="color: #666600;">/&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp;</span><span class="pun" style="color: #666600;">&lt;</span><span class="pln" style="color: #000000;">label&nbsp;</span><span class="kwd" style="color: #000088;">for</span><span class="pun" style="color: #666600;">=</span><span class="str" style="color: #008800;">"width"</span><span class="pun" style="color: #666600;">&gt;</span><span class="pln" style="color: #000000;">width</span><span class="pun" style="color: #666600;">:</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="pun" style="color: #666600;">&lt;</span><span class="pln" style="color: #000000;">input id</span><span class="pun" style="color: #666600;">=</span><span class="str" style="color: #008800;">"width"</span><span class="pln" style="color: #000000;">&nbsp;type</span><span class="pun" style="color: #666600;">=</span><span class="str" style="color: #008800;">"number"</span><span class="pln" style="color: #000000;">&nbsp;min</span><span class="pun" style="color: #666600;">=</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666600;">&gt;&lt;</span><span class="pln" style="color: #000000;">br</span><span class="pun" style="color: #666600;">/&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp;</span><span class="pun" style="color: #666600;">&lt;</span><span class="pln" style="color: #000000;">label&nbsp;</span><span class="kwd" style="color: #000088;">for</span><span class="pun" style="color: #666600;">=</span><span class="str" style="color: #008800;">"height"</span><span class="pun" style="color: #666600;">&gt;</span><span class="pln" style="color: #000000;">height</span><span class="pun" style="color: #666600;">:</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="pun" style="color: #666600;">&lt;</span><span class="pln" style="color: #000000;">input id</span><span class="pun" style="color: #666600;">=</span><span class="str" style="color: #008800;">"height"</span><span class="pln" style="color: #000000;">&nbsp;type</span><span class="pun" style="color: #666600;">=</span><span class="str" style="color: #008800;">"number"</span><span class="pln" style="color: #000000;">&nbsp;min</span><span class="pun" style="color: #666600;">=</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666600;">&gt;&lt;</span><span class="pln" style="color: #000000;">p</span><span class="pun" style="color: #666600;">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;"></span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="typ" style="color: #660066;">Select</span><span class="pln" style="color: #000000;">&nbsp;current sprite</span><span class="pun" style="color: #666600;">:</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="pun" style="color: #666600;">&lt;</span><span class="pln" style="color: #000000;">input type</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">range id</span><span class="pun" style="color: #666600;">=</span><span class="str" style="color: #008800;">"spriteSelect"</span><span class="pln" style="color: #000000;">&nbsp;value</span><span class="pun" style="color: #666600;">=</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666600;">&gt;</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="pun" style="color: #666600;">&lt;</span><span class="pln" style="color: #000000;">output id</span><span class="pun" style="color: #666600;">=</span><span class="str" style="color: #008800;">"spriteNumber"</span><span class="pun" style="color: #666600;">&gt;</span><span class="pln" style="color: #000000;"></span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;"></span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp;</span><span class="pun" style="color: #666600;">&lt;</span><span class="pln" style="color: #000000;">p</span><span class="pun" style="color: #666600;">/&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp;</span><span class="pun" style="color: #666600;">&lt;</span><span class="pln" style="color: #000000;">canvas id</span><span class="pun" style="color: #666600;">=</span><span class="str" style="color: #008800;">"canvas"</span><span class="pln" style="color: #000000;">&nbsp;width</span><span class="pun" style="color: #666600;">=</span><span class="str" style="color: #008800;">"48"</span><span class="pln" style="color: #000000;">&nbsp;height</span><span class="pun" style="color: #666600;">=</span><span class="str" style="color: #008800;">"92"</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="pun" style="color: #666600;">/&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp;</span><span class="pun" style="color: #666600;">&lt;/</span><span class="pln" style="color: #000000;">p</span><span class="pun" style="color: #666600;">&gt;</span><span class="pln" style="color: #000000;"></span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp;</span><span class="pun" style="color: #666600;">&lt;</span><span class="pln" style="color: #000000;">canvas id</span><span class="pun" style="color: #666600;">=</span><span class="str" style="color: #008800;">"spritesheet"</span><span class="pun" style="color: #666600;">&gt;&lt;/</span><span class="pln" style="color: #000000;">canvas</span><span class="pun" style="color: #666600;">&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp;</span><span class="pun" style="color: #666600;">&lt;/</span><span class="pln" style="color: #000000;">body</span><span class="pun" style="color: #666600;">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;">&lt;/</span><span class="pln" style="color: #000000;">html</span><span class="pun" style="color: #666600;">&gt;</span></li>
</ol></div><br>

Notice that we use an `<input type="range">` to select the current sprite, and we have two canvases: a small one for displaying the currently-selected sprite, and a larger one that contains the sprite sheet and in which we draw a red square to highlight the selected sprite.

Here's an extract from the JavaScript. You don't have to understand all the details, just look at the part in bold which extracts the individual sprites:

<div class="source-code" style="padding-left: 30px; padding-right: 30px; border: 1px solid black; line-height: 25.6px;"><ol class="linenums" style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li class="L0" style="margin-bottom: 0px;" value="1"><strong><span class="kwd" style="color: #000088;">var</span><span class="pln" style="color: #000000;">&nbsp;SPRITE_WIDTH&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="lit" style="color: #006666;">48</span><span class="pun" style="color: #666600;">; &nbsp; // Characteristics of the sprites and spritesheet</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="kwd" style="color: #000088;">var</span><span class="pln" style="color: #000000;">&nbsp;SPRITE_HEIGHT&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="lit" style="color: #006666;">92</span><span class="pun" style="color: #666600;">;</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="kwd" style="color: #000088;">var</span><span class="pln" style="color: #000000;">&nbsp;NB_ROWS&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="lit" style="color: #006666;">8</span><span class="pun" style="color: #666600;">;</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="kwd" style="color: #000088;">var</span><span class="pln" style="color: #000000;">&nbsp;NB_FRAMES_PER_POSTURE&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="lit" style="color: #006666;">13</span><span class="pun" style="color: #666600;">;</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">// the different input and output fields</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="kwd" style="color: #000088;">var</span><span class="pln" style="color: #000000;">&nbsp;xField</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;yField</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;wField</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;hField</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;spriteSelect</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;spriteNumber</span><span class="pun" style="color: #666600;">;<br><br></span></li>
<li class="L6" style="margin-bottom: 0px;"><span style="color: #000000;" color="#000000">// The two canvases and respective contexts</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="kwd" style="color: #000088;">var</span><span class="pln" style="color: #000000;">&nbsp;canvas</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;canvasSpriteSheet</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;ctx1</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;ctx2</span><span class="pun" style="color: #666600;">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">window</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">onload&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="kwd" style="color: #000088;">function</span><span class="pun" style="color: #666600;">()</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="pun" style="color: #666600;">{</span><span class="pln" style="color: #000000;"></span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; canvas&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;document</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">getElementById</span><span class="pun" style="color: #666600;">(</span><span class="str" style="color: #008800;">"canvas"</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; ctx1&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;canvas</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">getContext</span><span class="pun" style="color: #666600;">(</span><span class="str" style="color: #008800;">"2d"</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; canvasSpriteSheet&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;document</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">getElementById</span><span class="pun" style="color: #666600;">(</span><span class="str" style="color: #008800;">"spritesheet"</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; ctx2&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;canvasSpriteSheet</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">getContext</span><span class="pun" style="color: #666600;">(</span><span class="str" style="color: #008800;">"2d"</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln" style="line-height: 1.6;"></span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln" style="line-height: 1.6;">&nbsp; &nbsp; xField&nbsp;</span><span class="pun" style="line-height: 1.6;">=</span><span class="pln" style="line-height: 1.6;">&nbsp;document</span><span class="pun" style="line-height: 1.6;">.</span><span class="pln" style="line-height: 1.6;">querySelector</span><span class="pun" style="line-height: 1.6;">(</span><span class="str" style="line-height: 1.6;">"#x"</span><span class="pun" style="line-height: 1.6;">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; yField&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;document</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">querySelector</span><span class="pun" style="color: #666600;">(</span><span class="str" style="color: #008800;">"#y"</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; wField&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;document</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">querySelector</span><span class="pun" style="color: #666600;">(</span><span class="str" style="color: #008800;">"#width"</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; hField&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;document</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">querySelector</span><span class="pun" style="color: #666600;">(</span><span class="str" style="color: #008800;">"#height"</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; spriteSelect&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;document</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">querySelector</span><span class="pun" style="color: #666600;">(</span><span class="str" style="color: #008800;">"#spriteSelect"</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; spriteNumber&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;document</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">querySelector</span><span class="pun" style="color: #666600;">(</span><span class="str" style="color: #008800;">"#spriteNumber"</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp;&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; // Update values of the input fields in the page</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; wField</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">value&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;SPRITE_WIDTH</span><span class="pun" style="color: #666600;">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; hField</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">value&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;SPRITE_HEIGHT</span><span class="pun" style="color: #666600;">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; xField</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">value&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666600;">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; yField</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">value&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666600;">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;">&nbsp; &nbsp; // Set attributes for the slider depending on the number of sprites on the&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;">&nbsp; &nbsp; // sprite sheet</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; spriteSelect</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">min&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666600;">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; spriteSelect</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">max</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">NB_ROWS</span><span class="pun" style="color: #666600;">*</span><span class="pln" style="color: #000000;">NB_FRAMES_PER_POSTURE&nbsp;</span><span class="pun" style="color: #666600;">-</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="lit" style="color: #006666;">1</span><span class="pun" style="color: #666600;">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;">&nbsp; &nbsp; // By default the slider is disabled until the sprite sheet is fully loaded</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln" style="line-height: 1.6;">&nbsp; &nbsp; spriteSelect</span><span class="pun" style="line-height: 1.6;">.</span><span class="pln" style="line-height: 1.6;">disabled&nbsp;</span><span class="pun" style="line-height: 1.6;">=</span><span class="pln" style="line-height: 1.6;">&nbsp;</span><span class="kwd" style="line-height: 1.6;">true</span><span class="pun" style="line-height: 1.6;">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; spriteNumber</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">innerHTML</span><span class="pun" style="color: #666600;">=</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666600;">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;"></span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp;&nbsp;</span><span class="com" style="color: #880000;">// Load the spritesheet</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; spritesheet&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="kwd" style="color: #000088;">new</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="typ" style="color: #660066;">Image</span><span class="pun" style="color: #666600;">();</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; spritesheet</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">src</span><span class="pun" style="color: #666600;">=</span><span class="str" style="color: #008800;">"https://i.imgur.com/3VesWqx.png"</span><span class="pun" style="color: #666600;">;</span><span class="pln" style="color: #000000;"></span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;"></span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp;<strong>&nbsp;</strong></span><strong><span class="com" style="color: #880000;">// Called when the spritesheet has been loaded</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; spritesheet</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">onload&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="kwd" style="color: #000088;">function</span><span class="pun" style="color: #666600;">()</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="pun" style="color: #666600;">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com" style="color: #880000;">// enable slider</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; &nbsp; spriteSelect</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">disabled&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="kwd" style="color: #000088;">false</span><span class="pun" style="color: #666600;">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;"></span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com" style="color: #880000;">// Resize big canvas to the size of the sprite sheet image</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; &nbsp; canvasSpriteSheet</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">width&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;spritesheet</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">width</span><span class="pun" style="color: #666600;">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; &nbsp; canvasSpriteSheet</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">height&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;spritesheet</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">height</span><span class="pun" style="color: #666600;">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;"></span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// Draw the whole spritesheet</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; &nbsp;ctx2</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">drawImage</span><span class="pun" style="color: #666600;">(</span><span class="pln" style="color: #000000;">spritesheet</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666600;">);<br><br></span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// Draw the first sprite in the big&nbsp;canvas, corresponding to sprite 0</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// wireframe rectangle in the sprite sheet</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; &nbsp;drawWireFrameRect</span><span class="pun" style="color: #666600;">(</span><span class="pln" style="color: #000000;">ctx2</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;SPRITE_WIDTH</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;SPRITE_HEIGHT</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="str" style="color: #008800;">'red'</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="lit" style="color: #006666;">3</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp;<br></span><span class="com" style="color: #880000;">&nbsp; &nbsp; &nbsp;// small canvas, draw sub image corresponding to sprite 0</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; &nbsp;ctx1</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">drawImage</span><span class="pun" style="color: #666600;">(</span><span class="pln" style="color: #000000;">spritesheet</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;SPRITE_WIDTH</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;SPRITE_HEIGHT</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;"></span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="lit" style="color: #006666;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;0</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;SPRITE_WIDTH</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;SPRITE_HEIGHT</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp;</span><span class="pun" style="color: #666600;">};</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;"></span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp;</span><span class="com" style="color: #880000;">// input listener on the slider</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp;spriteSelect</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">oninput&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="kwd" style="color: #000088;">function</span><span class="pun" style="color: #666600;">(</span><span class="pln" style="color: #000000;">evt</span><span class="pun" style="color: #666600;">)</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="pun" style="color: #666600;">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// Current sprite number from 0 to NB_FRAMES_PER_POSTURE * NB_ROWS</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; &nbsp;</span><span class="kwd" style="color: #000088;">var</span><span class="pln" style="color: #000000;">&nbsp;index&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;spriteSelect</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">value</span><span class="pun" style="color: #666600;">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;"></span></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="pln" style="color: #000000;">&nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// Computation of the x and y position that corresponds to the sprite</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="pln" style="color: #000000;">&nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// number index as selected by the slider</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><strong><span class="pln" style="color: #000000;">&nbsp; &nbsp; &nbsp;</span><span class="kwd" style="color: #000088;">var</span><span class="pln" style="color: #000000;">&nbsp;x&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;index&nbsp;</span><span class="pun" style="color: #666600;">*</span><span class="pln" style="color: #000000;">&nbsp;SPRITE_WIDTH&nbsp;</span><span class="pun" style="color: #666600;">%</span><span class="pln" style="color: #000000;">&nbsp;spritesheet</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">width</span><span class="pun" style="color: #666600;">;</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><strong><span class="pln" style="color: #000000;">&nbsp; &nbsp; &nbsp;</span><span class="kwd" style="color: #000088;">var</span><span class="pln" style="color: #000000;">&nbsp;y&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="typ" style="color: #660066;">Math</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">floor</span><span class="pun" style="color: #666600;">(</span><span class="pln" style="color: #000000;">index&nbsp;</span><span class="pun" style="color: #666600;">/</span><span class="pln" style="color: #000000;">&nbsp;NB_FRAMES_PER_POSTURE</span><span class="pun" style="color: #666600;">)</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="pun" style="color: #666600;">*</span><span class="pln" style="color: #000000;">&nbsp;SPRITE_HEIGHT</span><span class="pun" style="color: #666600;">;</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;"></span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// Update fields</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; &nbsp;xField</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">value&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;x</span><span class="pun" style="color: #666600;">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; &nbsp;yField</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">value&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;y</span><span class="pun" style="color: #666600;">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;"></span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// Clear big canvas, draw wireframe rect at x, y, redraw stylesheet</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; &nbsp;ctx2</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">clearRect</span><span class="pun" style="color: #666600;">(</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;canvasSpriteSheet</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">width</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;canvasSpriteSheet</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">height</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; &nbsp;ctx2</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">drawImage</span><span class="pun" style="color: #666600;">(</span><span class="pln" style="color: #000000;">spritesheet</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; &nbsp;drawWireFrameRect</span><span class="pun" style="color: #666600;">(</span><span class="pln" style="color: #000000;">ctx2</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;x&nbsp;</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;y</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;SPRITE_WIDTH</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;SPRITE_HEIGHT</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="str" style="color: #008800;">'red'</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="lit" style="color: #006666;">3</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// Draw the current sprite in the small canvas</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; &nbsp;ctx1</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">clearRect</span><span class="pun" style="color: #666600;">(</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;SPRITE_WIDTH</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;SPRITE_HEIGHT</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; &nbsp;ctx1</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">drawImage</span><span class="pun" style="color: #666600;">(</span><span class="pln" style="color: #000000;">spritesheet</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;x</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;y</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;SPRITE_WIDTH</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;SPRITE_HEIGHT</span><span class="pun" style="color: #666600;">,</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;SPRITE_WIDTH</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;SPRITE_HEIGHT</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// Update output elem on the right of the slider</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; &nbsp;spriteNumber</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">innerHTML&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;index</span><span class="pun" style="color: #666600;">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp;&nbsp;</span><span class="pun" style="color: #666600;">};</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;">};</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="kwd" style="color: #000088;">function</span><span class="pln" style="color: #000000;">&nbsp;drawWireFrameRect</span><span class="pun" style="color: #666600;">(</span><span class="pln" style="color: #000000;">ctx</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;x</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;y</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;w</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;h</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;color</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;lineWidth</span><span class="pun" style="color: #666600;">)</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="pun" style="color: #666600;">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; ctx</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">save</span><span class="pun" style="color: #666600;">();</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; ctx</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">strokeStyle&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;color</span><span class="pun" style="color: #666600;">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; ctx</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">lineWidth&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;lineWidth</span><span class="pun" style="color: #666600;">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; ctx</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">strokeRect</span><span class="pun" style="color: #666600;">(</span><span class="pln" style="color: #000000;">x&nbsp;</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;y</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;w</span><span class="pun" style="color: #666600;">,</span><span class="pln" style="color: #000000;">&nbsp;h</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; ctx</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">restore</span><span class="pun" style="color: #666600;">();</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp;</span></li>
</ol></div><br>

__Explanations:__

+ _Lines 1-4_: characteristics of the sprite sheet. How many rows, i.e., how many sprites per row, etc.
+ _Lines 11-39_: initializations that run just after the page has been loaded. We first get the canvas and contexts. Then we set the minimum and maximum values of the slider (an `<input type=range>`) at _lines 31-32_, and disable it at line 34 (we cannot slide it before the sprite sheet image has been loaded). We display the current sprite number 0 in the `<output>` field to the right of the slider (_line 35_).  Finally, in lines 37-39, we load the sprite sheet image.
+ _Lines 42-58_: this callback is run once the sprite sheet image has been loaded. We enable the slider, set the big canvas to the size of the loaded image, and then draw it (_line 51_). We also draw the first sprite from the sprite sheet in the small canvas and draw a red wireframe rectangle around the first sprite in the sprite sheet (_lines 52-58_).
+ _Lines 61-87_: the input listener callback, called each time the slider moves. _Lines 65-68_ are the most important ones here: we compute the x and y position of the sprite selected with the slider. We take into account the number of sprites per posture, the number of rows, and the dimensions of each sprite. Then, as in the previous step, we draw the current sprite in the small canvas and highlight the current sprite with a red rectangle in the sprite sheet.

The code is generic enough to work with different kinds of sprite sheets. Adjust the global parameters in bold at lines 1-5 and try the extractor.


#### Example #2

This is the same application with another sprite sheet.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3d7BPMl')"
    src    = "https://bit.ly/3w0L1ZT"
    alt    = "We just changed these parameter values: try the same code but with another sprite sheet (the one with the robot) - see on JSBin."
    title  = "We just changed these parameter values: try the same code but with another sprite sheet (the one with the robot) - see on JSBin."
  />
</figure>

Now it's time to see how we can make a small sprite animation framework!









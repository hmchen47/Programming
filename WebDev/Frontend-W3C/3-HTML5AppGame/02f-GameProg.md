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
  + using time-based animation in draw function of the sprite model


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
      + 8 different sets of sprites, or postures, each corresponding to a direction
      + each comprising exactly 13 sprites, aligned in a single row across the sprite sheet
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

<div style="padding-left: 10px; padding-right: 30px; border: 1px solid black; line-height: 25.6px;"><ol style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li value="1">&lt;html lang<span style="color: #bb6600;">=<span style="color: #008800;">"en"</span><span style="color: #bb6600;">&gt;</span></li>
<li>&nbsp;<span style="color: #008800;">&lt;head&gt;</span></li>
<li>&nbsp;<span style="color: #008800;">&lt;title&gt;</span><span style="color: #aa0066;">Extract</span>&nbsp;<span style="color: #008888;">and</span>&nbsp;draw sprite<span style="color: #bb6600;">&lt;/</span>title<span style="color: #bb6600;">&gt;</span></li>
<li>&nbsp;<span style="color: #008800;">&lt;style&gt;</span></li>
<li>&nbsp; &nbsp;canvas&nbsp;<span style="color: #bb6600;">{</li>
<li>&nbsp; &nbsp; &nbsp; border<span style="color: #bb6600;">:</span>&nbsp;<span style="color: #006666;">1px</span>&nbsp;solid black<span style="color: #bb6600;">;</span></li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #bb6600;">}</span></li>
<li>&nbsp;<span style="color: #bb6600;">&lt;/</span>style<span style="color: #bb6600;">&gt;</span></li>
<li>&nbsp;<span style="color: #bb6600;">&lt;/</span>head<span style="color: #bb6600;">&gt;</span></li>
<li>&nbsp;<span style="color: #008800;">&lt;body&gt;</span></li>
<li>&nbsp; &nbsp;<span style="color: #aa0066;">Sprite&nbsp;width</span><span style="color: #bb6600;">:</span>&nbsp;<span style="color: #006666;">48<span style="color: #bb6600;">,</span>&nbsp;height<span style="color: #bb6600;">:</span>&nbsp;<span style="color: #006666;">92</span><span style="color: #bb6600;">,</span>&nbsp;rows<span style="color: #bb6600;">:&nbsp;<span style="color: #006666;">8</span><span style="color: #bb6600;">,</span>&nbsp;sprites per posture<span style="color: #bb6600;">:</span>&nbsp;<span style="color: #006666;">13</span><span style="color: #008800;">&lt;p&gt;</span></li>
<li>&nbsp; &nbsp;<span style="color: #bb6600;">&lt;</span>label&nbsp;<span style="color: #008888;">for</span><span style="color: #bb6600;">=</span><span style="color: #008800;">"x"</span><span style="color: #bb6600;">&gt;</span>x<span style="color: #bb6600;">:</span>&nbsp;<span style="color: #bb6600;">&lt;</span>input id<span style="color: #bb6600;">=</span><span style="color: #008800;">"x"</span>&nbsp;type<span style="color: #bb6600;">=</span><span style="color: #008800;">"number"</span>&nbsp;min<span style="color: #bb6600;">=</span><span style="color: #006666;">0</span><span style="color: #bb6600;">&gt;&lt;</span>br<span style="color: #bb6600;">/&gt;</span></li>
<li>&nbsp; &nbsp;<span style="color: #bb6600;">&lt;</span>label&nbsp;<span style="color: #008888;">for</span><span style="color: #bb6600;">=</span><span style="color: #008800;">"y"</span><span style="color: #bb6600;">&gt;</span>y<span style="color: #bb6600;">:</span>&nbsp;<span style="color: #bb6600;">&lt;</span>input id<span style="color: #bb6600;">=</span><span style="color: #008800;">"y"</span>&nbsp;type<span style="color: #bb6600;">=</span><span style="color: #008800;">"number"</span>&nbsp;min<span style="color: #bb6600;">=</span><span style="color: #006666;">0</span><span style="color: #bb6600;">&gt;&lt;</span>br<span style="color: #bb6600;">/&gt;</span></li>
<li>&nbsp; &nbsp;<span style="color: #bb6600;">&lt;</span>label&nbsp;<span style="color: #008888;">for</span><span style="color: #bb6600;">=</span><span style="color: #008800;">"width"</span><span style="color: #bb6600;">&gt;</span>width<span style="color: #bb6600;">:</span>&nbsp;<span style="color: #bb6600;">&lt;</span>input id<span style="color: #bb6600;">=</span><span style="color: #008800;">"width"</span>&nbsp;type<span style="color: #bb6600;">=</span><span style="color: #008800;">"number"</span>&nbsp;min<span style="color: #bb6600;">=</span><span style="color: #006666;">0</span><span style="color: #bb6600;">&gt;&lt;</span>br<span style="color: #bb6600;">/&gt;</span></li>
<li>&nbsp; &nbsp;<span style="color: #bb6600;">&lt;</span>label&nbsp;<span style="color: #008888;">for</span><span style="color: #bb6600;">=</span><span style="color: #008800;">"height"</span><span style="color: #bb6600;">&gt;</span>height<span style="color: #bb6600;">:</span>&nbsp;<span style="color: #bb6600;">&lt;</span>input id<span style="color: #bb6600;">=</span><span style="color: #008800;">"height"</span>&nbsp;type<span style="color: #bb6600;">=</span><span style="color: #008800;">"number"</span>&nbsp;min<span style="color: #bb6600;">=</span><span style="color: #006666;">0</span><span style="color: #bb6600;">&gt;&lt;</span>p<span style="color: #bb6600;">&gt;</span></li>
<li><span style="color: #bb6600;"></span></li>
<li><span style="color: #aa0066;">Select</span>&nbsp;current sprite<span style="color: #bb6600;">:</span>&nbsp;<span style="color: #bb6600;">&lt;</span>input type<span style="color: #bb6600;">=</span>range id<span style="color: #bb6600;">=<span style="color: #008800;">"spriteSelect"</span>&nbsp;value<span style="color: #bb6600;">=</span><span style="color: #006666;">0</span><span style="color: #bb6600;">&gt;</span>&nbsp;<span style="color: #bb6600;">&lt;output id<span style="color: #bb6600;">=</span><span style="color: #008800;">"spriteNumber"</span><span style="color: #bb6600;">&gt;</span></li>
<li><span style="color: #bb6600;"></span></li>
<li>&nbsp;<span style="color: #bb6600;">&lt;</span>p<span style="color: #bb6600;">/&gt;</li>
<li>&nbsp; &nbsp;<span style="color: #bb6600;">&lt;</span>canvas id<span style="color: #bb6600;">=</span><span style="color: #008800;">"canvas"</span>&nbsp;width<span style="color: #bb6600;">=</span><span style="color: #008800;">"48"</span>&nbsp;height<span style="color: #bb6600;">=</span><span style="color: #008800;">"92"</span>&nbsp;<span style="color: #bb6600;">/&gt;</span></li>
<li>&nbsp;<span style="color: #bb6600;">&lt;/</span>p<span style="color: #bb6600;">&gt;</span></li>
<li>&nbsp; &nbsp;<span style="color: #bb6600;">&lt;</span>canvas id<span style="color: #bb6600;">=</span><span style="color: #008800;">"spritesheet"</span><span style="color: #bb6600;">&gt;&lt;/</span>canvas<span style="color: #bb6600;">&gt;</span></li>
<li>&nbsp;<span style="color: #bb6600;">&lt;/</span>body<span style="color: #bb6600;">&gt;</span></li>
<li><span style="color: #bb6600;">&lt;/</span>html<span style="color: #bb6600;">&gt;</span></li>
</ol></div><br>

Notice that we use an `<input type="range">` to select the current sprite, and we have two canvases: a small one for displaying the currently-selected sprite, and a larger one that contains the sprite sheet and in which we draw a red square to highlight the selected sprite.

Here's an extract from the JavaScript. You don't have to understand all the details, just look at the part in bold which extracts the individual sprites:

<div style="padding-left: 10px; padding-right: 30px; border: 1px solid black; line-height: 25.6px;"><ol style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li value="1"><strong style="color: red;"><span style="color: #008888;">var</span>&nbsp;SPRITE_WIDTH&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #006666;">48</span><span style="color: #bb6600;">; &nbsp; // Characteristics of the sprites and spritesheet</span></strong></li>
<li><strong style="color: red;"><span style="color: #008888;">var</span>&nbsp;SPRITE_HEIGHT&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #006666;">92</span><span style="color: #bb6600;">;</span></strong></li>
<li><strong style="color: red;"><span style="color: #008888;">var</span>&nbsp;NB_ROWS&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #006666;">8</span><span style="color: #bb6600;">;</span></strong></li>
<li><strong style="color: red;"><span style="color: #008888;">var</span>&nbsp;NB_FRAMES_PER_POSTURE&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #006666;">13<span style="color: #bb6600;">;</span></strong></li>
<li>&nbsp;</li>
<li>// the different input and output fields</li>
<li><span style="color: #008888;">var</span>&nbsp;xField<span style="color: #bb6600;">,</span>&nbsp;yField<span style="color: #bb6600;">,</span>&nbsp;wField<span style="color: #bb6600;">,</span>&nbsp;hField<span style="color: #bb6600;">,</span>&nbsp;spriteSelect<span style="color: #bb6600;">,</span>&nbsp;spriteNumber<span style="color: #bb6600;">;<br><br></span></li>
<li>// The two canvases and respective contexts</li>
<li><span style="color: #008888;">var</span>&nbsp;canvas<span style="color: #bb6600;">,</span>&nbsp;canvasSpriteSheet<span style="color: #bb6600;">,</span>&nbsp;ctx1<span style="color: #bb6600;">,</span>&nbsp;ctx2<span style="color: #bb6600;">;</span></li>
<li>&nbsp;</li>
<li>window<span style="color: #bb6600;">.</span>onload&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #008888;">function</span><span style="color: #bb6600;">()</span>&nbsp;<span style="color: #bb6600;">{</span></li>
<li>&nbsp; &nbsp; canvas&nbsp;<span style="color: #bb6600;">=</span>&nbsp;document<span style="color: #bb6600;">.</span>getElementById<span style="color: #bb6600;">(</span><span style="color: #008800;">"canvas"</span><span style="color: #bb6600;">);</span></li>
<li>&nbsp; &nbsp; ctx1&nbsp;<span style="color: #bb6600;">=</span>&nbsp;canvas<span style="color: #bb6600;">.</span>getContext<span style="color: #bb6600;">(</span><span style="color: #008800;">"2d"</span><span style="color: #bb6600;">);</span></li>
<li>&nbsp; &nbsp; canvasSpriteSheet&nbsp;<span style="color: #bb6600;">=</span>&nbsp;document<span style="color: #bb6600;">.</span>getElementById<span style="color: #bb6600;">(</span><span style="color: #008800;">"spritesheet"</span><span style="color: #bb6600;">);</span></li>
<li>&nbsp; &nbsp; ctx2&nbsp;<span style="color: #bb6600;">=</span>&nbsp;canvasSpriteSheet<span style="color: #bb6600;">.</span>getContext<span style="color: #bb6600;">(</span><span style="color: #008800;">"2d"</span><span style="color: #bb6600;">);</span></li>
<li><span style="line-height: 1.6;"></span></li>
<li><span style="line-height: 1.6;">&nbsp; &nbsp; xField&nbsp;</span><span style="line-height: 1.6;">=</span><span style="line-height: 1.6;">&nbsp;document</span><span style="line-height: 1.6;">.</span><span style="line-height: 1.6;">querySelector</span><span style="line-height: 1.6;">(</span><span style="line-height: 1.6;">"#x"</span><span style="line-height: 1.6;">);</span></li>
<li>&nbsp; &nbsp; yField&nbsp;<span style="color: #bb6600;">=</span>&nbsp;document<span style="color: #bb6600;">.</span>querySelector<span style="color: #bb6600;">(</span><span style="color: #008800;">"#y"</span><span style="color: #bb6600;">);</span></li>
<li>&nbsp; &nbsp; wField&nbsp;<span style="color: #bb6600;">=</span>&nbsp;document<span style="color: #bb6600;">.</span>querySelector<span style="color: #bb6600;">(</span><span style="color: #008800;">"#width"</span><span style="color: #bb6600;">);</span></li>
<li>&nbsp; &nbsp; hField&nbsp;<span style="color: #bb6600;">=</span>&nbsp;document<span style="color: #bb6600;">.</span>querySelector<span style="color: #bb6600;">(</span><span style="color: #008800;">"#height"</span><span style="color: #bb6600;">);</span></li>
<li>&nbsp; &nbsp; spriteSelect&nbsp;<span style="color: #bb6600;">=</span>&nbsp;document<span style="color: #bb6600;">.</span>querySelector<span style="color: #bb6600;">(</span><span style="color: #008800;">"#spriteSelect"</span><span style="color: #bb6600;">);</span></li>
<li>&nbsp; &nbsp; spriteNumber&nbsp;<span style="color: #bb6600;">=</span>&nbsp;document<span style="color: #bb6600;">.</span>querySelector<span style="color: #bb6600;">(</span><span style="color: #008800;">"#spriteNumber"</span><span style="color: #bb6600;">);</span></li>
<li>&nbsp; &nbsp;&nbsp;</li>
<li>&nbsp; &nbsp; // Update values of the input fields in the page</li>
<li>&nbsp; &nbsp; wField<span style="color: #bb6600;">.</span>value&nbsp;<span style="color: #bb6600;">=</span>&nbsp;SPRITE_WIDTH<span style="color: #bb6600;">;</span></li>
<li>&nbsp; &nbsp; hField<span style="color: #bb6600;">.</span>value&nbsp;<span style="color: #bb6600;">=</span>&nbsp;SPRITE_HEIGHT<span style="color: #bb6600;">;</span></li>
<li>&nbsp; &nbsp; xField<span style="color: #bb6600;">.</span>value&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #006666;">0</span><span style="color: #bb6600;">;</span></li>
<li>&nbsp; &nbsp; yField<span style="color: #bb6600;">.</span>value&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #006666;">0</span><span style="color: #bb6600;">;</span></li>
<li><span style="color: #bb6600;">&nbsp; &nbsp; // Set attributes for the slider depending on the number of sprites on the&nbsp;</span></li>
<li><span style="color: #bb6600;">&nbsp; &nbsp; // sprite sheet</span></li>
<li>&nbsp; &nbsp; spriteSelect<span style="color: #bb6600;">.</span>min&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #006666;">0</span><span style="color: #bb6600;">;</span></li>
<li>&nbsp; &nbsp; spriteSelect<span style="color: #bb6600;">.</span><span>max</span><span style="color: #bb6600;">=</span>NB_ROWS<span style="color: #bb6600;">*NB_FRAMES_PER_POSTURE&nbsp;</span><span style="color: #bb6600;">-</span>&nbsp;<span style="color: #006666;">1</span><span style="color: #bb6600;">;</span></li>
<li><span style="color: #bb6600;">&nbsp; &nbsp; // By default the slider is disabled until the sprite sheet is fully loaded</span></li>
<li><span style="line-height: 1.6;">&nbsp; &nbsp; spriteSelect</span><span style="line-height: 1.6;">.</span><span style="line-height: 1.6;">disabled&nbsp;</span><span style="line-height: 1.6;">=</span><span style="line-height: 1.6;">&nbsp;</span><span style="line-height: 1.6;">true</span><span style="line-height: 1.6;">;</span></li>
<li>&nbsp; &nbsp; spriteNumber<span style="color: #bb6600;">.</span>innerHTML<span style="color: #bb6600;">=</span><span style="color: #006666;">0</span><span style="color: #bb6600;">;</span></li>
<li></li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #880000;">// Load the spritesheet</span></li>
<li>&nbsp; &nbsp; spritesheet&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #008888;">new</span>&nbsp;<span style="color: #aa0066;">Image</span><span style="color: #bb6600;">();</span></li>
<li>&nbsp; &nbsp; spritesheet<span style="color: #bb6600;">.</span>src<span style="color: #bb6600;">=</span><span style="color: #008800;">"https://i.imgur.com/3VesWqx.png"</span><span style="color: #bb6600;">;</span></li>
<li></li>
<li>&nbsp; &nbsp;<strong style="color: red;">&nbsp;</strong><strong style="color: red;"><span style="color: #880000;">// Called when the spritesheet has been loaded</span></strong></li>
<li>&nbsp; &nbsp; spritesheet<span style="color: #bb6600;">.</span>onload&nbsp;<span style="color: #bb6600;">=&nbsp;<span style="color: #008888;">function</span><span style="color: #bb6600;">()</span>&nbsp;<span style="color: #bb6600;">{</span></li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;<span style="color: #880000;">// enable slider</span></li>
<li>&nbsp; &nbsp; &nbsp; spriteSelect<span style="color: #bb6600;">.</span>disabled&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #008888;">false</span><span style="color: #bb6600;">;</span></li>
<li></li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;<span style="color: #880000;">// Resize big canvas to the size of the sprite sheet image</span></li>
<li>&nbsp; &nbsp; &nbsp; canvasSpriteSheet<span style="color: #bb6600;">.</span>width&nbsp;<span style="color: #bb6600;">=</span>&nbsp;spritesheet<span style="color: #bb6600;">.</span>width<span style="color: #bb6600;">;</span></li>
<li>&nbsp; &nbsp; &nbsp; canvasSpriteSheet<span style="color: #bb6600;">.</span>height&nbsp;<span style="color: #bb6600;">=</span>&nbsp;spritesheet<span style="color: #bb6600;">.</span>height<span style="color: #bb6600;">;</span></li>
<li></li>
<li>&nbsp; &nbsp; &nbsp;<span style="color: #880000;">// Draw the whole spritesheet</span></li>
<li>&nbsp; &nbsp; &nbsp;ctx2<span style="color: #bb6600;">.</span>drawImage<span style="color: #bb6600;">(</span>spritesheet<span style="color: #bb6600;">,</span>&nbsp;<span style="color: #006666;">0</span><span style="color: #bb6600;">,</span>&nbsp;<span style="color: #006666;">0</span><span style="color: #bb6600;">);<br><br></span></li>
<li>&nbsp; &nbsp; &nbsp;<span style="color: #880000;">// Draw the first sprite in the big&nbsp;canvas, corresponding to sprite 0</span></li>
<li>&nbsp; &nbsp; &nbsp;<span style="color: #880000;">// wireframe rectangle in the sprite sheet</span></li>
<li>&nbsp; &nbsp; &nbsp;drawWireFrameRect<span style="color: #bb6600;">(</span>ctx2<span style="color: #bb6600;">,</span>&nbsp;<span style="color: #006666;">0</span>&nbsp;<span style="color: #bb6600;">,</span>&nbsp;<span style="color: #006666;">0</span><span style="color: #bb6600;">,</span>&nbsp;SPRITE_WIDTH<span style="color: #bb6600;">,</span>&nbsp;SPRITE_HEIGHT<span style="color: #bb6600;">,</span>&nbsp;<span style="color: #008800;">'red'</span><span style="color: #bb6600;">,</span>&nbsp;<span style="color: #006666;">3</span><span style="color: #bb6600;">);</span></li>
<li>&nbsp;<br><span style="color: #880000;">&nbsp; &nbsp; &nbsp;// small canvas, draw sub image corresponding to sprite 0</span></li>
<li>&nbsp; &nbsp; &nbsp;ctx1<span style="color: #bb6600;">.</span>drawImage<span style="color: #bb6600;">(</span>spritesheet<span style="color: #bb6600;">,</span>&nbsp;<span style="color: #006666;">0</span><span style="color: #bb6600;">,</span>&nbsp;<span style="color: #006666;">0</span><span style="color: #bb6600;">,</span>&nbsp;SPRITE_WIDTH<span style="color: #bb6600;">,</span>&nbsp;SPRITE_HEIGHT<span style="color: #bb6600;">,</span></li>
<li><span style="color: #006666;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;0</span><span style="color: #bb6600;">,</span>&nbsp;<span style="color: #006666;">0</span><span style="color: #bb6600;">,</span>&nbsp;SPRITE_WIDTH<span style="color: #bb6600;">,</span>&nbsp;SPRITE_HEIGHT<span style="color: #bb6600;">);</span></li>
<li>&nbsp; &nbsp;<span style="color: #bb6600;">};</span></li>
<li></li>
<li>&nbsp; &nbsp;<span style="color: #880000;">// input listener on the slider</span></li>
<li>&nbsp; &nbsp;spriteSelect<span style="color: #bb6600;">.</span>oninput&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #008888;">function</span><span style="color: #bb6600;">(</span>evt<span style="color: #bb6600;">)</span>&nbsp;<span style="color: #bb6600;">{</span></li>
<li>&nbsp; &nbsp; &nbsp;<span style="color: #880000;">// Current sprite number from 0 to NB_FRAMES_PER_POSTURE * NB_ROWS</span></li>
<li>&nbsp; &nbsp; &nbsp;<span style="color: #008888;">var</span>&nbsp;index&nbsp;<span style="color: #bb6600;">=</span>&nbsp;spriteSelect<span style="color: #bb6600;">.</span>value<span style="color: #bb6600;">;</span></li>
<li></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp;<span style="color: #880000;">// Computation of the x and y position that corresponds to the sprite</span></strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp;<span style="color: #880000;">// number index as selected by the slider</span></strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp;<span style="color: #008888;">var</span>&nbsp;x&nbsp;<span style="color: #bb6600;">=</span>&nbsp;index&nbsp;<span style="color: #bb6600;">*</span>&nbsp;SPRITE_WIDTH&nbsp;<span style="color: #bb6600;">%</span>&nbsp;spritesheet<span style="color: #bb6600;">.</span>width<span style="color: #bb6600;">;</span></strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp;<span style="color: #008888;">var</span>&nbsp;y&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #aa0066;">Math</span><span style="color: #bb6600;">.</span>floor<span style="color: #bb6600;">(</span>index&nbsp;<span style="color: #bb6600;">/</span>&nbsp;NB_FRAMES_PER_POSTURE<span style="color: #bb6600;">)</span>&nbsp;<span style="color: #bb6600;">*</span>&nbsp;SPRITE_HEIGHT<span style="color: #bb6600;">;</span></strong></li>
<li></li>
<li>&nbsp; &nbsp; &nbsp;<span style="color: #880000;">// Update fields</span></li>
<li>&nbsp; &nbsp; &nbsp;xField<span style="color: #bb6600;">.</span>value&nbsp;<span style="color: #bb6600;">=</span>&nbsp;x<span style="color: #bb6600;">;</span></li>
<li>&nbsp; &nbsp; &nbsp;yField<span style="color: #bb6600;">.</span>value&nbsp;<span style="color: #bb6600;">=</span>&nbsp;y<span style="color: #bb6600;">;</span></li>
<li></li>
<li>&nbsp; &nbsp; &nbsp;<span style="color: #880000;">// Clear big canvas, draw wireframe rect at x, y, redraw stylesheet</span></li>
<li>&nbsp; &nbsp; &nbsp;ctx2<span style="color: #bb6600;">.</span>clearRect<span style="color: #bb6600;">(</span><span style="color: #006666;">0</span><span style="color: #bb6600;">,</span>&nbsp;<span style="color: #006666;">0</span><span style="color: #bb6600;">,</span>&nbsp;canvasSpriteSheet<span style="color: #bb6600;">.</span>width<span style="color: #bb6600;">,</span>&nbsp;canvasSpriteSheet<span style="color: #bb6600;">.</span>height<span style="color: #bb6600;">);</span></li>
<li>&nbsp; &nbsp; &nbsp;ctx2<span style="color: #bb6600;">.</span>drawImage<span style="color: #bb6600;">(</span>spritesheet<span style="color: #bb6600;">,</span>&nbsp;<span style="color: #006666;">0</span><span style="color: #bb6600;">,</span>&nbsp;<span style="color: #006666;">0</span><span style="color: #bb6600;">);</span></li>
<li>&nbsp; &nbsp; &nbsp;drawWireFrameRect<span style="color: #bb6600;">(</span>ctx2<span style="color: #bb6600;">,</span>&nbsp;x&nbsp;<span style="color: #bb6600;">,</span>&nbsp;y<span style="color: #bb6600;">,</span>&nbsp;SPRITE_WIDTH<span style="color: #bb6600;">,</span>&nbsp;SPRITE_HEIGHT<span style="color: #bb6600;">,</span>&nbsp;<span style="color: #008800;">'red'</span><span style="color: #bb6600;">,</span>&nbsp;<span style="color: #006666;">3</span><span style="color: #bb6600;">);</span></li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp;<span style="color: #880000;">// Draw the current sprite in the small canvas</span></li>
<li>&nbsp; &nbsp; &nbsp;ctx1<span style="color: #bb6600;">.</span>clearRect<span style="color: #bb6600;">(</span><span style="color: #006666;">0</span><span style="color: #bb6600;">,</span>&nbsp;<span style="color: #006666;">0</span><span style="color: #bb6600;">,</span>&nbsp;SPRITE_WIDTH<span style="color: #bb6600;">,</span>&nbsp;SPRITE_HEIGHT<span style="color: #bb6600;">);</span></li>
<li>&nbsp; &nbsp; &nbsp;ctx1<span style="color: #bb6600;">.</span>drawImage<span style="color: #bb6600;">(</span>spritesheet<span style="color: #bb6600;">,</span>&nbsp;x<span style="color: #bb6600;">,</span>&nbsp;y<span style="color: #bb6600;">,</span>&nbsp;SPRITE_WIDTH<span style="color: #bb6600;">,</span>&nbsp;SPRITE_HEIGHT<span style="color: #bb6600;">,</span></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<span style="color: #006666;">0</span><span style="color: #bb6600;">,</span>&nbsp;<span style="color: #006666;">0</span><span style="color: #bb6600;">,</span>&nbsp;SPRITE_WIDTH<span style="color: #bb6600;">,</span>&nbsp;SPRITE_HEIGHT<span style="color: #bb6600;">);</span></li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp;<span style="color: #880000;">// Update output elem on the right of the slider</span></li>
<li>&nbsp; &nbsp; &nbsp;spriteNumber<span style="color: #bb6600;">.</span>innerHTML&nbsp;<span style="color: #bb6600;">=</span>&nbsp;index<span style="color: #bb6600;">;</span></li>
<li>&nbsp;&nbsp;<span style="color: #bb6600;">};</span></li>
<li><span style="color: #bb6600;">};</span></li>
<li>&nbsp;</li>
<li><span style="color: #008888;">function</span>&nbsp;drawWireFrameRect<span style="color: #bb6600;">(</span>ctx<span style="color: #bb6600;">,</span>&nbsp;x<span style="color: #bb6600;">,</span>&nbsp;y<span style="color: #bb6600;">,</span>&nbsp;w<span style="color: #bb6600;">,</span>&nbsp;h<span style="color: #bb6600;">,</span>&nbsp;color<span style="color: #bb6600;">,</span>&nbsp;lineWidth<span style="color: #bb6600;">)</span>&nbsp;<span style="color: #bb6600;">{</span></li>
<li>&nbsp; ctx<span style="color: #bb6600;">.</span>save<span style="color: #bb6600;">();</span></li>
<li>&nbsp; ctx<span style="color: #bb6600;">.</span>strokeStyle&nbsp;<span style="color: #bb6600;">=</span>&nbsp;color<span style="color: #bb6600;">;</span></li>
<li>&nbsp; ctx<span style="color: #bb6600;">.</span>lineWidth&nbsp;<span style="color: #bb6600;">=</span>&nbsp;lineWidth<span style="color: #bb6600;">;</span></li>
<li>&nbsp; ctx<span style="color: #bb6600;">.</span>strokeRect<span style="color: #bb6600;">(</span>x&nbsp;<span style="color: #bb6600;">,</span>&nbsp;y<span style="color: #bb6600;">,</span>&nbsp;w<span style="color: #bb6600;">,</span>&nbsp;h<span style="color: #bb6600;">);</span></li>
<li>&nbsp; ctx<span style="color: #bb6600;">.</span>restore<span style="color: #bb6600;">();</span></li>
<li><span style="color: #bb6600;">}</span></li>
<li>&nbsp;</li>
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
    + drawing within the animation loop
    + taking into account elapsed time: creating a realistic "delay" btw each change of sprite image

+ Example: walking woman w/ multiple postures/sheet
  + HTML snippet
    + tasks:
      + use a slide to select the current sprite
      + two canvases: small one for the current selected sprite while the large one for the sprite sheet
      + draw a red square to highlight the selected sprite of the large canvas
    + display default settings: `<p>Sprite width: 48, height: 92, rows: 8, sprites per posture: 13</p>`
    + row input of sprite sheet: `<label for="x">x <input id="x" type="number" min=0><br/>`
    + column input of sprite sheet: `<label for="y">y <input id="y" type="number" min=0><br/>`
    + width input of selected posture: `<label for="width">width <input id="width" type="number" min=0><br/>`
    + height input of selected posture: `<label for="height">height <input id="height" type="number" min=0><br/>`
    + slider to select sprite: `<p>Select current sprite <input type=range id="spriteSelect" value=0> <output id="spriteNumber"></output></p>`
    + selected sprite image: `<p><canvas id="canvas" width=48 height=92 /></p>`
    + display sprite sheet: `<p><canvas id="spritesheet"></canvas></p>`
  + JavaScript snippet:
    + tasks:
      + set characteristics of the sprite sheet
      + initialize after the page loaded, get canvas and context, set max and min values of the sliders, disable slider before spritsheet loaded, and load the sprite sheet
      + run callback once spritesheet loaded, enable the slider, set big canvas size, and draw it
      + draw the selected sprite in small canvas and red frame in big canvas
      + move slider to trigger events, compute the x and y position of sprite sheet w/ the number of sprites per posture, the number of rows, and the dimensions of each sprite, and then update the drawing on two canvas 
    + set characteristics of sprite and sprite sheet: `var SPRITE_WIDTH = 48; var SPRITE_HEIGHT = 92; var NB_ROWS = 8; var NB_FRAMES_PER_POSTURE = 13;`
    + declare variables: `var xField, yField, wField, hField, spriteSheet, spriteNumber; var canvas, canvasSpriteSheet, ctx1, ctx2;`
    + init page after DOM ready<a name="init"></a>: `window.onload = function() {...}`
      + access canvas and set context: `canvas = document.getElementById("canvas"); ctx1 = canvas.getContext("2d"); canvasSpriteSheet = document.getElementById("spritesheet"); ctx2 = canvasSpriteSheet.getContext("2d");`
      + access elements: `xField = document.querySelector("#x"); yField = document.querySelector("#y"); wField = document.querySelector("#width"); hField = document.querySelector("#height"); spriteSelect = document.querySelector("#spriteSelect"); spriteNumber = document.querySelector("#spriteNumber");`
      + update values of input fields: `wField.value = SPRITE_WIDTH; hField.value = SPRITE_HEIGHT; xField.value = 0; yField.value = 0;`
      + set attributes of slider and default values: `spriteSelect.value = 0; spriteSelect.min = 0; spriteSelect.max = NB_ROWS*NB_FRAMES_PER_POSTURE - 1; spriteSelect.disabled = true; spriteNumber.innerHTML = 0;`
      + load spritesheet: `spritesheet = new img(); spritesheet.src="https://i.imgur.com/3VesWqx.png";`
      + process after sprite sheet downloaded<a name="loadSpritesheet"></a>: `spritesheet.onload = function(evt) {...}`
        + delcare variable: `var index = spriteSelect.value;`
        + compute the position of selected posture: `var x = index*SPRITE_WIDTH % spritesheet.width; var y = Math.floor(index/NB_FRAMES_PER_POSTURE) * SPRITE_HEIGHT;`
        + update fields: `xField.value = x; yField.value = y;`
        + draw red wireframe for selected sprite: `ctx2.clearRect(0, 0, canvasSpriteSheet.width, canvasSpriteSheet.height); ctx2.drawImage(spritesheet, 0, 0); drawWireFrameRect(ctx2, x, y, SPRITE_WIDTH, SPRITE_HEIGHT, 'red', 3);`
        + draw select sprite in small canvas: `ctx1.clearRect(0, 0, SPRITE_WIDTH, SPRITE_HEIGHT); ctx1.drawImage(spritesheet, x, y, SPRITE_WIDTH, SPRITE_HEIGHT, 0, 0, SPRITE_WIDTH, SPRITE_HEIGHT);`
        + update output element for slider: `spriteNumber.innerHTML = index;`
    + draw wireframe: `function drawWireFrameRect(ctx, x, y, w, h, color, lineWidth) {...}`
      + save ctx: `ctx.save();`
      + set and draw wireframe: `ctx.strokeStyle = color; ctx.lineWidth = lineWidth; ctx.strokeRect(x, y, w, h);`
      + restore ctx: `ctx.restore();`


### 2.6.4 A small sprite animation framework

Now that we have presented the principle of sprite extraction (sprites as sub-images of a single composite image), let's write a small sprite animation framework.


#### Sprite animation framework

Here is how you would create and animate a sprite:

<div style="padding-left: 10px; padding-right: 30px; border: 1px solid black; line-height: 25.6px;"><ol style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li value="1"><strong style="color: red;"><span style="color: #008888;">var</span>&nbsp;robot<span style="color: #bb6600;">;</span></strong></li>
<li>&nbsp;</li>
<li>window<span style="color: #bb6600;">.</span>onload&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #008888;">function</span><span style="color: #bb6600;">()</span>&nbsp;<span style="color: #bb6600;">{</span></li>
<li>&nbsp; &nbsp;canvas&nbsp;<span style="color: #bb6600;">=</span>&nbsp;document<span style="color: #bb6600;">.</span>getElementById<span style="color: #bb6600;">(</span><span style="color: #008800;">"canvas"</span><span style="color: #bb6600;">);</span></li>
<li>&nbsp; &nbsp;ctx&nbsp;<span style="color: #bb6600;">=</span>&nbsp;canvas<span style="color: #bb6600;">.</span>getContext<span style="color: #bb6600;">(</span><span style="color: #008800;">"2d"</span><span style="color: #bb6600;">);</span></li>
<li></li>
<li>&nbsp;&nbsp;<span style="color: #880000;">// Load the spritesheet</span></li>
<li>&nbsp; spritesheet&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #008888;">new</span>&nbsp;<span style="color: #aa0066;">Image</span><span style="color: #bb6600;">();</span></li>
<li>&nbsp; spritesheet<span style="color: #bb6600;">.</span>src&nbsp;<span style="color: #bb6600;">=</span>&nbsp;SPRITESHEET_URL<span style="color: #bb6600;">;</span></li>
<li></li>
<li>&nbsp;&nbsp;<span style="color: #880000;">// Called when the spritesheet has been loaded</span></li>
<li>&nbsp; spritesheet<span style="color: #bb6600;">.</span>onload&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #008888;">function</span><span style="color: #bb6600;">()</span>&nbsp;<span style="color: #bb6600;">{</span></li>
<li><span style="color: #bb6600;">&nbsp; &nbsp; ...</span></li>
<li>&nbsp; &nbsp;&nbsp;<strong style="color: red;">robot&nbsp;</strong><strong style="color: red;"><span style="color: #bb6600;">=</span>&nbsp;<span style="color: #008888;">new</span>&nbsp;<span style="color: #aa0066;">Sprite</span><span style="color: #bb6600;">();</span></strong></li>
<li><strong style="color: red;"><span style="color: #bb6600;">&nbsp; &nbsp; // 1 is the posture number in the sprite sheet. We have</span></strong></li>
<li><strong style="color: red;"><span style="color: #bb6600;">&nbsp; &nbsp; // only one with the robot.</span></strong></li>
<li><strong style="color: red;"><span style="line-height: 1.6;">&nbsp; &nbsp; robot</span><span style="line-height: 1.6;">.</span><span style="line-height: 1.6;">extractSprites</span><span style="line-height: 1.6;">(</span><span style="line-height: 1.6;">spritesheet</span><span style="line-height: 1.6;">,</span><span style="line-height: 1.6;">&nbsp;NB_POSTURES</span><span style="line-height: 1.6;">, 1,</span></strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;NB_FRAMES_PER_POSTURE<span style="color: #bb6600;">,</span></strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;SPRITE_WIDTH<span style="color: #bb6600;">,</span>&nbsp;SPRITE_HEIGHT<span style="color: #bb6600;">);</span></strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; robot<span style="color: #bb6600;">.</span>setNbImagesPerSecond<span style="color: #bb6600;">(</span><span style="color: #006666;">20</span><span style="color: #bb6600;">);</span></strong></li>
<li></li>
<li>&nbsp; &nbsp; requestAnimationFrame<span style="color: #bb6600;">(</span>mainloop<span style="color: #bb6600;">);</span></li>
<li>&nbsp;<span style="color: #bb6600;">};</span>&nbsp;<span style="color: #880000;">// onload</span></li>
<li><span style="color: #bb6600;">};</span></li>
<li>&nbsp;</li>
<li><span style="color: #008888;">function</span>&nbsp;mainloop<span style="color: #bb6600;">()</span>&nbsp;<span style="color: #bb6600;">{</span></li>
<li>&nbsp;&nbsp;<span style="color: #880000;">// Clear the canvas</span></li>
<li>&nbsp; ctx<span style="color: #bb6600;">.</span>clearRect<span style="color: #bb6600;">(</span><span style="color: #006666;">0</span><span style="color: #bb6600;">,</span>&nbsp;<span style="color: #006666;">0</span><span style="color: #bb6600;">,</span>&nbsp;canvas<span style="color: #bb6600;">.</span>width<span style="color: #bb6600;">,</span>&nbsp;canvas<span style="color: #bb6600;">.</span>height<span style="color: #bb6600;">);</span></li>
<li>&nbsp;&nbsp;<strong style="color: red;"><span style="color: #880000;">// draw sprite at 0, 0 in the small canvas</span></strong></li>
<li><strong style="color: red;">&nbsp; robot<span style="color: #bb6600;">.</span>draw<span style="color: #bb6600;">(</span>ctx<span style="color: #bb6600;">,</span>&nbsp;<span style="color: #006666;">0</span><span style="color: #bb6600;">,</span>&nbsp;<span style="color: #006666;">0</span><span style="color: #bb6600;">,</span>&nbsp;<span style="color: #006666;">1</span><span style="color: #bb6600;">);</span></strong></li>
<li></li>
<li>&nbsp; requestAnimationFrame<span style="color: #bb6600;">(</span>mainloop<span style="color: #bb6600;">);</span></li>
<li><span style="color: #bb6600;">}</span></li>
</ol></div><br>

Try [the example on JSBin](https://jsbin.com/rugosu/edit?js,output) that uses this framework first! Experiment by editing _line 20_: __`robot.setNbImagesPerSecond(20);`__ changing the value of the parameter and observing the result.

[Local Demo](src/02f-example04.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick= "window.open('https://bit.ly/3wRtk01')"
    src    = "https://bit.ly/3gYQpad"
    alt    = "Example of the sprite framework on JsBin. Screenshot"
    title  = "Example of the sprite framework on JsBin. Screenshot"
  />
</figure>


#### The `SpriteImage` object and sprite models

In this small framework we use "`SpriteImage`", a JS object we build to  represent one sprite image. Its properties are: the global sprite sheet to which it belongs, its position in the sprite sheet, and its size. It also has a `draw` method for drawing the sprite image at an `xPos`, `yPos` position, and at an appropriate size.

<div style="padding-left: 30px; padding-right: 30px; border: 1px solid black; line-height: 25.6px;"><ol style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li value="1"><span style="color: #008888;">function</span>&nbsp;<span style="color: #aa0066;">SpriteImage<span style="color: #bb6600;">(</span>img<span style="color: #bb6600;">,</span>&nbsp;x<span style="color: #bb6600;">,</span>&nbsp;y<span style="color: #bb6600;">,</span>&nbsp;width<span style="color: #bb6600;">,</span>&nbsp;height<span style="color: #bb6600;">)</span>&nbsp;<span style="color: #bb6600;">{</span></li>
<li>&nbsp; &nbsp;<span style="color: #008888;">this</span><span style="color: #bb6600;">.</span>img&nbsp;<span style="color: #bb6600;">=</span>&nbsp;img<span style="color: #bb6600;">;</span>&nbsp;<span style="color: #880000;">// the whole image that contains all sprites</span></li>
<li>&nbsp; &nbsp;<span style="color: #008888;">this</span><span style="color: #bb6600;">.</span>x&nbsp;<span style="color: #bb6600;">=</span>&nbsp;x<span style="color: #bb6600;">;</span>&nbsp; &nbsp; &nbsp;<span style="color: #880000;">// x, y position of the sprite image in the whole image</span></li>
<li>&nbsp; &nbsp;<span style="color: #008888;">this</span><span style="color: #bb6600;">.</span>y&nbsp;<span style="color: #bb6600;">=</span>&nbsp;y<span style="color: #bb6600;">;</span></li>
<li>&nbsp; &nbsp;<span style="color: #008888;">this</span><span style="color: #bb6600;">.</span>width&nbsp;<span style="color: #bb6600;">=</span>&nbsp;width<span style="color: #bb6600;">;</span>&nbsp;<span style="color: #880000;">// width and height of the sprite image</span></li>
<li>&nbsp; &nbsp;<span style="color: #008888;">this</span><span style="color: #bb6600;">.</span>height&nbsp;<span style="color: #bb6600;">=</span>&nbsp;height<span style="color: #bb6600;">;</span></li>
<li>&nbsp;&nbsp;</li>
<li>&nbsp; &nbsp;<span style="color: #008888;">this</span><span style="color: #bb6600;">.</span>draw&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #008888;">function</span><span style="color: #bb6600;">(</span>ctx<span style="color: #bb6600;">,</span>&nbsp;xPos<span style="color: #bb6600;">,</span>&nbsp;yPos<span style="color: #bb6600;">,</span>&nbsp;scale<span style="color: #bb6600;">)</span>&nbsp;<span style="color: #bb6600;">{</span></li>
<li>&nbsp; &nbsp; &nbsp; ctx<span style="color: #bb6600;">.</span>drawImage<span style="color: #bb6600;">(</span><span style="color: #008888;">this</span><span style="color: #bb6600;">.</span>img<span style="color: #bb6600;">,</span></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<span style="color: #008888;">this</span><span style="color: #bb6600;">.</span>x<span style="color: #bb6600;">,</span>&nbsp;<span style="color: #008888;">this</span><span style="color: #bb6600;">.</span>y<span style="color: #bb6600;">,</span>&nbsp;<span style="color: #880000;">// x, y, width and height of img to extract</span></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<span style="color: #008888;">this</span><span style="color: #bb6600;">.</span><span>width<span style="color: #bb6600;">,&nbsp;<span style="color: #008888;">this</span><span style="color: #bb6600;">.</span>height<span style="color: #bb6600;">,</span></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; xPos<span style="color: #bb6600;">,</span>&nbsp;yPos<span style="color: #bb6600;">,</span>&nbsp;<span style="color: #880000;">// x, y, width and height of img to draw</span></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<span style="color: #008888;">this</span><span style="color: #bb6600;">.</span>width<span style="color: #bb6600;">*</span>scale<span style="color: #bb6600;">,</span>&nbsp;<span style="color: #008888;">this</span><span style="color: #bb6600;">.</span>height<span style="color: #bb6600;">*</span>scale<span style="color: #bb6600;">);</span></li>
<li>&nbsp;<span style="color: #bb6600;">};</span></li>
<li><span style="color: #bb6600;">}</span></li>
</ol></div><br>

We define the `Sprite` model. This is the one we used to create the small robot in the previous example.

+ A Sprite is defined by an array of `SpriteImage` objects.
+ It has a method for extracting all `SpriteImages` from a given sprite sheet and filling the above array.
+ It has a `draw` method which will draw the current `SpriteImage`. A `Sprite` is an animated object, therefore, calling draw multiple times will involve an automatic change of the current `SpriteImage` being drawn.
+ The number of different images to be drawn per second is a parameter of the sprite.

Here is the code of the Sprite model:

<div style="padding-left: 30px; padding-right: 30px; border: 1px solid black; line-height: 25.6px;"><ol style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li value="1"><span style="color: #008888;">function</span>&nbsp;<span style="color: #aa0066;">Sprite</span><span style="color: #bb6600;">()</span>&nbsp;<span style="color: #bb6600;">{</span></li>
<li>&nbsp;&nbsp;<span style="color: #008888;">this</span><span style="color: #bb6600;">.</span>spriteArray&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #bb6600;">[];</span></li>
<li>&nbsp;&nbsp;<span style="color: #008888;">this</span><span style="color: #bb6600;">.</span>currentFrame&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #006666;">0</span><span style="color: #bb6600;">;</span></li>
<li>&nbsp;&nbsp;<span style="color: #008888;">this</span><span style="color: #bb6600;">.</span>delayBetweenFrames&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #006666;">10</span><span style="color: #bb6600;">;</span></li>
<li></li>
<li>&nbsp;&nbsp;<span style="color: #008888;">this</span><span style="color: #bb6600;">.</span>extractSprites&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #008888;">function</span><span style="color: #bb6600;">(</span>spritesheet<span style="color: #bb6600;">,</span></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;nbPostures<span style="color: #bb6600;">,</span>&nbsp;postureToExtract, </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;nbFramesPerPosture<span style="color: #bb6600;">,</span></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;spriteWidth<span style="color: #bb6600;">,</span>&nbsp;spriteHeight<span style="color: #bb6600;">)</span>&nbsp;<span style="color: #bb6600;">{</span></li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #880000;">// number of sprites per row in the spritesheet</span></li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #008888;">var</span>&nbsp;nbSpritesPerRow&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #aa0066;">Math</span><span style="color: #bb6600;">.</span>floor<span style="color: #bb6600;">(</span>spritesheet<span style="color: #bb6600;">.</span>width&nbsp;<span style="color: #bb6600;">/</span>&nbsp;spriteWidth<span style="color: #bb6600;">);</span></li>
<li></li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #880000;">// Extract each sprite</span></li>
<li><span style="color: #880000;">&nbsp; &nbsp; var startIndex = (postureToExtract -1) *&nbsp;</span><span style="line-height: 25.6px;">nbFramesPerPosture;</span></li>
<li><span style="line-height: 25.6px;">&nbsp; &nbsp; var endIndex = startIndex +&nbsp;</span><span style="line-height: 25.6px;">nbFramesPerPosture;</span></li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #008888;">for</span><span style="color: #bb6600;">(</span><span style="color: #008888;">var</span>&nbsp;index&nbsp;<span style="color: #bb6600;">=</span>&nbsp;</span><span style="color: #006666;" color="#006666">startIndex</span><span style="color: #bb6600;">;</span>&nbsp;index&nbsp;<span style="color: #bb6600;">&lt;</span>&nbsp;maxIndex<span style="color: #bb6600;">;</span>&nbsp;index<span style="color: #bb6600;">++)</span>&nbsp;<span style="color: #bb6600;">{</span></li>
<li>&nbsp; &nbsp; <span style="color: #880000;">// Computation of the x and y position that corresponds to the sprite</span></li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;<span style="color: #880000;">// index</span></li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;<span style="color: #880000;">// x is the rest of index/nbSpritesPerRow * width of a sprite</span></li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;<span style="color: #008888;">var</span>&nbsp;x&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #bb6600;">(</span>index&nbsp;<span style="color: #bb6600;">%</span>&nbsp;nbSpritesPerRow<span style="color: #bb6600;">)</span>&nbsp;<span style="color: #bb6600;">*</span>&nbsp;spriteWidth<span style="color: #bb6600;">;</span></li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;<span style="color: #880000;">// y is the divisor of index by nbSpritesPerRow * height of a sprite</span></li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;<span style="color: #008888;">var</span>&nbsp;y&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #aa0066;">Math</span><span style="color: #bb6600;">.</span>floor<span style="color: #bb6600;">(</span>index&nbsp;<span style="color: #bb6600;">/</span>&nbsp;nbSpritesPerRow<span style="color: #bb6600;">)</span>&nbsp;<span style="color: #bb6600;">*</span>&nbsp;spriteHeight<span style="color: #bb6600;">;</span></li>
<li></li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;<span style="color: #880000;">// build a spriteImage object</span></li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;<span style="color: #008888;">var</span>&nbsp;s&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #008888;">new</span>&nbsp;<span style="color: #aa0066;">SpriteImage</span><span style="color: #bb6600;">(</span>spritesheet<span style="color: #bb6600;">,</span>&nbsp;x<span style="color: #bb6600;">,</span>&nbsp;y<span style="color: #bb6600;">,</span>&nbsp;spriteWidth<span style="color: #bb6600;">,</span>&nbsp;spriteHeight<span style="color: #bb6600;">);</span></li>
<li></li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;<span style="color: #008888;">this</span><span style="color: #bb6600;">.</span>spriteArray<span style="color: #bb6600;">.</span>push<span style="color: #bb6600;">(</span>s<span style="color: #bb6600;">);</span></li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #bb6600;">}</span></li>
<li>&nbsp;&nbsp;<span style="color: #bb6600;">};</span></li>
<li></li>
<li>&nbsp;&nbsp;<span style="color: #008888;">this</span><span style="color: #bb6600;">.</span><span style="color: #008888;">then</span>&nbsp;<span style="color: #bb6600;">=</span>&nbsp;performance<span style="color: #bb6600;">.</span>now<span style="color: #bb6600;">();</span></li>
<li>&nbsp;&nbsp;<span style="color: #008888;">this</span><span style="color: #bb6600;">.</span>totalTimeSinceLastRedraw&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #006666;">0</span><span style="color: #bb6600;">;</span></li>
<li></li>
<li>&nbsp;&nbsp;<span style="color: #008888;">this</span><span style="color: #bb6600;">.</span>draw&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #008888;">function<span style="color: #bb6600;">(</span>ctx<span style="color: #bb6600;">,</span>&nbsp;x<span style="color: #bb6600;">,</span>&nbsp;y<span style="color: #bb6600;">)</span>&nbsp;<span style="color: #bb6600;">{</span></li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #880000;">// Use time based animation to draw only a few images per second</span></li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #008888;">var</span>&nbsp;now&nbsp;<span style="color: #bb6600;">=</span>&nbsp;performance<span style="color: #bb6600;">.</span>now<span style="color: #bb6600;">();</span></li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #008888;">var</span>&nbsp;delta&nbsp;<span style="color: #bb6600;">=</span>&nbsp;now&nbsp;<span style="color: #bb6600;">-</span>&nbsp;<span style="color: #008888;">this</span><span style="color: #bb6600;">.</span><span style="color: #008888;">then</span><span style="color: #bb6600;">;</span></li>
<li></li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #880000;">// Draw currentSpriteImage</span></li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #008888;">var</span>&nbsp;currentSpriteImage&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #008888;">this</span><span style="color: #bb6600;">.</span>spriteArray<span style="color: #bb6600;">[</span><span style="color: #008888;">this</span><span style="color: #bb6600;">.</span>currentFrame<span style="color: #bb6600;">];</span></li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #880000;">// x, y, scale. 1 = size unchanged</span></li>
<li>&nbsp; &nbsp; currentSpriteImage<span style="color: #bb6600;">.</span>draw<span style="color: #bb6600;">(</span>ctx<span style="color: #bb6600;">,</span>&nbsp;x<span style="color: #bb6600;">,</span>&nbsp;y<span style="color: #bb6600;">,</span>&nbsp;<span style="color: #006666;">1</span><span style="color: #bb6600;">);</span></li>
<li></li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #880000;">// if the delay between images is elapsed, go to the next one</span></li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #008888;">if</span>&nbsp;<span style="color: #bb6600;">(</span><span style="color: #008888;">this</span><span style="color: #bb6600;">.</span>totalTimeSinceLastRedraw&nbsp;<span style="color: #bb6600;">&gt;</span>&nbsp;<span style="color: #008888;">this</span><span style="color: #bb6600;">.</span>delayBetweenFrames<span style="color: #bb6600;">)</span>&nbsp;<span style="color: #bb6600;">{</span></li>
<li>&nbsp; &nbsp; <span style="color: #880000;">// Go to the next sprite image</span></li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;<span style="color: #008888;">this</span><span style="color: #bb6600;">.</span>currentFrame<span style="color: #bb6600;">++;</span></li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;<span style="color: #008888;">this</span><span style="color: #bb6600;">.</span>currentFrame&nbsp;<span style="color: #bb6600;">%=</span>&nbsp;<span style="color: #008888;">this</span><span style="color: #bb6600;">.</span>spriteArray<span style="color: #bb6600;">.</span>length<span style="color: #bb6600;">;</span></li>
<li></li>
<li>&nbsp; &nbsp; <span style="color: #880000;">// reset the total time since last image has been drawn</span></li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;<span style="color: #008888;">this</span><span style="color: #bb6600;">.</span>totalTimeSinceLastRedraw&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #006666;">0</span><span style="color: #bb6600;">;</span></li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #bb6600;">}</span>&nbsp;<span style="color: #008888;">else</span>&nbsp;<span style="color: #bb6600;">{</span></li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;<span style="color: #880000;">// sum the total time since last redraw</span></li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;<span style="color: #008888;">this</span><span style="color: #bb6600;">.</span>&nbsp;totalTimeSinceLastRedraw&nbsp;<span style="color: #bb6600;">+=</span>&nbsp;delta<span style="color: #bb6600;">;</span></li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #bb6600;">}</span></li>
<li></li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #008888;">this</span><span style="color: #bb6600;">.</span><span style="color: #008888;">then</span>&nbsp;<span style="color: #bb6600;">=</span>&nbsp;now<span style="color: #bb6600;">;</span></li>
<li>&nbsp;&nbsp;<span style="color: #bb6600;">};</span></li>
<li></li>
<li>&nbsp;&nbsp;<span style="color: #008888;">this</span><span style="color: #bb6600;">.</span>setNbImagesPerSecond&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #008888;">function</span><span style="color: #bb6600;">(</span>nb<span style="color: #bb6600;">)</span>&nbsp;<span style="color: #bb6600;">{</span></li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #880000;">// delay in ms between images</span></li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #008888;">this</span><span style="color: #bb6600;">.</span>delayBetweenFrames&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #006666;">1000</span>&nbsp;<span style="color: #bb6600;">/</span>&nbsp;nb<span style="color: #bb6600;">;</span></li>
<li>&nbsp;&nbsp;<span style="color: #bb6600;">};</span></li>
<li><span style="color: #bb6600;">}</span></li>
</ol></div><br>


#### Same example but with the walking woman sprite sheet

[Try this JsBin](http://jsbin.com/fekacu/edit?js,output)

[Local Demo](src/02f-example05.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
    onclick= "window.open('https://bit.ly/3wRtk01')"
    src    = "https://bit.ly/3j4TVT1"
    alt    = "Woman animated"
    title  = "Woman animated"
  />
</figure>


This time, we have changed the parameters of the sprites and sprite sheet. Now you can select the index of the posture to extract: the woman sprite sheet has 8 different postures, so you can call:

<div><ol>
<li value="1"> womanDown.extractSprites(spritesheet, NB_POSTURES, <strong style="color: red;">1</strong>, </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;NB_FRAMES_PER_POSTURE, </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;SPRITE_WIDTH, SPRITE_HEIGHT);</li>
<li>&nbsp;</li>
<li> womanDiagonalBottomLeft.extractSprites(spritesheet, NB_POSTURES, <strong style="color: red;">2</strong>, </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; NB_FRAMES_PER_POSTURE, </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; SPRITE_WIDTH, SPRITE_HEIGHT);</li>
<li>&nbsp;</li>
<li> womanLeft.extractSprites(spritesheet, NB_POSTURES, <strong style="color: red;">3</strong>, </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;NB_FRAMES_PER_POSTURE, </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;SPRITE_WIDTH, SPRITE_HEIGHT);</li>
<li>// etc...</li>
</ol></div><br>

#### Moving the sprites, stopping the sprites

[Example at JsBin](https://jsbin.com/muwoje/edit?js,output)

[Local Demo](src/02f-example06.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick= "window.open('https://bit.ly/3wRtk01')"
    src    = "https://bit.ly/3qnzPoA"
    alt    = "Woman moving left and right, jsbin screenshot"
    title  = "Woman moving left and right, jsbin screenshot"
  />
</figure>


As usual, we used key listeners, an `inputStates` global object, and this time we created 8 woman sprites, one for each direction.

Notice that we added a `drawStopped` method in the `Sprite` model in order to stop animating the woman when no key is pressed for moving her.


#### External resource

+ Game development tutorial (5 May 2020): [Draw images and sprite animations](https://bit.ly/2SlJek3)


#### Notes for 2.6.4 A small sprite animation framework

+ Example: sprite animation framework w/ walking robot
  + declare variable: `var robot;`
  + [init page after DOM ready](#init)
    + ...
    + [process after sprite sheet downloaded](#loadSpritesheet)
      + ...
      + create robot: `robot = new Sprite();`
      + extract sprite: `robot.extractSprites(spritesheet, NB_SPRITES, 1, NB_FRAMES_PER_POSTURE, SPRITE_WIDTH, SPRITE_HEIGHT);`
      + set frame rate: `robot.setNbImagesPerSecond(20);`
      + start frame: `requestAnimationFrame(mainloop);`
  + generate animation loop: `function mainloop() {...}`
    + clear canvas: `ctx.clearRect(0, 0, canvas.width, canvas.height);`
    + call self to draw robot: `robot.draw(ctx, 0, 0, 0);`
    + call next frame: `requestAnimationFrame(mainloop);`

+ `SpriteImage` class
  + declare class<a name="spriteImg"></a>: `function SpriteImage(img, x, y, width, height) {...}`
  + delcare properties: `this.img = img; this.x = x; this.y = y; this.width = width; this.height = height;`
  + declare draw method: `this.draw = function(ctx, xPos, yPos, scale) {ctx.drawImage(this.img, this.x, this.y, this.width, this.height, xPos, yPos, this.width*scale, this.height*scale);}`

+ `Sprite` class
  + an animated object
  + defined by an array of `SpriteImage` objects
  + a method for extracting all`SpriteImage` from a given sheet and filling the array
  + `draw` method: draw current `SpriteImage`
  + drawing multiple times involve an automatic change of the current `SpriteImage` being drawn
  + number of different images drawn per second: a parameter of the sprite
  + declare class<a name="sprite"></a>: `function Sprite() {...}`
    + declare properties: `this.spriteArray = []; this.currentFrame = 0; this.delayBetweenFrames = 10;`
    + declare extract method: `this.extractSprite = function(spritesheet, nbPosture, postureToExtract, nbFramesPerPosture, spriteWidth, spriteHeight) {...};`
      + compute number of sprites per row: `var nbSpritesPerRow = Math.floor(spritesheet.width / spriteWidth);`
      + compute the start and end indice: `var startIndex = (postureToExtract - 1)*nbFramesPerPosture; var endIndex = startIndex + nbFramesPerRow;`
      + iterate through the row: `for (var index=startIndex; index<maxIndex; index++) {...}`
      + compute x and y position: `var x = (index % nbSpritePerRow)*spriteWidth; var y = Math.floor(index/nbSpritePerRow) * spriteHeight;`
      + build a spriteImage object: `var s = new SpriteImage(spritesheet, x, y, spriteWidth, spriteHeight);`
      + put into array: `this.spriteArray.push(s);`
    + declare to stop draw<a name="stop"></a>: `this.drawStopped = function(ctx, x, y) { var currentSpriteImage = this.spriteArray[this.currentFrame]; currentSpriteImage(ctx, x, y,1); }`
    + declare time-related properties: `this.then = performance.now(); this.totalTimeSinceLastRedraw = 0;`
    + declare draw method<a name="draw"></a>: `this.draw = function(ctx, x, y) {...}`
      + set variables: `var now = performance.now(); var delta = now - this.then;`
      + draw current sprite image: `var currentSpriteImage = this.spriteArray(this.currentFrame); currentSpriteImage.draw(ctx, x, y, 1);`
      + check the time elapsed w/ delay: `if (this.totalTimeSinceLastRedraw > this.delayBetweenFrames) { // next sprite } else { // last redraw };`
        + move to next sprite: `this.currentFrame++; this.currentFrame %= this.spriteArray.length; this.totalTimeSinceLastRedraw = 0;`
        + increase delta time: `this.totalTimeSinceLastRedraw += delta;`
      + update the time: `this.then = now;`
    + declare method to set number of images per second: `this.setNbImagesPerSecond = function(nb) { this.delayBetweenFrames = 1000 / nb; };`


### 2.6.5 Adding sprites to the game framework

Let us use the animated woman example and take the sprite utility functions and some predefined values, such as the sprite sheet URL, the size of the sprites, the number of postures, etc., and add it all to one of the examples that used the game framework (the last one from the time based animation lesson (to keep things simple, we did not use the ones with gamepad, etc)).

First, try [this example](https://jsbin.com/mifeva/edit?js,console,output) at JsBin

[Local Demo](src/02f-example07.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick= "window.open('https://bit.ly/35QbiPO')"
    src    = "https://bit.ly/3xULb6l"
    alt    = "The woman sprite in the game framework, jsbin screenshot"
    title  = "The woman sprite in the game framework, jsbin screenshot"
  />
</figure>


#### How to add sprites to the game framework...

1. We declare a `woman` object, similar to the `monster` object, with `x`, `y`, `speed`, `width` properties. We add a `direction` property that corresponds to a posture's index (so direction = 2 corresponds to the sprite animation for the woman moving to the left, whereas direction = 6 corresponds to the posture of the woman moving to the right...)
2. We add the `Sprite` and `SpriteImage` objects to the game framework,
3. We write a `loadAssets(callback)` function which: a) loads the sprite sheet, b) extracts all the woman sprites and builds the `womanSprites` array, and c) calls the `callback` function passed as a parameter once finished,
4. We call the `loadAssets` function from the game framework `start` function, and we start the animation loop only when the `loadAssets` function has completed loading and extracting the sprites. In a real game the `loadAssets` function would also load the sounds, and perhaps other sprite sheets or resources etc. In this function, you could use the `BufferLoader` utility for loading multiple resources asynchronously, as  discussed during Module 1.

Source code extract:

<div><ol>
<li value="1">// Inits</li>
<li>window.onload = function init() {</li>
<li> var game = new GF();</li>
<li> game.start();</li>
<li>};</li>
<li>&nbsp;</li>
<li>// GAME FRAMEWORK STARTS HERE</li>
<li>var GF = function(){</li>
<li>&nbsp; &nbsp;...</li>
<li>&nbsp; &nbsp;// Woman object and sprites</li>
<li>&nbsp; &nbsp;// sprite index corresponding to posture</li>
<li>&nbsp; &nbsp;var WOMAN_DIR_RIGHT = 6;</li>
<li>&nbsp; &nbsp;var WOMAN_DIR_LEFT = 2;</li>
<li>&nbsp; &nbsp;var woman = {</li>
<li>&nbsp; &nbsp; &nbsp; x:100,</li>
<li>&nbsp; &nbsp; &nbsp; y:200,</li>
<li>&nbsp; &nbsp; &nbsp; width:48,</li>
<li>&nbsp; &nbsp; &nbsp; speed:100, // pixels/s this time!</li>
<li>&nbsp; &nbsp; &nbsp; direction: WOMAN_DIR_RIGHT </li>
<li>&nbsp; &nbsp;};</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;var womanSprites = [];</li>
<li>&nbsp;</li>
<li><strong style="color: red;">&nbsp; &nbsp;var mainLoop = function(time){</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp;... </strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp;// Draw a woman moving left and right</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; womanSprites[woman.direction].draw(ctx, woman.x, woman.y);</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; updateWomanPosition(delta);</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; ...</strong></li>
<li><strong style="color: red;">&nbsp;&nbsp;};</strong></li>
<li> </li>
<li>&nbsp;&nbsp;function updateWomanPosition(delta) {</li>
<li>&nbsp; &nbsp; // check collision on left or right</li>
<li>&nbsp; &nbsp;&nbsp;if(((woman.x+woman.width) &gt; canvas.width) || (woman.x &lt; 0)) {</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;// inverse speed</li>
<li>&nbsp; &nbsp; &nbsp; woman.speed = -woman.speed;</li>
<li>&nbsp; &nbsp;&nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp;&nbsp;// change sprite direction</li>
<li>&nbsp; &nbsp;&nbsp;if(woman.speed &gt;= 0) {</li>
<li>&nbsp; &nbsp; &nbsp; woman.direction = WOMAN_DIR_RIGHT;</li>
<li>&nbsp; &nbsp;&nbsp;} else {</li>
<li>&nbsp; &nbsp; &nbsp; woman.direction = WOMAN_DIR_LEFT;</li>
<li>&nbsp; &nbsp;&nbsp;}</li>
<li>&nbsp; &nbsp; woman.x += calcDistanceToMove(delta, woman.speed);</li>
<li>&nbsp;&nbsp;}</li>
<li>&nbsp;</li>
<li>&nbsp;&nbsp;/*---------------------------------------*/</li>
<li>&nbsp; /* SPRITE UTILITY FUNCTIONS &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;*/</li>
<li>&nbsp;&nbsp;/*---------------------------------------*/</li>
<li>&nbsp;&nbsp;function SpriteImage(img, x, y, width, height) {</li>
<li>&nbsp; &nbsp;&nbsp;...</li>
<li>&nbsp; &nbsp;&nbsp;this.draw = function(ctx, xPos, yPos, scale) {...};</li>
<li>&nbsp; }</li>
<li>&nbsp;</li>
<li>&nbsp; function Sprite() {</li>
<li>&nbsp; &nbsp;&nbsp;...</li>
<li>&nbsp; &nbsp;&nbsp;this.extractSprites = function(...) {...}; </li>
<li>&nbsp; &nbsp;&nbsp;this.drawStopped = function(ctx, x, y) {...}; </li>
<li>&nbsp; &nbsp;&nbsp;this.draw = function(ctx, x, y) {...}; </li>
<li>&nbsp; &nbsp;&nbsp;this.setNbImagesPerSecond = function(nb) {...};</li>
<li>&nbsp; }</li>
<li>&nbsp;&nbsp;/*---------------------------------------*/</li>
<li>&nbsp;&nbsp;/* EN OF SPRITE UTILITY FUNCTIONS &nbsp; &nbsp; &nbsp; &nbsp;*/</li>
<li>&nbsp;&nbsp;/*---------------------------------------*/</li>
<li> </li>
<li> var loadAssets = function(callback) {</li>
<li>&nbsp; &nbsp;&nbsp;var SPRITESHEET_URL = "https://i.imgur.com/3VesWqx.png";</li>
<li>&nbsp; &nbsp;&nbsp;var SPRITE_WIDTH = 48;</li>
<li>&nbsp; &nbsp;&nbsp;var SPRITE_HEIGHT = 92;</li>
<li>&nbsp; &nbsp;&nbsp;var NB_POSTURES=8;</li>
<li>&nbsp; &nbsp; var NB_FRAMES_PER_POSTURE = 13;</li>
<li> </li>
<li>&nbsp; &nbsp;&nbsp;// load the spritesheet</li>
<li>&nbsp; &nbsp;&nbsp;var spritesheet = new Image();</li>
<li>&nbsp; &nbsp; spritesheet.src = SPRITESHEET_URL; </li>
<li> </li>
<li>&nbsp; &nbsp;&nbsp;// Called when the spritesheet has been loaded</li>
<li>&nbsp; &nbsp; spritesheet.onload = function() {</li>
<li>&nbsp; &nbsp; &nbsp; // Create woman sprites</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;for(var i = 0; i &lt; NB_POSTURES; i++) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;var sprite = new Sprite();</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; sprite.extractSprites(spritesheet, NB_POSTURES, (i+1), </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; NB_FRAMES_PER_POSTURE, </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; SPRITE_WIDTH, SPRITE_HEIGHT);</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; sprite.setNbImagesPerSecond(20);</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; womanSprites[i] = sprite;</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;}</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;// call the callback function passed as a parameter, </li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;// we're done with loading assets and building the sprites</li>
<li>&nbsp; &nbsp; &nbsp; callback();</li>
<li>&nbsp; &nbsp;&nbsp;};</li>
<li>&nbsp;&nbsp;};</li>
<li> </li>
<li>&nbsp;&nbsp;var start = function(){</li>
<li>&nbsp; &nbsp;&nbsp;...</li>
<li>&nbsp; &nbsp;&nbsp;<strong style="color: red;">// Load sounds and images, then when this is done, start the mainLoop</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; loadAssets(function() {</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp; &nbsp;// We enter here only when all assets have been loaded</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp; &nbsp;requestAnimationFrame(mainLoop);</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp;&nbsp;});</strong></li>
<li>&nbsp;&nbsp;};</li>
<li>&nbsp;&nbsp;...</li>
<li>&nbsp;};</li>
<li>&nbsp;</li>
</ol></div><br>


#### Notes for 2.6.5 Adding sprites to the game framework

+ Adding sprites to game framework - walking woman
  + declare a `woman` object w/ `x`, `y`, `speed`, `width` and `direction` properties, where `direction` corresponding to a posture's index
  + add the `Sprite` and `SpriteImage` objects to the game framework
  + create a `loadAssets(callback)` function
    + loading the sprite sheet
    + extracting all the woman sprites and building the `womanSprites` array
    + calling the `callback` function passed as a parameter once finished
  + call the `loadAssets` function from the game framework `start` function
    + start the animation loop only when the `loadAssets` function completed loading and extract the sprites
    + real game: `loadAssets` function probably loading the sounds, sprite sheets or resources, etc.
    + using the `BufferLoader` utility for loading multiple resources asynchronously

+ Example: game framework w/ sprites - Init Page
  + init page after DOM ready: `window.onload = function init() {...}`
  + create game framework: `var game = new GF();`
  + call self to start game: `game.start();`

+ Example: Game framework class w/ sprites - GF class
  + declare game framework: `var GF = function() {...}`
  + ...
  + declare variables for sprite directions: `var WOMAN_DIR_RIGHT = 6; var WOMAN_DIR_LEFT = 2;`
  + declare woman object: `var woman = {x: 10, y: 200, width: 48, speed: 100, direction: WOMAN_DIR_RIGHT};`
  + declare array for sprites: `var womanSprites = [];`
  + geneate animation loop: `var mainLoop = function(time) {...}`
    + ...
    + draw woman left or right: `womanSprites[woman.direction].draw(ctx, woman.x, woman.y); updateWomanPosition(delta);`
    + ...
  + declare to update woman position: `function updateWomanPosition(delta) {...}`
    + check collision on both sides: `if (((woman.x+woman.width) > canvas.width) || (woman.x <0)) { woman.speed = -woman.speed; }`
    + change direction: `if (woman.speed >= 0) { woman.direction = WOMAN_DIR_RIGHT; } else { woman.direction = WOMAN_DIR_LEFT; }`
    + update position: `woman.x += calcDistanceToMove(delta, woman.speed);`
  + declare [Sprite class](#sprite)
  + declare to load assets: `var loadAssets = function(callback) {...}`
    + declare spritesheet variables: `var SPRITESHEET_URL = "https://i.imgur.com/3VesWqx.png"; var SPRITE_WIDTH = 48; var SPRITE_HEIGHT = 92; var NB_POSTURES = 8; var NB_FRAMES_PER_POSTURE = 13;`
    + load spritesheet: `var spritesheet = new image(); spritesheet.src = SPRITESHEET_URL;`
    + create sprites after spritesheet loaded: `spritesheet.onload = function() {...}`
      + iterate through all postures: `for (var i=0; i<NB_POSTURES; i++) {...}`
        + create sprite: `var sprite = new Sprite();`
        + extract sprite: `sprite.extractSprites(spritesheet, NB_POSTURES, (i+1), NB_FRAMES_PER_POSTURE, SPRITE_WIDTH, SPRITE_HEIGHT);`
        + set frame rate: `sprite.setNbImagesPerSecond(20);`
        + store created sprite into array: `womanSprites[i] = sprite;`
      + call the callback function passed as a parameter: `callback();`
  + declare start method: `var start = function() {...}`
    + ...
    + call to load assets and start animation: `loadAssets(function() { requestAnimationFrame(mainLoop); });`


### 2.6.6 Discussion and projects

Here is the discussion forum for this part of the course. Please either post your comments/observations/questions or share your creations.


#### Suggested topics of discussion:

+ The sprite framework that we have developed during this course can be greatly improved to support other types of sprite sheets or alphabet sprite sheets for writing text made of sprites. If you improve the given code, please share!
+ Please share some nice demos of your own with more sprite sheet examples found on the Web!
+ If you find any good tools or tutorials for creating sprite sheets, please share!


#### Optional projects:

+ Try to improve the last example presented in the course with the woman moving in all directions.
+ Here is a complete set of sprite sheets for the robot postures. Try to make a nice demo that uses all the postures! An [archive of robot sprites](https://bit.ly/35MVVaV) is available for download.




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






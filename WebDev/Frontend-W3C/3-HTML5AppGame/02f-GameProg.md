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
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3gQmAIU')"
    src    = "https://bit.ly/3gKIVsy"
    alt    = "sprite sheet of a woman walking, with different postures"
    title  = "sprite sheet of a woman walking, with different postures"
  />
</figure>


The first line corresponds to the direction we called "south", the second "south west", the third "west", etc. The 8 lines cover movement in all eight cardinal directions.

Each line is composed of 13 small images which together comprise an "animated" sprite. If we draw each of the 13 animations of the first line, in turn; we will see a woman who seems to move towards the screen. And if we draw each sprite a little closer to the bottom of the screen, we obtain a woman who appears to approach the bottom of the screen, swinging her arms and legs, as she walks!

Try it yourself: here is a [quick and dirty example](https://jsbin.com/jokodod/edit?html,js,console,output) to try at JSBin working with the above sprite sheet.  Use the arrow keys and take a look! We accentuated the movement by changing the scale of the sprite as the woman moves up (further from us) or down (closer to us).

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3gQmAIU')"
    src    = "https://bit.ly/3gOqcMP"
    alt    = "A woman animated using sprite. Screenshot of the JsBin example that explain how to run it in standalone mode"
    title  = "A woman animated using sprite. Screenshot of the JsBin example that explain how to run it in standalone mode"
  />
</figure>


We have not yet investigated how this works, nor have we built it into the small game engine we started to build in earlier chapters. First, let's explain how to use "sprites" in JavaScript and canvas.





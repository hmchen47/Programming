# Module 3: Playing with HTML5 APIs

## 3.5 Playing sound samples and music

### 3.5.1 Background music (streamed)

__Warning about the autoplay policy__

Since 2018, most browsers have adopted [the Autoplay Policy that prevents any Web page to start making music or playing sounds without a user interaction](https://developers.google.com/web/updates/2017/09/autoplay-policy-changes).

For a user, it means that most examples from this course won't make sounds until you interact with the application (i.e. clicking on the canvas for the game example). For a developer, if you use libraries such as Howler.js, there are good chances that you won't have to change your code. If you are programming with [the WebAudio API](https://www.w3.org/TR/webaudio/), then you'll need to resume the AudioContext after the first user interaction. 


#### Background music (streamed)

In a previous section, we saw how we can add music to our Web page, using the `<audio></audio>` element. We can even hide its GUI and control the play/pause of the music from JavaScript. Streaming music is perfect for providing a background atmosphere in a video game.

Here is one simple example of background music control from JavaScript:

[CodePen Demo](https://codepen.io/w3devcampus/pen/ZeNpyx)

[Local Demo](src/03e-example01.html)


#### Notes for 3.5.1 Background music (streamed)

+ Background music
  + using `WebAudio` API
  + audio element: `<audio src = "https://.../humbug.mp3"  id="audioPlayer"  controls> </audio>`
  + playing music: `function play() {...}`
    + access element: `var player = document.querySelector("#audioPlayer");`
    + play streamed music: `player.play();`
  + pausing music: `function pause() {...}`
    + access element: `var player = document.querySelector("#audioPlayer");`
    + paus playing: `player.pause();`


### 3.5.2 Sound effects using howler.js

#### Live coding video: using sound samples

<a href="https://edx-video.net/W3CJSIXX2016-V003500_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/3h4yssk3)

#### Howler.js for using sound samples in memory

If you want to play short sounds that can occur very rapidly, streamed sound/music is not a good solution. This is where the WebAudio API, made by W3C and implemented by your browser, comes in handy. This API allows you to download and decode sound samples in memory, and play them on demand, using nearly zero CPU and with no delay when you play the sound (no buffering etc.).

However, this API is a bit complicated to use for beginners. Fortunately there are several JavaScript libraries that simplify the use of the WebAudio API. [HowlerJS is one of these.](https://howlerjs.com/)

__Example that uses Howler.js to load a sound sample from a remote server, then decode it in memory, and play it:__

[CodePen Demo](https://codepen.io/w3devcampus/pen/ZeNpEX)

[Local Demo](src/03e-example02.html)

HTML code: this is how we say that we are using an external library:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&nbsp;&nbsp; &lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&nbsp;&nbsp; </span><span class="tag">&nbsp;&nbsp; </span><span class="tag">&lt;script</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://cdnjs.cloudflare.com/ajax/libs/howler/1.1.28/howler.min.js"</span><span class="tag">&gt;&lt;/script&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&nbsp;&nbsp; </span><span class="tag">&nbsp;&nbsp; </span><span class="tag">&lt;title&gt;</span><span class="pln">Simple example that uses howler.js for playing sound samples</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <span class="pln"></span><span class="pln"></span><span class="tag"></span><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">&gt;</span></span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&nbsp;&nbsp; </span><span class="tag">&lt;/head&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&nbsp;&nbsp; </span><span class="tag">&lt;body&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&nbsp;&nbsp; </span><span class="tag">&nbsp;&nbsp; </span><span class="tag">&lt;p&gt;</span><span class="pln">Turn volume 1. As soon as the button becomes enabled, that means that the sound sample</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> has been downloaded and decoded in memory. It can now be played. Click on the button to play</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> this sound. Click it rapidly: you see, it's ok for a game!</span><span class="tag">&lt;/p&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="tag">&nbsp;&nbsp; </span><span class="tag">&nbsp;&nbsp; </span><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">playSound</span><span class="pun">();</span><span class="atv">"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"button1"</span><span class="pln"> </span><span class="atn">disabled</span><span class="tag">&gt;</span><span class="pln">Play sound sample 1</span><span class="tag">&lt;/button&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&nbsp;&nbsp; </span><span class="tag">&lt;/body&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>

+ _Lines 3-5_ indicate that in our example we are using an external library.
+ _Line 12_ declares a button, that is greyed by default and cannot be clicked. This is done by the disabled=true attribute.

JavaScript code:

<div class="source-code" style="padding-left: 30px; padding-right: 30px; border: 1px solid black;"><ol class="linenums" style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">window</span><span class="pun" style="color: #666600;">.</span><span class="pln">onload&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;init</span><span class="pun" style="color: #666600;">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd" style="color: #AA0088;">var</span><span class="pln">&nbsp;sound</span><span class="pun" style="color: #666600;">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd" style="color: #AA0088;">function</span><span class="pln">&nbsp;init</span><span class="pun" style="color: #666600;">()</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd" style="color: #AA0088;">&nbsp; &nbsp; var</span><span class="pln">&nbsp;button&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;document</span><span class="pun" style="color: #666600;">.</span><span class="pln">querySelector</span><span class="pun" style="color: #666600;">(</span><span class="str" style="color: #008800;">"#button1"</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;<strong>sound&nbsp;</strong></span><strong><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #AA0088;">new</span><span class="pln">&nbsp;</span><span class="typ" style="color: #660066;">Howl</span><span class="pun" style="color: #666600;">({</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; urls</span><span class="pun" style="color: #666600;">:</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">[ &nbsp;&nbsp;</span><span class="str" style="color: #008800;">'https://.../assets/sounds/plop.mp3'</span><span class="pun" style="color: #666600;">],</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; onload</span><span class="pun" style="color: #666600;">:</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #AA0088;">function</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">()</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">{</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; console</span><span class="pun" style="color: #666600;">.</span><span class="pln">log</span><span class="pun" style="color: #666600;">(</span><span class="str" style="color: #008800;">"Loaded asset "</span><span class="pun" style="color: #666600;">);</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; button</span><span class="pun" style="color: #666600;">.</span><span class="pln">disabled&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #AA0088;">false</span><span class="pun" style="color: #666600;">;</span><span class="pln">&nbsp;</span><span class="com" style="color: #880000;">// enable the play sound button</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="pun" style="color: #666600;">&nbsp; &nbsp; &nbsp; &nbsp; }</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="pun" style="color: #666600;">&nbsp; &nbsp; });</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="kwd" style="color: #AA0088;">function</span><span class="pln">&nbsp;playSound</span><span class="pun" style="color: #666600;">()</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; sound</span><span class="pun" style="color: #666600;">.</span><span class="pln">play</span><span class="pun" style="color: #666600;">();</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;">}</span></li>
</ol></div>

The important part is located in lines 8-12: the Howler library is to be used like this: `sound = new Howl({...});` The part between the { and } is an object. The `url's` property is an array with at least one element: the URL of the sound we want to use, located on remote servers. The call to new Howl({...}); will start downloading the sound in background, then, once it has loaded, it will "decode it" (i.e., an mp3 file will use some cpu to be decoded on the fly and played, whereas a decoded sound will use nearly zero cpu, which makes it good for games!).

Finally, once the sound is decoded, the `onload` callback is executed. In other words, the function after `onload`: will be executed (at _lines 10-12_). In this callback, we enable the button because the sound is ready to be played.

The `playSound` function can only be called when the button is enabled (when the sound sample has been loaded and decoded). In order to play a sound loaded by Howler.JS, we just call the `play()` method (_line 18_).


#### Notes for 3.5.2 Sound effects using howler.js

+ Sound effect w/ howler.js
  + streamed audio not suitable for short sounds
  + WebAudio API:
    + allowing to download and decode sound samples in memory and play them on demand
    + using nearly zero CPU and w/o delay when playing (no buffering)
    + complicated to use for this purpose
  + [howler.js](https://howlerjs.com/) simplifying the use of the WebAudio API
  + example: [sound sample w/ howler.js](src/03e-example02.html)
    + howler.js library: `<script src="https://cdnjs.cloudflare.com/ajax/libs/howler/1.1.28/howler.min.js"></script>`
    + button element to trigger sound effect: `<button onclick="playSound();" id="button1" disabled>Play sound sample 1</button>`
    + init setting after the DOM ready: `function init() {...}`
      + access button element: `var button = document.querySelector("#button1");`
      + create object, start downloading the sound in background, and decode it:

        ```js
        sound = new Howl({
            urls: ['https://.../assets/sounds/plop.mp3'],
            onload: function () {
                console.log("Loaded asset ");
                button.disabled = false; // enable the play sound button
            }
        });
        ```

    + play sound: `function playSound() { sound.play(); }`


### 3.5.3 Adding music and sound effects

Here is the last version of the game from Module 2 with music and sound effects (when the player eats a ball):

[CodePen Demo](https://codepen.io/w3devcampus/pen/EWzgpr)

[local Demo](src/03e-example03.html)

Look at the HTML part: we included the Howler.js library and we also added an `<audio>` player (invisible; we removed the `controls` attribute) for background music.

In the JavaScript code, we start the background music as soon as the page is loaded.

We then used HowlerJS to load a sound sample in background. Only once this sample has been loaded and decoded do we start the animation.


#### Notes for 3.5.3 Adding music and sound effects

+ Example: [adding music amd sound effects for bouncing ball game](src/03e-example03.html)
  + refer to [bouncing ball game](src/02f-example13.html)
  + most JS code remained the same as the previous example
  + global variable: `let ballEatenSound;`
  + audio element: `<audio src = "https://.../sounds/humbug.mp3" id="audioPlayer"> </audio>`
  + init the game after the DOM ready: `window.onload = function init() {...}`
    + start playing the background music as soon as the page loaded: `playBackgroundMusic();`
    + load the sound and start the game only when the sound has been loaded

      ```js
      ballEatenSound = new Howl({
          urls: ['https://.../sounds/plop.mp3'],
          onload: function () { // start the animation
            mainLoop();
          }
      });
      ```

  + play background music: `function playBackgroundMusic() {...}`
    + access sound element: `let audioPlayer = document.querySelector("#audioPlayer");`
    + play music: `audioPlayer.play();`
  + pause background music: `function pausebackgroundMusic() {...}`
    + access sound element: `let audioPlayer = document.querySelector("#audioPlayer");`
    + pause music: `audioPlayer.pause();`
  + collision detection w/ player: `function testCollisionWithPlayer(b, index) {...}`
    + play a sound: `ballEatenSound.play();`


### 3.5.4 [Advanced] a multiple image, sound and music loader

#### Live coding video: a multiple image, sound and music loader

<a href="https://edx-video.net/W3CJSIXX2016-V003600_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/18yk2t33)


#### A utility background loader for images, music and sound samples

This comes from the module 2 of the W3Cx [HTML5 Apps and Games](https://www.edx.org/course/html5-apps-and-games) course.

In video games, you very often need to load assets before starting the game:

+ Images must be loaded (background image, game logo, sprite sheets, etc.)
+ Sound samples must be loaded and decoded (the previous example used only one single sound sample, but with multiple samples it becomes more difficult to know when they are all ready to be used, as they come asynchronously over the network),
+ For streamed music, you need an `<audio>` player element. If you use different pieces of music, you may use multiple audio elements, and you pause one and start another when you change the music. Alternatively you may use a single audio element, and change its `src` attribute.

So, we wrote a multiple "asset loader" to make all these tasks easy.

Here is a small example that you may use if you like, which takes an array of "assets to be loaded", that can be either an image, a sound sample or streamed background music. You call the `loadAssets(callback)` function, passing as a parameter a single callback function of yours. When all assets are loaded, your callback will be executed, and will get a single parameter: the assets ready to be used!

Example (to hear the music and sound sample, there are two lines to uncomment in the `startGame(...)` function):

[CodePen Demo](https://codepen.io/w3devcampus/pen/QpRGrz)

[Local Demo](src/03e-example04.html)

Extract from the JavaScript source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">window</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> init</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> assetsToLoadURLs </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; backgroundImage</span><span class="pun">:</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> url</span><span class="pun">:</span><span class="pln"> </span><span class="str">'https://.../assets/images/background.png'</span><span class="pln"> </span><span class="pun">},</span><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; logo1</span><span class="pun">:</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> url</span><span class="pun">:</span><span class="pln"> </span><span class="str">"https://.../assets/images/SkywardWithoutBalls.png"</span><span class="pln"> </span><span class="pun">},</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; logo2</span><span class="pun">:</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> url</span><span class="pun">:</span><span class="pln"> </span><span class="str">"https://.../assets/images/BoundsWithoutBalls.png"</span><span class="pln"> </span><span class="pun">},</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; bell</span><span class="pun">:</span><span class="pln">&nbsp;&nbsp;</span><span class="pun">{</span><span class="pln"> url</span><span class="pun">:</span><span class="pln"> </span><span class="str">"https://.../assets/images/bells.png"</span><span class="pln"> </span><span class="pun">},</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; spriteSheetBunny</span><span class="pun">:</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> url</span><span class="pun">:</span><span class="pln"> </span><span class="str">'https://.../assets/images/bunnySpriteSheet.png'</span><span class="pln"> </span><span class="pun">},</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; plop</span><span class="pun">:</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> url</span><span class="pun">:</span><span class="pln"> </span><span class="str">'https://.../assets/sounds/plop.mp3'</span><span class="pun">,</span><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; buffer</span><span class="pun">:</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">,<span style="color: #000000;" color="#000000">&nbsp;</span></span>loop<span class="pun">:</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">,</span><span class="pln"> volume</span><span class="pun">:</span><span class="pln"> </span><span class="lit">1.0</span><span class="pln"> </span><span class="pun">},</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; humbug</span><span class="pun">:</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> url</span><span class="pun">:</span><span class="pln"> </span><span class="str">'https://.../assets/sounds/humbug.mp3'</span><span class="pun">,</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; buffer</span><span class="pun">:</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">,</span><span class="pln"> loop</span><span class="pun">:</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">,</span><span class="pln"> volume</span><span class="pun">:</span><span class="pln"> </span><span class="lit">1.0</span><span class="pln"> </span><span class="pun">},</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; concertino</span><span class="pun">:</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> url</span><span class="pun">:</span><span class="pln"> </span><span class="str">'https://.../assets/sounds/christmas_concertino.mp3'</span><span class="pun">,</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; buffer</span><span class="pun">:</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">,</span><span class="pln"> loop</span><span class="pun">:</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">,</span><span class="pln"> volume</span><span class="pun">:</span><span class="pln"> </span><span class="lit">1.0</span><span class="pln"> </span><span class="pun">},</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; xmas</span><span class="pun">:</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> url</span><span class="pun">:</span><span class="pln"> </span><span class="str">'https://.../assets/sounds/xmas.mp3'</span><span class="pun">,</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; buffer</span><span class="pun">:</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">,</span><span class="pln"> loop</span><span class="pun">:</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">,</span><span class="pln"> volume</span><span class="pun">:</span><span class="pln"> </span><span class="lit">0.6</span><span class="pln"> </span><span class="pun">}</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">};</span></li>
</ol><ol class="linenums">
<li class="L5" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> loadedAssets</span><span class="pun">; // above assets, ready to be used</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> init</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; // Once the page is loaded, we load all assets. We pass the function</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; // that will be called when assets are ready. In our case "startGame"</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // this call will load all assets</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; loadAssets</span><span class="pun">(</span><span class="pln">startGame</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> startGame</span><span class="pun">(</span><span class="pln">assetsReadyToBeUsed</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; // This function is executed once all assets are ready.</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; // It is called by the asset loader, and receives as a unique</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; // parameter, the assets (sounds, images etc.) ready to be used</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; // we store them in the loadedAssets variable</span></li>
<li class="L3" style="margin-bottom: 0px;"><span style="color: #880000;" color="#880000">&nbsp; &nbsp;&nbsp;</span>loadedAssets <span class="pun">=</span><span class="pln"> assetsReadyToBeUsed</span><span class="pun">;</span><br><span class="pln"></span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // Now we can use them! e.g., draw the images in a canvas</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; drawImages</span><span class="pun">();</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp;// or play one of the pieces of background music</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;playHumbug</span><span class="pun">();</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp;// Or use sound samples, for example let's play a plop every second</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;setInterval</span><span class="pun">(</span><span class="pln">playPlop</span><span class="pun">,</span><span class="pln"> </span><span class="lit">1000</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> playHumbug</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; loadedAssets</span><span class="pun">.</span><span class="pln">humbug</span><span class="pun">.</span><span class="pln">play</span><span class="pun">();</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> playPlop</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; loadedAssets</span><span class="pun">.</span><span class="pln">plop</span><span class="pun">.</span><span class="pln">play</span><span class="pun">();</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> drawImages</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; var</span><span class="pln"> canvas </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'#myCanvas'</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; var</span><span class="pln"> ctx </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">getContext</span><span class="pun">(</span><span class="str">'2d'</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // background image drawImage can have different syntaxes : </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; // drawImage(img, x, y); or</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // drawImage(x, y, width, height), </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; // for other syntaxes see HTML5 fundamentals course</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">drawImage</span><span class="pun">(</span><span class="pln">loadedAssets</span><span class="pun">.</span><span class="pln">backgroundImage</span><span class="pun">,</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="lit">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0<span style="color: #666600;" color="#666600">,</span></span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; canvas</span><span class="pun">.</span><span class="pln">width</span><span class="pun">,</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">height</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">drawImage</span><span class="pun">(</span><span class="pln">loadedAssets</span><span class="pun">.</span><span class="pln">bell</span><span class="pun">,</span><span class="pln"> </span><span class="lit">20</span><span class="pun">,</span><span class="pln"> </span><span class="lit">20</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">drawImage</span><span class="pun">(</span><span class="pln">loadedAssets</span><span class="pun">.</span><span class="pln">spriteSheetBunny</span><span class="pun">,</span><span class="pln"> </span><span class="lit">190</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>


__Two games that have been written by students from the HTML5 advanced MOOC (which has a module dedicated to game programming):__

These games are not for JavaScript beginners, but it's time to spend some time having fun :-) You can look at the source code: it's been written by students like you who followed the HTML5 advanced course.

1 - Star Warriors, written by two Ukrainian ladies who won the first prize in [a W3C contest we organized in March 2017](https://www.w3.org/2017/WWW26/contests.html):

+ [Play it online](https://mainline.i3s.unice.fr/mooc/StarWarriors/), wait until all assets have been loaded (you can follow the loading of assets by opening the devtools console). Use arrows + space bar to fire.
+ [See the source code on CodePen](https://codepen.io/w3devcampus/pen/pemjRj) (also, you can play from there).

[CodePen Demo](https://codepen.io/w3devcampus/pen/pemjRj)

[Local Demo](src/03e-example05.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/otpo7jp7')"
    src    ="https://tinyurl.com/p94pa4t6"
    alt    ="Star Warrior, an HTML5 games that uses the multiple asset loader"
    title  ="Star Warrior, an HTML5 games that uses the multiple asset loader"
  />
</figure>

2 - Skyward Bounds: written in less than a week by a group of students from the W3Cx HTML5 Apps and Games course W3Cx, during the Christmas 2016 session.

Michel Buffa helped them actively in the forum, and one student rapidly took the lead in developing the game, while another composed the music, another helped with the graphics, etc.

The game runs on phones, tablets (using touch events), can be resized, rotated, etc. It also uses the multiple asset loader presented.

+ [Play it online](https://mainline.i3s.unice.fr/mooc/SkywardBound/) (mouse or fingers)
+ Or [download the source code](https://tinyurl.com/1dl608s3) (multiple files). (once unzipped, just double click index.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/otpo7jp7')"
    src    ="https://tinyurl.com/5ezejsem"
    alt    ="Skyward Bouds, a HTML5 game written by students, who uses the same asset loader"
    title  ="Skyward Bouds, a HTML5 game written by students, who uses the same asset loader"
  />
</figure>

#### Notes for 3.5.4 [Advanced] a multiple image, sound and music loader

+ Background loader
  + video games usually required to load assets before starting the game
  + assets
    + images: background image, game logo, sprite sheets, etc
    + sound samples: loaded and decoded
    + streamed music w/ `<audio>` element
      + multiple samples elements probably required
      + pause one and start another when changig music
  + alternatively, change `src` attribute

+ Example: [asset loader](src/03e-example04.html)
  + container to display images: `<canvas id="myCanvas" width=400 height=400></canvas>`
  + list of assets:

    ```js
    var assetsToLoadURLs = {
      backgroundImage: { url: 'https://.../assets/images/background.png' }, 
      logo1: { url: "https://.../assets/images/SkywardWithoutBalls.png" },
      logo2: { url: "https://.../assets/images/BoundsWithoutBalls.png" },
      bell:  { url: "https://.../assets/images/bells.png" },
      spriteSheetBunny: { url: 'https://.../assets/images/bunnySpriteSheet.png' },
      plop: { url: 'https://.../assets/sounds/plop.mp3', 
        buffer: false, loop: false, volume: 1.0 },
      humbug: { url: 'https://.../assets/sounds/humbug.mp3', 
        buffer: true, loop: true, volume: 1.0 },
      concertino: { url: 'https://.../assets/sounds/christmas_concertino.mp3', 
        buffer: true, loop: true, volume: 1.0 },
      xmas: { url: 'https://.../assets/sounds/xmas.mp3', 
        buffer: true, loop: true, volume: 0.6 }
    }
    ```

  + global variable for loaded assets: `var loadedAssets;`
  + the DOM ready and then load assets: `function init() { loadAssets(startGame); }`
  + load all assets: `function loadAssets(callback) { loadAssetsUsingHowlerAndNoXhr(assetsToLoadURLs, callback); }`
  + load assets and decoded w/ howler & NoXhr (setails see the JS code): `loadAssetsUsingHowlerAndNoXhr(assetsToLoadURLs, callback);`
  + start the game once assets loaded: `function startGame(assetsReadyToBeUsed) {...}`
    + draw images in canvas: `drawImages();`
    + play background music: `playHumbug();` $\to$ `loadedAssets.humbug.play();`
    + play plop every second: `setInterval(playPlop, 1000);`
  + drawing all images in canvas: `function drawImages() {...}`
    + access canvas element: `var canvas = document.querySelector('#myCanvas');`
    + create 2d object: `var ctx = canvas.getContext('2d');`
    + draw images: `ctx.drawImage(loadedAssets.backgroundImage, 0, 0, canvas.width, canvas.height); ctx.drawImage(loadedAssets.bell, 20, 20); ctx.drawImage(loadedAssets.spriteSheetBunny, 190, 0);`

### 3.5.5 Discussion and projects

Here is the discussion forum for this part of the course. Please either post your comments/observations/questions or share your creations.

#### Suggested topics

+ Who amongst you is a composer? Would you propose free music or free sound samples that other students can use?
+ HowlerJS is an easy way to manipulate "the real API" that is named WebAudio. If you are curious, look at the [webaudiodemos.appspot.com](https://webaudiodemos.appspot.com/) Web site, look on twitter with the hashtag #webaudio, or on YouTube. This API is really powerful! 
+ Do you know other libraries similar to HowlerJS, useful for manipulating audio (streamed or as sound samples)?
+ Your instructor wrote some open source WebAudio applications.... find which ones! :-)
+ You can also use another funny library for synthesizing 8 bits sound effects, [try this demo](https://jeromeetienne.github.io/webaudiox/examples/jsfx.html)!


#### Optional projects

+ Try to make nice audio player that will chain background musics, when one is finished the next one starts (use an "`ended`" event listener on the audio element, for example, add `onended="...."`)
+ Add some buttons/menu to the game so that we can choose between 2 or 3 different background musics, or turn the music off.
+ Add a slider for adjusting the volume of the background music
+ [advanced] Use the multiple image/music/sound loader for adding multiple sound effects to your game, make different sounds depending on the color of balls that collide with the player
+ [advanced, harder] try to think about a way to display a progress bar while the multiple image/sound/music loader is loading the files...


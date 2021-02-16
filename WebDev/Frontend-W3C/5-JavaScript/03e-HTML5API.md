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

However, this API is a bit complicated to use for beginners. Fortunately there are several JavaScript libraries that simplify the use of the WebAudio API. HowlerJS is one of these.

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
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln" style="color: #000000;">window</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">onload&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;init</span><span class="pun" style="color: #666600;">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd" style="color: #000088;">var</span><span class="pln" style="color: #000000;">&nbsp;sound</span><span class="pun" style="color: #666600;">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd" style="color: #000088;">function</span><span class="pln" style="color: #000000;">&nbsp;init</span><span class="pun" style="color: #666600;">()</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="pun" style="color: #666600;">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;"></span><span class="kwd" style="color: #000088;">&nbsp; &nbsp; var</span><span class="pln" style="color: #000000;">&nbsp;button&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;document</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">querySelector</span><span class="pun" style="color: #666600;">(</span><span class="str" style="color: #008800;">"#button1"</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;"></span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp;&nbsp;<strong>sound&nbsp;</strong></span><strong><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="kwd" style="color: #000088;">new</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="typ" style="color: #660066;">Howl</span><span class="pun" style="color: #666600;">({</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><strong><span class="pln" style="color: #000000;">&nbsp; &nbsp; &nbsp; &nbsp; urls</span><span class="pun" style="color: #666600;">:</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="pun" style="color: #666600;">[ &nbsp;&nbsp;</span><span class="str" style="color: #008800;">'https://.../assets/sounds/plop.mp3'</span><span class="pun" style="color: #666600;">],</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><strong><span class="pln" style="color: #000000;">&nbsp; &nbsp; &nbsp; &nbsp; onload</span><span class="pun" style="color: #666600;">:</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="kwd" style="color: #000088;">function</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="pun" style="color: #666600;">()</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="pun" style="color: #666600;">{</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><strong><span class="pln" style="color: #000000;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; console</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">log</span><span class="pun" style="color: #666600;">(</span><span class="str" style="color: #008800;">"Loaded asset "</span><span class="pun" style="color: #666600;">);</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="pln" style="color: #000000;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; button</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">disabled&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="kwd" style="color: #000088;">false</span><span class="pun" style="color: #666600;">;</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="com" style="color: #880000;">// enable the play sound button</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln" style="color: #000000;"></span><span class="pun" style="color: #666600;">&nbsp; &nbsp; &nbsp; &nbsp; }</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="pln" style="color: #000000;"></span><span class="pun" style="color: #666600;">&nbsp; &nbsp; });</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="kwd" style="color: #000088;">function</span><span class="pln" style="color: #000000;">&nbsp;playSound</span><span class="pun" style="color: #666600;">()</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="pun" style="color: #666600;">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; sound</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">play</span><span class="pun" style="color: #666600;">();</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;">}</span></li>
</ol></div>

The important part is located in lines 8-12: the Howler library is to be used like this: `sound = new Howl({...});` The part between the { and } is an object. The `url's` property is an array with at least one element: the URL of the sound we want to use, located on remote servers. The call to new Howl({...}); will start downloading the sound in background, then, once it has loaded, it will "decode it" (i.e., an mp3 file will use some cpu to be decoded on the fly and played, whereas a decoded sound will use nearly zero cpu, which makes it good for games!).

Finally, once the sound is decoded, the `onload` callback is executed. In other words, the function after `onload`: will be executed (at _lines 10-12_). In this callback, we enable the button because the sound is ready to be played.

The `playSound` function can only be called when the button is enabled (when the sound sample has been loaded and decoded). In order to play a sound loaded by Howler.JS, we just call the `play()` method (_line 18_).






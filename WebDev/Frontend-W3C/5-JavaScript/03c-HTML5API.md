# Module 3: Playing with HTML5 APIs

## 3.3 HTML5 multimedia and JavaScript API

### 3.3.1 Playing audio and video streams

These examples are adapted from the ones in the W3Cx [HTML5 Coding Essentials and Best Practices](https://www.edx.org/course/html5-coding-essentials-and-best-practices) course, which covers multimedia in depth. The [HTML5 advanced course](https://www.edx.org/course/html5-apps-and-games) also gives further examples covering topics such as making a video player with chapter navigation, clickable transcript, audio EQ, etc.


#### The `<video>` element

The `<video>` element of HTML5 is one of the two "Flash killers" (the other being the `<canvas>` element). It was designed to replace horrible things like embedded Flash objects that we used to encounter not so long ago.

The new way of doing things is a lot better... (please open this [live example at JS Bin](https://jsbin.com/kimayesazo/edit?html,output)).

[JS Bin Demo](https://jsbin.com/kimayesazo/edit?html,output)

[Local Demo](src/03c-example01.html)

The source code of this example shows the typical usage of the `<video>` element:

<div class="source-code" style="padding-left: 30px; padding-right: 30px; border: 1px solid black;"><ol class="linenums" style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag" style="color: #008888;">&lt;video</span><span class="pln">&nbsp;</span><span class="atn" style="color: #AA0066;">width</span><span class="pun" style="color: #666600;">=</span><span class="atv" style="color: #008800;">"320"</span><span class="pln">&nbsp;</span><span class="atn" style="color: #AA0066;">height</span><span class="pun" style="color: #666600;">=</span><span class="atv" style="color: #008800;">"240"</span><span class="pln">&nbsp;</span><span class="atn" style="color: #AA0066;">controls</span><span class="pun" style="color: #666600;">=</span><span class="atv" style="color: #008800;">"controls"</span><span class="tag" style="color: #008888;">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag" style="color: #008888;">&lt;source</span><span class="pln">&nbsp;</span><span class="atn" style="color: #AA0066;">src</span><span class="pun" style="color: #666600;">=</span><span class="atv" style="color: #008800;">"movie.mp4"</span><span class="pln">&nbsp;</span><span class="atn" style="color: #AA0066;">type</span><span class="pun" style="color: #666600;">=</span><span class="atv" style="color: #008800;">"video/mp4"</span><span class="pln">&nbsp;</span><span class="tag" style="color: #008888;">/&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag" style="color: #008888;">&lt;source</span><span class="pln">&nbsp;</span><span class="atn" style="color: #AA0066;">src</span><span class="pun" style="color: #666600;">=</span><span class="atv" style="color: #008800;">"movie.ogg"</span><span class="pln">&nbsp;</span><span class="atn" style="color: #AA0066;">type</span><span class="pun" style="color: #666600;">=</span><span class="atv" style="color: #008800;">"video/ogg"</span><span class="pln">&nbsp;</span><span class="tag" style="color: #008888;">/&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;Your browser does not support the&nbsp;</span><span class="tag" style="color: #008888;">&lt;video&gt;</span><span class="pln">&nbsp;element.</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag" style="color: #008888;">&lt;/video&gt;</span></li>
</ol></div>

Please note that:

+ The `controls` attribute indicates that a control panel with play/stop/volume/progress widgets should be displayed;
+ Usually the browser  will use the first format it recognizes  (in this case, the browser checks whether `mp4` is supported, and if not, it will check for the `ogg` format, and so on). Some browsers may use a different heuristic and choose a "preferred" format.
+ The `<video>` element is a DOM member, so  CSS styling can be applied, as well as manipulation using the DOM API.

__You will learn more about the different attributes of the `<video>` element later on in the course.__

__Restriction: you cannot embed a YouTube or a Daily Motion video using the `<video>` element__

Help! `<video src="my youtube video URL"></video>` does not work! 

<div style="border: 2px solid red; margin: 10px; padding: 10px;">
<p><span style="color: #ff0000;"><strong>BEWARE</strong></span>:&nbsp;<em>you cannot directly embed videos from most of the popular social Web sites such as YouTube, Dailymotion, Vimeo, etc.&nbsp;<span style="line-height: 1.6;">For commercial&nbsp;reasons, and because advertising is automatically &nbsp;added to the&nbsp;videos, these Web sites do not allow "regular" embedding of their videos.</span></em></p>
</div>

While they use HTML5 to render their videos, these hosting sites (YouTube, etc.) use rather complex techniques in order to prevent you from using them with the `<video>` element. Instead, you often need to embed an `<iframe>` that will render the HTML5 videos in your Web site, and of course, the advertising that comes along with them.

Usually you have an "embed" button close to the videos that prompts you with some HTML code that you can copy and paste for embedding.


__An example using YouTube:__

Here is the HTML code you need to copy and paste in order to embed a video (in this case, a tutorial that tells you how to embed a YouTube video):

<div class="source-code" style="padding-left: 30px; padding-right: 30px; border: 1px solid black;"><ol class="linenums" style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag" style="color: #008888;">&lt;iframe</span><span class="pln">&nbsp;</span><span class="atn" style="color: #AA0066;">width</span><span class="pun" style="color: #666600;">=</span><span class="atv" style="color: #008800;">"560"</span><span class="pln">&nbsp;</span><span class="atn" style="color: #AA0066;">height</span><span class="pun" style="color: #666600;">=</span><span class="atv" style="color: #008800;">"315"</span><span class="pln">&nbsp;</span><span class="atn" style="color: #AA0066;">src</span><span class="pun" style="color: #666600;">=</span><span class="atv" style="color: #008800;">"https://www.youtube.com/embed/ZH1XOsv8Oyo"</span><span class="pln">&nbsp;</span><span class="atn" style="color: #AA0066;">frameborder</span><span class="pun" style="color: #666600;">=</span><span class="atv" style="color: #008800;">"0"</span><span class="pln">&nbsp;</span><span class="atn" style="color: #AA0066;">allowfullscreen</span><span class="tag" style="color: #008888;">&gt;&lt;/iframe&gt;</span></li>
</ol></div>

Below is the YouTube video embedded in this page using the above code: it's HTML5 but it's not a `<video>` element directly inserted in the HTML of this page - it's an `<iframe>`.

<p><iframe src="https://www.youtube.com/embed/ZH1XOsv8Oyo" allowfullscreen="" width="560" height="315" frameborder="0"></iframe></p>


#### The `<audio>` element

##### Introduction

HTML5 audio is composed of several layers:

+ [__The `<audio>` element__](https://www.w3.org/wiki/HTML/Elements/audio) is useful for embedding an audio player into a Web page. It is dedicated for <u>streamed audio</u>. It is very similar to the `<video>` element, both in its use and in its API.
+ [__The "Web Audio API"__](https://www.w3.org/TR/webaudio/) is designed for musical applications and for adding sound effects to games. This pure JavaScript API supports manipulation of sound samples (loops, etc.), music synthesis and sound generation (oscillators, etc.). It also comes with a set of predefined sound processing modules (reverb, delay, etc.).

<div style="border: 1px solid red; padding: 10px;">This course focuses on the&nbsp;<span style="font-family: 'courier new', courier;">&lt;audio&gt;</span>&nbsp;element. Please check for&nbsp; <a href="https://www.w3.org/TR/webaudio/" target="_blank">the Web Audio API</a>&nbsp;and other advanced parts of HTML5 in W3Cx's <a href="https://www.edx.org/course/html5-apps-and-games" target="_blank">HTML5 Apps and Games</a> course.</div>

The attributes, event set and JavaScript API of the `<audio>` element are just a "reduced" version of the ones from the `<video>` element, and here we will only address their differences and peculiarities.


##### The `<audio>` element - basic usage

The most simple basic example

[Online example from JS Bin](https://jsbin.com/xojobirowo/edit?html,output)

[JS Bin Demo](https://jsbin.com/xojobirowo/edit?html,output)

[Local Demo](src/03c-example02.html)

<p>Press play to stream the neigh&nbsp;of a&nbsp;horse: &nbsp;&nbsp;<audio controls="controls">
 <source src="https://mainline.i3s.unice.fr/mooc/week2p1/horse.ogg" type="audio/ogg">
  <source src="https://mainline.i3s.unice.fr/mooc/week2p1/horse.mp3" type="audio/mp3">
  Your browser does not support the audio element.
</audio></p>

As you can see, the code is very similar to the basic `<video>` element usage.

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&nbsp;&nbsp; &lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&nbsp;&nbsp; </span><span class="tag">&nbsp;&nbsp; </span><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&nbsp;&nbsp; </span><span class="tag">&nbsp;&nbsp; </span><span class="tag">&lt;title&gt;</span><span class="pln">Draw a monster in a canvas</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag"><span class="tag">&nbsp;&nbsp; </span>&lt;/head&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&nbsp;&nbsp; </span><span class="tag">&lt;body&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&nbsp;&nbsp; </span><span class="tag">&nbsp;&nbsp; </span><span class="tag">&lt;audio</span><span class="pln"> </span><span class="atn">controls</span><span class="pun">=</span><span class="atv">"controls" crossorigin="anonymous"</span><span class="tag">&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&nbsp;&nbsp; </span><span class="tag">&nbsp;&nbsp; </span><span class="tag">&nbsp;&nbsp; </span><span class="tag">&lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://mainline.i3s.unice.fr/mooc/week2p1/horse.ogg"</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="tag">&nbsp;&nbsp; </span><span class="tag">&nbsp;&nbsp; </span><span class="tag">&nbsp;&nbsp; </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"audio/ogg"</span><span class="pln"> </span><span class="tag">/&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="tag">&nbsp;&nbsp; </span><span class="tag">&nbsp;&nbsp; </span><span class="tag">&nbsp;&nbsp; </span><span class="tag">&lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://mainline.i3s.unice.fr/mooc/week2p1/horse.mp3"</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&nbsp;&nbsp; </span><span class="tag">&nbsp;&nbsp; </span><span class="tag">&nbsp;&nbsp; </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"audio/mp3"</span><span class="pln"> </span><span class="tag">/&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"><span class="tag">&nbsp;&nbsp; </span></span><span class="pln"><span class="tag"><span class="tag">&nbsp;&nbsp; </span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag">&nbsp;&nbsp; </span></span></span>Your browser does not support the audio element.</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"><span class="tag">&nbsp;&nbsp; </span></span><span class="pln"><span class="tag"><span class="tag">&nbsp;&nbsp; </span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag">&nbsp;&nbsp; </span></span></span>Download the audio/video in</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&nbsp;&nbsp; </span><span class="tag">&nbsp;&nbsp; </span><span class="tag">&nbsp;&nbsp; </span><span class="tag">&lt;a</span><span class="pln"> </span><span class="atn">href</span><span class="pun">=</span><span class="atv">”https://mainline.i3s.unice.fr/mooc/week2p1/horse.ogg”</span><span class="tag">&gt;</span><span class="pln">OGG</span><span class="tag">&lt;/a&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"><span class="tag">&nbsp;&nbsp; </span></span><span class="pln"><span class="tag"><span class="tag">&nbsp;&nbsp; </span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag">&nbsp;&nbsp; </span></span></span>or</span><span class="tag"></span><span class="tag"></span><span class="tag">&lt;a</span><span class="pln"> </span><span class="atn">href</span><span class="pun">=</span><span class="atv">”https://mainline.i3s.unice.fr/mooc/week2p1/horse.mp3”</span><span class="tag">&gt;</span><span class="pln">MP3</span><span class="tag">&lt;/a&gt;</span><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"><span class="tag">&nbsp;&nbsp; </span></span><span class="pln"><span class="tag"><span class="tag">&nbsp;&nbsp; </span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag">&nbsp;&nbsp; </span></span></span>format.</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&nbsp;&nbsp; </span><span class="tag">&nbsp;&nbsp; </span><span class="tag">&lt;/audio&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&nbsp;&nbsp; </span><span class="tag">&lt;/body&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/html&gt;</span></li>
</ol></div>

In this example, just as for the `<video>` element, we used the `controls` attribute in order to render the play/stop, time, volume and progress widgets.

Notice the other similarities: between the `<audio>...</audio>` tags, we added a text message that is displayed if the Web browser doesn't support the `<audio>` element, and we used several `<source>...</source>` elements that link to different audio formats for the same file. The browser will use the first format it recognizes.

_Lines 8-12_:  we suggest downloading the audio files if the browser does not support the `<audio>` element. This is also a best practice!


#### Notes for 3.3.1 Playing audio and video streams

+ `<video>` element
  + one of the two "Flash  killer" ('<canvas>` as the other)
  + a DOM member $\implies$ CSS styling applied and maipulating w/ the DOM API
  + unable to embedded a YouTube and Daily Motion video
  + typical usage

    ```html
    <video width="320" height="240" controls="controls">
      <source src="movie.mp4" type="video/mp4" />
      <source src="movie.ogg" type="video/ogg" />
      Your browser does not support the <video> element.
    </video>
    ```

    + `control` attribute: displaying a control panel w/ play/stop/volume/progress widget
    + browser using the 1st format recognized but some browsers probably choose a "preferred" format
  
  + example using YouTube: `<iframe width="560" height="315" src="https://www.youtube.com/embed/ZH1XOsv8Oyo" frameborder="0" allowfullscreen></iframe>`

+ Audio 
  + `<audio>` element
    + useful for embedding an audio player into a Web page
    + dedicated for _streamed audio_
    + a DOM member $\implies$ VSS styling applied and manipulating w/ the DOM API
    + attributes: a reduced version of `<video>` element
    + typical usage

      ```html
      <audio controls="controls" crossorigin="anonymous">
         <source src="https://mainline.i3s.unice.fr/mooc/week2p1/horse.ogg" type="audio/ogg" />
         <source src="https://mainline.i3s.unice.fr/mooc/week2p1/horse.mp3" type="audio/mp3" />
         Your browser does not support the audio element.
         Download the audio/video in
         <a href=”https://mainline.i3s.unice.fr/mooc/week2p1/horse.ogg”>OGG</a>
         or<a href=”https://mainline.i3s.unice.fr/mooc/week2p1/horse.mp3”>MP3</a> format.
      </audio>
      ```

      + `control` attribute: render the play/stop, time, volume and progress widgets
      + adding text message of the Wen browser not supporting the `<audio>` element
      + `<source>...</source>` element: link to different audio formats for the same file
      + browser using the 1st format recognized
  + Wen Audio API
    + designed for musical applications and for adding sound effects to games
    + manipulation of sund samples (loops. etc.), music synthesis and sound generation (oscillators, etc.)
    + w/ a set of predefined sound processing modules (reverb, delay, etc.)


#### Knowledge check 3.3.1

1. The `<video>` element is like any other HTML element: I can style it using CSS and interact programmatically with it using the JavaScript DOM API. (True/False)

  Ans: <br>
  Explanation: 




# Module 1: Advanced HTML5 multimedia section


## 1.2 The Timed Text Track API


### 1.2.1 The Timed Text Track API


#### Live coding video: intro to the Timed Text Track API

<a href="https://edx-video.net/W3CHTM52/W3CHTM52T415-V000500_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript Download](https://bit.ly/2S2MEIa)


#### Knowledge check 1.2.1

1. Do the most recent versions of all major browsers provide a menu for choosing the subtitle or the caption track? (Yes/No)

  Ans: 


#### Contents

In the [W3Cx HTML5 Coding Essentials and Best Practices](https://bit.ly/3we2vSS) course, we saw that `<video>` and `<audio>` elements can have `<track>` elements. A `<track>` can have a `label`, a `kind` (subtitles, captions, chapters, metadata, etc.), a language (`srclang` attribute), a source URL (`src` attribute), etc.

Here is a small example of a video with 3 different tracks ("......" masks the real URL here, as it is too long to fit in this page width!):

```html
<video id="myVideo" preload="metadata" controls crossOrigin="anonymous">
    <source src="https://...../elephants-dream-medium.mp4" type="video/mp4">
    <source src="https://...../elephants-dream-medium.webm" type="video/webm">
    <track label="English subtitles" kind="subtitles" srclang="en"
           src="https://...../elephants-dream-subtitles-en.vtt">
    <track label="Deutsch subtitles" kind="subtitles" srclang="de"
           src="https://...../elephants-dream-subtitles-de.vtt" default>
    <track label="English chapters" kind="chapters" srclang="en"
           src="https://...../elephants-dream-chapters-en.vtt">
</video>
```

And here is how it renders in your current browser (please play the video and try to show/hide the subtitles/captions):

<video id="myVideo" preload="metadata" controls="controls" crossorigin="anonymous"> 
  <source src="https://mainline.i3s.unice.fr/mooc/elephants-dream-medium.mp4" type="video/mp4"> 
  <source src="https://mainline.i3s.unice.fr/mooc/elephants-dream-medium.webm" type="video/webm"> 
  
  <track kind="subtitles" src="https://mainline.i3s.unice.fr/mooc/elephants-dream-subtitles-en.vtt" srclang="en" label="English subtitles"> 
  <track kind="subtitles" src="https://mainline.i3s.unice.fr/mooc/elephants-dream-subtitles-de.vtt" srclang="de" label="Deutsch subtitles" default=""> 
  <track kind="chapters" src="https://mainline.i3s.unice.fr/mooc/elephants-dream-chapters-en.vtt" srclang="en" label="English chapters"> 
</video>

Notice that the support for multiple tracks may differs significantly from one browser to another, in particular if you are using old versions. Here is a quick summary (as in May 2020).

+ Safari provides a menu  you can use to choose which subtitle/caption track to display. If one of the defined text tracks has the default attribute set, then it is loaded by default. Otherwise, the default is off.

  <figure style="margin: 0.5em; text-align: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
      onclick= "window.open('https://bit.ly/3v0DqL4')"
      src    = "https://bit.ly/3v0Yxg3"
      alt    = "screenshot of safari menu fr choosing subtitle track"
      title  = "screenshot of safari menu fr choosing subtitle track"
    />
  </figure>

+ Chrome and Opera both provide a subtitle menu and load the text track set that matches the browser language. If none of the available text tracks match the browser’s language, then it loads the track with the default attribute, if there is one. Otherwise, it loads none. Let's say that support is very incomplete (!).
+ Firefox provides also a subtitle menu but will show the first defined text track only if it has default set. It will load all tracks in memory as soon as the page is loaded.

Also there is [a Timed Text Track API in the HTML5/HTML5.1 specification](https://bit.ly/33RJsl8) that enables us to manipulate `<track>` contents from JavaScript. Do you recall that text tracks are associated with WebVTT files? As a quick reminder, let's look at a WebVTT file:

```
WEBVTT
 
1
00:00:15.000 --> 00:00:18.000 align:start
<v Proog>On the left we can see...</v>
 
2
00:00:18.167 --> 00:00:20.083 align:middle
<v Proog>On the right we can see the...</v>
 
3
00:00:20.083 --> 00:00:22.000
<v Proog>...the <c.highlight>head-snarlers</c></v>
 
4
00:00:22.000 --> 00:00:24.417 align:end
<v Proog>Everything is safe. Perfectly safe.</v>
remote controller with subtitles button
```

The different time segments are called "cues" and each cue has an id (1, 2, 3 and 4 in the above example), a startTime and an endTime, and a text content that can contain HTML tags for styling (`<b>`, etc...) or be associated with a "voice" as in the above example. In this case, the text content is wrapped inside `<v name_of_speaker>...</v>` elements.

It's now time to look at the JavaScript API for manipulating tracks, cues, and events associated with their life cycle. In the following lessons, we will look at different examples which use this API to implement missing features such as:

+ how to  build a menu for choosing the subtitle track language to display,
+ how to display a synchronized description of a video (useful for disabled people, for example),
+ how to display a clickable transcript aside the video (similar to what the edX video player does),
+ how to show chapters,
+ how to use JSON encoded cue contents (useful for showing external resources in the HTML document while a video is playing),
etc.


#### Notes for 1.2.1 The Timed Text Track API




### 1.2.2 The HTML track element





### 1.2.3 The TextTrack object





### 1.2.4 Working with cues





### 1.2.5 Listening to events




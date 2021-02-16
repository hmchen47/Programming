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





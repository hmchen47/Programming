# JavaScript - Document Object Model (DOM)


## The `<video>` element

+ [DOM JavaScript API](../WebDev/Frontend-W3C/2-HTML5Coding/02b-Multimedia.md#225-control-players-from-javascript)
	+ __methods__: controlling the behavior, such as `play()`, `pause()`, etc.
	+ __properties__:
		+ read/write mode, e.g., volume
		+ read-only mode, e.g., encoding, duration, etc.
	+ __event__:
		+ generated during the lifecycle of the element
		+ processed using JavaScript callbacks
		+ able to send events to control the video player
	+ example:

		<div><ul>
		<li style="margin-bottom: 0px;"><span>var</span><span> video </span><span>=</span><span> document</span><span>.</span><span>createElement</span><span>(</span><span>'video'</span><span>);</span></li>
		<li style="margin-bottom: 0px;"><span>video</span><span>.</span><span>src </span><span>=</span><span> </span><span>'video.mp4'</span><span>;</span></li>
		<li style="margin-bottom: 0px;"><span>video</span><span>.</span><span>controls </span><span>=</span><span> </span><span>true</span><span>;</span></li>
		<li style="margin-bottom: 0px;"><span>document</span><span>.</span><span>body</span><span>.</span><span>appendChild</span><span>(</span><span>video</span><span>);</span></li>
		</ul></div>


+ [The most interesting methods, properties, and events provided by the `<video>` element API](../WebDev/Frontend-W3C/2-HTML5Coding/02b-Multimedia.md#226-the-javascript-api)

	<table style="font-family: Arial,Helvetica,Sans-Serif; margin: 0 auto; width: 40vw;" cellspacing="0" cellpadding="5" border="1">
  	<caption style="font-size: 1.5em; margin: 0.2em;"><a href="https://www.w3.org/2010/05/video/mediaevents.html">HTML5 Video Events and API</a></caption>
		<thead>
		<tr style="font-size: 1.2em;">
			<th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Methods</th>
			<th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">Properties</th>
			<th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">Events</th>
		</tr>
	<tbody>
		<tr>
			<td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">play()</span></strong></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">currentSrc</span></strong></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">play</span></strong></td>
		</tr>
		<tr>
			<td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">pause()</span></strong></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">currentTime</span></strong></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">pause</span></strong></td>
		</tr>
		<tr>
			<td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">load()</span></strong></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">startTime (readonly)</span></strong></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">progress</span></strong></td>
		</tr>
		<tr>
			<td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;">canPlayType()</strong></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">videoWidth</span></strong></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;">error</strong></td>
		</tr>
		<tr>
			<td></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">videoHeight</span></strong></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;">timeupdate</strong></td>
		</tr>
		<tr>
			<td></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">duration (readonly)</span></strong></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;">ended</strong></td>
		</tr>
		<tr>
			<td></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">ended (readonly)</span></strong></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;">abort</strong></td>
		</tr>
		<tr>
			<td></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">error</span></strong></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;">empty</strong></td>
		</tr>
		<tr>
			<td></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">paused (readonly)</span></strong></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;">emptied</strong></td>
		</tr>
		<tr>
			<td></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">muted</span></strong></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;">waiting</strong></td>
		</tr>
		<tr>
			<td></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">seeking</span></strong></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;">loadedmetadata</strong></td>
		</tr>
		<tr>
			<td></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">volume</span></strong></td> <td></td>
		</tr>
		<tr>
			<td></td>	<td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">height</span></strong></td> <td></td>
		</tr>
		<tr>
			<td></td> <td> <p style="margin: 0px 0px 10px;"><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">width</span></strong></p> </td> <td></td>
		</tr>
		<tr>
			<td></td> <td> <p style="margin: 0px 0px 10px;"><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;" face="courier new, courier, monospace">seekable (readonly)</span></strong></p> </td> <td></td>
		</tr>
		<tr>
			<td></td> <td> <p style="margin: 0px 0px 10px;"><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">played (readonly)</span></strong></p> </td> <td></td>
		</tr>
	</tbody>
	</table>

+ [The `<video>` element JavaScript API](../WebDev/Frontend-W3C/2-HTML5Coding/02b-Multimedia.md#227-the-video-element-javascript-api)
	+ useful for implementing playlists, making custom user interfaces and many other interesting things
	+ use external buttons to control the player's behavior
		+ HTML code
			+ `<button onclick="playVideo();" style="cursor: pointer;">Play</button>`
			+ `<button onclick="pauseVideo();" style="cursor: pointer;">Pause</button>`
		+ JavaScript:
			+ `vid = document.querySelector("#vid");`: get the JavaScript object corresponding to the video element
			+ `vid.play();` & `vid.pause()`: methods from API for plating/pausing the video
			+ `vid.currentTime = 0;`: rewind the video
			+ `vid.load()`: rewind the video to `vid.currentTime = 0` and pause the video
	+ detect end of the video and start another one
		+ HTML code: `vid.addEventListener('ended', playNextVideo, false);`
		+ JavaScript:

			```js
			function playNextVideo(e) {
				// Whatever you want to do after the event, change the src attribute
				// of the video element, for example, in order to play another video
			}
			```

	+ manage playlist
		+ HTML code
			+ `var sources = ["https://mainline.i3s.unice.fr/mooc/samuraiPizzacat.mp4", "https://www.archive.org/.../P1120973_512kb.mp4"];`: a list for videos to play
			+ `<body onload="init()">`: call `init()` as the page loaded
		+ JavaScript:
			+ `myVideo = document.querySelector("#myVideo");`: used the DOM to get the JavaScript object corresponding to the video element
			+ `myVideo.addEventListener('ended', loadAndplayNextVideo, false);`: define the listerner for the `ended` event
			+ `loadNextVideo();`: callback function to react the `ended` event
				+ `currentVideo`: a variable corresonding to the the index of the current video
        + `myVideo.src = sources [currentVideo % sources.length]`: set the `src` of the video element to `sources[0]`, then to `sources[1]`, and module w/ the length of the list to repeat the playing


## The `<track>` element

+ [The `<track>` JavaScript API](../WebDev/Frontend-W3C/2-HTML5Coding/02c-Multimedia.md#237-the-track-javascript-api)
  + powerful API used to develop many interesting features
    + dynamically building a navigation menu
    + synchronizing page content w/ timestamps in the WebVTT file
    + displaying all the subtitles/captions at once
    + making an app for creating on the fly subtitles/captions
    + etc.


## The `getUserMedia` API - Accessing Webcam & Microphone

+ [The `getUserMedia` API - Webcam access](../WebDev/Frontend-W3C/2-HTML5Coding/02d-Multimedia.md#241-webcam)
  + useful for controlling a Webcam video stream
  + one component of the [WebRTC specification](https://www.w3.org/TR/webrtc/)
  + not considered a "real" part of the HTML5 specification
  + dealing w/ video streams: always used in conjunction w/ the `<video>` element
  + specification: https://www.w3.org/TR/mediacapture-streams/
  + Webcam usage
    + set the `srcObject` attribute of a `<video>` element to the live video stream object coming out of the Webcam
    + `navigator.getUserMedia(params)` method: get the stream
    + return an [ES6 promise](https://tinyurl.com/y4atxcjf); ES = ECMAScript
  + mandatory to access the page that contains the JavaScript code through `https://`

+ [The `getUserMedia` API - start/stop the Webcam](../WebDev/Frontend-W3C/2-HTML5Coding/02d-Multimedia.md#242-more-on-getusermedia)
  + `navigator.mediaDevices.getUserMedia({audio: true, video: true})`: 
    + parameters to capture the video and the audio from the current device (default Webcam)
    + return an ES6 promise
  + `then(stream)` method: get the current audio/video stream as parameter if success
  + `video.srcObject = stream;`: set the audio/video stream of the default Webcam to the `srcObject` attribute of the video element
  + `video.play();`: displaying stream in the video player
  + `webcamStream = stream;`: store the stream in a global variable
  + `catch((error) => ...)`: catch error event
  + `webcamStream.getTracks()[0].stop(); // audio`: stopping audio of the Webcam
  + `webcamStream.getTracks()[1].stop(); // video`: stopping video of the Webcam

+ [Accessing the microphone](../WebDev/Frontend-W3C/2-HTML5Coding/02d-Multimedia.md#243-using-the-microphone)
  + `navigator.getUserMedia({audio:true}, onSuccess, onError)`: capture the microphone input
  + `navigator.getUserMedia({video:true, audio:true}, onSuccess, onError)`: access the video and audio simultaneously
  + [WebRTC](https://www.w3.org/TR/webrtc/): a W3C specification for P2P audio/video/data Real Time Communication


+ [Webcam resolutions](../WebDev/Frontend-W3C/2-HTML5Coding/02d-Multimedia.md#244-webcam-resolution)
  + "constraint" object: 
    + As constraints applied to an existing local video stream using the "change constraints" API, where it may cause the video engine to reconfigure the device or codec for that particular stream.
    + As constraints applied to an incoming video stream using the "change constrains" API on a MediaStreamTrack, where it serves to inform the video engine about the desirable properties of the video track, which may lead to the video engine choosing to reencode the video and/or signal a remote video source that it wishes certain constraints to be put in place.
  + [example: different resolutions](../WebDev/Frontend-W3C/2-HTML5Coding/02d-Multimedia.md#full-example-choose-between-3-different-resolutions)
    + buttons for different resolutions: `<button id="qvga">QVGA</button>`, `<button id="vga">VGA</button>` & `<button id="hd">HD</button>`
    + initial buttons: ` vgaButton = document.querySelector('button#vga');`, `hdButton = document.querySelector('button#hd');`
    + callback fucntion for different resultions: `getMedia(qvgaConstraints);`, ` getMedia(vgaConstraints);` & `getMedia(hdConstraints);`
    + event listeners:

      ```js
      video.addEventListener('play', function() {
          setTimeout(function() {
                  displayVideoDimensions();
              }, 500);
          });
      }
      ```

    + values for the constraints on resolutions

      ```js
      var qvgaConstraints = {
          video: {
              width: { max: 320 },
              height: { max: 180 }
          }
      };
      ```

  + [rear and front camera in smartphone](../WebDev/Frontend-W3C/2-HTML5Coding/02d-Multimedia.md#selecting-the-front-or-rear-camera-on-smartphones)

    ```js
    document.getElementById('flip-button').onclick = function() {
        front = !front;
    };

    // toggle front and back camera (mobile) by clicking a button
    constraints = { video: { facingMode: (front? "user" : "environment") } };
    ```

+ [`MediaDevices.getUserMedia()` - MDN](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia)
  + syntax: `var promise = navigator.mediaDevices.getUserMedia(constraints);`
  + parameters
    + `constraints`:
      + a `MediaStreamConstraints` object with two members: `video` and `audio`
      + if the browser cannot find all media tracks with the specified types that meet the constraints given, then the returned promise is rejected with `NotFoundError`
      + `{audio: true, video: true}`: both audio and video without any specific requirements
  + return: a Promise whose fulfillment handler receives a `MediaStream` object when the requested media has successfully been obtained
  + examples
    + `video: {width: 1280, height: 720}` & `video: {width: {min: 1024, ideal: 1280, max: 1920}, height: {min: 576, ideal: 720, max: 1080}}`: request the microphone capabilities w/ additional constraints
    + `{audio: true, video: { facingMode: "user"}}`: prefer the front camera (if one is available) over the rear one
    + `{ audio: true, video: {facingMode: {exact: "environment"}}}`: the rear camera



## The MediaRecorder API

+ [The MediaRecorder API](../WebDev/Frontend-W3C/2-HTML5Coding/02d-Multimedia.md#245-the-mediarecorder-api): [usage procedure](../WebDev/Frontend-W3C/2-HTML5Coding/02d-Multimedia.md#five-steps-are-needed-to-use-the-mediarecorder-object)
  + creating a mediaRecorder from a stream
  + adding a "data handler" and call the `start()` method
    + `var recordedChunks = []; // will hold the recorded stream`: an array of bytes to hold the recorded stream
    + `mediaRecorder.ondataavailable = handleDataAvailable;`: declare the callback function to be called while the stream captured
    + `function handleDataAvailable(event)`: a function collecting the chunk of data that corresponds to a few seconds of video, and store it in the recordedChunks byte array
  + info mediaRecorder to stop while done
    + `mediaRecorder.stop();`: end the periodic execution of the handleDataAvailable method, and stop the data capture
  + creating a blob (large binary object) as the `src` attribute of the video player
    + `recordedChunks` array: a blob
    + `URL.createObjectURL(recordedChunks)`: create another object used as a value to set the `src` attribute
  + download the capture stream
    + creating an invisible link w/ a `download` attribute and a `href` attribute that points to the blob object containing the recorded stream encoded using a given codec
    + generate programmatically a click event on the link


+ [MediaRecorder - MDN](https://developer.mozilla.org/en-US/docs/Web/API/MediaRecorder)
  + Docstring:
    + Create a new MediaRecorder object, given a MediaStream to record
    + Options available to do things like set the container's MIME type (such as "video/webm" or "video/mp4") and the bit rates of the audio and video tracks or a single overall bit rate.
  + properties:
    + `MediaRecorder.mimeType` (read only): the MIME type selected as the recording container for the MediaRecorder object
    + `MediaRecorder.state` (read only): he current state of the MediaRecorder object (inactive, recording, or paused)
    + `MediaRecorder.stream` (read only): the stream that was passed into the constructor
    + `MediaRecorder.ignoreMutedMedia`: indicate whether the MediaRecorder instance will record input when the input MediaStreamTrack is muted, default: false
    + `MediaRecorder.videoBitsPerSecond` (read only): the video encoding bit rate in use
    + `MediaRecorder.audioBitsPerSecond` (read only): the audio encoding bit rate in use
  + methods
    + `MediaRecorder.pause()`: pause the recording of media
    + `MediaRecorder.requestData()`:
      + a Blob containing the saved data received thus far
      + after calling this method, recording continues, but in a new Blob
    + `MediaRecorder.resume()`: recording of media after having been paused
    + `MediaRecorder.start()`: begin recording media
    + `MediaRecorder.stop()`: stop recording, at which point a `dataavailable` event containing the final Blob of saved data is fired
  + static methods
    + `MediaRecorder.isTypeSupported()`: return a Boolean value indicating if the given MIME media type is supported by the current user agent
  + event handlers
    + `MediaRecorder.ondataavailable`
      + called to handle the `dataavailable` event
      + periodically triggered each time `timeslice` milliseconds of media recorded
    + `MediaRecorder.onerror`: called to handle the `error` event, including reporting errors that arise with media recording
    + `MediaRecorder.onpause`: called to handle the `resume` event, which occurs when media recording resumes after being paused
    + `MediaRecorder.onresume`: called to handle the `resume` event, which occurs when media recording resumes after being paused
    + `MediaRecorder.onstart`: called to handle the `start` event, which occurs when media recording starts
    + `MediaRecorder.onstop`: called to handle the `stop` event, which occurs when media recording ends
  + event
    + listen to these events using `addEventListener()` or by assigning an event listener to the `oneventname` property of this interface
    + `error`: fired when an error occurs, available via the `onerror` property




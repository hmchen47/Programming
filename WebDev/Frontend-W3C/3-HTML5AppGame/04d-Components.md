# Module 4: Web components and other HTML5 APIs section


## 4.4 The Orientation and Device Motion APIs


### 4.4.1 The Orientation API

This section covers the [HTML5 orientation API](https://www.w3.org/TR/screen-orientation/): a way to use angle measures provided by accelerometers from mobile devices or laptops such as MacBooks.

__Beware__: all examples must be run on a device with an orientation sensor and/or with an accelerometer. Furthermore, Chrome/Safari and Mozilla support this API, but Opera mobile doesn't (yet) at the time of writing. 

If it provides a "mobile device emulation mode", you can use the devtools of a desktop browser to fake the orientation values (see the support table below, the columns for desktop versions of browsers are about the support for this emulation mode).

#### External resources:

+ The W3C specification: [The Screen Orientation API](https://www.w3.org/TR/screen-orientation/)
+ Article on HTML5Rocks.com about device orientation: [Device Orientation and Motion](https://www.html5rocks.com/en/tutorials/device/orientation/)
+ Browser compatibility:
  + [DeviceOrientation & DeviceMotion events](https://caniuse.com/#feat=deviceorientation) on CanIUse
  + [DeviceOrientationEvent](https://developer.mozilla.org/en-US/docs/Web/API/Detecting_device_orientation#Browser_compatibility) and [DeviceMotionEvent](https://developer.mozilla.org/en-US/docs/Web/API/Detecting_device_orientation#Browser_compatibility) on MDN


#### Notes for 4.4.1 The Orientation API

+ HTML5 orientation API
  + a way to use angle measures provided by accelerometers form mobile devices or desktops such a sMacBook
  + mobile device emulation mode: able to use the devtools of a desktop browser to fake the orientation values


### 4.4.2 The coordinate system

Transformations between the Earth coordinate frame and the device coordinate frame uses the following system of rotations.

#### Rotations and mobile devices

Rotations use the right-hand convention, such that positive rotation around an axis is clockwise when viewed along the positive direction of the axis. When considering rotations, always think in terms of looking down: either at your feet on the ground or at a device (or map) lying flat on a table. We count _clockwise rotation as a positive number, and anti-clockwise as negative_. In this case, _rotations are measured in degrees_.

If you are not familiar with using a compass to navigate, here is an illustrated explanation of [relating compass readings to the real-world/a map](https://www.wikihow.com/Use-a-Compass).

As well as the (2D) left/right, forward/backward directions on a map (or HTML5 canvas!), we need to consider other types of movements.

For example height/depth: there might be a huge difference in position between being at the top or the bottom of a cliff, and yet the horizontal distance from one to the other is small.

Another direction that is not apparent when we assume our world is as flat as a map, is to tilt. If you've ever ridden a motor-cycle you will know that it is easier to change its direction by leaning over, than by trying to turn the handlebar. Imagine then, tilting or twisting your device to steer your character in a motorcycle or airplane game!

Before making use of a _location_-aware device, we must align its understanding of _direction_ with our own view of 'the Earth'. Once we have a unified _coordinate system_, we apply rotations in the following order:


#### Rotation with z axis - alpha degree

__Rotate the device frame around its z axis by alpha degrees, with alpha in [0, 360]__

+ Device in the initial position, with Earth (XYZ) and body (xyz) frames aligned.
+ Device rotated through angle alpha about z axis, with previous locations of x and y axes shown as $x_0$ and $y_0$.

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="https://bit.ly/3yjqD88" ismap target="_blank">
      <img style="margin: 0.1em;" height=250
        src   = "https://dev.w3.org/geo/api/start.png"
        alt   = "start orientation"
        title = "start orientation"
      >
      <img style="margin: 0.1em;" height=250
        src   = "http://dev.w3.org/geo/api/c-rotation.png"
        alt   = "rotation about z axis"
        title = "rotation about z axis"
      >
    </a>
  </div>


#### Rotation with x axis - beta degree

__Rotate the device frame around its x axis by beta degrees, with beta in[-180, 180]__

+ Device in the initial position, with Earth (XYZ) and body (xyz) frames aligned.
+ Device rotated through angle beta about new x axis, with previous locations of y and z axes shown as $y_0$ and $z_0$.

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="https://bit.ly/3yjqD88" ismap target="_blank">
      <img style="margin: 0.1em;" height=250
        src   = "https://dev.w3.org/geo/api/start.png"
        alt   = "start orientation"
        title = "start orientation"
      >
      <img style="margin: 0.1em;" height=250
        src   = "http://dev.w3.org/geo/api/a-rotation.png"
        alt   = "rotation about x axis"
        title = "rotation about x axis"
      >
    </a>
  </div>

#### Rotation with y axis - gamma degree

__Rotate the device frame around its y axis by gamma degrees, with gamma in [-90, 90]__

+ Device in the initial position, with Earth (XYZ) and body (xyz) frames aligned.
+ Device rotated through angle gamma about new y axis, with previous locations of x and z axes shown as $x_0$ and $z_0$.

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="https://bit.ly/3yjqD88" ismap target="_blank">
      <img style="margin: 0.1em;" height=250
        src   = "https://dev.w3.org/geo/api/start.png"
        alt   = "start orientation"
        title = "start orientation"
      >
      <img style="margin: 0.1em;" height=250
        src   = "http://dev.w3.org/geo/api/b-rotation.png"
        alt   = "rotation about y axis"
        title = "rotation about y axis"
      >
    </a>
  </div>


#### Notes for 4.4.2 The coordinate system

+ Rotations
  + using right-hand convention
  + positive rotation around an axis clockwise while viewed along the positive direction of the axis
  + always think of looking down
    + at your feet on the ground
    + at a device (or map) lying flat on a table
  + clockwise rotation as a positive number while anti-clockwise as a negative
  + rotations measured in degrees

+ Rotations and unified coordinate 
  + initial position: Earth (XYZ) and frames (xyz) aligned
  + around z-axis:
    + alpha degree w/ range [0, 360]
    + device rotated through angle alpha while $x_0$ and $y_0$ as the previous locations of x and y axes
  + around x-axis:
    + beta degree w/ range [-180, 180]
    + device rotated through angle beta about new x axis while $y_0$ and $z_0$ as the previous locations of y and z axes
  + around y-axis:
    + gamma degree w/ range [-90, 90]
    + device rotated through angle gamma about new y axis while $x_0$ and $z_0$ as the previous locations of x and z axes

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="https://bit.ly/3yjqD88" ismap target="_blank">
      <img style="margin: 0.1em;" height=180
        src   = "https://dev.w3.org/geo/api/start.png"
        alt   = "start orientation"
        title = "start orientation"
      >
      <img style="margin: 0.1em;" height=180
        src   = "http://dev.w3.org/geo/api/c-rotation.png"
        alt   = "rotation about z axis"
        title = "rotation about z axis"
      >
      <img style="margin: 0.1em;" height=180
        src   = "http://dev.w3.org/geo/api/a-rotation.png"
        alt   = "rotation about x axis"
        title = "rotation about x axis"
      >
      <img style="margin: 0.1em;" height=180
        src   = "http://dev.w3.org/geo/api/b-rotation.png"
        alt   = "rotation about y axis"
        title = "rotation about y axis"
      >
    </a>
  </div>


### 4.4.3 Get different angles


#### HTML5 orientation API

__Typical use using the JavaScript HTML5 orientation API__

The use of this API is very straightforward:

1. Test if your browser supports the orientation API (`window.DeviceOrientationEvent` is not null),
2. Define a listener for the 'deviceorientation' event as follows: `window.addEventListener('deviceorientation', callback, false);` with the callback function accepting the event object as its single input parameter,
3. Extract the angles from the event (use its properties: `alpha`, `beta`, `gamma`).

Here's [an example on JsBin](https://jsbin.com/limugat/edit). Try it with a smartphone, a tablet, or a device with an accelerometer:

[Local Demo](src/04d-example01.html)

(If using a mobile device,  open [the page in standalone mode](https://jsbin.com/limugat) (without the JsBin editor))

[Local Demo](src/04d-example02.html)


<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3rNf9aj')"
    src    = "https://bit.ly/3fjy4EX"
    alt    = "orientation api 2"
    title  = "orientation api 2"
  />
</figure>

The above screenshot came from an iPad laying immobile on a desk. Theoretically, all the angle values will be zero when the device is laid flat, providing it has not been moved since the page loaded. However, depending on the hardware, these values may change even if the device is stationary: a very sensitive sensor might report constantly changing values. This is why, in the example, we round the returned values with Math.round() at display time (see code).

If we change the orientation of the device here are the results:

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://bit.ly/3rNf9aj" ismap target="_blank">
    <img style="margin: 0.1em;" height=150
      src   = "https://bit.ly/3zXuubb"
      alt   = "orientation api 3"
      title = "orientation api 3"
    >
    <img style="margin: 0.1em;" height=150
      src   = "https://bit.ly/3C6Ea5l"
      alt   = "orientation api 1"
      title = "orientation api 1"
    >
    <img style="margin: 0.1em;" height=150
      src   = "https://bit.ly/3xi4DsM"
      alt   = "orientation api 2"
      title = "orientation api 2"
    >
  </a>
</div>


Typical use / code from the above example:

<div><ol>
<li value="1">...</li>
<li> &lt;h2&gt;Device Orientation with HTML5&lt;/h2&gt;</li>
<li>You need to be on a mobile device or use a laptop with accelerometer/orientation</li>
<li> device.</li>
<li> &lt;p&gt;</li>
<li> &lt;div id="LR"&gt;&lt;/div&gt;</li>
<li> &lt;div id="FB"&gt;&lt;/div&gt;</li>
<li> &lt;div id="DIR"&gt;&lt;/div&gt;</li>
<li> &lt;script type="text/javascript"&gt;</li>
<li>&nbsp;&nbsp; if (window.DeviceOrientationEvent) {</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; console.log("DeviceOrientation is supported");</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <strong style="color: red;">window</strong><strong style="color: red;">.addEventListener('deviceorientation', function(eventData) {</strong></li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; // gamme is for left/right inclination</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; var LR =<strong style="color: red;"> eventData.gamma;</strong></li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; // beta is for front/back inclination</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; var FB =<strong style="color: red;"> eventData.beta;</strong></li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; // alpha is for orientation</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; var DIR =<strong style="color: red;"> eventData.alpha;</strong></li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; // display values on screen</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; deviceOrientationHandler(LR, FB, DIR);</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }, false);</li>
<li>&nbsp;&nbsp; } else {</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; alert("Device orientation not supported on your device or browser. Sorry.");</li>
<li>&nbsp;&nbsp; }</li>
<li> </li>
<li> function deviceOrientationHandler(LR, FB, DIR) {</li>
<li>&nbsp;&nbsp; document.querySelector("#LR").innerHTML = "gamma : " + Math.round(LR);</li>
<li>&nbsp;&nbsp; document.querySelector("#FB").innerHTML = "beta : " + Math.round(FB);</li>
<li>&nbsp;&nbsp; document.querySelector("#DIR").innerHTML = "alpha : " + Math.round(DIR);</li>
<li> }</li>
<li> &lt;/script&gt;</li>
<li>&nbsp;...</li>
</ol></div>


#### Rotation using The rotation API and CSS3 3D rotations

__Another example that shows how to orient the HTML5 logo using the orientation API + CSS3 3D rotations__

This is just a [variation of the previous example](https://jsbin.com/manobezoji/edit?html,js,output), try it at JsBin

[Local Demo](src/04d-example03.html)

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://bit.ly/3rNf9aj" ismap target="_blank">
    <img style="margin: 0.1em;" height=200
      src   = "https://bit.ly/2VmgBEz"
      alt   = "orientation api example 3"
      title = "orientation api example 3"
    >
    <img style="margin: 0.1em;" height=200
      src   = "https://bit.ly/3xjP0RA"
      alt   = "orientation api example 1"
      title = "orientation api example 1"
    >
    <img style="margin: 0.1em;" height=200
      src   = "https://bit.ly/3fk153i"
      alt   = "orientation api example 2"
      title = "orientation api example 2"
    >
  </a>
</div>


Results on the iPad: the logo rotates when we change the iPad's orientation. This is a good "visual feedback" for an orientation controlled game...

This example is also on [video](https://www.youtube.com/watch?v=OrNLhOAGSdE).

Code from the example:

<div><ol>
<li value="1">...</li>
<li> &lt;h2&gt;Device Orientation with HTML5&lt;/h2&gt;</li>
<li>You need to be on a mobile device or use a laptop with accelerometer/orientation</li>
<li> device.</li>
<li> &lt;p&gt;</li>
<li> &lt;div id="LR"&gt;&lt;/div&gt;</li>
<li> &lt;div id="FB"&gt;&lt;/div&gt;</li>
<li> &lt;div id="DIR"&gt;&lt;/div&gt;</li>
<li> &lt;img src="https://www.html5</li>
<li>rocks.com/en/tutorials/device/orientation/html5_logo.png" id="imgLogo"</li>
<li> class="logo"&gt;</li>
<li> &lt;script type="text/javascript"&gt;</li>
<li>&nbsp;&nbsp; if (window.DeviceOrientationEvent) {</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; console.log("DeviceOrientation is supported");</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; window.addEventListener('deviceorientation', function(eventData) {</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; var LR = eventData.gamma;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; var FB = eventData.beta;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; var DIR = eventData.alpha;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; deviceOrientationHandler(LR, FB, DIR);</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }, false);</li>
<li>&nbsp;&nbsp; } else {</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; alert("Not supported on your device or browser. Sorry.");</li>
<li>&nbsp;&nbsp; }</li>
<li> </li>
<li>&nbsp;&nbsp; function deviceOrientationHandler(LR, FB, DIR) {</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; // USE CSS3 rotations for rotating the HTML5 logo</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; //for webkit browser</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; document.getElementById("imgLogo").style.webkitTransform = </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "rotate(" + LR + "deg) rotate3d(1,0,0, " + (FB * -1) + "deg)";</li>
<li> </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; //for HTML5 standard-compliance</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; document.getElementById("imgLogo").style.transform = </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "rotate(" + LR + "deg) rotate3d(1,0,0, " + (FB * -1) + "deg)";</li>
<li> </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; document.querySelector("#LR").innerHTML = "gamma : " + Math.round(LR);</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; document.querySelector("#FB").innerHTML = "beta : " + Math.round(FB);</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; document.querySelector("#DIR").innerHTML = "alpha : " + Math.round(DIR);</li>
<li> }</li>
<li> &lt;/script&gt;</li>
<li>&nbsp;...</li>
</ol></div>

#### A simple level tool using device orientation

This example works in Firefox, Chrome, and IOS Safari. Created by [Derek Anderson](https://twitter.com/derekanderson) @[Media Upstream](https://mediaupstream.com/). Original source code available [GitHub](https://github.com/mediaupstream/levelToolJS).

[We adapted the source code](https://jsbin.com/quboge/edit) so that you can tweak it in JsBin, or test it in [standalone mode](https://jsbin.com/quboge) (using a mobile device).

[Local Demo](src/04d-example04.html)

[Local Demo - Standalone mode](src/04d-exampl05.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick= "window.open('https://bit.ly/3rNf9aj')"
    src    = "https://bit.ly/37ezNXu"
    alt    = "level tool using device orientation"
    title  = "level tool using device orientation"
  />
</figure>


#### Other interesting uses: mix orientation API and WebSockets

You can imagine the above example that sends the current orientation of the device to a server using WebSockets. The server in turn updates the logo and position on a PC screen. If multiple devices connect, they can chat together and take control of the 3D Logo.

This video shows one of the above examples slightly modified: the JavaScript code running in the Web page on the iPad sends in real time the device orientation using the Web Sockets API to a server that in turns sends the orientation to a client running on a desktop browser. In this way the tablet "controls" the HTML5 logo that is shown on the desktop browser:

Click on the image to see the [YouTube video](https://www.youtube.com/watch?v=_CgIgJBK-Ys)



#### Notes for 4.4.3 Get different angles

+ HTML5 orientation API
  + typical procedure
    + test if browser supports the orientation API w/ `window.DeviceOrientationEvent !== null`
    + define listener for the `deviceorientation` event: `window.addEventListener('deviceorientation', callback, false);` w/ the callback function accepting the event object as its single input parameter
    + extract the angles from the events: the properties, `alpha`, `beta` and `gamma`
  + incorporating w/ `WebSockets`:
    + sending the real-time device orientation to server via `WebSockets`
    + server sending the orientation to a client running on a desktop browser
    + allowing multiple devices connecting to the server and chatting together

+ Example: device orientation in standalone version
  + containers for device rotation angles<a name="containers"></a>: `<div id="LR"></div> <div id="FB"></div> <div id="DIR"></div>`
  + Javascript inline snippet: `<script type="text/javascript>...</script>`
    + check browser support of orientation API<a name="getOrient"></a>: `if (window.DeviceOrientationEvent) {...} else { // not supported }`
      + log msg: `console.log("DeviceOrientation is supported");`
      + add device orientation handler: `window.addEventListener('deviceorientation', function(evtData) {...}, false);`
        + gamma for right/left inclination: `var LR = evtData.gamma;`
        + beta for front/back inclination: `var FB = evtData.beta;`
        + alpha fpr orientation: `var DIR = evtData.alpha;`
        + display values on screen: `deviceOrientationHandler(LR, FB, DIR);`
      + display not supported msg: `alert("Device orientation not supported on your device or browser: Sorry.");`
    + display msg in containers: `function deviceOrientationHandler(LR, FB, DIR) {...}`
      + left/right inclination: `document.querySelector("#LR").innerHTML = "gamma: " + Math.round(LR);`
      + front/back inclination: `document.querySelector("#LR").innerHTML = "beta: " + Math.round(FB);`
      + orientation: `document.querySelector("#LR").innerHTML = "alpha: " + Math.round(DIR);`

+ Example: device orintation w/ image
  + task: using CSS3  rotations for rotating the image
  + HTML snippet
    + containers for [device rotation angles](#containers)
    + image container: `<img src="https://.../log.png" id="imgLogo">
  + Javascript inline snippet: `<script type="text/javascript>...</script>`
    + check browser support of [orientation API](#getOrient)
    + tilt image to reflect device <a name="orientation"></a>: `function deviceOrientationHandler(LR, FB, DIR) {...}`
      + access image container and set style w/ webkit browser: `document.getElementById("imgLogo").style.webkitTransform = "rotate(" + LR + "deg) rotate3d(1, 0, 0 " + (FB *-1) + "deg)";`
      + access image container and set style w/ HTML5 standard-compliance: `document.getElementById("imgLogo").style.Transform = "rotate(" + LR + "deg) rotate3d(1, 0, 0 " + (FB *-1) + "deg)";`


### 4.4.4 The Device Motion API

This section presents the Device Motion API which is used in a similar manner to the device orientation API discussed earlier.

The deviceMotion API deals with _accelerations_ instead of _orientation_ only.

Use cases proposed by the specification are:

+ __Controlling a game:__ a gaming Web application monitors the device's orientation and interprets tilting in a certain direction as a means to control an on-screen sprite.
+ __Gesture recognition:__ a Web application monitors the device's acceleration and applies signal processing in order to recognize certain specific gestures. For example, using a shaking gesture to clear a web form.
+ __Mapping:__ a mapping Web application uses the device's orientation to correctly align the map with reality.


#### Basic usage

<div><ol>
<li value="1">function handleMotionEvent(event) {</li>
<li> </li>
<li>&nbsp;&nbsp; var x = event.accelerationIncludingGravity.x;</li>
<li>&nbsp;&nbsp; var y = event.accelerationIncludingGravity.y;</li>
<li>&nbsp;&nbsp; var z = event.accelerationIncludingGravity.z;</li>
<li> </li>
<li>&nbsp;&nbsp; // Process ...</li>
<li>}</li>
<li> </li>
<li>window.addEventListener("devicemotion", handleMotionEvent, true);</li>
</ol></div>

#### Basics about acceleration

The deviceMotion API is rather straightforward and is very similar to the orientation API except that it returns more than just the rotation information, it also returns [acceleration](https://en.wikipedia.org/wiki/Acceleration) information reflecting the device's actual movement.

The _acceleration_ is in three parts:

1. along the X axis
2. along the Y axis
3. along the Z axis

Each value is measured in [meters per second squared](https://en.wikipedia.org/wiki/Metre_per_second_per_second) ($m/s^2$) - multiply by 3.281 if you'd prefer an _approximation_ in feet per second per second.

The acceleration is returned by the API as an _acceleration event_. The two pertinent properties are: `accelerationIncludingGravity` and `acceleration`. The latter excludes the effects of gravity.

Why are there two different values? Because some devices have the capability of excluding the effects of [gravity](https://en.wikipedia.org/wiki/Gravity), eg if equipped with a gyroscope. Indeed there is [acceleration due implicitly to gravity](https://en.wikipedia.org/wiki/Acceleration_of_gravity), see also this: [Acceleration of Gravity on Earth...](https://en.wikipedia.org/wiki/Gravity_of_Earth)

If the device doesn't have a gyroscope, the `acceleration` property will be returned as null. In this case, you have no choice but to use the `accelerationIncludingGravity` property. Note that all IOS devices, so far, are equipped with a gyroscope.

So, the _device motion event_ is a superset of the _device orientation event_; it returns _rotation_ as well as _acceleration_ information from the device.


#### Example of acceleration values

If a laptop is in its normal position with the screen facing up, the data returned would be (info taken from this [article](https://developers.google.com/web/fundamentals/native-hardware/device-orientation/)):

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 50vw;"
    onclick= "window.open('https://bit.ly/2VfpNuP')"
    src    = "https://bit.ly/3yinTId"
    alt    = "acceleration values 1"
    title  = "acceleration values 1"
  />
</figure>


A mobile phone rotated along the x-axis so the screen is perpendicular to its normal position would return:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 50vw;"
    onclick= "window.open('https://bit.ly/2VfpNuP')"
    src    = "https://bit.ly/37gqEOm"
    alt    = "acceleration values 2"
    title  = "acceleration values 2"
  />
</figure>


Remember the coordinate system for a mobile phone:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick= "window.open('https://bit.ly/2VfpNuP')"
    src    = "https://bit.ly/3jaEjfo"
    alt    = "telephone coordinates system"
    title  = "telephone coordinates system"
  />
</figure>


#### Common steps

The principles are the same as for the orientation API:

1. Test if the API is supported by the browser,
2. Add a listener for 'devicemotion' events,
3. Get the acceleration values from the DOM event that has been passed to the listener,
4. Process the data.

__Common processing with acceleration values__

Test the value of the `acceleration.z` property: If > 0 then the device is facing up, otherwise it is facing down. This would be useful if you wanted to play [heads or tails](https://en.wikipedia.org/wiki/Coin_flipping) with your phone ;-)

<div><ol>
<li value="1">// For example, if acceleration.z is &gt; 0 then the phone is facing up</li>
<li> var facingUp = -1;</li>
<li> if (acceleration.z &gt; 0) {</li>
<li>&nbsp;&nbsp; facingUp = +1;</li>
<li> } </li>
</ol></div>

Compute the angle corresponding to the Left / Right and Front / Back tilts. This example uses the `accelerationIncludingGravity` property of the event.

<div><ol>
<li value="1">function deviceMotionHandler(eventData) {</li>
<li>&nbsp;&nbsp; // Grab the acceleration including gravity from the results</li>
<li>&nbsp;&nbsp; var acceleration = eventData.accelerationIncludingGravity;</li>
<li> </li>
<li>&nbsp;&nbsp; // Convert the value from acceleration to degrees </li>
<li>&nbsp; &nbsp;// acceleration.x|y is the&nbsp;acceleration according</li>
<li>&nbsp;&nbsp; // &nbsp;to gravity, we'll assume we're on&nbsp; Earth and divide</li>
<li>&nbsp;&nbsp; // by 9.81 (earth gravity) to get a percentage value,&nbsp;</li>
<li>&nbsp;&nbsp; //&nbsp;and then multiply that&nbsp;by 90 to convert to degrees. </li>
<li>&nbsp;&nbsp; var tiltLR = Math.round(((acceleration.x) / 9.81) * -90);</li>
<li>&nbsp;&nbsp; var tiltFB = Math.round(((acceleration.y + 9.81) / 9.81) * 90 * facingUp);</li>
<li> </li>
<li>&nbsp;&nbsp; // ... do something</li>
<li>}</li>
</ol></div>

Compute the vertical (direction of the sky) - this extract comes from a complete example further down this page...

<div><ol>
<li value="1">... </li>
<li>var angle = Math.atan2(accel.y,accel.x);</li>
<li> </li>
<li>var canvas = document.getElementById('myCanvas');</li>
<li>var ctx = canvas.getContext('2d');</li>
<li>&nbsp;</li>
<li>ctx.moveTo(50,50);</li>
<li>// Draw sky direction in the canvas</li>
<li>ctx.lineTo(50-50*Math.cos(angle),50+50*Math.sin(angle));</li>
<li>ctx.stroke();</li>
</ol></div>

Use acceleration values to move a ball on the screen of a tablet when the tablet is tilted front / back or left / right (complete example later on)...

<div><ol>
<li value="1">...</li>
<li> </li>
<li>ball.x += acceleration.x;</li>
<li>ball.y += acceleration.y;</li>
<li> </li>
<li>...</li>
</ol></div>


#### Complete examples

__Move the HTML5 logo__

[Online example at JsBin](https://jsbin.com/pasoboyucu/edit?html,js,output).

[Local Demo](src/04d-example06.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick= "window.open('https://bit.ly/2VfpNuP')"
    src    = "https://bit.ly/3lhpOsR"
    alt    = "Device motion API example"
    title  = "Device motion API example"
  />
</figure>


Code from this example:

<div><ol>
<li value="1">&lt;!doctype html&gt;</li>
<li>&lt;html&gt;</li>
<li> </li>
<li>&nbsp;&nbsp; &lt;head&gt;&lt;/head&gt;</li>
<li> </li>
<li>&nbsp;&nbsp; &lt;body&gt;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;h2&gt;Device Orientation with HTML5&lt;/h2&gt;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; You need to be on a mobile device or use a laptop with accelerometer/orientation</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; device.</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;p&gt;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;div id="rawAccel"&gt;&lt;/div&gt;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;div id="tiltFB"&gt;&lt;/div&gt;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;div id="tiltLR"&gt;&lt;/div&gt;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;div id="upDown"&gt;&lt;/div&gt;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;img src="https://www.html5rocks.com/en/tutorials/device/orientation/html5_logo.png" id="imgLogo" class="logo"&gt;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;script type="text/javascript"&gt;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if (window.DeviceMotionEvent != undefined) {</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; console.log("DeviceMotion is supported");</li>
<li> </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; window.addEventListener('devicemotion', function(eventData) {</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; // Grab the acceleration including gravity from the results</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; var acceleration = eventData.accelerationIncludingGravity;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; // Display the raw acceleration data</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; var rawAcceleration = "[" + Math.round(acceleration.x) + ", " + Math.round(acceleration.y)&nbsp;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; + ", " + Math.round(acceleration.z) + "]";</li>
<li> </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; // Z is the acceleration in the Z axis, and if the device </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // is facing up or down</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; var facingUp = -1;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if (acceleration.z &gt; 0) {</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; facingUp = +1;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }</li>
<li> </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; // Convert the value from acceleration to degrees </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // acceleration.x|y is the&nbsp;acceleration according to gravity,</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; // &nbsp;we'll assume we're on Earth and divide </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; // by 9.81 (earth gravity) to get a percentage value, &nbsp;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; //&nbsp;and then multiply that&nbsp;by 90 to convert to degrees. </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; var tiltLR = Math.round(((acceleration.x) / 9.81) * -90);</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; var tiltFB = Math.round(((acceleration.y + 9.81) / 9.81) * 90 * facingUp);</li>
<li> </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; document.querySelector("#rawAccel").innerHTML = </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"Raw acceleration" + rawAcceleration;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; document.querySelector("#tiltFB").innerHTML = </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"Tilt front/back : " + tiltFB;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; document.querySelector("#tiltLR").innerHTML = </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"Tilt left/right : " + tiltLR;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; document.querySelector("#upDown").innerHTML = </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"Face Up:Down : " + facingUp;</li>
<li> </li>
<li> </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; updateLogoOrientation(tiltLR, tiltFB);</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }, false);</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; } else {</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; alert("Not supported on your device or browser. Sorry.");</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }</li>
<li> </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; function updateLogoOrientation(tiltLR, tiltFB) {</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; // USE CSS3 rotations for rotating the HTML5 logo</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; //for webkit browser</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; document.getElementById("imgLogo").style.webkitTransform =</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "rotate(" + tiltLR + "deg) rotate3d(1,0,0, " + (tiltFB * -1) + "deg)";</li>
<li> </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; //for HTML5 standard-compliance</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; document.getElementById("imgLogo").style.transform =</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "rotate(" + tiltLR + "deg) rotate3d(1,0,0, " + (tiltFB * -1) + "deg)";</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }</li>
<li>&nbsp;&nbsp; &lt;/script&gt;</li>
<li>&nbsp; &lt;/body&gt;</li>
<li> </li>
<li>&lt;/html&gt;</li>
</ol></div>


__Interesting example that uses jQuery mobile__

This example shows how the X and Y acceleration values can be used for indicating the sky's direction (vertical), and how the Z acceleration is, in fact, an indicator for the face up / face down orientation of the device.

[This example](https://jsbin.com/uyuqek/4/edit) has been adapted and put on jsbin.com so that you can tweak it.

[Local Demo](src/04d-example07.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick= "window.open('https://bit.ly/2VfpNuP')"
    src    = "https://bit.ly/2TOY0kf"
    alt    = "devicemotion API"
    title  = "devicemotion API"
  />
</figure>


Code from the example:

<div><ol>
<li value="1">&lt;html&gt; </li>
<li>&nbsp;&nbsp; &lt;head&gt; </li>
<li> </li>
<li>&nbsp;&nbsp; &nbsp; &lt;meta http-equiv="content-type" content="text/html; charset=utf-8"&gt; </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp; &lt;meta name="viewport" content="user-scalable=no, width=device-width" /&gt;</li>
<li> </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp; &lt;link rel="stylesheet" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;href="https://code.jquery.com/mobile/1.0b2/jquery.mobile-1.0b2.min.css" /&gt;</li>
<li> </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp; &lt;script type="text/javascript" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;src = "https://code.jquery.com/jquery-1.6.2.min.js"&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;/script&gt;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp; &lt;script type="text/javascript" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;src = "https://code.jquery.com/mobile/1.0b2/jquery.mobile-1.0b2.min.js"&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;/script&gt;</li>
<li> </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp; &lt;script type="text/javascript"&gt;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $(document).ready(function(){</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; window.addEventListener("devicemotion",onDeviceMotion,false);</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; });</li>
<li> </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; function onDeviceMotion(event){</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; var ctx = document.getElementById("c").getContext("2d");</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; var accel = event.accelerationIncludingGravity;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $("#sliderX").val(Math.round(accel.x)).slider("refresh");</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $("#sliderY").val(Math.round(accel.y)).slider("refresh"); </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $("#sliderZ").val(Math.round(accel.z)).slider("refresh");</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; // sky direction</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; var angle = Math.atan2(accel.y,accel.x) </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ctx.clearRect(0,0,100,100);</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ctx.beginPath();</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ctx.arc(50,50,5,0,2*Math.PI,false);</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ctx.moveTo(50,50);</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; // Draw sky direction</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ctx.lineTo(50-50*Math.cos(angle),50+50*Math.sin(angle));</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ctx.stroke();</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp; &lt;/script&gt;</li>
<li> </li>
<li>&nbsp;&nbsp; &lt;/head&gt; </li>
<li>&nbsp;&nbsp; &lt;body&gt; </li>
<li> </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;div data-role="page" id = "intropage"&gt;</li>
<li> </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; &lt;div data-role="header"&gt;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;h1&gt;Accelerometer&lt;/h1&gt;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;/div&gt;</li>
<li> </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;div data-role="content"&gt; </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;label for="sliderX"&gt;X Acceleration (Roll)&lt;/label&gt;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;input type="range" name="sliderX" id="sliderX" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; value="0" min="-10" max="10" data-theme="a" /&gt;</li>
<li> </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;label for="sliderY"&gt;Y Acceleration (Pitch)&lt;/label&gt;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;input type="range" name="sliderY" id="sliderY" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; value="0" min="-10" max="10" data-theme="b" /&gt;</li>
<li> </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;label for="sliderZ"&gt;Z Acceleration (&lt;strike&gt;Yaw&lt;/strike&gt; </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Face up/down)</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&lt;/label&gt;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;input type="range" name="sliderZ" id="sliderZ" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; value="0" min="-10" max="10" data-theme="c" /&gt;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;/div&gt; </li>
<li> </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;p style = "text-align:center"&gt;SKY direction: </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; follow this line:&lt;/p&gt;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;div style = "text-align:center;margin-top:10px;"&gt;</li>
<li> </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;canvas id="c" width="100" height="100"&gt;&lt;/canvas&gt;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;/div&gt;</li>
<li> </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp; &lt;/div&gt;</li>
<li> </li>
<li>&nbsp;&nbsp; &lt;/body&gt; </li>
<li>&lt;/html&gt;</li>
</ol></div>

__Move a ball on the screen__

[Try this example at JsBin](https://jsbin.com/eyahuv/2/edit). If using a mobile device, use [this URL instead](https://jsbin.com/eyahuv/2)!

[Local Demo](src/04d-example08.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick= "window.open('https://bit.ly/2VfpNuP')"
    src    = "https://bit.ly/3zZ03Bt"
    alt    = "moving balls"
    title  = "moving balls"
  />
</figure>


Code from this example:

<div><ol>
<li value="1">&lt;!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "https://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"&gt;</li>
<li>&lt;html xmlns="https://www.w3.org/1999/xhtml"&gt;</li>
<li> </li>
<li>&nbsp;&nbsp;&nbsp; &lt;head&gt;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /&gt;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;meta name="viewport" content="width=device-width, </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; target-densityDpi=device-dpi, </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; initial-scale=1.0, </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; user-scalable=no, </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; maximum-scale=1.0"&gt;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;title&gt;iOS 4.2 Device Accellerometer&lt;/title&gt;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;style&gt;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; body {</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; font-family:Arial, Helvetica, sans-serif;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; font-size: 14px;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; #board {</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; position:absolute;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; left:0px;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; right:0px;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; top:0px;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; bottom:0px;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; #ball {</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; position:absolute;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; width: 60px;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; height: 60px;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; border-radius: 30px;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; background-image: -webkit-gradient(radial, 45% 45%, 5, 60% 60%, </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 40, from(red), color-stop(75%, black), to(rgba(255, 255, 255, 0)));</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; -webkit-box-shadow: 3px 3px 5px #888;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;/style&gt;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;script src="https://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&lt;/script&gt;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;script&gt;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; !window.jQuery &amp;&amp; document.write('&lt;script src="./js/jquery.min.js"&gt;&lt;\/script&gt;')</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;/script&gt;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;script&gt;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; var offset;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; var velocity;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; var board;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; var ball;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; var interval;</li>
<li> </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $(document).ready(function() {</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; window.addEventListener("devicemotion", onDeviceMotion, false);</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $('#timestamp').html(new Date().toString());</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $('#status').html("Ready!");</li>
<li> </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; velocity = {};</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; velocity.x = 0;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; velocity.y = 0;</li>
<li> </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; offset = {};</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; board = $('#board');</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ball = $('#ball');</li>
<li> </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; offset.left = (board.width() - ball.width()) / 2;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; offset.top = (board.height() - ball.height()) / 2;</li>
<li> </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $('#ball').offset(offset);</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; interval = setInterval(updateBall, 25);</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; });</li>
<li> </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; function onDeviceMotion(event) {</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $('#timestamp').html(new Date().toString());</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $('#status').html("Device Motion Event");</li>
<li> </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; var eventDetails;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; try {</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; var accel = event.accelerationIncludingGravity;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; eventDetails = "accelerationIncludingGravity: {" +</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "&lt;br&gt;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x: " + accel.x +</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "&lt;br&gt;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;y: " + accel.y +</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "&lt;br&gt;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;z: " + accel.z +</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "&lt;br/&gt;} &lt;br/&gt;&lt;br/&gt;" +</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "interval: " + event.interval;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; updateVelocity(event);</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; } catch (e) {</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; eventDetails = e.toString();</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }</li>
<li> </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $('#details').html(eventDetails);</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }</li>
<li> </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; var decay = .9;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; var bounceDecay = .95;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; var maxVelocity = 100;</li>
<li> </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; function updateVelocity(event) {</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; velocity.x += event.accelerationIncludingGravity.x;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if (Math.abs(velocity.x) &gt; maxVelocity) {</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if (velocity.x &gt; 0) velocity.x = maxVelocity;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; else velocity.x = -maxVelocity;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }</li>
<li> </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; velocity.y += event.accelerationIncludingGravity.y;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if (Math.abs(velocity.y) &gt; maxVelocity) {</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if (velocity.y &gt; 0) velocity.y = maxVelocity;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; else velocity.y = -maxVelocity;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }</li>
<li> </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; function updateBall() {</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if (offset.left &lt;= -(ball.width() / 2)) {</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; velocity.x = Math.abs(velocity.x * bounceDecay);</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; } else if (offset.left &gt;= (board.width() - (ball.width() / 2))) {</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; velocity.x = -Math.abs(velocity.x * bounceDecay);</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; } else {</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; velocity.x = parseInt(velocity.x);</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; velocity.x *= decay;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }</li>
<li> </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if (offset.top &lt;= -(ball.height() / 2)) {</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; velocity.y = -Math.abs(velocity.y * bounceDecay);</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; } else if (offset.top &gt;= (board.height() - (ball.height() / 2))) {</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; velocity.y = Math.abs(velocity.y * bounceDecay);</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; } else {</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; velocity.y = parseInt(velocity.y);</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; velocity.y *= decay;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }</li>
<li> </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; offset.left += velocity.x;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; offset.top -= velocity.y;</li>
<li> </li>
<li> </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $('#ball').offset(offset);</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }</li>
<li>&nbsp;&nbsp;&nbsp; &lt;/script&gt;</li>
<li>&nbsp; &lt;/head&gt;</li>
<li> </li>
<li>&nbsp; &lt;body&gt;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp; &lt;div id="timestamp"&gt;&lt;/div&gt;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp; &lt;div id="status"&gt;&lt;/div&gt;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp; &lt;div id="details"&gt;&lt;/div&gt;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp; &lt;div id="board"&gt;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;div id="ball"&gt;&lt;/div&gt;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp; &lt;/div&gt;spec: &lt;a href="https://w3c.github.io/deviceorientation/spec-source-orientation.html" target="https://w3c.github.io/deviceorientation/spec-source-orientation.html"&gt;https://w3c.github.io/deviceorientation/spec-source-orientation.html&lt;/a&gt;</li>
<li> </li>
<li>&nbsp; &lt;/body&gt;</li>
<li> </li>
<li>&lt;/html&gt;</li>
</ol></div>

#### External resources

+ From the W3C specification: [devicemotion Event](https://w3c.github.io/deviceorientation/spec-source-orientation.html#devicemotion)
+ From Google Devs: "[Device Orientation & Motion](https://developers.google.com/web/fundamentals/native-hardware/device-orientation/)"
+ On Dev. Opera: "[The W3C Device Orientation API: Detecting Orientation and Acceleration](https://dev.opera.com/articles/w3c-device-orientation-api/)"


#### Notes for 4.4.4 The Device Motion API

+ The `deviceMotion` API
  + dealing w/ the acceleration instead of orientation only
  + use cases proposed
    + __controlling a game:__ a gaming Web application monitors the device's orientation and interprets tilting in a certain direction as a means to control an on-screen sprite
    + __+gesture recognition:__ a Web application monitors the device's acceleration and applies signal processing in order to recognize certain specific gesture
    + __mapping:__ a mapping Web application uses the device's orientation to correctly align the map w/ reality
  + basic syntax: 
    + handle motion event: `function handleMotionEvent(evt) {...}`
      + x-axis: `var x = evt.accelerationIncludingGravity.x;`
      + x-axis: `var y = evt.accelerationIncludingGravity.y;`
      + x-axis: `var z = evt.accelerationIncludingGravity.z;`
      + processing ...
    + add even listener for device motion: `window.addEventListener('devicemotion', handleMotionEvent, true);`

+ Acceleration
  + `deviceMotion` API similar to the `orientation` API
  + returning both the rotation infomation and aceration information
  + reflecting the device's actual movement
  + containing 3 parts: along the x axis, along the  axis, and along the z axis
  + unit: $m/s^2 \sim \frac{1}{3.281} ft/s^2$
  + returned by the API as an _acceleration_ event w/ properties
    + `accelerationIncludingGravity`
    + `acceleration`: presented w/ gyroscope, otherwise `null`
  + device motion event: a superset of the device orientation event, returning both rotation and acceleration info from the device
  + example of acceleration values
    + top diagram: device screen sits up right as normal position
    + botton diagram: device screen perpendicular to it normal position

    <figure style="margin: 0.5em; text-align: center;">
      <img style="margin: 0.1em; padding-top: 0.5em; width: 50vw;"
        onclick= "window.open('https://bit.ly/2VfpNuP')"
        src    = "https://bit.ly/3yinTId"
        alt    = "acceleration values 1"
        title  = "acceleration values 1"
      />
    </figure>

    <figure style="margin: 0.5em; text-align: center;">
      <img style="margin: 0.1em; padding-top: 0.5em; width: 50vw;"
        onclick= "window.open('https://bit.ly/2VfpNuP')"
        src    = "https://bit.ly/37gqEOm"
        alt    = "acceleration values 2"
        title  = "acceleration values 2"
      />
    </figure>

+ Common procedure fro acceleration
  + test if the API supported by the browser
  + add a listener for `devicemotion` event
  + get the acceleration values form the DOM event
  + process the data

+ Common processing w/ acceleration values
  + `acceleration.z` property:
    + acceleration.z $> 0$: device facing up
    + acceleration.z $\le 0$: device facing down
  + typical snippet for `acceleration.z` property<a name="faceUp"></a>
    + declare facing up variable: `var facingUp = -1;`
    + check acceleration.z property: `if (acceleration.z > 0) { facingUp = +1; }`
  + `accelerationIncludingGravity` perperty
    + computing the angle corresponding to the left/right and front/back titls
    + converting the value from acceleration to degrees
    + `acceleration.x`/`acceleration.y`:
      + the acceleration according to gravity
      + dividing by 9.81 (Earth gravity) to get a percentage value and then multipy that by 90 to convert to degrees
  + common snippet: `function deviceMotionHandler(evtData) {...}`
    + set acceleration variable: `var acceleration = evtData.accelerationIncludingGravity;`
    + convert the value to degrees<a name="val2Deg"></a>: `var tiltLR = Math.round(((acceleration.x)/9.81) * -90); var tiltFB = Math.round(((acceleration.y + 9.81)/9.81) * 90 * facingUp);`
    + processing w/ the degrees
  + common snippet to compute the vertical (direction to the sky)
    + set angle: `var angle = Math.atan(accel.y, accel.x);`
    + access canvas and set 2D context: `var canvas = document.getElementById('myCanvas'); var ctx = canvas.getContext('2d');`
    + draw sky direction: `ctx.moveTo(50, 50); ctx.lineTo(50-50*Math.cos(angle), 50+50*Math.sin(angle)); ctx.stroke();`
  + using acceleration values to move a ball on the screen of a tablet when tablet is tilted front/back or left/right
    + x position: `ball.x += acceleration.x;`
    + y position: `ball.y += acceleration.y;`

+ Example: displaying logo up when tilting
  + HTML snippet:
    + containers for acceleration values: `<div id="rawAccel"></div> <div id="tiltFB"></div> <div id="tiltLR"></div> <div id="upDown"></div>`
    + container for image: `<img src="https://.../logo.png" id="imglogo">`
  + JavaScript inline snippet: `<script type="text/javascript">...</script>`
    + check browser support: `if (window.DeviceMotionEvent != undefined) {...} else { // not supported }`
      + log console msg: `console.log("DeviceMotion is supported");`
      + add device motion handler: `window.addEventListener("devicemotion', function(evtDta) {...}, flase);`
        + set acceleration var: `var acceleration = evtData.accelerationIncludingGravity;`
        + display raw acceleration data: `var rawAcceleration = "[" + Mathround(acceleration.x) + "," + Math.round(acceleration.y) + "," + Math.round(acceleration.z) + "]";`
        + check [facing up or down](#facingUp)
        + convert [value to the degree](#val2Deg)
        + set raw acceleration value: `document.querySelector("#rawAccel").innerHTML = "Raw acceleration: " + rawAccelaeration;`
        + set tilt FB vale: `document.querySelector("#tiltFB").innerHTML = "Tilt fron/back: " + tiltFB;`
        + set tilt LR vale: `document.querySelector("#tiltLR").innerHTML = "Tilt left/right: " + tiltLR;`
        + set face up/down: `document.querySelector("#upDown").innerHTML = "Face up/down: " + facingUp;`
        + call to update logo orientation: `updateLogoOrientation("tiltLR, tiltFB);`
      + display not supported msg: `alert("Not supported on your device or browser. Sorry");`
    + update [tilt image to reflect device](#orientation)

+ Example: orientations w/ X, Y, and Z accelerations
  + tasks
    + using the X and Y acceleration values for indicating the sky's direction (vertical)
    + using the Z acceleration value for the face up / down orientation of the device
  + HTML header portion
    + link jQuery CSS: `<link rel="stylesheet" href="https://code.jquery.com/mobile/1.0b2/jquery.mobile-1.0b2.min.css" />`
    + link jQuery JS: `<script type="text/javascript" src = "https://code.jquery.com/jquery-1.6.2.min.js"></script>`
    + link jQuery mobile JS: `<script type="text/javascript" src = "https://code.jquery.com/mobile/1.0b2/jquery.mobile-1.0b2.min.js"></script>`
  + JavaScript inline script in header portion: `<script type="text/javascript">...</script>`
    + add device motion handler if page ready: `$(document).ready(function() { window.addEventListener("devicemotion", onDeviceMotion, false); });`
    + device motion callback: `function onDeiceMotion(evt) {...}`
    + access canvas and set context: `var ctx = document.getElementById("c").getContext("2d");`
    + set acceleraton: `vr accel = evtData.accelerationIncludingGravity;`
    + refresh all sliders: `$("#sliderX").val(Math.round(accel.x)).slider("refresh"); $("#sliderY").val(Math.round(accel.y)).slider("refresh"); $$("#sliderZ").val(Math.round(accel.z)).slider("refresh");`
    + set sky direction: `var angle = Math.atan2(accel.y, accel.x);`
    + draw sky direction: `cyx.clearRec(0, 0, 100, 100); ctx.arc(50, 50, 0, 2*Math.PI, false); ctx.moveTo(50, 50); ctx.lineTo(50-50*Math.cos(angle), 50+50*Math.sine(angle)); ctx.stroke();`
  + HTML body snippet:
    + page container: `div data-role="page" id="intrppage">...</div>`
    + header container: `<div data-role="header"<h1>Accelerometer</h1></div>`
    + content container: `<div data-role="content">...</div>`
      + X acceleration slider: `<label for="sliderX">X Acceleration (Roll)</label> <input type="range" name="sliderX" id="sliderX" value=0 min=-10 max=10 data-theme="a" />`
      + Y acceleration slider: `<label for="sliderY">Y Acceleration (Pitch)</label> <input type="range" name="sliderY" id="sliderY" value=0 min=-10 max=10 data-theme="b" />`
      + Z acceleration slider: `<label for="sliderZ">Z Acceleration (<strike>Yaw</strike>Face up/down)</label> <input type="range" name="sliderZ" id="sliderZ" value=0 min=-10 max=10 data-theme="c" />`
    + sky direction: `<p style="text-align: center;">SKY direction: follow this line:</p>`
    + camvas: `<div style="text-align: center; margin-top: 10px;"><canvas id="c" width=100 height=100></canvas></div>`

+ Example: moving ball on mobile screen
  + inline CSS style: `<style>...</style>`
    + body style: `body {font-family: Arial, Helvetica, sans-serif; font-size: 10px; }`
    + board style: `#board { position: absolute; left: 0px; right: 0px; top: 0px; button: 0px; }`
    + ball style: `#ball { position: absolute; width: 60px; height: 60px; border-radius: 30px; background-image: -webkit-gradiebnt(rdaial, 45%, 45%, 5, 60%, 60%, 40 from(red), color-stop(75%, black), to(rgba(255, 255, 255, 0))); -webkit-box-shadow: 3px 3px 5px #888; }`
  + JavaScript inline snippet:
    + link jQuery JS: `<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>`
    + link local jQuery JS: `<script>!window.jQuery && document.write('<script src="./js/jquery.min.js"><\/script>')</script>`
  + inline JavaScript: `<script>...</script>`
    + declar global variables: `var offset; var velocity; var board; var ball; var interval;`
    + init page after DOM ready: `$(document).ready(function() {...})`
      + add device motion handler: `window.addEventListener("devicemotion", onDeviceMotion, false);`
      + display time and status: `$('#timestamp').html(new Date().toString()); $('$status').html("Ready!");`
      + init vecolity: `veclocity = {}; velocity.x = 0; velocit.y = 0;`
      + set offset and access board and balls: `offset = {}; board = $('#board'); ball = $('#ball');`
      + offset ball position: `$('#ball').offset(offset);`
      + draw ball initially: `interval = setInterval(updateBall, 25);`
    + callback for device motion: `fucntion onDeviceMotion(evt) {...}`
      + display date and status: `$('#timestamp').html(new Date().toString()); $('$status').html("Device Motion Event!");`
      + declare variable: `var evtDetails;`
      + event handler: `try {...} catch (e) {eventDetails = e.toString(); }`
        + set acceleration: `var accel = evt.accelerationIncludingGravity; eventDetails = "accelerationIncludingGravity: {" + "<br> x: " + accel.x + "<br> y: " + accel.y + "<br> z: " + accel.z + <br/>}<br/><br/>" + "interval: " + evt.interval;`
        + call to update vecolcity: `updateVelocity(evt);`
      + display detail info: `$('#details').html(eventDetails);`
    + init variables for velocity: `var delay = -.9; var bounceDecay = .95; var maxVelocity = 100;`
    + update velocity: `function updateVeclocity(evt) {...}`
      + set x velocity: `velocity.x += evt.accelerationIncludingGravity.x;`
      + truncate x velocity: `if (Math.abs(velocity.x) > maxVelocity) { if (velocity.x > 0) { velocity.x = maxVelocity; } else { velocity.x = -maxVelcoity; }}`
      + set y velocity: `velocity.y += evt.accelerationIncludingGravity.y;`
      + truncate y velocity: `if (Math.abs(velocity.y) > maxVelocity) { if (velocity.y > 0) { velocity.y = maxVelocity; } else { velocity.y = -maxVelcoity; }}`
    + update ball position: `function updateBall() {...}`
      + check left boundary: `if (offset.left <= -(ball.width() / 2)) { velocity.x = Math.abs(velocity.x * bounceDecay); }`
      + check right bounday: `else if (offset.left >= (board.width() -  (ball.width() / 2))) { velocity.x = -Math.abs(velocity.x * bounceDecay); }`
      + not hit left/right boundaries: `else { velocity.x = parseInt(velocity.x); velocity.x += decay; }`
      + check top boundary: `if (offset.top <= -(ball.height() / 2)) { velocity.y = -Math.bas(velocity,y * bounceDecay); }`
      + check botton bounday: `else if (offset.top >= (board.height() - (ball.height() / 2))) { velocity.y = Math.abs(velocity.y -* bounceDecay); }`
      + not hit top/bottom boundaries: `else { velocity.y = parseInt(velocity.y); velocity.y *= decay; }`
      + set offset values: `offset.x += velocity.x; offset.y -= velocity.y; $('#ball').offset(offset);`
  + HTML snippet:
    + timestamp container: `<div id="timestamp"></div>`
    + status container: `<div id="status"></div>`
    + acceleration position: `<div id="details"></div>`
    + board container with ball: `<div id ="board"><div id="ball"></div></div>`
 

### 4.4.5 Discussion and projects

Here is the discussion forum for this part of the course. Please post your comments/observations/questions and share your creations.

#### Suggested topics of discussion:

+ Did you know that you can "fake" the orientation using the devtools of some desktop browsers?
+ What kind of application would benefit from the Orientation and Motion APIs (apart from games)?


#### Optional projects:

+ The [Christmas game](https://mainline.i3s.unice.fr/mooc/SkywardBound/) developed by students from the previous run is a perfect candidate to be controlled using the APIs seen in this course!! I would start with the orientation API and try to move the bunny left/right... 
+ Using the game framework, try to control the monster using the orientation API, so that it avoids the balls - see the last example from Module 2 of the course!






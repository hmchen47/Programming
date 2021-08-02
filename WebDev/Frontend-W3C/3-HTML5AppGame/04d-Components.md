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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1">...</li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;h2&gt;</span><span class="pln">Device Orientation with HTML5</span><span class="tag">&lt;/h2&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">You need to be on a mobile device or use a laptop with accelerometer/orientation</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> device.</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;p&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;div</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"LR"</span><span class="tag">&gt;&lt;/div&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;div</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"FB"</span><span class="tag">&gt;&lt;/div&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;div</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"DIR"</span><span class="tag">&gt;&lt;/div&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;script</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"text/javascript"</span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">window</span><span class="pun">.</span><span class="typ">DeviceOrientationEvent</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"DeviceOrientation is supported"</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <strong>window</strong></span><strong><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'deviceorientation'</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">eventData</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="com">// gamme is for left/right inclination</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">var</span><span class="pln"> LR </span><span class="pun">=</span><strong><span class="pln"> eventData</span><span class="pun">.</span><span class="pln">gamma</span><span class="pun">;</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="com">// beta is for front/back inclination</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">var</span><span class="pln"> FB </span><span class="pun">=</span><strong><span class="pln"> eventData</span><span class="pun">.</span><span class="pln">beta</span><span class="pun">;</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="com">// alpha is for orientation</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">var</span><span class="pln"> DIR </span><span class="pun">=</span><strong><span class="pln"> eventData</span><span class="pun">.</span><span class="pln">alpha</span><span class="pun">;</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="com">// display values on screen</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; deviceOrientationHandler</span><span class="pun">(</span><span class="pln">LR</span><span class="pun">,</span><span class="pln"> FB</span><span class="pun">,</span><span class="pln"> DIR</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="pun">},</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; alert</span><span class="pun">(</span><span class="str">"Device orientation not supported on your device or browser. Sorry."</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> deviceOrientationHandler</span><span class="pun">(</span><span class="pln">LR</span><span class="pun">,</span><span class="pln"> FB</span><span class="pun">,</span><span class="pln"> DIR</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#LR"</span><span class="pun">).</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> </span><span class="str">"gamma : "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">round</span><span class="pun">(</span><span class="pln">LR</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#FB"</span><span class="pun">).</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> </span><span class="str">"beta : "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">round</span><span class="pun">(</span><span class="pln">FB</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#DIR"</span><span class="pun">).</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> </span><span class="str">"alpha : "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">round</span><span class="pun">(</span><span class="pln">DIR</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/script&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;...</span></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1">...</li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;h2&gt;</span><span class="pln">Device Orientation with HTML5</span><span class="tag">&lt;/h2&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">You need to be on a mobile device or use a laptop with accelerometer/orientation</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> device.</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;p&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;div</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"LR"</span><span class="tag">&gt;&lt;/div&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;div</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"FB"</span><span class="tag">&gt;&lt;/div&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;div</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"DIR"</span><span class="tag">&gt;&lt;/div&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;img</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://www.html5</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="atv">rocks.com/en/tutorials/device/orientation/html5_logo.png"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"imgLogo"</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="atn">class</span><span class="pun">=</span><span class="atv">"logo"</span><span class="tag">&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;script</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"text/javascript"</span><span class="tag">&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">window</span><span class="pun">.</span><span class="typ">DeviceOrientationEvent</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"DeviceOrientation is supported"</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; window</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'deviceorientation'</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">eventData</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">var</span><span class="pln"> LR </span><span class="pun">=</span><span class="pln"> eventData</span><span class="pun">.</span><span class="pln">gamma</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">var</span><span class="pln"> FB </span><span class="pun">=</span><span class="pln"> eventData</span><span class="pun">.</span><span class="pln">beta</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">var</span><span class="pln"> DIR </span><span class="pun">=</span><span class="pln"> eventData</span><span class="pun">.</span><span class="pln">alpha</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; deviceOrientationHandler</span><span class="pun">(</span><span class="pln">LR</span><span class="pun">,</span><span class="pln"> FB</span><span class="pun">,</span><span class="pln"> DIR</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="pun">},</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; alert</span><span class="pun">(</span><span class="str">"Not supported on your device or browser. Sorry."</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="pun">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="kwd">function</span><span class="pln"> deviceOrientationHandler</span><span class="pun">(</span><span class="pln">LR</span><span class="pun">,</span><span class="pln"> FB</span><span class="pun">,</span><span class="pln"> DIR</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="com">// USE CSS3 rotations for rotating the HTML5 logo</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="com">//for webkit browser</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">"imgLogo"</span><span class="pun">).</span><span class="pln">style</span><span class="pun">.</span><span class="pln">webkitTransform </span><span class="pun">=</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="str">"rotate("</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> LR </span><span class="pun">+</span><span class="pln"> </span><span class="str">"deg) rotate3d(1,0,0, "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="pun">(</span><span class="pln">FB </span><span class="pun">*</span><span class="pln"> </span><span class="pun">-</span><span class="lit">1</span><span class="pun">)</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="str">"deg)"</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="com">//for HTML5 standard-compliance</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">"imgLogo"</span><span class="pun">).</span><span class="pln">style</span><span class="pun">.</span><span class="pln">transform </span><span class="pun">=</span><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="str">"rotate("</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> LR </span><span class="pun">+</span><span class="pln"> </span><span class="str">"deg) rotate3d(1,0,0, "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="pun">(</span><span class="pln">FB </span><span class="pun">*</span><span class="pln"> </span><span class="pun">-</span><span class="lit">1</span><span class="pun">)</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="str">"deg)"</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#LR"</span><span class="pun">).</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> </span><span class="str">"gamma : "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">round</span><span class="pun">(</span><span class="pln">LR</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#FB"</span><span class="pun">).</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> </span><span class="str">"beta : "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">round</span><span class="pun">(</span><span class="pln">FB</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#DIR"</span><span class="pun">).</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> </span><span class="str">"alpha : "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">round</span><span class="pun">(</span><span class="pln">DIR</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/script&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;...</span></li>
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
    + image container: `<img src="https://.../log.png" id="imgLogo" class="logo">
  + Javascript inline snippet: `<script type="text/javascript>...</script>`
    + check browser support of [orientation API](#getOrient)
    + tilt image to reflect device orientation: `function deviceOrientationHandler(LR, FB, DIR) {...}`
      + access image container and set style w/ webkit browser: `document.getElementById("imgLogo").style.webkitTransform = "rotate(" + LR + "deg) rotate3d(1, 0, 0 " + (FB *-1) + "deg)";`
      + access image container and set style w/ HRML5 standard-compliance: `document.getElementById("imgLogo").style.Transform = "rotate(" + LR + "deg) rotate3d(1, 0, 0 " + (FB *-1) + "deg)";`






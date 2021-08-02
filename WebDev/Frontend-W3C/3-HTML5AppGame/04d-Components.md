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
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <strong style="color: red;">window</strong></span><strong style="color: red;"><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'deviceorientation'</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">eventData</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="com">// gamme is for left/right inclination</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">var</span><span class="pln"> LR </span><span class="pun">=</span><strong style="color: red;"><span class="pln"> eventData</span><span class="pun">.</span><span class="pln">gamma</span><span class="pun">;</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="com">// beta is for front/back inclination</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">var</span><span class="pln"> FB </span><span class="pun">=</span><strong style="color: red;"><span class="pln"> eventData</span><span class="pun">.</span><span class="pln">beta</span><span class="pun">;</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="com">// alpha is for orientation</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">var</span><span class="pln"> DIR </span><span class="pun">=</span><strong style="color: red;"><span class="pln"> eventData</span><span class="pun">.</span><span class="pln">alpha</span><span class="pun">;</span></strong></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> handleMotionEvent</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="kwd">var</span><span class="pln"> x </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">event</span><span class="pun">.</span><span class="pln">accelerationIncludingGravity</span><span class="pun">.</span><span class="pln">x</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="kwd">var</span><span class="pln"> y </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">event</span><span class="pun">.</span><span class="pln">accelerationIncludingGravity</span><span class="pun">.</span><span class="pln">y</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="kwd">var</span><span class="pln"> z </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">event</span><span class="pun">.</span><span class="pln">accelerationIncludingGravity</span><span class="pun">.</span><span class="pln">z</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="com">// Process ...</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">window</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">"devicemotion"</span><span class="pun">,</span><span class="pln"> handleMotionEvent</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">);</span></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com">// For example, if acceleration.z is &gt; 0 then the phone is facing up</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> facingUp </span><span class="pun">=</span><span class="pln"> </span><span class="pun">-</span><span class="lit">1</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">acceleration</span><span class="pun">.</span><span class="pln">z </span><span class="pun">&gt;</span><span class="pln"> </span><span class="lit">0</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; facingUp </span><span class="pun">=</span><span class="pln"> </span><span class="pun">+</span><span class="lit">1</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span><span class="pln"> </span></li>
</ol></div>

Compute the angle corresponding to the Left / Right and Front / Back tilts. This example uses the `accelerationIncludingGravity` property of the event.

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> deviceMotionHandler</span><span class="pun">(</span><span class="pln">eventData</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="com">// Grab the acceleration including gravity from the results</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="kwd">var</span><span class="pln"> acceleration </span><span class="pun">=</span><span class="pln"> eventData</span><span class="pun">.</span><span class="pln">accelerationIncludingGravity</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="com">// Convert the value from acceleration to degrees </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp;// acceleration.x|y is the&nbsp;</span>acceleration according</li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="com">// &nbsp;to gravity, we'll assume we're on&nbsp;</span> Earth and divide</li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="com">// by 9.81 (earth gravity) to get a percentage value,&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="com">//&nbsp;and then multiply that&nbsp;by 90 to convert to degrees. </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="kwd">var</span><span class="pln"> tiltLR </span><span class="pun">=</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">round</span><span class="pun">(((</span><span class="pln">acceleration</span><span class="pun">.</span><span class="pln">x</span><span class="pun">)</span><span class="pln"> </span><span class="pun">/</span><span class="pln"> </span><span class="lit">9.81</span><span class="pun">)</span><span class="pln"> </span><span class="pun">*</span><span class="pln"> </span><span class="pun">-</span><span class="lit">90</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="kwd">var</span><span class="pln"> tiltFB </span><span class="pun">=</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">round</span><span class="pun">(((</span><span class="pln">acceleration</span><span class="pun">.</span><span class="pln">y </span><span class="pun">+</span><span class="pln"> </span><span class="lit">9.81</span><span class="pun">)</span><span class="pln"> </span><span class="pun">/</span><span class="pln"> </span><span class="lit">9.81</span><span class="pun">)</span><span class="pln"> </span><span class="pun">*</span><span class="pln"> </span><span class="lit">90</span><span class="pln"> </span><span class="pun">*</span><span class="pln"> facingUp</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="com">// ... do something</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

Compute the vertical (direction of the sky) - this extract comes from a complete example further down this page...

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">...</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> angle </span><span class="pun">=</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">atan2</span><span class="pun">(</span><span class="pln">accel</span><span class="pun">.</span><span class="pln">y</span><span class="pun">,</span><span class="pln">accel</span><span class="pun">.</span><span class="pln">x</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> canvas </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'myCanvas'</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> ctx </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">getContext</span><span class="pun">(</span><span class="str">'2d'</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">moveTo</span><span class="pun">(</span><span class="lit">50</span><span class="pun">,</span><span class="lit">50</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="com">// Draw sky direction in the canvas</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">lineTo</span><span class="pun">(</span><span class="lit">50</span><span class="pun">-</span><span class="lit">50</span><span class="pun">*</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">cos</span><span class="pun">(</span><span class="pln">angle</span><span class="pun">),</span><span class="lit">50</span><span class="pun">+</span><span class="lit">50</span><span class="pun">*</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">sin</span><span class="pun">(</span><span class="pln">angle</span><span class="pun">));</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">stroke</span><span class="pun">();</span></li>
</ol></div>

Use acceleration values to move a ball on the screen of a tablet when the tablet is tilted front / back or left / right (complete example later on)...

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">...</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">ball</span><span class="pun">.</span><span class="pln">x </span><span class="pun">+=</span><span class="pln"> acceleration</span><span class="pun">.</span><span class="pln">x</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">ball</span><span class="pun">.</span><span class="pln">y </span><span class="pun">+=</span><span class="pln"> acceleration</span><span class="pun">.</span><span class="pln">y</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">...</span></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!doctype html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="tag">&lt;head&gt;&lt;/head&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="tag">&lt;body&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="tag">&lt;h2&gt;</span><span class="pln">Device Orientation with HTML5</span><span class="tag">&lt;/h2&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; You need to be on a mobile device or use a laptop with accelerometer/orientation</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; device.</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="tag">&lt;p&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="tag">&lt;div</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"rawAccel"</span><span class="tag">&gt;&lt;/div&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="tag">&lt;div</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"tiltFB"</span><span class="tag">&gt;&lt;/div&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="tag">&lt;div</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"tiltLR"</span><span class="tag">&gt;&lt;/div&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="tag">&lt;div</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"upDown"</span><span class="tag">&gt;&lt;/div&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="tag">&lt;img</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://www.html5rocks.com/en/tutorials/device/orientation/html5_logo.png"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"imgLogo"</span><span class="pln"> </span><span class="atn">class</span><span class="pun">=</span><span class="atv">"logo"</span><span class="tag">&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="tag">&lt;script</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"text/javascript"</span><span class="tag">&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">window</span><span class="pun">.</span><span class="typ">DeviceMotionEvent</span><span class="pln"> </span><span class="pun">!=</span><span class="pln"> </span><span class="kwd">undefined</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"DeviceMotion is supported"</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; window</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'devicemotion'</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">eventData</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="com">// Grab the acceleration including gravity from the results</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">var</span><span class="pln"> acceleration </span><span class="pun">=</span><span class="pln"> eventData</span><span class="pun">.</span><span class="pln">accelerationIncludingGravity</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="com">// Display the raw acceleration data</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">var</span><span class="pln"> rawAcceleration </span><span class="pun">=</span><span class="pln"> </span><span class="str">"["</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">round</span><span class="pun">(</span><span class="pln">acceleration</span><span class="pun">.</span><span class="pln">x</span><span class="pun">)</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="str">", "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">round</span><span class="pun">(</span><span class="pln">acceleration</span><span class="pun">.</span><span class="pln">y</span><span class="pun">)&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="pln"></span><span class="pln"></span><span class="pun">+</span><span class="pln"> </span><span class="str">", "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">round</span><span class="pun">(</span><span class="pln">acceleration</span><span class="pun">.</span><span class="pln">z</span><span class="pun">)</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="str">"]"</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="com">// Z is the acceleration in the Z axis, and if the device </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // is facing up or down</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">var</span><span class="pln"> facingUp </span><span class="pun">=</span><span class="pln"> </span><span class="pun">-</span><span class="lit">1</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">acceleration</span><span class="pun">.</span><span class="pln">z </span><span class="pun">&gt;</span><span class="pln"> </span><span class="lit">0</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; facingUp </span><span class="pun">=</span><span class="pln"> </span><span class="pun">+</span><span class="lit">1</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="pun">}</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="com">// Convert the value from acceleration to degrees </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // acceleration.x|y is the&nbsp;</span>acceleration according to gravity,</li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="com">// &nbsp;we'll assume we're on Earth and divide </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="com">// by 9.81 (earth gravity) to get a percentage value, &nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="com">//&nbsp;and then multiply that&nbsp;by 90 to convert to degrees. </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">var</span><span class="pln"> tiltLR </span><span class="pun">=</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">round</span><span class="pun">(((</span><span class="pln">acceleration</span><span class="pun">.</span><span class="pln">x</span><span class="pun">)</span><span class="pln"> </span><span class="pun">/</span><span class="pln"> </span><span class="lit">9.81</span><span class="pun">)</span><span class="pln"> </span><span class="pun">*</span><span class="pln"> </span><span class="pun">-</span><span class="lit">90</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">var</span><span class="pln"> tiltFB </span><span class="pun">=</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">round</span><span class="pun">(((</span><span class="pln">acceleration</span><span class="pun">.</span><span class="pln">y </span><span class="pun">+</span><span class="pln"> </span><span class="lit">9.81</span><span class="pun">)</span><span class="pln"> </span><span class="pun">/</span><span class="pln"> </span><span class="lit">9.81</span><span class="pun">)</span><span class="pln"> </span><span class="pun">*</span><span class="pln"> </span><span class="lit">90</span><span class="pln"> </span><span class="pun">*</span><span class="pln"> facingUp</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#rawAccel"</span><span class="pun">).</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="str">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"Raw acceleration"</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> rawAcceleration</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#tiltFB"</span><span class="pun">).</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="str">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"Tilt front/back : "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> tiltFB</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#tiltLR"</span><span class="pun">).</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="str">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"Tilt left/right : "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> tiltLR</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#upDown"</span><span class="pun">).</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="str">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"Face Up:Down : "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> facingUp</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; updateLogoOrientation</span><span class="pun">(</span><span class="pln">tiltLR</span><span class="pun">,</span><span class="pln"> tiltFB</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="pun">},</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; alert</span><span class="pun">(</span><span class="str">"Not supported on your device or browser. Sorry."</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="pun">}</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">function</span><span class="pln"> updateLogoOrientation</span><span class="pun">(</span><span class="pln">tiltLR</span><span class="pun">,</span><span class="pln"> tiltFB</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="com">// USE CSS3 rotations for rotating the HTML5 logo</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="com">//for webkit browser</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">"imgLogo"</span><span class="pun">).</span><span class="pln">style</span><span class="pun">.</span><span class="pln">webkitTransform </span><span class="pun">=</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="str">"rotate("</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> tiltLR </span><span class="pun">+</span><span class="pln"> </span><span class="str">"deg) rotate3d(1,0,0, "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="pun">(</span><span class="pln">tiltFB </span><span class="pun">*</span><span class="pln"> </span><span class="pun">-</span><span class="lit">1</span><span class="pun">)</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="str">"deg)"</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="com">//for HTML5 standard-compliance</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">"imgLogo"</span><span class="pun">).</span><span class="pln">style</span><span class="pun">.</span><span class="pln">transform </span><span class="pun">=</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="str">"rotate("</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> tiltLR </span><span class="pun">+</span><span class="pln"> </span><span class="str">"deg) rotate3d(1,0,0, "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="pun">(</span><span class="pln">tiltFB </span><span class="pun">*</span><span class="pln"> </span><span class="pun">-</span><span class="lit">1</span><span class="pun">)</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="str">"deg)"</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="pun">}</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="tag">&lt;/script&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="tag">&lt;/body&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;html&gt;</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&nbsp;&nbsp; &lt;head&gt;</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; &nbsp; </span><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">http-equiv</span><span class="pun">=</span><span class="atv">"content-type"</span><span class="pln"> </span><span class="atn">content</span><span class="pun">=</span><span class="atv">"text/html; charset=utf-8"</span><span class="tag">&gt;</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">name</span><span class="pun">=</span><span class="atv">"viewport"</span><span class="pln"> </span><span class="atn">content</span><span class="pun">=</span><span class="atv">"user-scalable=no, width=device-width"</span><span class="pln"> </span><span class="tag">/&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="tag">&lt;link</span><span class="pln"> </span><span class="atn">rel</span><span class="pun">=</span><span class="atv">"stylesheet"</span><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;href</span><span class="pun">=</span><span class="atv">"https://code.jquery.com/mobile/1.0b2/jquery.mobile-1.0b2.min.css"</span><span class="pln"> </span><span class="tag">/&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="tag">&lt;script</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"text/javascript"</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;src</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> </span><span class="atv">"https://code.jquery.com/jquery-1.6.2.min.js"</span><span class="tag">&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp; &nbsp;&lt;/script&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="tag">&lt;script</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"text/javascript"</span><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;src</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> </span><span class="atv">"https://code.jquery.com/mobile/1.0b2/jquery.mobile-1.0b2.min.js"</span><span class="tag">&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp; &nbsp;&lt;/script&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="tag">&lt;script</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"text/javascript"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $</span><span class="pun">(</span><span class="pln">document</span><span class="pun">).</span><span class="pln">ready</span><span class="pun">(</span><span class="kwd">function</span><span class="pun">(){</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; window</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">"devicemotion"</span><span class="pun">,</span><span class="pln">onDeviceMotion</span><span class="pun">,</span><span class="kwd">false</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="pun">});</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">function</span><span class="pln"> onDeviceMotion</span><span class="pun">(</span><span class="pln">event</span><span class="pun">){</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">var</span><span class="pln"> ctx </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">"c"</span><span class="pun">).</span><span class="pln">getContext</span><span class="pun">(</span><span class="str">"2d"</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">var</span><span class="pln"> accel </span><span class="pun">=</span><span class="pln"> event</span><span class="pun">.</span><span class="pln">accelerationIncludingGravity</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $</span><span class="pun">(</span><span class="str">"#sliderX"</span><span class="pun">).</span><span class="pln">val</span><span class="pun">(</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">round</span><span class="pun">(</span><span class="pln">accel</span><span class="pun">.</span><span class="pln">x</span><span class="pun">)).</span><span class="pln">slider</span><span class="pun">(</span><span class="str">"refresh"</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $</span><span class="pun">(</span><span class="str">"#sliderY"</span><span class="pun">).</span><span class="pln">val</span><span class="pun">(</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">round</span><span class="pun">(</span><span class="pln">accel</span><span class="pun">.</span><span class="pln">y</span><span class="pun">)).</span><span class="pln">slider</span><span class="pun">(</span><span class="str">"refresh"</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $</span><span class="pun">(</span><span class="str">"#sliderZ"</span><span class="pun">).</span><span class="pln">val</span><span class="pun">(</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">round</span><span class="pun">(</span><span class="pln">accel</span><span class="pun">.</span><span class="pln">z</span><span class="pun">)).</span><span class="pln">slider</span><span class="pun">(</span><span class="str">"refresh"</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="com">// sky direction</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">var</span><span class="pln"> angle </span><span class="pun">=</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">atan2</span><span class="pun">(</span><span class="pln">accel</span><span class="pun">.</span><span class="pln">y</span><span class="pun">,</span><span class="pln">accel</span><span class="pun">.</span><span class="pln">x</span><span class="pun">)</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ctx</span><span class="pun">.</span><span class="pln">clearRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="lit">0</span><span class="pun">,</span><span class="lit">100</span><span class="pun">,</span><span class="lit">100</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ctx</span><span class="pun">.</span><span class="pln">beginPath</span><span class="pun">();</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ctx</span><span class="pun">.</span><span class="pln">arc</span><span class="pun">(</span><span class="lit">50</span><span class="pun">,</span><span class="lit">50</span><span class="pun">,</span><span class="lit">5</span><span class="pun">,</span><span class="lit">0</span><span class="pun">,</span><span class="lit">2</span><span class="pun">*</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">PI</span><span class="pun">,</span><span class="kwd">false</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ctx</span><span class="pun">.</span><span class="pln">moveTo</span><span class="pun">(</span><span class="lit">50</span><span class="pun">,</span><span class="lit">50</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="com">// Draw sky direction</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ctx</span><span class="pun">.</span><span class="pln">lineTo</span><span class="pun">(</span><span class="lit">50</span><span class="pun">-</span><span class="lit">50</span><span class="pun">*</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">cos</span><span class="pun">(</span><span class="pln">angle</span><span class="pun">),</span><span class="lit">50</span><span class="pun">+</span><span class="lit">50</span><span class="pun">*</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">sin</span><span class="pun">(</span><span class="pln">angle</span><span class="pun">));</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ctx</span><span class="pun">.</span><span class="pln">stroke</span><span class="pun">();</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="pun">}</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="tag">&lt;/script&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&nbsp;&nbsp; &lt;/head&gt;</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&nbsp;&nbsp; &lt;body&gt;</span><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;div</span><span class="pln"> </span><span class="atn">data-role</span><span class="pun">=</span><span class="atv">"page"</span><span class="pln"> </span><span class="atn">id</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> </span><span class="atv">"intropage"</span><span class="tag">&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; </span><span class="tag">&lt;div</span><span class="pln"> </span><span class="atn">data-role</span><span class="pun">=</span><span class="atv">"header"</span><span class="tag">&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="tag">&lt;h1&gt;</span><span class="pln">Accelerometer</span><span class="tag">&lt;/h1&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="tag">&lt;/div&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="tag">&lt;div</span><span class="pln"> </span><span class="atn">data-role</span><span class="pun">=</span><span class="atv">"content"</span><span class="tag">&gt;</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="tag">&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"sliderX"</span><span class="tag">&gt;</span><span class="pln">X Acceleration (Roll)</span><span class="tag">&lt;/label&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"range"</span><span class="pln"> </span><span class="atn">name</span><span class="pun">=</span><span class="atv">"sliderX"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"sliderX"</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; value</span><span class="pun">=</span><span class="atv">"0"</span><span class="pln"> </span><span class="atn">min</span><span class="pun">=</span><span class="atv">"-10"</span><span class="pln"> </span><span class="atn">max</span><span class="pun">=</span><span class="atv">"10"</span><span class="pln"> </span><span class="atn">data-theme</span><span class="pun">=</span><span class="atv">"a"</span><span class="pln"> </span><span class="tag">/&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="tag">&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"sliderY"</span><span class="tag">&gt;</span><span class="pln">Y Acceleration (Pitch)</span><span class="tag">&lt;/label&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"range"</span><span class="pln"> </span><span class="atn">name</span><span class="pun">=</span><span class="atv">"sliderY"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"sliderY"</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; value</span><span class="pun">=</span><span class="atv">"0"</span><span class="pln"> </span><span class="atn">min</span><span class="pun">=</span><span class="atv">"-10"</span><span class="pln"> </span><span class="atn">max</span><span class="pun">=</span><span class="atv">"10"</span><span class="pln"> </span><span class="atn">data-theme</span><span class="pun">=</span><span class="atv">"b"</span><span class="pln"> </span><span class="tag">/&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="tag">&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"sliderZ"</span><span class="tag">&gt;</span><span class="pln">Z Acceleration (</span><span class="tag">&lt;strike&gt;</span><span class="pln">Yaw</span><span class="tag">&lt;/strike&gt;</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Face up/down)</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&lt;/label&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"range"</span><span class="pln"> </span><span class="atn">name</span><span class="pun">=</span><span class="atv">"sliderZ"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"sliderZ"</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; value</span><span class="pun">=</span><span class="atv">"0"</span><span class="pln"> </span><span class="atn">min</span><span class="pun">=</span><span class="atv">"-10"</span><span class="pln"> </span><span class="atn">max</span><span class="pun">=</span><span class="atv">"10"</span><span class="pln"> </span><span class="atn">data-theme</span><span class="pun">=</span><span class="atv">"c"</span><span class="pln"> </span><span class="tag">/&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="tag">&lt;/div&gt;</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="tag">&lt;p</span><span class="pln"> </span><span class="atn">style</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> </span><span class="atv">"</span><span class="pln">text</span><span class="pun">-</span><span class="pln">align</span><span class="pun">:</span><span class="pln">center</span><span class="atv">"</span><span class="tag">&gt;</span><span class="pln">SKY direction: </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; follow this line:</span><span class="tag">&lt;/p&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="tag">&lt;div</span><span class="pln"> </span><span class="atn">style</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> </span><span class="atv">"</span><span class="pln">text</span><span class="pun">-</span><span class="pln">align</span><span class="pun">:</span><span class="pln">center</span><span class="pun">;</span><span class="pln">margin</span><span class="pun">-</span><span class="pln">top</span><span class="pun">:</span><span class="lit">10px</span><span class="pun">;</span><span class="atv">"</span><span class="tag">&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="tag">&lt;canvas</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"c"</span><span class="pln"> </span><span class="atn">width</span><span class="pun">=</span><span class="atv">"100"</span><span class="pln"> </span><span class="atn">height</span><span class="pun">=</span><span class="atv">"100"</span><span class="tag">&gt;&lt;/canvas&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="tag">&lt;/div&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="tag">&nbsp;&nbsp;&nbsp;&nbsp; &lt;/div&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&nbsp;&nbsp; &lt;/body&gt;</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "https://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">xmlns</span><span class="pun">=</span><span class="atv">"https://www.w3.org/1999/xhtml"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp; </span><span class="tag">&lt;head&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">http-equiv</span><span class="pun">=</span><span class="atv">"Content-Type"</span><span class="pln"> </span><span class="atn">content</span><span class="pun">=</span><span class="atv">"text/html; charset=UTF-8"</span><span class="pln"> </span><span class="tag">/&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">name</span><span class="pun">=</span><span class="atv">"viewport"</span><span class="pln"> </span><span class="atn">content</span><span class="pun">=</span><span class="atv">"width=device-width, </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="atv">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; target-densityDpi=device-dpi, </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="atv">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; initial-scale=1.0, </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="atv">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; user-scalable=no, </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="atv">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; maximum-scale=1.0"</span><span class="tag">&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="tag">&lt;title&gt;</span><span class="pln">iOS 4.2 Device Accellerometer</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="tag">&lt;style&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; body </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; font</span><span class="pun">-</span><span class="pln">family</span><span class="pun">:</span><span class="typ">Arial</span><span class="pun">,</span><span class="pln"> </span><span class="typ">Helvetica</span><span class="pun">,</span><span class="pln"> sans</span><span class="pun">-</span><span class="pln">serif</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; font</span><span class="pun">-</span><span class="pln">size</span><span class="pun">:</span><span class="pln"> </span><span class="lit">14px</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="pun">}</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="com">#board {</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; position</span><span class="pun">:</span><span class="pln">absolute</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; left</span><span class="pun">:</span><span class="lit">0px</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; right</span><span class="pun">:</span><span class="lit">0px</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; top</span><span class="pun">:</span><span class="lit">0px</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; bottom</span><span class="pun">:</span><span class="lit">0px</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="com">#ball {</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; position</span><span class="pun">:</span><span class="pln">absolute</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; width</span><span class="pun">:</span><span class="pln"> </span><span class="lit">60px</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; height</span><span class="pun">:</span><span class="pln"> </span><span class="lit">60px</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; border</span><span class="pun">-</span><span class="pln">radius</span><span class="pun">:</span><span class="pln"> </span><span class="lit">30px</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; background</span><span class="pun">-</span><span class="pln">image</span><span class="pun">:</span><span class="pln"> </span><span class="pun">-</span><span class="pln">webkit</span><span class="pun">-</span><span class="pln">gradient</span><span class="pun">(</span><span class="pln">radial</span><span class="pun">,</span><span class="pln"> </span><span class="lit">45</span><span class="pun">%</span><span class="pln"> </span><span class="lit">45</span><span class="pun">%,</span><span class="pln"> </span><span class="lit">5</span><span class="pun">,</span><span class="pln"> </span><span class="lit">60</span><span class="pun">%</span><span class="pln"> </span><span class="lit">60</span><span class="pun">%,</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="lit">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 40</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">from</span><span class="pun">(</span><span class="pln">red</span><span class="pun">),</span><span class="pln"> color</span><span class="pun">-</span><span class="pln">stop</span><span class="pun">(</span><span class="lit">75</span><span class="pun">%,</span><span class="pln"> black</span><span class="pun">),</span><span class="pln"> to</span><span class="pun">(</span><span class="pln">rgba</span><span class="pun">(</span><span class="lit">255</span><span class="pun">,</span><span class="pln"> </span><span class="lit">255</span><span class="pun">,</span><span class="pln"> </span><span class="lit">255</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">)));</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="pun">-</span><span class="pln">webkit</span><span class="pun">-</span><span class="pln">box</span><span class="pun">-</span><span class="pln">shadow</span><span class="pun">:</span><span class="pln"> </span><span class="lit">3px</span><span class="pln"> </span><span class="lit">3px</span><span class="pln"> </span><span class="lit">5px</span><span class="pln"> </span><span class="com">#888;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="pun">}</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="tag">&lt;/style&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="tag">&lt;script</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"</span><span class="tag">&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp; &nbsp; &nbsp;&lt;/script&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="tag">&lt;script&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="pun">!</span><span class="pln">window</span><span class="pun">.</span><span class="pln">jQuery </span><span class="pun">&amp;&amp;</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">write</span><span class="pun">(</span><span class="str">'&lt;script src="./js/jquery.min.js"&gt;&lt;\/script&gt;'</span><span class="pun">)</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="tag">&lt;/script&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="tag">&lt;script&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">var</span><span class="pln"> offset</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">var</span><span class="pln"> velocity</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">var</span><span class="pln"> board</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">var</span><span class="pln"> ball</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">var</span><span class="pln"> interval</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $</span><span class="pun">(</span><span class="pln">document</span><span class="pun">).</span><span class="pln">ready</span><span class="pun">(</span><span class="kwd">function</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; window</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">"devicemotion"</span><span class="pun">,</span><span class="pln"> onDeviceMotion</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $</span><span class="pun">(</span><span class="str">'#timestamp'</span><span class="pun">).</span><span class="pln">html</span><span class="pun">(</span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Date</span><span class="pun">().</span><span class="pln">toString</span><span class="pun">());</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $</span><span class="pun">(</span><span class="str">'#status'</span><span class="pun">).</span><span class="pln">html</span><span class="pun">(</span><span class="str">"Ready!"</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; velocity </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{};</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; velocity</span><span class="pun">.</span><span class="pln">x </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; velocity</span><span class="pun">.</span><span class="pln">y </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; offset </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{};</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; board </span><span class="pun">=</span><span class="pln"> $</span><span class="pun">(</span><span class="str">'#board'</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ball </span><span class="pun">=</span><span class="pln"> $</span><span class="pun">(</span><span class="str">'#ball'</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; offset</span><span class="pun">.</span><span class="pln">left </span><span class="pun">=</span><span class="pln"> </span><span class="pun">(</span><span class="pln">board</span><span class="pun">.</span><span class="pln">width</span><span class="pun">()</span><span class="pln"> </span><span class="pun">-</span><span class="pln"> ball</span><span class="pun">.</span><span class="pln">width</span><span class="pun">())</span><span class="pln"> </span><span class="pun">/</span><span class="pln"> </span><span class="lit">2</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; offset</span><span class="pun">.</span><span class="pln">top </span><span class="pun">=</span><span class="pln"> </span><span class="pun">(</span><span class="pln">board</span><span class="pun">.</span><span class="pln">height</span><span class="pun">()</span><span class="pln"> </span><span class="pun">-</span><span class="pln"> ball</span><span class="pun">.</span><span class="pln">height</span><span class="pun">())</span><span class="pln"> </span><span class="pun">/</span><span class="pln"> </span><span class="lit">2</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $</span><span class="pun">(</span><span class="str">'#ball'</span><span class="pun">).</span><span class="pln">offset</span><span class="pun">(</span><span class="pln">offset</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; interval </span><span class="pun">=</span><span class="pln"> setInterval</span><span class="pun">(</span><span class="pln">updateBall</span><span class="pun">,</span><span class="pln"> </span><span class="lit">25</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="pun">});</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">function</span><span class="pln"> onDeviceMotion</span><span class="pun">(</span><span class="pln">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $</span><span class="pun">(</span><span class="str">'#timestamp'</span><span class="pun">).</span><span class="pln">html</span><span class="pun">(</span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Date</span><span class="pun">().</span><span class="pln">toString</span><span class="pun">());</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $</span><span class="pun">(</span><span class="str">'#status'</span><span class="pun">).</span><span class="pln">html</span><span class="pun">(</span><span class="str">"Device Motion Event"</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">var</span><span class="pln"> eventDetails</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">try</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">var</span><span class="pln"> accel </span><span class="pun">=</span><span class="pln"> event</span><span class="pun">.</span><span class="pln">accelerationIncludingGravity</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; eventDetails </span><span class="pun">=</span><span class="pln"> </span><span class="str">"accelerationIncludingGravity: {"</span><span class="pln"> </span><span class="pun">+</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="str">"&lt;br&gt;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x: "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> accel</span><span class="pun">.</span><span class="pln">x </span><span class="pun">+</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="str">"&lt;br&gt;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;y: "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> accel</span><span class="pun">.</span><span class="pln">y </span><span class="pun">+</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="str">"&lt;br&gt;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;z: "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> accel</span><span class="pun">.</span><span class="pln">z </span><span class="pun">+</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="str">"&lt;br/&gt;} &lt;br/&gt;&lt;br/&gt;"</span><span class="pln"> </span><span class="pun">+</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="str">"interval: "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> event</span><span class="pun">.</span><span class="pln">interval</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; updateVelocity</span><span class="pun">(</span><span class="pln">event</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="pun">}</span><span class="pln"> </span><span class="kwd">catch</span><span class="pln"> </span><span class="pun">(</span><span class="pln">e</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; eventDetails </span><span class="pun">=</span><span class="pln"> e</span><span class="pun">.</span><span class="pln">toString</span><span class="pun">();</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $</span><span class="pun">(</span><span class="str">'#details'</span><span class="pun">).</span><span class="pln">html</span><span class="pun">(</span><span class="pln">eventDetails</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">var</span><span class="pln"> decay </span><span class="pun">=</span><span class="pln"> </span><span class="pun">.</span><span class="lit">9</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">var</span><span class="pln"> bounceDecay </span><span class="pun">=</span><span class="pln"> </span><span class="pun">.</span><span class="lit">95</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">var</span><span class="pln"> maxVelocity </span><span class="pun">=</span><span class="pln"> </span><span class="lit">100</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">function</span><span class="pln"> updateVelocity</span><span class="pun">(</span><span class="pln">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; velocity</span><span class="pun">.</span><span class="pln">x </span><span class="pun">+=</span><span class="pln"> event</span><span class="pun">.</span><span class="pln">accelerationIncludingGravity</span><span class="pun">.</span><span class="pln">x</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">abs</span><span class="pun">(</span><span class="pln">velocity</span><span class="pun">.</span><span class="pln">x</span><span class="pun">)</span><span class="pln"> </span><span class="pun">&gt;</span><span class="pln"> maxVelocity</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">velocity</span><span class="pun">.</span><span class="pln">x </span><span class="pun">&gt;</span><span class="pln"> </span><span class="lit">0</span><span class="pun">)</span><span class="pln"> velocity</span><span class="pun">.</span><span class="pln">x </span><span class="pun">=</span><span class="pln"> maxVelocity</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">else</span><span class="pln"> velocity</span><span class="pun">.</span><span class="pln">x </span><span class="pun">=</span><span class="pln"> </span><span class="pun">-</span><span class="pln">maxVelocity</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="pun">}</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; velocity</span><span class="pun">.</span><span class="pln">y </span><span class="pun">+=</span><span class="pln"> event</span><span class="pun">.</span><span class="pln">accelerationIncludingGravity</span><span class="pun">.</span><span class="pln">y</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">abs</span><span class="pun">(</span><span class="pln">velocity</span><span class="pun">.</span><span class="pln">y</span><span class="pun">)</span><span class="pln"> </span><span class="pun">&gt;</span><span class="pln"> maxVelocity</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">velocity</span><span class="pun">.</span><span class="pln">y </span><span class="pun">&gt;</span><span class="pln"> </span><span class="lit">0</span><span class="pun">)</span><span class="pln"> velocity</span><span class="pun">.</span><span class="pln">y </span><span class="pun">=</span><span class="pln"> maxVelocity</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">else</span><span class="pln"> velocity</span><span class="pun">.</span><span class="pln">y </span><span class="pun">=</span><span class="pln"> </span><span class="pun">-</span><span class="pln">maxVelocity</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="pun">}</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">function</span><span class="pln"> updateBall</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">offset</span><span class="pun">.</span><span class="pln">left </span><span class="pun">&lt;=</span><span class="pln"> </span><span class="pun">-(</span><span class="pln">ball</span><span class="pun">.</span><span class="pln">width</span><span class="pun">()</span><span class="pln"> </span><span class="pun">/</span><span class="pln"> </span><span class="lit">2</span><span class="pun">))</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; velocity</span><span class="pun">.</span><span class="pln">x </span><span class="pun">=</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">abs</span><span class="pun">(</span><span class="pln">velocity</span><span class="pun">.</span><span class="pln">x </span><span class="pun">*</span><span class="pln"> bounceDecay</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">offset</span><span class="pun">.</span><span class="pln">left </span><span class="pun">&gt;=</span><span class="pln"> </span><span class="pun">(</span><span class="pln">board</span><span class="pun">.</span><span class="pln">width</span><span class="pun">()</span><span class="pln"> </span><span class="pun">-</span><span class="pln"> </span><span class="pun">(</span><span class="pln">ball</span><span class="pun">.</span><span class="pln">width</span><span class="pun">()</span><span class="pln"> </span><span class="pun">/</span><span class="pln"> </span><span class="lit">2</span><span class="pun">)))</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; velocity</span><span class="pun">.</span><span class="pln">x </span><span class="pun">=</span><span class="pln"> </span><span class="pun">-</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">abs</span><span class="pun">(</span><span class="pln">velocity</span><span class="pun">.</span><span class="pln">x </span><span class="pun">*</span><span class="pln"> bounceDecay</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; velocity</span><span class="pun">.</span><span class="pln">x </span><span class="pun">=</span><span class="pln"> parseInt</span><span class="pun">(</span><span class="pln">velocity</span><span class="pun">.</span><span class="pln">x</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; velocity</span><span class="pun">.</span><span class="pln">x </span><span class="pun">*=</span><span class="pln"> decay</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="pun">}</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">offset</span><span class="pun">.</span><span class="pln">top </span><span class="pun">&lt;=</span><span class="pln"> </span><span class="pun">-(</span><span class="pln">ball</span><span class="pun">.</span><span class="pln">height</span><span class="pun">()</span><span class="pln"> </span><span class="pun">/</span><span class="pln"> </span><span class="lit">2</span><span class="pun">))</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; velocity</span><span class="pun">.</span><span class="pln">y </span><span class="pun">=</span><span class="pln"> </span><span class="pun">-</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">abs</span><span class="pun">(</span><span class="pln">velocity</span><span class="pun">.</span><span class="pln">y </span><span class="pun">*</span><span class="pln"> bounceDecay</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">offset</span><span class="pun">.</span><span class="pln">top </span><span class="pun">&gt;=</span><span class="pln"> </span><span class="pun">(</span><span class="pln">board</span><span class="pun">.</span><span class="pln">height</span><span class="pun">()</span><span class="pln"> </span><span class="pun">-</span><span class="pln"> </span><span class="pun">(</span><span class="pln">ball</span><span class="pun">.</span><span class="pln">height</span><span class="pun">()</span><span class="pln"> </span><span class="pun">/</span><span class="pln"> </span><span class="lit">2</span><span class="pun">)))</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; velocity</span><span class="pun">.</span><span class="pln">y </span><span class="pun">=</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">abs</span><span class="pun">(</span><span class="pln">velocity</span><span class="pun">.</span><span class="pln">y </span><span class="pun">*</span><span class="pln"> bounceDecay</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; velocity</span><span class="pun">.</span><span class="pln">y </span><span class="pun">=</span><span class="pln"> parseInt</span><span class="pun">(</span><span class="pln">velocity</span><span class="pun">.</span><span class="pln">y</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; velocity</span><span class="pun">.</span><span class="pln">y </span><span class="pun">*=</span><span class="pln"> decay</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; offset</span><span class="pun">.</span><span class="pln">left </span><span class="pun">+=</span><span class="pln"> velocity</span><span class="pun">.</span><span class="pln">x</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; offset</span><span class="pun">.</span><span class="pln">top </span><span class="pun">-=</span><span class="pln"> velocity</span><span class="pun">.</span><span class="pln">y</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $</span><span class="pun">(</span><span class="str">'#ball'</span><span class="pun">).</span><span class="pln">offset</span><span class="pun">(</span><span class="pln">offset</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="pun">}</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp; </span><span class="tag">&lt;/script&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="tag">&lt;/head&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="tag">&lt;body&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="tag">&lt;div</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"timestamp"</span><span class="tag">&gt;&lt;/div&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="tag">&lt;div</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"status"</span><span class="tag">&gt;&lt;/div&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="tag">&lt;div</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"details"</span><span class="tag">&gt;&lt;/div&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="tag">&lt;div</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"board"</span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="tag">&lt;div</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"ball"</span><span class="tag">&gt;&lt;/div&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="tag">&lt;/div&gt;</span><span class="pln">spec: </span><span class="tag">&lt;a</span><span class="pln"> </span><span class="atn">href</span><span class="pun">=</span><span class="atv">"https://w3c.github.io/deviceorientation/spec-source-orientation.html"</span><span class="pln"> </span><span class="atn">target</span><span class="pun">=</span><span class="atv">"https://w3c.github.io/deviceorientation/spec-source-orientation.html"</span><span class="tag">&gt;</span><span class="pln">https://w3c.github.io/deviceorientation/spec-source-orientation.html</span><span class="tag">&lt;/a&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="tag">&lt;/body&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
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
    + container for image: `<img src="https://.../logo.png" id="imglogo" class="logo">`
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






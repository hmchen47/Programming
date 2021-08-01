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


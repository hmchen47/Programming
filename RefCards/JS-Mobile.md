# Mobile Related Issues and APIs


## Mobile Coordinate System

+ [Rotations](../WebDev/Frontend-W3C/3-HTML5AppGame/04d-Components.md#442-the-coordinate-system)
  + using right-hand convention
  + positive rotation around an axis clockwise while viewed along the positive direction of the axis
  + always think of looking down
    + at your feet on the ground
    + at a device (or map) lying flat on a table
  + clockwise rotation as a positive number while anti-clockwise as a negative
  + rotations measured in degrees

+ [Rotations and unified coordinate](../WebDev/Frontend-W3C/3-HTML5AppGame/04d-Components.md#442-the-coordinate-system)
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



## Acceleration

+ [Acceleration](../WebDev/Frontend-W3C/3-HTML5AppGame/04d-Components.md#444-the-device-motion-api)
  + `deviceMotion` API similar to the `orientation` API
  + returning both the rotation infomation and aceration information
  + reflecting the device's actual movement
  + containing 3 parts: along the x axis, along the y axis, and along the z axis
  + unit: $m/s^2 \sim 3.281 ft/s^2$
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




## The Orientation API

+ [HTML5 orientation API overview](../WebDev/Frontend-W3C/3-HTML5AppGame/04d-Components.md#441-the-orientation-api)
  + a way to use angle measures provided by accelerometers form mobile devices or desktops such as MacBook
  + mobile device emulation mode: able to use the devtools of a desktop browser to fake the orientation values

+ [HTML5 orientation API](../WebDev/Frontend-W3C/3-HTML5AppGame/04d-Components.md#443-get-different-angles)
  + typical procedure
    + test if browser supports the orientation API w/ `window.DeviceOrientationEvent !== null`
    + define listener for the `deviceorientation` event: `window.addEventListener('deviceorientation', callback, false);` w/ the callback function accepting the event object as its single input parameter
    + extract the angles from the events: the properties, `alpha`, `beta` and `gamma`
  + incorporating w/ `WebSockets`:
    + sending the real-time device orientation to server via `WebSockets`
    + server sending the orientation to a client running on a desktop browser
    + allowing multiple devices connecting to the server and chatting together

+ Example: [device orientation in standalone version](../WebDev/Frontend-W3C/3-HTML5AppGame/04d-Components.md#443-get-different-angles)

+ Example: [device orintation w/ image](../WebDev/Frontend-W3C/3-HTML5AppGame/04d-Components.md#443-get-different-angles)


## The Device Motion API

+ [The `deviceMotion` API](../WebDev/Frontend-W3C/3-HTML5AppGame/04d-Components.md#444-the-device-motion-api)
  + dealing w/ the acceleration instead of orientation only
  + use cases proposed
    + __controlling a game:__ a gaming Web application monitors the device's orientation and interprets tilting in a certain direction as a means to control an on-screen sprite
    + __gesture recognition:__ a Web application monitors the device's acceleration and applies signal processing in order to recognize certain specific gesture
    + __mapping:__ a mapping Web application uses the device's orientation to correctly align the map w/ reality
  + basic syntax: 
    + handle motion event: `function handleMotionEvent(evt) {...}`
      + x-axis: `var x = evt.accelerationIncludingGravity.x;`
      + y-axis: `var y = evt.accelerationIncludingGravity.y;`
      + z-axis: `var z = evt.accelerationIncludingGravity.z;`
      + process: `// processing w. x, y, and z ...`
    + add even listener for device motion: `window.addEventListener('devicemotion', handleMotionEvent, true);`

+ [Common procedure for acceleration](../WebDev/Frontend-W3C/3-HTML5AppGame/04d-Components.md#444-the-device-motion-api)
  + test if the API supported by the browser
  + add a listener for `devicemotion` event
  + get the acceleration values form the DOM event
  + process the data

+ [Common processing w/ acceleration values](../WebDev/Frontend-W3C/3-HTML5AppGame/04d-Components.md#444-the-device-motion-api)
  + `acceleration.z` property:
    + acceleration.z $> 0$: device facing up
    + acceleration.z $\le 0$: device facing down
  + typical snippet for `acceleration.z` property<a name="facingUp"></a>
    + declare facing up variable: `var facingUp = -1;`
    + check `acceleration.z` property: `if (acceleration.z > 0) { facingUp = +1; }`
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

+ Example: [displaying logo up when tilting](../WebDev/Frontend-W3C/3-HTML5AppGame/04d-Components.md#444-the-device-motion-api)

+ Example: [orientations w/ X, Y, and Z accelerations](../WebDev/Frontend-W3C/3-HTML5AppGame/04d-Components.md#444-the-device-motion-api)

+ Example: [moving ball on mobile screen](../WebDev/Frontend-W3C/3-HTML5AppGame/04d-Components.md#444-the-device-motion-api)
 






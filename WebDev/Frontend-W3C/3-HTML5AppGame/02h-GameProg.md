# Module 2: Game programming with HTML5 section


## 2.8 Exercises - Module 2 (12 Questions)

### 2.8.1 User interaction (1-4)

1. Listen in the loop?

  What is the best way to deal with multiple events (multiple keys + mouse buttons, movements, etc.) at the same time?

  a. Use a global object to store the state of the input keys, check it in the mainloop, update the x and y position of the player accordingly<br>
  b. Update the x and y position of the player directly in the input event listeners<br>

  Ans: a<br>
  Explanation: In the mainloop, the best practice is to check the states of the different input devices. This is done very quickly and produces smooth movements: the left key is down. Then do x = x-1, and this is done sixty times per second -> smooth movement. On the other hand, changing x and y in the listeners is a bad idea: keep a key pressed and you will enter in the listener maybe 10 times per second, producing a sluggish animation.


2. Gamepad updated or not....

  In order to get the gamepad(s) status (buttons, joysticks) up to date, is it best practice to call navigator.getGamepads() regularly (in the game loop, for example)?

  a. Yes.<br>
  b. No, it's not necessary: once you get a reference to a gamepad (for example, in the gamepadconnected event listener), its state reflects its current status. It's updated automatically by the browser.<br>

  Ans: a<br>
  Explanation:
    + In the course's examples, we check for connected gamepads every 1/60th second, and we update the gamepad global variable with the first gamepad object returned by the browser. We need to do this as what we get is a "snapshot" of the gamepad state, with fixed values for the buttons, axes, etc. If we want to check the current button and joystick statuses, we need to poll the browser at a high frequency and ask for an updated snapshot.
    + From the specification: "getGamepads retrieves a snapshot of the data for the the currently connected and interacted-with gamepads."


3. Axes values?

  The values of the gamepad axes are...?

  a. Between -5 and +5<br>
  b. Between -1 and +1<br>
  c. Between 1 and 0<br>

  Ans: b<br>
  Explanation: These values, between -1 and +1, correspond to the cosinus or the sinus of the angle made by the joystick.


4. Trigger me!

  How do you test if a gamepad button is analog (eg an R2 or L2 trigger on a XBox 360 or PS2/PS3 gamepad)?

  a. We test if the button's property `pressed` is true, then if its `value` property is defined. This property gives the pressure on the trigger.<br>
  b. Analog buttons are considered as axes.<br>

  Ans: a<br>
  Explanation: Let `b` be a gamepad button. If `b.pressed` is true, then `b` is pressed. If `b.value` is defined, then `b` is an analog trigger and `b.value` is a floating point value between 0 and 1.


### 2.8.2 Time-based animation (5-8)

5. What time is it?

  A graphic object moves across the screen. With time-based animation, how quickly does it move?

  a. It will remain constant<br>
  b. It will depend on the device running the script<br>

  Ans: a<br>
  Explanation: With time-based animation, we compute the time that has elapsed between the previous frame drawn and the current one, and depending on this delta of time, we adjust the distance we move objects on the screen so that their speed in pixels per second remains constant.


6. Setting the frame rate

  We have a mainloop that targets 60 frames/second and we use the `requestAnimationFrame` API for implementing it. How can we set the frame rate to nearly 37 frames/s, for example?

  a. We can measure the deltas of time between frames, and sum them up. If the sum is superior to the delay that corresponds to 1/37s, then we draw the frame, otherwise we do nothing.<br>
  b. We should stop using `requestAnimationFrame` and use `setInterval` instead - it's better.<br>
  c. We can't.<br>

  Ans: a<br>
  Explanation: The mainloop, for all the reasons explained during the HTML5 Part 1 course, should use the `requestAnimation` API. In order not to draw at 60 frames/s but less, we should measure the time elapsed and sum the deltas of time. When the sum is superior to the delay that corresponds to 1/37s (for 37 frames/s), then we draw the frame.


7. I prefer HD!

  Which of these gives a high resolution time (with a sub millisecond accuracy)? (2 correct answers.)

  a. `var time = new Date().getTime();`<br>
  b. `var time = performance.now();`<br>
  c. `var time = Date.now();`<br>
  d. Use the parameter passed to the `mainloop` when called by `requestAnimationFrame(mainloop)`<br>

  Ans: bd<br>
  Explanation: The `performance.now()` and the `requestAnimationFrame` APIs provide high resolution time.


8. Sprites and time based animation?

  The sprite animation framework proposed in the course...

  a. used time-based animation in the draw method of the sprite object model<br>
  b. did not use time-based animation as it did not address the moving object problem<br>

  Ans: <font style="color: magenta;">a</font>, xb<br>
  Explanation: It used time-based animation in the draw function of the sprite model to set the number of times we will draw a new image of animation, per second.








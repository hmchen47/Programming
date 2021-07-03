# Module 2: Game programming with HTML5 section


## 2.8 Exercises - Module 2 (12 Questions)

### 2.8.1 User interaction (1-4)

1. Listen in the loop?

  What is the best way to deal with multiple events (multiple keys + mouse buttons, movements, etc.) at the same time?

  a. Use a global object to store the state of the input keys, check it in the mainloop, update the x and y position of the player accordingly<br>
  b. Update the x and y position of the player directly in the input event listeners<br>

  Ans: <br>
  Explanation


2. Gamepad updated or not....

  In order to get the gamepad(s) status (buttons, joysticks) up to date, is it best practice to call navigator.getGamepads() regularly (in the game loop, for example)?

  a. Yes.<br>
  b. No, it's not necessary: once you get a reference to a gamepad (for example, in the gamepadconnected event listener), its state reflects its current status. It's updated automatically by the browser.<br>

  Ans: <br>
  Explanation


3. Axes values?

  The values of the gamepad axes are...?

  a. Between -5 and +5<br>
  b. Between -1 and +1<br>
  c. Between 1 and 0<br>

  Ans: <br>
  Explanation


4. Trigger me!

  How do you test if a gamepad button is analog (eg an R2 or L2 trigger on a XBox 360 or PS2/PS3 gamepad)?

  a. We test if the button's property `pressed` is true, then if its `value` property is defined. This property gives the pressure on the trigger.<br>
  b. Analog buttons are considered as axes.<br>

  Ans: <br>
  Explanation





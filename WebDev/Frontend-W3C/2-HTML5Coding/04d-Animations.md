# Week 4: HTML5 Animations

## 4.4 Exercises - Week 4


### 4.4.1 Intro exercises - Week 4

Here is an opportunity to show that you can now animate content on the Web, and are ready to have fun drawing and animating a monster!

Please complete the following 12 exercises in a timely manner. As stated in the grading policy page, they count towards 15% of your final grade.


### 4.4.2 Old methods... (1-3)

1. Draw me!

  <pre>setInterval(draw, 2000);

  function draw() {
    // ...
  }
  </pre>

  The call to setInterval will...

  a. Call it after 2000 seconds<br/>
  b. Call the draw function repeatedly every 2 seconds<br/>
  c. Call it once after 2 seconds<br/>

  Ans: b<br/>
  Explanation: The second parameter is the interval of time between each call of the function draw. It's in milliseconds.


2. Am I late?

  <pre>setTimeout(draw, 2000);

  function draw() {
    // ...
    setTimeout(draw, 2000);
  }
  </pre>

  What will the above code do?

  a. This is not the correct way to use setTimeout for doing animation.<br/>
  b. The animation will start after 2 seconds. Call the draw function every two seconds once the animation has started.<br/>
  c. The animation will start immediately. Call the draw function every two seconds once the animation has started.<br/>

  Ans: <span style="color: magenta;">b</span>, xa<br/>
  Explanation: `setTimeout` calls the function passed as first parameter after a delay passed as second parameter, in milliseconds (ms). Draw is called the first time after 2seconds. Then, as setTimeout is called again at the end of draw, draw will be called every two seconds again and again.


3. Choose carefully!

  I want to perform an animation at 60 frames/s on modern browsers. What is my preferred choice?

  a. Using requestAnimationFrame<br/>
  b. Using setTimeout<br/>
  c. Using setInterval<br/>

  Ans: a<br/>
  Explanation: HTML5 introduced the `requestAnimationFrame` API for 60 frames/s animation as a target. This method comes with many advantages presented in the course: optimization, merging of multiple animations, better scheduling accuracy, etc.





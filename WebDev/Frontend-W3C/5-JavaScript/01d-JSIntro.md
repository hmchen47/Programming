# Module 1: Introduction to JavaScript

## 1.4 Your first HTML/CSS/JS page

#### 1.4.1 Creating an HTML/CSS/JS project

Let's create a small HTML/CSS/JS project together.

It's time for you (and me) to create a small HTML/CSS/JS project, step by step, following some best practices. We will do this using different tools: source code editors + files but also two online IDEs (JsBin.com and CodePen.io). We will see how to write/debug the code and also how to migrate a project prototyped with online tools to a project you can run and edit on your hard drive using regular source code editors.

Many things we use in this example may be new to you. Don't worry. We will cover them either later on this week or over the following weeks. It's time to throw you in the deep end of the JavaScript world, getting you to write code, and look at examples etc. And from time to time, we will take a break and have a "real", "academic", look at the concepts of the language you have been using. We think this is the best way for you to learn!

#### Topic

We will write a small, interactive HTML page that will use some HTML input fields for indicating the name of a math function we'd like to plot, the ranges for the x and y values, the color of the curve etc.

We will first write this application online, using the JsBin.com editor, then we will do the same thing using the CodePen online editor, then, using a regular source code editor and .html, .css and .js files.

__Here is what the resulting Web page will look like:__

[CodePen Demo](https://codepen.io/w3devcampus/pen/bqGboZ)

[Local Demo](src/01d-example01.html)


### 1.4.2 Using CodePen

#### Live coding video: using CodePen

<a href="https://edx-video.net/W3CJSIXX2016-V001300_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/yxs66n8t)

In the video, at 3:19, there are some mistakes in the HTML code:

1. This line uses a wrong value for the for attribute (it should be the same value as the id attribute of the input field): `<label for="yMax">Color: </label> value: ...` should be: `<label for="color">Color value: </label> ...`
1. Improvement in the code could be to replace all empty paragraphs `<p></p>` by line breaks `<br>` or by a single `<p>`.


#### CodePen example with the starting code used in the video

If you want to code while watching the video, [please open this CodePen](https://codepen.io/w3devcampus/pen/GmbpzZ). It contains the source code of the example we started coding from. 

And [here is the same version](https://codepen.io/w3devcampus/pen/PjomvR?editors=1000#0) with the polyfill for the `<input type="color">` input field, not yet supported by Safari.

In case you have a hard time to follow the video, [here is the full example](https://codepen.io/w3devcampus/pen/bqGboZ) (this link points to the example from the previous course page).







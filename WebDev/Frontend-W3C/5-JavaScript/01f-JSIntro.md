# Module 1: Introduction to JavaScript

## 1.6 Simple JavaScript examples to play with

### 1.6.1 Introduction

This section does not detail the examples presented. Some of them are studied later in the course, some won't.

The examples are just here to bring some fun whilst making you play with some various uses of JavaScript. You are invited to look at their source code, and to tweak the examples. Do not worry if you don't understand how they work. We are just giving you "a taste" of JavaScript. There will be no graded exercises about them.


### 1.6.2 The devtool console

Using the `console.log(...)` instruction, you can __write messages to the devtool console__ of your browser. This is a common way to debug your code!

For example, let's say you added a button to your Web page, but nothing happens when you click on it.
It can be very difficult to spot your error without using the devtool console and `console.log(...)`!


#### Example

Let's check that some parts of the code you wrote are executed correctly.

[CodePen Demo](https://codepen.io/w3devcampus/pen/YNbvgP?editors=1000)

[Local Demo](src/01f-example01.html)

Normally, when the button is clicked, we should call the `addXToThePage()` function, which in turn should display the value of the variable x inside an HTML paragraph.

Let's check if the function is really executed. We need to add a `console.log("In the addXToThePage function");` as the first instruction of the function:

[CodePen Demo](https://codepen.io/w3devcampus/pen/YNbvoX)

[Local Demo](src/01f-example02.html)


#### Notes for 1.6.2 The devtool console

+ devtool console
  + a common way to debug JavaScript code
  + `console.log(...)`: instruction to write message to the devtool console




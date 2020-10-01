# Week 3: HTML5 Graphics

## 3.5 Colors, gradients, patterns, etc.


### 3.5.1 Canvas context: colors

In previous examples, we saw how to set the current color using the `strokeStyle` and `fillStyle` properties of the canvas context object.

Let's look at color in a little more detail, and see how we can use gradients or patterns/textures/images (in other words: fill shapes or fill the outline of the shapes with some images that repeat themselves).


#### Colors and transparency

You can use [the same syntax for colors that is supported by CSS3](https://www.w3.org/TR/css3-color/). The next lines show possible values/syntaxes.

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">strokeStyle </span><span class="pun">=</span><span class="pln"> </span><span class="str">'red'</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">fillStyle </span><span class="pun">=</span><span class="pln"> </span><span class="str">"#00ff00"</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">strokeStyle </span><span class="pun">=</span><span class="pln"> </span><span class="str">"rgb(0, 0, 255)"</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">fillStyle </span><span class="pun">=</span><span class="pln"> </span><span class="str">"rgba(0, 0, 255, 0.5)"</span><span class="pun">;</span></li>
</ol></div>

Note that:

+ All values are strings;
+ Line 4 defines a "transparent color", the "a" of "rgba" means "alpha channel". Its value is between 0 and 1, where 0 means "completely transparent" and 1 means "opaque".

Here is an example that shows how to draw different filled rectangles in blue, with different levels of transparency. 

Try [it online](https://jsbin.com/famoxoteju/1/edit?html,output): ([Local Example - Transparency](src/3.5.1-example1.html))

transparent rgba color example


#### Knowledge check 3.5.1

1. Do the color values that can be used to set the `fillStyle` or `strokeStyle` follow the CSS3 syntax? (Yes/No)

  Ans: 






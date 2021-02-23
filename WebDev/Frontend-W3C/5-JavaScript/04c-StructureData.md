# Module 4: Structuring data

## 4.3 Objects (part 3): creating multiple objects

### 4.3.1 Classes: definition

Let's study what is the concept of "class" in object oriented programming languages.

So far in this course, we've only used singleton objects: objects that only occur once: player, darkVador, etc.dark vador and his friend named pikachu

Ok, this is not quite true, I'd forgotten that we created many balls in the module 2 game. We'll come back to this example further down the page!

But even with the balls from module 2, we did not use a template to tell us how to easily create multiple objects that share the same properties and the same methods, but whose properties' values may differ.

For example, imagine Luke Skywalker, Ian Solo and Dark Vador. What do they have in common? They all are Star Wars heroes, they all have a name, they all belong to one side (the good/bad people, or rebels vs empire), etc. Imagine that we have a way of programming that describes not the objects themselves, but a "model", a "template" for these objects. We could call it StarWarsHero and use it for creating our heroes' objects.

Imagine the balls from module 2: they all had the same shape (circle), the same x, y, radius and color properties, but they were all different. They all belonged to the same class of object (ball), but they were all different in terms of their properties' values.

<span style="color: brown; font-weight: bold;">In many programming languages, these templates are called "classes".</span>

+ Before 2015, in JavaScript 5 (also called ES5), we did not have such a concept, instead we had "constructor functions".
+ In modern JavaScript (after 2015),  we have the concept of classes, and the syntax is rather similar to what we find in other object oriented programming languages.

Let's introduce these two ways of defining "pseudo classes" with ES5's function constructors, and with modern JavaScript's classes!







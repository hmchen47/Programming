/* ES5's constructor function syntax is not easy to read. If someone does not respect the "conventions" that we've just discussed (start the class with an uppercase, etc.), then the code may work, but it will be difficult to guess that we are not in front of a regular function.

ES5 construction function
*/
function HeroES5(name, side) {
  this.name = name;
  this.side = side;
  
  this.describeYourself = function() {
    console.log("I'm " + this.name + " and I'm from the " + this.side);
  }
}

let ianSoloES5 = new HeroES5('Ian Solo', 'Rebels');


/* ES6 created a class keyword and a constructor keyword, along with advanced concepts that will be the subject of an "advanced JavaScript" course. 

Using ES6 classes
*/
class Hero {
  // must be UNIQUE!, called when "new" is used
  constructor(name, side) { 
    this.name = name;
    this.side = side;   
  }
  
  // no "function" keyword here!
  speak() {
    return "<p>My name is " + this.name +
      ", I'm with the " + this.side + ".</p>";
  }
}

var darkVador = new Hero("Dark Vador", "empire");
var luke = new Hero("Luke Skywalker", "rebels");
var ianSolo = new Hero("Ian Solo", "rebels");

function makeHeroesSpeak() {
  document.body.innerHTML += darkVador.speak();
   document.body.innerHTML += luke.speak();
   document.body.innerHTML += ianSolo.speak();
}





// name, side are called "instance properties"
// speak is called an "instance method"
// they are used preceeding them by the name of the instance object
// Ex: luke.speak(), luke.name etc.
class Hero {
  // must be UNIQUE!, called when "new" is used
  constructor(name, side) { 
    this.name = name;
    this.side = side;  
    Hero.numberHeroesCreated++;
  }
  
  static getHowManyHeroesYouCreated() {
    return Hero.numberHeroesCreated;
  }
  // no "function" keyword here!
  speak() {
    console.log("ERROR: " + Hero.numberHeroesCreated);
    return "<p>My name is " + this.name +
      ", I'm with the " + this.side + ".</p>";
  }
}
// This cannot be declared before the class as unlike functions
// classes must be declared before being used.
Hero.numberHeroesCreated = 0;

//var darkVador = new Hero("Dark Vador", "empire");
var luke = new Hero("Luke Skywalker", "rebels");
//var ianSolo = new Hero("Ian Solo", "rebels");

function makeHeroesSpeak() {
  document.body.innerHTML += darkVador.speak();
   document.body.innerHTML += luke.speak();
   document.body.innerHTML += ianSolo.speak();
}


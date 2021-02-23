function Hero(name, side) {
  this.name = name;
  this.side = side;
  
  this.speak = function() {
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


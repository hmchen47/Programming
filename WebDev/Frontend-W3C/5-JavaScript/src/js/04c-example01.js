// ES5 construction function
function Hero(name, side) {
  this.name = name;
  this.side = side;
  
  this.describeYourself = function() {
    console.log("I'm " + this.name + " and I'm from the " + this.side);
  }
}

let ianSolo = new Hero("Ian Solo", "Rebels");
let lukeSkywalker = new Hero("Luke Skywalker", "Rebels");
let darkVador = new Hero("Dark Vador", "Empire");


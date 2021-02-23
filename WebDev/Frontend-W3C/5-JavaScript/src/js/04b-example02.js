// empty object with properties/methods
var darkVador = {};

// add properties after darkVador has been created
 darkVador.race = 'human';
 darkVador.job = 'villain';

// add some methods
  darkVador.talk = function() {
    return 'come to the dark side, Luke!' + this.breathe();
  };

  darkVador.describeYourself = function() {
    return "I'm a " + this.race 
      + " and I'm a " + this.job 
      + " in a series of movies!" + this.breathe();
  };

  darkVador.breathe = function() {
    return ".....shhhhhhhhh.....";
  };


function dvSpeak() {
 document.body.innerHTML += '<p>Dark Vador describes himself: ' + darkVador.describeYourself(); + '</p>';  document.body.innerHTML += '<p>Dark Vador says: ' + darkVador.talk(); + '</p>';
}

function deleteSomeProperties() {
  delete darkVador.race;
  delete darkVador.job;
}


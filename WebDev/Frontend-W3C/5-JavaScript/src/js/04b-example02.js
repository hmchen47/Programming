var darkVador = {
  race: 'human',
  job: 'villain',
  talk: function() {
    return 'come to the dark side, Luke!';
  },
  describeYourself: function() {
    return "I'm a " + this.race + " and I'm a " + this.job + " in a series of movies!";
  }
}

function dvSpeak() {
 document.body.innerHTML += '<p>Dark Vador describes himself: ' + darkVador.describeYourself(); + '</p>';  document.body.innerHTML += '<p>Dark Vador says ' + darkVador.talk(); + '</p>';
}


function soundLoaded() {
  
  // enable buttons, the sounds are loaded
	
   var button1 = document.querySelector("#explosion");
   button1.disabled = false;
   button1.addEventListener("click", function() {
	 sound.play('blast');
   });
		
   var button2 = document.querySelector("#basic_explosion");
   button2.disabled = false;
   button2.addEventListener("click", function() {
     sound.play('laser');
   });
  
   var button3 = document.querySelector("#winner");
   button3.disabled = false;
   button3.addEventListener("click", function() {
     sound.play('winner');
   });
}


// Load and decode sounds
var sound = new Howl({
  urls: ['https://goldfirestudios.com/proj/howlerjs/sounds.mp3', 'https://goldfirestudios.com/proj/howlerjs/sounds.ogg'],
  sprite: {
    blast: [0, 2000],
    laser: [3000, 700],
    winner: [5000, 9000]
  }, 
  onload: function() { 
     console.log("Sound loaded");
     soundLoaded();
  }
});


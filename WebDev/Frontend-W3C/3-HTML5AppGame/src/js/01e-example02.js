var ctx;

window.onload = function() {
  // the page is loaded
  ctx = new AudioContext();
  
  // the most simple source 
  var player = document.getElementById("player");
  
  player.onplay = (e) => {
    ctx.resume()
  }
    
  var source = ctx.createMediaElementSource(player);
  
  source.connect(ctx.destination);
};
    

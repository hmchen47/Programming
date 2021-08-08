/**
 *  levelTool - A simple level tool, utilizing `deviceorientation`
 *  
 *  Copyright 2011 Derek Anderson | Media Upstream
 *  MIT License
 */
var levelTool = {};

// Cache results of 180 / PI for FF fix
levelTool.pf = (180 / Math.PI);

// calculate the x / y (beta / gamma) changes and update the UI
levelTool.run = function(e){
  if (!e.gamma && !e.beta) { 
    e.gamma = -(e.x * levelTool.pf);
    e.beta = -(e.y * levelTool.pf);
  }
  var v = (e.beta ) + 32;
  var h = (e.gamma) + 32;
  
  v = (v > 68) ? 68 : v;
  v = (v < 0) ? 0 : v;
  
  h = (h > 68) ? 68 : h;
  h = (h < 0) ? 0 : h;
  
  levelTool.v.css('top', v +'%');
  levelTool.h.css('left', h +'%');
};



// Attach the event listeners and dislpay message to unsupported browsers
levelTool.init = function(){
  
  levelTool.v = $('#v');
  levelTool.h = $('#h');
    
  window.addEventListener('deviceorientation', levelTool.run, false);
  window.addEventListener('MozOrientation', levelTool.run, false);

  // "Is Device Orientation There?", "Hell No! ... Device Orientation don't live here no more!"
  if (!('ondeviceorientation' in window) && !(window.onmozorientation)) {
    $('#sorry').fadeIn();
  } else {
    $('#level-h, #level-v').fadeIn('fast');
  }
};

// helpers
levelTool.percentOf = function(a, b){ return Math.floor((a/b)*100); };
levelTool.toFloat = function(num){ return (num/100); };
levelTool.invertPercent = function(num){ return (100-num); };


$(function(){
  // initialize our Tool.
  levelTool.init();
});


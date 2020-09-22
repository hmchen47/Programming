var video;

function init() {
  // function called when the page is loaded
  
  video = document.querySelector("#myVideo");
  
  // For initial value
  video.width = window.innerWidth;
  video.height = window.innerHeight;
    
  // For dealing with window resize
  window.onresize = function() {
      video.width = window.innerWidth;
      video.height = window.innerHeight;
  };
 
}

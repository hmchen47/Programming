window.onload = init;

var progressBar;

function init() {
  progressBar = document.querySelector(".progress div");

  window.addEventListener("scroll", function() {
      var max = document.body.scrollHeight - window.innerHeight;
      var percent = (window.pageYOffset / max) * 100;
      progressBar.style.width = percent + "%";
  });
}
 

window.onload = init;

function init() {
  // we're sure that the DOM is ready
  // before querying it
  
  // add a shadow to all images
  // select all images
  var listImages = document.querySelectorAll("img");

  // change all their width to 100px
  listImages.forEach(function(img) {
    // img = current image
    img.style.boxShadow = "5px 5px 15px 5px grey";
    img.style.margin = "10px";
  });  
  
}

function addBorderToFirstImage() {
  // select the first image with id = img1
  var img1 = document.querySelector('#img1');

  // Add a red border, 3px wide
  img1.style.border = '3px solid red';  
}

function resizeAllImages() {
  // select all images
  var listImages = document.querySelectorAll("img");

  // change all their width to 100px
  listImages.forEach(function(img) {
    // img = current image
    img.width = 100;
  });
}

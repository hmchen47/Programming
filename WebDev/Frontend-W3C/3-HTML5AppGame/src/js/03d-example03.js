function readFilesAndDisplayPreview(files) {
  // Loop through the FileList and render image files as thumbnails.
  for (var i = 0, f; f = files[i]; i++) {

    // Only process image files.
    if (!f.type.match('image.*')) {
      continue;
    }

    var reader = new FileReader();

    //capture the file information.
    reader.onload = function(e) {
        // Render thumbnail.
        var span = document.createElement('span');
        span.innerHTML = "<img class='thumb' src='" + e.target.result + "'/>";
        document.getElementById('list').insertBefore(span, null);
      };

    // Read the image file as a data URL.
    reader.readAsDataURL(f);
  }
}

function handleFileSelect(evt) {
  var files = evt.target.files; // FileList object
  readFilesAndDisplayPreview(files);
}

window.onload = function() {
  document.getElementById('files').addEventListener('change', handleFileSelect, false);
}


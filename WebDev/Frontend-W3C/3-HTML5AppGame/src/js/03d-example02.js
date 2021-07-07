function dragLeaveHandler(event) {
    console.log("drag leave");
    // Set style of drop zone to default
    event.target.classList.remove('draggedOver'); 
}

function dragEnterHandler(event) {
    console.log("Drag enter");
    // Show some visual feedback
    event.target.classList.add('draggedOver'); 
}

function dragOverHandler(event) {
    //console.log("Drag over a droppable zone");
    // Do not propagate the event
    event.stopPropagation();
    // Prevent default behavior, in particular when we drop images or links
    event.preventDefault(); 
}

function dropHandler(event) {
    console.log('drop event');
  
    // Do not propagate the event
    event.stopPropagation();
    // Prevent default behavior, in particular when we drop images or links
    event.preventDefault();         

    // reset the visual look of the drop zone to default
    event.target.classList.remove('draggedOver'); 
  
  
    // get the files from the clipboard
    var files = event.dataTransfer.files;
    var filesLen = files.length; 
    var filenames = "";

    // iterate on the files, get details using the file API
    // Display file names in a list.
    for(var i = 0 ; i < filesLen ; i++) {
      filenames += '\n' + files[i].name; 
      // Create a li, set its value to a file name, add it to the ol
      var li = document.createElement('li');
      li.textContent = files[i].name;    
      document.querySelector("#droppedFiles").appendChild(li);
    }
    console.log(files.length + ' file(s) have been dropped:\n' + filenames);
  
    readFilesAndDisplayPreview(files);
}  

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
            span.innerHTML = "<img class='thumb' width='100' src='" + e.target.result + "'/>";
            document.getElementById('list').insertBefore(span, null);
        };

        // Read in the image file as a data URL.
        reader.readAsDataURL(f);
    }
}

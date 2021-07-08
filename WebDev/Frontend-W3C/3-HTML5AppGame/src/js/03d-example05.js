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
        var li =     document.createElement('li');
        li.textContent = files[i].name;    document.querySelector("#droppedFiles").appendChild(li);
    }

    console.log(files.length + ' file(s) have been dropped:\n' + filenames);
  
    uploadAllFilesUsingAjax(files);
  
}  

function uploadAllFilesUsingAjax(files) {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'upload.html');

    xhr.upload.onprogress = function(e) {
        progress.value = e.loaded;
        progress.max = e.total;
    };
    
    xhr.onload = function() {
        alert('Upload complete!');
    };

    var form = new FormData();
    for(var i = 0 ; i < files.length ; i++) {  
        form.append('file', files[i]);
    }

    xhr.send(form);
}

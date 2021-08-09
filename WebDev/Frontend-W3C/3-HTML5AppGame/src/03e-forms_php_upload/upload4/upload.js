// object that holds form values
var formValues;

// function that iterates through the form and dynamically assigns properties/values to the form values objects, 
// and stores it to sessionStorage
storeValues = function () {
	var formElements = document.formUpload.elements;
	
	for (i = 0; i < formElements.length; i++) {
		var formElement = formElements[i];
		
		if (formElement.localName == "input") {
			var name = formElements[i].name;
			var value = formElements[i].value;
			formValues[name] = value;
		}
	}
	// Store the object as a JSON String
	sessionStorage.setItem('formUploadSave', JSON.stringify(formValues));
};

// on loading, retrieve any form values previously stored in this session.
// called by body onLoad

// function that  retrieves form values from sessionStorage, iterates through form and restores properties/values 
// to form elements; also it assigns onchange event listener.
retrieveValues = function () {
	var formElements = document.formUpload.elements;

	// Retrieve the object from storage
	var retrievedValues = JSON.parse(sessionStorage.getItem("formUploadSave"));

	// If found, populate form
	for (i = 0; i < formElements.length; i++) {
		var formElement = formElements[i];

		if (formElement.localName == "input") {
			// Assign onchange event listener                   
			formElement.addEventListener("change", storeValues, false);
  
			var formElementName = formElement.name;

			if (retrievedValues) {// != null
				formElement.value = retrievedValues[formElementName];
			}
		}
	}
};

var nbFilesUpload = 0;

function uploadForm() {
	var xhr = new XMLHttpRequest();
	xhr.onreadystatechange = function() 
	{ 
		if(xhr.readyState == 4) 
		{ 
			if(xhr.status == 200) 
			{ 
				document.getElementById("message").innerHTML = xhr.responseText;
			}
		} 
	}; 
	xhr.open('POST', 'upload.php');
	var myForm = new FormData();
	myForm.append("firstname", document.getElementById("firstname").value);
	myForm.append("lastname", document.getElementById("lastname").value);
	xhr.send(myForm);
}			

function uploadOneFile(file, indice) {
	var xhr = new XMLHttpRequest();
	xhr.onreadystatechange = function() 
	{ 
		if(xhr.readyState == 4) 
		{ 
			if(xhr.status == 200) 
			{ 
				var li = document.createElement('li');
				li.textContent = xhr.responseText;
				document.getElementById("message").appendChild(li);
			}
		} 
	}; 
	xhr.open('POST', 'upload.php');
	// looks like PHP / Apache should automatically translate
	// header X_FILENAME in HTTTP-X-FILENAME which is the correct header
	// in some case they don't do that so let's write it a clean way
	xhr.setRequestHeader("X-FILENAME", file.name);
	var progressBar = document.getElementById("progressBar"+indice);
	xhr.upload.onprogress = function(e) 
	{
		progressBar.value = e.loaded;
		progressBar.max = e.total;
	};

	// Send the Ajax request
	xhr.send(file);
}


/*************************************
DRAG AND DROP
*************************************/

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
    li.textContent = files[i].name + " ";    
    var progressBar = document.createElement('progress');
    progressBar.id = "progressBar"+i;
    progressBar.value = 0;
    progressBar.max = 100;
    li.appendChild(progressBar);
    document.querySelector("#droppedFiles").appendChild(li);
    memFiles.push(files[i]);
  }
  console.log(files.length + ' file(s) have been dropped:\n' + filenames);
}
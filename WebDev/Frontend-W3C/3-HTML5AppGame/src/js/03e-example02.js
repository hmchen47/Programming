// object that holds form values
var formValues = {};

// function that iterates through the form and dynamically assigns properties/values, and stores them to sessionStorage
storeValues = function () {
var formElements = document.formUpload.elements;

	for (i = 0; i < formElements.length; i++) {
		var formElement = formElements[i];
		if (formElement.localName == "input" && formElement.type == "text") {
			var name = formElements[i].name;
			var value = formElements[i].value;
			formValues[name] = value;
			}
	}
	// Stores the object as a JSON String
	sessionStorage.setItem('formUploadSave', JSON.stringify(formValues));
};

// on loading, retrieve any form values previously stored in this session.
// called by body onLoad

// function that retrieves form values from sessionStorage, iterates through the form and restores properties/values 
// to form elements; also assigns an onchange event listener.

retrieveValues = function () {
	var formElements = document.formUpload.elements;

	// Retrieves the object from session storage
	var retrievedValues = JSON.parse(sessionStorage.getItem("formUploadSave"));
	
	// If found, populate form
	for (i = 0; i < formElements.length; i++) {
		var formElement = formElements[i];

		if (formElement.localName == "input" && formElement.type == "text") {
			// Assign onchange event listener                   
			formElement.addEventListener("change", storeValues, false);

			var formElementName = formElement.name;

			if (retrievedValues) {// != null
				formElement.value = retrievedValues[formElementName];
			}
		}
	}

	// On refresh we have no file to restore cuase drag'n'drop div is not a form element
	document.getElementById("namesAllFiles").value = '';
	document.getElementById("submitForm").disabled = true;
};

var nbFilesUpload = 0;

function sendForm(event) {
	document.getElementById("formFiles").value = null;
}

function uploadOneFile(file, indice, nbFiles) {
	var xhr = new XMLHttpRequest();
	xhr.open('POST', 'upload.php');
	// looks like PHP / Apache should automatically translate
	// header X_FILENAME in HTTTP-X-FILENAME which is the correct header
	// in some case they don't do that so let's write it a clean way
	xhr.setRequestHeader("X-FILENAME", file.name);
	var progressBar = document.getElementById("progressBar"+indice);
	xhr.upload.onprogress = function(e) {
		progressBar.value = e.loaded;
		progressBar.max = e.total;
		if(progressBar.value == progressBar.max) {
			nbFilesUpload++;
			if(nbFilesUpload == nbFiles) {
				document.getElementById("submitForm").disabled = false;
			}
		}
	}; 
  // Send the Ajax request
  xhr.send(file);
}

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

	// to upload files in more than one drag'n'drop
	// we have to count already uploaded files to set an unused id for the progress bar
	if(document.getElementById('namesAllFiles').value === "") {
		var nbUploadedFiles = 0;
	}
	else {
		var nbUploadedFiles = document.getElementById('namesAllFiles').value.split('::').length;
	}

	// iterate on the files, get details using the file API
	// Display file names in a list.
	for(var i = 0 ; i < filesLen ; i++) {
		filenames += '\n' + files[i].name; 
		// Create a li, set its value to a file name, add it to the ol
		var li =     document.createElement('li');
		li.textContent = files[i].name;
		// add a progress bar for this file upload
		var progressBar = document.createElement('progress');
		progressBar.id = "progressBar"+(nbUploadedFiles+i);
		progressBar.value = 0;
		progressBar.max = 100;
		li.appendChild(progressBar);   
	
		document.querySelector("#droppedFiles").appendChild(li);
		uploadOneFile(files[i], (nbUploadedFiles+i), filesLen);
		// if there is more than on uploaded file or more than one file to upload
		// we need to concatenate
		console.log(document.getElementById("namesAllFiles").value);
		if (nbUploadedFiles >= 1 || i >= 1) {
			document.getElementById("namesAllFiles").value += "::" + files[i].name;
		} else {
			document.getElementById("namesAllFiles").value += files[i].name;
		}
		console.log(document.getElementById("namesAllFiles").value);
	}
	console.log(files.length + ' file(s) have been dropped:\n' + filenames);
}


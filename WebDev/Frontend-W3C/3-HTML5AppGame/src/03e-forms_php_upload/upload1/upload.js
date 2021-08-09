// object that holds form values
var formValues = {};

// function that iterates through the form and dynamically assigns properties/values to form values object, and store it to sessionStorage
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
	// Store the object as a JSON String
	sessionStorage.setItem('formUploadSave', JSON.stringify(formValues));
};

// on loading, retrieve any form values previously stored in the session.
// called by body onload

// function that retrieves form values from sessionStorage, iterates through the form and restores input fields values; also assign onchange event listener.
retrieveValues = function () {
	var formElements = document.formUpload.elements;

	// Retrieve the object from storage
	var retrievedValues = JSON.parse(sessionStorage.getItem("formUploadSave"));

	// If found, populate the form
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

	// On refresh we restore only last uploaded files so we have to
	// - reconstruct namesAllFiles concatenation
	// - reconstruct files list with progress bar
	// - enable send button if there's restored file(s)
	document.getElementById("namesAllFiles").value = '';
	uploadFileWithoutParameters();
	if(document.getElementById('formFiles').files.length)
	{
		document.getElementById("submitForm").disabled = false;
	}
};

function uploadFileWithoutParameters() {
	// to upload files in more than one drag'n'drop
	// we have to count already uploaded files to set an unused id for the progress bar
	if(document.getElementById('namesAllFiles').value === "") {
		nbUploadedFiles = 0;
	}
	else {
		nbUploadedFiles = document.getElementById('namesAllFiles').value.split('::').length;
	}
	var inputFiles = document.getElementById('formFiles');
	var files = inputFiles.files;
	for(i=0; i<files.length; i++) {
		var li =     document.createElement('li');
		li.textContent = files[i].name;
		// create a progress bar for each file
		var progressBar = document.createElement('progress');
		progressBar.id = "progressBar"+(nbUploadedFiles+i);
		progressBar.value = 0;
		progressBar.max = 100;
		li.appendChild(progressBar);   
		document.getElementById("message").appendChild(li);
		uploadOneFile(files[i], (nbUploadedFiles+i), files.length);
		// if there is more than on uploaded file or more than one file to upload
		// we need to concatenate
		if (nbUploadedFiles >= 1 || i >= 1) {
			document.getElementById("namesAllFiles").value += "::" + files[i].name;
		}
		else
		{
			document.getElementById("namesAllFiles").value += files[i].name;
		}
	}
}

var nbFilesUpload = 0;

function sendForm(event) {
	// here we reinit the files form to no file to restore 
	document.getElementById("formFiles").value = null;
}	

function uploadOneFile(file, indice, nbFiles) {
	var xhr = new XMLHttpRequest();
	xhr.open("POST", formUpload.getAttribute("action"), true);
	// looks like PHP / Apache should automatically translate
	// header X_FILENAME in HTTTP-X-FILENAME which is the correct header
	// in some case they don't do that so let's write it a clean way
	xhr.setRequestHeader("X-FILENAME", file.name);
	var progressBar = document.getElementById("progressBar"+indice);
	xhr.upload.onprogress = function(e) 
	{
		progressBar.value = e.loaded;
		progressBar.max = e.total;
		if(progressBar.value == progressBar.max)
		{
			nbFilesUpload++;
			if(nbFilesUpload == nbFiles)
			{
				document.getElementById("submitForm").disabled = false;
			}
		}
	};
  // Send the Ajax request
  xhr.send(file);
}
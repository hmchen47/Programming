// object that hold form values
var formValues;

// function that iterates through the form and dynamically assigns properties/values to form values object, and stores it to sessionStorage
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

// on loading, retrieve any form values previously stored this session.
// called by body onLoad

// function that retrieves form values from sessionStorage, iterates through form and restores properties/values to form elements; also assigns onchange event listener.
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

function uploadFileWithoutParameters() {
	// creates a FormData object that contains all the different fields values.
	var fd = new FormData(document.getElementById("formUpload"));

	// add the file
	var inputFiles = document.getElementById('formFiles');
	var memFiles = inputFiles.files;

	for(i=0; i<memFiles.length; i++) {
		fd.append(inputFiles.name, memFiles[i]);
	}                                      

	// prepare the request
	var xhr = new XMLHttpRequest();
	xhr.open("POST", formUpload.getAttribute("action"), true);
      
	// Define the callbacks
	xhr.upload.onprogress = function(e) {
		progress.value = e.loaded;
		progress.max = e.total;
	};
	xhr.onload = function() {
		//alert("Upload termine");
	};
	// send the request
	xhr.send(fd);
}
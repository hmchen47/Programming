var memFiles = new Array();
var formId = document.getElementById("formUpload");
var firstnameId = document.getElementById("firstname");
var lastnameId = document.getElementById("lastname");

formId.onsubmit = function(event) {

	// Prevent default behavior, in particular when we drop images or links
	event.preventDefault(); 
      
	uploadForm();			
	for(i=0; i<memFiles.length; i++) {
		uploadOneFile(memFiles[i], i);
	}
}
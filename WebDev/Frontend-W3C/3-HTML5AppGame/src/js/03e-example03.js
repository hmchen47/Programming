var formId, firstnameId, lastnameId;
// object that holds the form values
var formValues = {};


// on loading, retrieve any form values previously stored in this session.
// called by <body onLoad>

// function that retrieves the form values from sessionStorage, 
// iterates through form and restores properties/values 
// to form elements; also it assigns onchange event listener.
retrieveValues = function () {
   formId = document.getElementById("formUpload");
   firstnameId = document.getElementById("firstname");
   lastnameId = document.getElementById("lastname");
  
   formId.onsubmit = createProgressBar;

    var formElements = document.formUpload.elements;

    // Retrieves the object from session storage
    var retrievedValues = JSON.parse(sessionStorage.getItem("formUploadSave"));

    // If found, populate form
    for (i = 0; i < formElements.length; i++) {
        var formElement = formElements[i];

        if (formElement.localName === "input" && formElement.type === "text") {
            // Assign onchange event listener                   
            formElement.addEventListener("change", storeValues, false);

            var formElementName = formElement.name;

            if (retrievedValues) {// != null
                formElement.value = retrievedValues[formElementName];
            }
        }
    }
    // On refresh we restore only last uploaded files so we have to
    // - re-execute uploadOneFile for each file
    // - re-execute the send onSubmit callback
    createProgressBar();
};

// function that iterates through the form and dynamically assigns properties/values to form values objects, 
// and stores it to sessionStorage
storeValues = function () {
    var formElements = document.formUpload.elements;

    for (i = 0; i < formElements.length; i++) {
        var formElement = formElements[i];

        if (formElement.localName === "input") {
            var name = formElements[i].name;
            var value = formElements[i].value;
            formValues[name] = value;
        }
    }
    // Store the object as a JSON String
    sessionStorage.setItem('formUploadSave', JSON.stringify(formValues));
};


function uploadForm() {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                document.getElementById("status").innerHTML = xhr.responseText;
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
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4){
            if (xhr.status === 200) {
                var li = document.createElement('li');
                li.textContent = xhr.responseText;
                document.getElementById("status").appendChild(li);
            }
        }
    };
    xhr.open('POST', 'upload.php');
    // looks like PHP / Apache should automatically translate
    // header X_FILENAME in HTTTP-X-FILENAME which is the correct header
    // in some case they don't do that so let's write it a clean way
    xhr.setRequestHeader("X-FILENAME", file.name);
    var progressBar = document.getElementById("progressBar" + indice);
    xhr.upload.onprogress = function (e) {

        progressBar.value = e.loaded;
        progressBar.max = e.total;
    };
    // Send the Ajax request
    xhr.send(file);
}

function createProgressBar(event) {

    // Prevent default behavior, in particular when we drop images or links
    if (event) {
        event.preventDefault();
    }

    uploadForm();

    var inputFiles = document.getElementById('formFiles');
    var files = inputFiles.files;

    nbUploadedFiles = document.querySelectorAll("#message li").length;

    for (i = 0; i < files.length; i++) {
        var li = document.createElement('li');
        li.textContent = files[i].name + " ";
        
        var progressBar = document.createElement('progress');
        progressBar.id = "progressBar" + (nbUploadedFiles + i);
        progressBar.value = 0;
        progressBar.max = 100;
        li.appendChild(progressBar);
        
        document.getElementById("message").appendChild(li);
        uploadOneFile(files[i], (nbUploadedFiles + i));
    }
}


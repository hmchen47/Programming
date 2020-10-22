// Different elements from the form in the HTML page
var contactForm, lastNameField, firstNameField, telField, childrenField, emailField, birthDateField;

// Array of contacts to save/load to/from localStorage
var contacts = [];

var textMessageInvalid = "This field contains invalid chjaracters";
var dateMessageInvalid = "Bith date should be in the past";

window.addEventListener("load", function() {
  // called when the page has been entirely loaded
  
  // the form element
  contactForm = document.forms[0]; 
  
  // get the fields elements
  lastNameField = contactForm.familyName;
  firstNameField = contactForm.givenName;
  telField = contactForm.tel;
  emailField = contactForm.email;
  childrenField = contactForm.children;
  birthDateField = contactForm.birthDate;
  
  // read contacts from localStorag
  contacts = getContacts();
  
  // Builds and display the table of contacts
  buildContactTable(contacts);
  

  // Listener for input events on the two text fields. Check for
  // invalid charcters %, &, $, ! that are forbidden.
  lastNameField.oninput = firstNameField.oninput = function() {
	if (this.value.match(/[%&$!]/)) {
		this.setCustomValidity(textMessageInvalid);
	} else {
		this.setCustomValidity("");
	}
};

  // Listener for input events on the date field. Checks that the date is 
  // in the past
birthDateField.oninput = function() {
	if (this.valueAsDate >= new Date()) {
		this.setCustomValidity(dateMessageInvalid);
	} else {
		this.setCustomValidity("");
	}
}; 
  
});

// Called when the form is submitted
function submitForm() {
  // When we execute this function, the form has already been validated
  // by the HTML5 built-in validation system (bubbles etc.)
  console.log("We are saving the current contact in the form");
  
  // Create a new contact JavaScript object with the current values
  // in the form inoput fields
 var contact = {};
  contact.givenName = firstNameField.value;
  contact.familyName = lastNameField.value;
  contact.tel = telField.value;
  contact.email = emailField.value;
  contact.birthDate = birthDateField.value; 
  contact.children = childrenField.value;
  
  // Add the contact in the array of contacts
  contacts.push(contact);
  
  // Save the array of contacts in JSON format
  localStorage.contacts = JSON.stringify(contacts); 
  
  // Update the HTML table with the new contact at the end
  addLineToHTMLTable(contact);
  
  // do not submit the form using HTTP, return false prevents this
  // submission
  return false;
} 
  
function buildContactTable(contacts) {
	var rowIndex, row;
		
	// iterate on the contact array passed as parameter
	for (rowIndex = 0; rowIndex < contacts.length; rowIndex++) {		
		// Add a line in the HTML table for the current contact
		addLineToHTMLTable(contacts[rowIndex]);
	}
}

// Add a line to the HTML table, corresponding to the contact
// passed as parameter
function addLineToHTMLTable(contact) {
  	var row, lastNameColumn, firstNameColumn, telColumn, bithDateColumn; 
	var childrenColumn, emailColumn;
  
    var tableBody = document.getElementById("tableContactBody");
	
    // create a table row element and all tds inside for the diffent
    // contact properties
	row = document.createElement("tr");
	firstNameColumn = document.createElement("td");
	lastNameColumn = document.createElement("td");
    telColumn = document.createElement("td");
	bithDateColumn = document.createElement("td");
	emailColumn = document.createElement("td");
	childrenColumn = document.createElement("td");
		
	// fill the tds
	lastNameColumn.innerHTML = contact.familyName;
	firstNameColumn.innerHTML = contact.givenName;
    telColumn.innerHTML = contact.tel;
	bithDateColumn.innerHTML = contact.birthDate;
	emailColumn.innerHTML = contact.email;
	childrenColumn.innerHTML = contact.children;
		
				
	// Adds tds to the row		
	row.appendChild(lastNameColumn);
	row.appendChild(firstNameColumn);
    row.appendChild(telColumn);
	row.appendChild(bithDateColumn);
	row.appendChild(emailColumn);
	row.appendChild(childrenColumn);
  
    // add row to the table body
    tableBody.appendChild(row);
}

// Read contacts from localStorage
function getContacts() {
	var contacts = localStorage.contacts;
	if (contacts) {
		return JSON.parse(contacts);
	} else {
		return [];
	}
}


var fieldFamilyName, fieldGivenName;
// Array to save
var contacts = [];

function init() {
  fieldFamilyName=document.getElementById("familyName");
  fieldGivenName= document.querySelector("#givenName");

  
  console.log("I'm checking if   there are customers in local storage");
  if(localStorage.contacts) {
    contacts = JSON.parse(localStorage.contacts);
  } 
  
  console.log("init done");
}

function submitForm()  {
  //when we execute this function, the form content is necessary valid
  console.log("form saved");
  console.log("Family name's value : " + fieldFamilyName.value);
  
 // We create a JavaScript object for the contact

 var contact = {};
  contact.familyName = fieldFamilyName.value;
  contact.givenName = fieldGivenName.value;
  
  // Add the curent contact to the array
  contacts.push(contact);
  
  // Save in JSON
  localStorage.contacts = JSON.stringify(contacts);
  
  return false;
} 


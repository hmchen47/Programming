
function restoreFormContent() {
  console.log("restoring form content from localStorage");
  
  if(localStorage.firstName !== undefined) 
    document.getElementById("firstName").value = localStorage.firstName;
 
  if(localStorage.lastName !== undefined) 
    document.getElementById("lastName").value = localStorage.lastName;
  
  if(localStorage.email !== undefined) 
    document.getElementById("email").value = localStorage.email;

  if(localStorage.age !== undefined) 
    document.getElementById("age").value = localStorage.age;
  
  if(localStorage.date !== undefined) 
    document.getElementById("date").value = localStorage.date;

}

// Called when the page is loaded
window.onload = restoreFormContent;




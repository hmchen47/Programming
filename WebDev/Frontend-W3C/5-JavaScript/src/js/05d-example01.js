  function search() {    
    // Send an XhR2 query. See HTML5 games and Apps MOOC at W3Cx
    // for detailed explanation about XhR2.
    var queryURL = "https://jsonplaceholder.typicode.com/users";
    
    var xhr = new XMLHttpRequest();
    xhr.open('GET', queryURL, true);
    
    xhr.onload = function(e) {
      var users = JSON.parse(xhr.response);
      
      displayUsersAsATable(users);
    }
    
    xhr.send();
    
} 
  
function displayUsersAsATable(users) {
     // users is a JavaScript object
  
    // empty the div that contains the results
    var usersDiv = document.querySelector("#users");
    usersDiv.innerHTML = "";
  
    // creates and populate the table with users
    var table = document.createElement("table");
  
    users.forEach(function(currentUser) {
      var row = table.insertRow();
      row.innerHTML = "<td>"+ currentUser.name+ "</td><td>" 
        + currentUser.email + "</td>";
    });
  
    usersDiv.append(table);
}


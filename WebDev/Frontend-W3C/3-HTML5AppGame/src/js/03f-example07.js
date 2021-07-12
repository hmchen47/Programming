var db=null;

function createDatabase() {
  
  if (!window.indexedDB) {
    window.alert("Your browser doesn't support a stable version of IndexedDB. Such and such feature will not be available.");
}
  
// This is what our customer data looks like.
var customerData = [
  { ssn: "444-44-4444", name: "Bill", age: 35, email: "bill@company.com" },
  { ssn: "555-55-5555", name: "Donna", age: 32, email: "donna@home.org" }
];
var dbName = "CustomerDB";
 
// Open database with version=2. Use integer valueonly ! Not 1.1, 1.2 etc.
var request = indexedDB.open(dbName, 2);
 
request.onerror = function(event) {
  // Handle errors.
  console.log("request.onerror errcode=" + event.target.error.name);
};
request.onupgradeneeded = function(event) {
  console.log("request.onupgradeneeded, we are creating a new version of the dataBase");
  db = event.target.result;
 
  // Create an objectStore to hold information about our customers. We're
  // going to use "ssn" as our key path because it's guaranteed to be
  // unique.
  var objectStore = db.createObjectStore("customers", { keyPath: "ssn" });
 
  // Create an index to search customers by name. We may have duplicates
  // so we can't use a unique index.
  objectStore.createIndex("name", "name", { unique: false });
 
  // Create an index to search customers by email. We want to ensure that
  // no two customers have the same email, so use a unique index.
  objectStore.createIndex("email", "email", { unique: true });
 
  // Store values in the newly created objectStore.
  for (var i in customerData) {
    objectStore.add(customerData[i]);
  }
};
  
  request.onsuccess = function(event) {
  // Handle errors.
  console.log("request.onsuccess, database opened, now we can add / remove / look for data in it!");
    // The result is the database itself
  db = event.target.result;  
  };
   }

  function addACustomer() {
    if(db === null) {
      alert('Database must be opened first, please click the Create CustomerDB Database first');
      return;
    }
    
    var transaction = db.transaction(["customers"], "readwrite");
    
    // Do something when all the data is added to the database.
    transaction.oncomplete = function(event) {
        console.log("All done!");
    };
 
    transaction.onerror = function(event) {
       console.log("transaction.onerror" + event.target.errorCode);
    };
 
    var objectStore = transaction.objectStore("customers");
    
    var newCustomer={};
    newCustomer.ssn = document.querySelector("#ssn").value;
    newCustomer.name = document.querySelector("#name").value;
    newCustomer.age = document.querySelector("#age").value;
    newCustomer.email = document.querySelector("#email").value;
    alert('adding customer ssn=' + newCustomer.ssn);
    var request = objectStore.add(newCustomer);
    
    request.onsuccess = function(event) {
     console.log("Customer with ssn= " + event.target.result + " added.");
    };
     request.onerror = function(event) {
     alert("request.onerror, could not insert customer, errcode = " + event.target.error.name + ". Certainly either the ssn or the email is already present in the Database");
    };

}

 function removeACustomer() {
    if(db === null) {
      alert('Database must be opened first, please click the Create CustomerDB Database first');
      return;
    }
    
    var transaction = db.transaction(["customers"], "readwrite");
    
    // Do something when all the data is added to the database.
    transaction.oncomplete = function(event) {
        console.log("All done!");
    };
 
    transaction.onerror = function(event) {
       console.log("transaction.onerror errcode=" + event.target.error.name);
    };
 
    var objectStore = transaction.objectStore("customers");
    
   
    alert('removing customer ssn=444-44-4444');
    var request = objectStore.delete("444-44-4444");
    
    request.onsuccess = function(event) {
     console.log("Customer removed.");
    };

     request.onerror = function(event) {
     alert("request.onerror, could not remove customer, errcode = " + event.target.error.name + ". The ssn does not exist in the Database");
    };

}

  function updateACustomer() {
    if(db === null) {
      alert('Database must be opened first, please click the Create CustomerDB Database first');
      return;
    }
    
    var transaction = db.transaction(["customers"], "readwrite");
    
    // Do something when all the data is added to the database.
    transaction.oncomplete = function(event) {
        console.log("All done!");
    };
 
    transaction.onerror = function(event) {
       console.log("transaction.onerror errcode=" + event.target.error.name);
    };
 
    var objectStore = transaction.objectStore("customers");
    
    var customerToUpdate={};
    customerToUpdate.ssn = document.querySelector("#ssn").value;
    customerToUpdate.name = document.querySelector("#name").value;
    customerToUpdate.age = document.querySelector("#age").value;
    customerToUpdate.email = document.querySelector("#email").value;
    alert('updating customer ssn=' + customerToUpdate.ssn);
    
    var request = objectStore.put(customerToUpdate);
    
    request.onsuccess = function(event) {
     console.log("Customer updated.");
    };
     request.onerror = function(event) {
     alert("request.onerror, could not update customer, errcode = " + event.target.error.name + ". The ssn is not in the Database");
    };

}

function searchACustomer() {
    if(db === null) {
      alert('Database must be opened first, please click the Create CustomerDB Database first');
      return;
    }
    
    var transaction = db.transaction(["customers"], "readwrite");
    
    // Do something when all the data is added to the database.
    transaction.oncomplete = function(event) {
        console.log("All done!");
    };
 
    transaction.onerror = function(event) {
       console.log("transaction.onerror errcode" + event.target.error.name);
    };
 
    var objectStore = transaction.objectStore("customers");
    
    var customerToSearch={};
  
    customerToSearch.ssn = document.querySelector("#ssn").value;
   
    alert('Looking for customer ssn=' + customerToSearch.ssn);
    
    var request = objectStore.get(customerToSearch.ssn);
    
    request.onsuccess = function(event) {
     console.log("Customer found" + event.target.result.name);
     document.querySelector("#name").value = event.target.result.name;
     document.querySelector("#age").value = event.target.result.age;
     document.querySelector("#email").value = event.target.result.email;
    };
     request.onerror = function(event) {
     alert("request.onerror, could not find customer, errcode = " + event.target.error.name + ". The ssn is not in the Database");
    };

}
 function searchACustomerShort() {
    if(db === null) {
      alert('Database must be opened first, please click the Create CustomerDB Database first');
      return;
    }
    
      db.transaction("customers").objectStore("customers")
         .get(document.querySelector("#ssn").value).onsuccess = function(event) {
           document.querySelector("#name").value = event.target.result.name;
           document.querySelector("#age").value = event.target.result.age;
           document.querySelector("#email").value = event.target.result.email;
         };
}

function listAllCustomers() {
  if(db === null) {
      alert('Database must be opened first, please click the Create CustomerDB Database first');
      return;
    }
  
  var objectStore = db.transaction("customers").objectStore("customers");
 
objectStore.openCursor().onsuccess = function(event) {
  var cursor = event.target.result;
  if (cursor) {
    alert("Name for SSN " + cursor.key + " is " + cursor.value.name);
    cursor.continue();
  }
  else {
    alert("No more entries!");
  }
};
}


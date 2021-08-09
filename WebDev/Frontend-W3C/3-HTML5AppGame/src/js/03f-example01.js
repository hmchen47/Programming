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
  var db = event.target.result;
 
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
  var db = event.target.result;  
};
 
}


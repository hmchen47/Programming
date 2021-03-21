class Contact {
	constructor(name, email) {
		this.name = name;
		this.email = email;
	}
}

class ContactManager {
	constructor() {
		// when we build the contact manager, it
		// has an empty list of contacts
		this.listOfContacts = [];
	}
	
	// Will erase all contacts
	empty() {
		this.listOfContacts = [];
	}
	
	add(contact) {
		this.listOfContacts.push(contact);
	}
	
	remove(contact) {
		for(let i = 0; i < this.listOfContacts.length; i++) { 
			var c = this.listOfContacts[i];

			if(c.email === contact.email) {
				// remove the contact at index i
				this.listOfContacts.splice(i, i);
				// stop/exit the loop
				break;
			}
		}
	}
	
	sort() {
		// As our array contains objects, we need to pass as argument
		// a method that can compare two contacts.
		// we use for that a class method, similar to the distance(p1, p2)
		// method we saw in the ES6 Point class in module 4
		// We always call such methods using the name of the class followed
		// by the dot operator
		this.listOfContacts.sort(ContactManager.compareByName);
	}
	
	// class method for comparing two contacts by name
	static compareByName(c1, c2) {
		// JavaScript has builtin capabilities for comparing strings
		// in alphabetical order
		if (c1.name < c2.name)
     		return -1;
		
    		if (c1.name > c2.name)
     			return 1;
  
    	return 0;
	}
	
	printContactsToConsole() {
		if(this.listOfContacts.length === 0) {
			console.log("EMPTY LIST!");
			return;
		}
		
		this.listOfContacts.forEach(function(c) {
			console.log(c.name);
		});
	}
	
	load() {
		if(localStorage.contacts !== undefined) {
			// the array of contacts is saved in JSON, let's convert
			// it back to a reak JavaScript object.
			this.listOfContacts = JSON.parse(localStorage.contacts);
		}
	}
	
	save() {
		// We can only save strings in local Storage. So, let's convert
		// ou array of contacts to JSON
		localStorage.contacts = JSON.stringify(this.listOfContacts);
	}
}

var cm = new ContactManager();
var c1 = new Contact("Jimi Hendrix", "jimi@rip.com");
var c2 = new Contact("Robert Fripp", "robert.fripp@kingcrimson.com");
var c3 = new Contact("Angus Young", "angus@acdc.com");
var c4 = new Contact("Arnold Schwarzenneger", "T2@terminator.com");

console.log("--- Adding 4 contacts ---")
cm.add(c1);
cm.add(c2);
cm.add(c3);
cm.add(c4);

cm.printContactsToConsole();

// trying to remove c2
console.log("--- Removing the second one! ---");
cm.remove(c2); 
cm.printContactsToConsole();

console.log("--- Sorting contacts ---");
cm.sort();
cm.printContactsToConsole();

console.log("--- Saving contacts to local storage ---");
cm.save(); 

console.log("--- Emptying the list of contacts ---");
cm.empty();
cm.printContactsToConsole();

console.log("--- Loading contacts from local storage ---");
cm.load();
cm.printContactsToConsole();
console.log("Do you notice: contacts have all been restored!");


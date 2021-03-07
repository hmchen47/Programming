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
	
		printContactsToConsole() {
		    this.listOfContacts.forEach(function(c) {
			       console.log(c.name);
		    });
	  }
	}
	
// ALWAYS TEST YOUR CODE WITH SIMPLE EXAMPLES, or by typing in the devtool console
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


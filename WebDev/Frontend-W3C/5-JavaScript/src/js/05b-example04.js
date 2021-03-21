/* 
	in JavaScript, and in many other programming languages, 
	a string is not modifiable at all. 

	When we do var s = s + "hello", in fact, we are building 
	a new string somewhere in memory, and we assign this 
	new value to the variable s. 
	We never "modify" the characters of the string s, 
	we just give to s another address in memory to point to. 
*/
var name = 'Michel'; // use this rather than using new String(...)

console.log("name = " + name);
console.log("name.length = " + name.length);

console.log("name[0] = " + name[0]);

console.log("But trying to do name[0] = 'Z' will do nothing!!!");
name[0] = 'Z';
console.log("name = " + name);
console.log("name.length = " + name.length);

console.log("name is UNCHANGED! Strings cannot be modified!");

// However doing name = name + " says hello" works, it will create a new
// string in memory with value "Michel says hello" and make the name
// variable reference this new location in memory

/*
Useful methods: toUpperCase, toLowerCase, indexOf, charAt

These methods are all inherited from the String object:

toUpperCase: returns the string in upper case. Do not change the original string.

toLowerCase: returns the string in lower case. Do not change the original string.

indexOf: returns the index of the string value passed as parameter, -1 if the string value is not found in the original string.

charAt: returns the char at the index passed as parameter. Returns an empty string if the index is out of bounds (less than 0 or greater than the length of the string).
*/
console.log("\n\nUSEFUL METHODS");
var s = "I'm the Walrus";
console.log("s = " + s);

console.log("\n\ntoUpperCase() and toLowerCase()");
console.log("s1 = s.toUpperCase();");
var s1 = s.toUpperCase();
console.log("s1 = " + s1);

console.log("s2 = s1.toLowerCase();");
var s2 = s1.toUpperCase();
console.log("s2 = " + s2);

console.log("s is unchanged. s = " + s);


console.log("\n\nindexof()");

console.log("s.indexOf('w'): " + s.indexOf('w'));
s.indexOf('w'); // no ‘w’ in s

console.log("s2.indexOf('w'): " + s2.indexOf('w'));
console.log("s2[8] = " + s2[8]);
console.log("s2.charAt(8) = " + s2.charAt(8)); // same as s2[8]

//Other useful methods: lastIndexOf, chaining methods
// lastIndexOf: returns the last index of the string value passed as parameter
console.log("\n\nlastIndexof()");

s = 'wow wow wow!';
console.log("s = " + s);

console.log("s.lastIndexOf('w') = " + s.lastIndexOf('w'));
console.log("s.indexOf('w', 1) = " + s.indexOf('w', 1));

var s1 = s.toUpperCase();
console.log("s1 = s.toUpperCase(); s1 = " + s1);

 
console.log("We can chain methods: s1.toLowerCase().lastIndexOf('w') = " + s1.toLowerCase().lastIndexOf('w')); // we can chain method calls using ‘.’


/*
The slice and substring methods

Both these methods can be used to extract a substring from a string.

They take two parameters: the start and end index of the slice (element at end index will NOT be included in the slice): “please cut from this index, to this one, not included!”. 

The slice() method will not change the string while substring() will.
*/
console.log("\n\nsubstring() and Slice() -beginners only use substring!");
s = "My name is Bond! James Bond!";
console.log("s = " + s);
var result = s.substring(11, 16);
console.log("s.substring(11, 16) returns " + result);

console.log("But s is unchanged. s = " + s);

console.log("To remove a slice: do s = s.substring(11, 16)"); 
 
s = s.substring(11, 16);
console.log("This time s references a new value: s = " + s);
 
console.log("\n\nsplit() and join() methods");
// The split method returns an array of strings, the parameter is a separator. 
// The join method builds a string from an array of strings.
s = "My name is Bond! James Bond!";
var ar = s.split(" ");
console.log("ar = s.split(' ') returns an array of strings. ar = " + ar);
console.log("But s is unchanged. s = " + s);

result = ar.join('.');
console.log("ar.join('.') will return a string made of the array elements returned joined by '.'");
console.log("result = " + result);
console.log("And s is still unchanged. s = " + s);


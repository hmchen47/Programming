let o = {}; // creation of an empty object
o.name = "Michel";
 
let o1 = new Object(); // same thing as in line 1
o1.name = "Michel";

// But this does not work: "Uncaught TypeError: Cannot set property 'name' of undefined"
// let o2;
// o2.name = "Michel";

// So... writing let o = {}; (or with properties and methods), or using "new" and ES5
// constructor functions or ES6 classes, as seen in Module 4, builds an Object

// On all objects you can use properties and methods that are "inherited" from the predefined
// Object in JavaScript. We say "predefined object", but Java or C# programmers can also
// understand it as "predefined class"...

// Useful inherited methods: toString() and valueOf();
console.log("\n\nLet's try with an array (arrays are objects, do you remember?)")

let t = [1, 2, 3];
 
console.log("t.valueOf() returns the value of t (as an array)...");
// Try typing t.valueOf() in the devtool console
 
console.log("t.toString() = " + t.toString());
console.log("t = " + t + ", in this case, t.toString() is implicit");

console.log("\n\nLet's try with an object")
let p = {
	name:"Michel",
	age:52
}

console.log("p.toString() = " + p.toString());
console.log("p.valueOf() returns the value of p (as an object), try to type p.valueOf() in the devtool console..." );


let a1 = new Array(); // same as a1 = []; use this instead!

 
let b1 = new Array(1, 2, 3); // equivalent to b1 = [1, 2, 3];

let c1 = new Array(10); // if only one parameter, then, it's the size of the array!
console.log("c1.length = " + c1.length);
// try to see the value of c
 

// The length property
console.log("\n\nTHE LENGTH PROPERTY OF ARRAYS!")
let a2 = [1, 2];
console.log("a2.length = " + a2.length);

// remember that arrays are objects, and that we can add properties to objects
// after their creation
a2.name = "Michel"; // AVOID!!!

console.log("a2.length after we set name='Michel', still:" + a2.length);
console.log("only elements with a numeric index are taken into account by length!");

// The length property can be modified: reducing or increasing the size of an array

// If you give to the length property a value bigger 
// than the number of elements in an array, 
// it adds undefined elements to it:
a2.length = 5;
console.log("a2 after a2.length = 5: " + a2);
// type a1 in the devtool console!

// If you give to the length property a value 
// less than the array’s number of elements, it reduces the size of the array:
a2.length = 1;
console.log("a2 after a2.length = 1: " + a2);
// type a1 in the devtool console!

console.log("\n\nUSEFUL METHODS!")
/* 
Most useful methods you can use on arrays: sort(), join(), slice(), splice(), push() and pop()

sort: sort the elements in the array. Either alphabetically if they are strings, or in ascending order if they are numbers. There is also a way to sort the elements using other criteria, which is explained a bit further on in the course. With a call to var b = a.sort(), a is also sorted. The sort method sorts the array + returns it.

join: adds a string between each element and returns the result as a string

slice: returns a sub-array without modifying the original array

splice: modifies the array, it removes “a slice” and it also adds new elements

push: appends an element at the end of the array and returns the new length

pop: removes the last element and returns it
*/
console.log("\n\nTypical usages of  push, pop, sort, join");

// PUSH
var a = [3, 5, 1, 7, 'test'];
console.log("We start with the array a = [3, 5, 1, 7, 'test']");
console.log ("a = " + a);
console.log("\n\na.push('new'); adds a new element to a and returns the new length");
a.push('new'); // appends at the end and returns the new length
console.log ("After a.push('new'), a = " + a); 
// Try typing a in the devtool console
 

// POP
console.log("\n\na.pop(); removes the last element and returns it.");

a.pop(); // removes the last element and returns it
console.log ("a = " + a); 
 
// SORT
console.log("\n\nsort() sorts the elements in an array and returns a sorted array too.");
console.log("Let's try b = a.sort()");

var b = a.sort();
// a is also sorted. The sort method sorts the array + returns it
console.log ("After a.sort(): a = " + a); 
console.log ("And b = " + b); 
 
 // JOIN
 console.log("\n\nvar b = a.join(' and '); adds a string between each element and returns the result as a string");
console.log ("a = " + a); 
var b = a.join(' and ');
console.log ("b = " + b); 

// SLICE
console.log("\n\nThe slice() method returns a sub-array without modifying the original array:");
console.log ("a = " + a); 
console.log("var b = a.slice(1, 3);");
b = a.slice(1, 3); // elements of indexes = 1 and 2,
                   // element at index=3 NOT included
console.log ("b = " + b); 

console.log("var b = a.slice(0, 1);");
b = a.slice(0, 1); // element at index 0, elem at index=1 not included
console.log ("b = " + b); 

console.log("var b = a.slice(0, 2);");
b = a.slice(0, 2); // element at index 0 and 1, elem at index=2 not included
console.log ("b = " + b); 

// SPLICE
// The splice() method modifies the array: 
// it removes “a slice” and also adds new elements
// The first two parameters are start and end indexes, the other parameters are the 
// elements to add to the array to replace the slice that will be removed.
console.log("\n\nThe splice() method modifies the array: it removes “a slice” and also adds new elements");
console.log ("a = " + a); 
console.log("b = a.splice(1, 2, 100, 101, 102);");
b = a.splice(1, 2, 100, 101, 102);
console.log ("b = " + b); 
console.log ("a = " + a); 
console.log("Elements have been inserted where the slice has been removed");

console.log("a.splice(1, 3) will just remove the slice from a");
b = a.splice(1, 3);
console.log ("b = " + b); 
console.log ("a = " + a); 



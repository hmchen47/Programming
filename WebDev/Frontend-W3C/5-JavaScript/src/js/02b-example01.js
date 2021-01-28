var javaScriptCourse = true;

if(javaScriptCourse) {
   console.log("This is a JavaScript course!");
} else {
  console.log("This is NOT a JavaScript course!"); 
}

// comparison operators
// < > <= >= == !=, and === !==
// comparison operators: < > <= >= == !=

var age = "72";

if(age < 2) {
  console.log("I'm a baby");
} else if(age < 18) { 
  console.log("I'm a child");
} else if (age < 60) {
  console.log("I'm an adult");
} else {
  // age >= 60
  console.log("I'm old");
}

if(age === 72) { 
  console.log("I'm 72!");
}

if((age > 12) || (age < 14)) {
  console.log("I'm a young teenager!");
}


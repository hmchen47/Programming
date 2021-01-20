#!/usr/bin/env nodejs

// local scope again, but mistake! We forgot var
// when declaring the local variable x
// -> same as declaring a global function var x = 3; 
function f3() {
  x = 3;      // mistake, we forgot "var"
              // x is no more a local variable, 
              // x is now global!
  var y = 5;  // real local variable
  console.log(x); // displays '3'. 
}

function f4() {
  console.log(x); // will display 3 even if there is no
                  // global declaration var x outside of 
                  // functions. The error in the declaration of x
                  // in f3 has made x global
}

function f5() {
  console.log(y); // error, no global variable y
}

f3(); // displays 3
f4(); // displays 3, x declared without var in f3
      // is considered global, and usable in f4

f5(); // error, y is a variable local to the f3 function

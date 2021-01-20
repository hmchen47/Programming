var x = 1; // global variable, could be "masked" by local variables

function f2(x) {
  console.log(x); // displays the given argument  
                  // not the global value of x (value = 1)
                  // the x parameter acts as a variable
                  // local to the function, that "masks"
                  // the global variable x
}

f2(3); // will display 3

// local scope again
function f3() {
  var x = 4;      // local variable, scope = the function
  console.log(x); // displays '4'. The local variable x
                  // "masks" the global variable x
}

f3(); // will display '4' 


var a = 1; // global variable

function f() {
  if (true) {
    // this is a block, defined by "{" and "}"
    var a = 4; // this "a" is NOT local to the block
  }

  alert(a); // alerts '4', not the global value of '1'
            // a variable declared with "var" in a 
            // function is local to the function!
            // and can be used anywhere in the function
            // so here, the local a masks the global a!
}

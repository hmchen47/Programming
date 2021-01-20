#!/use/bin/exec nodejs

var a = 1; // global variable

function f() {
  if (true) {
    // this is a block, defined by { and }
    let a = 4; // this "a" IS LOCAL TO THE BLOCK
  }

  alert(a); // alerts '1', a is the global variable
            // a variable declared with "let" in a 
            // block is local to the block!
            // and is not defined anywhere else
            // The a defined in the if block is not
            // visible here, so the a we have here
            // is the "global" a!
}


postMessage("Hey, in 3s, I'll start to compute prime numbers...");

setTimeout(function() {
	// The setTimeout is just useful for displaying the message in line 1 for 3 seconds and
	// make it visible
	var n = 1;
	search: while (true) {
	  n += 1;
	  for (var i = 2; i <= Math.sqrt(n); i += 1)
	    if (n % i == 0)
	     continue search;
	  // found a prime!
	  postMessage(n);
	}
}, 3000);

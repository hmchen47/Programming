let a = ['Monday', 'Tuesday', 'Wednesday'];

/*
a.forEach(function(day, index, arr) {
  // day will be the current day
  document.body.innerHTML += day + " is at index: " + index + " from an array of " + arr.length + " elements!<br>";
});
*/
for(let i = 0; i < a.length; i+=2) {
  document.body.innerHTML += a[i] + "<br>";
}


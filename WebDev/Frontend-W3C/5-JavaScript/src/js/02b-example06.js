
// WHILE LOOP
// [initialization]
// while([condition]) {
//    .....
// }
// condition no more satisfied
/*
var n = 1, m = 1; 
 
while (n < 4) {
    console.log("n = " + n)
    n += 1; 
    m += n;
}
console.log("While loop, at the end n=" + n + " and m=" + m); 
*/

// Do... while loop
// do {
//     ...
// } while([condition]);
/*
var i = 0;
 
do {
    console.log('i = ' + i);
    i++;
} while(i < 20);
 
console.log('Value of i after the do-while statement: ' + i);
*/

// FOR LOOPS
// for ([initialization]; [condition]; [final-expression]) {} 

// count 1 by 1 from an initial value to a final value
/*for(var i=0; i < 5; i+=2) {
  console.log(i);
}*/
// count 2 by 2

// iterate on an array
var daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];

for(var i=0; i < daysOfWeek.length; i++) {
  console.log(daysOfWeek[i]);
}

// two for loops: iterate on a two dimensional array,
// in this case a 2x3 matrix
var a = [
 [1,2], // line 1
 [3,4], // line 2
 [5,6]  // line 3
];


for (var i=0; i < a.length; i++) {
 // a[i] = line i The next loop iterates on the elements
 // of the array a[i]: on the elements of the ith line
 for (var j=0; j < a[i].length; j++) {
   console.log(a[i][j]);
 }
}


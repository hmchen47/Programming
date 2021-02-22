/*CONDITIONAL STATEMENTS*/
/*if statement*/

var num = 10;
if (num == 10) {
    num = 20;
}

console.log('if statement,\n num>> ' + num);

/*if-else statement*/

var num = 10;
if (num > 10) {
    num = 20;
} else {
    num = 0;
}

console.log('if-else statement,\n num>> ' +num);

/*
Question 1 
how to replace this code by an expression including one operator?
*/
var max; 
var min;
// Try to uncomment that and // see the difference!
// var min=1;
if (min){
    max = min + 10;
} else {
    max = 10;
}
console.log('question1, \n max>> ' + max);
//Answer is at the end of the document


/*switch statement*/


//switch statement behaviour when break keyword is missing
//comment and uncomment cloudColor variable to see the different results

var gear = '';
//var cloudColor;
//var cloudColor = 'green';
var cloudColor = 'black';
switch(cloudColor) {
    case 'green': gear += 'spacesuit';
        break;
    case 'black': gear += 'boots, ';
    case 'grey': gear += 'umbrella, ';
    case 'white': gear += 'jacket, ';
    default: gear += 'watch';
}

console.log('switch2,\n gear >> ' + gear);

//The above example with break; 

var gear = '';
//var cloudColor;
//var cloudColor = 'green';
var cloudColor = 'black';
switch(cloudColor) {
    case 'green': 
      gear += 'spacesuit';
      break;
    case 'black': 
      gear += 'boots, ';
      break;
    case 'grey': 
      gear += 'umbrella, ';
      break;
    case 'white': 
      gear += 'jacket, ';
      break;
    default: 
      gear += 'watch';
}

console.log('swtich3,\n gear >> ' + gear);



/*
Question 1 
how to replace this code by an expression including one operator?
var max;
var min;
if (min){
    max = min + 10;
} else {
    max = 10;
}
*/

//Answer
var max;
var min;
max = (min)? min+10 : 10;
//console.log('question 1,\n max >> ' + max);



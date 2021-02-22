let myarr = ['red', 'blue', 'yellow', 'purple'];

// each element has an index, starting at 0  

let persons = [
	  {givenName: 'Michel', familyName: 'Buffa', age:51},
    {givenName: 'Pig',    familyName: 'Bodine', age:20},
    {givenName: 'Pirate', familyName: 'Prentice', age:32}
];

function compareByAge(a, b) { // comparison function
  if (a.age < b.age)         // compare by age
    return -1;
  if (a.age > b.age)
    return 1;
  return 0;
}

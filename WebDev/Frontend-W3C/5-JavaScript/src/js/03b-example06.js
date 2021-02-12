var persons = [
  {name:'Michel', age:51},
  {name:'Henri', age:20},
  {name:'Francois', age:29}
];

for(var i = 0; i < persons.length; i++) {
  var p = persons[i]; // current element
  
  document.body.innerHTML += p.name + "<br>"; 
}


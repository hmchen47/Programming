window.onload = init();


function init() {

  var persons = [
    {name:'Michel', age:51},
    {name:'Henri', age:20},
    {name:'Francois', age:29},
    {name:'John', age:69}
  ];
  
  for(var i = 0; i < persons.length; i+=2) {
    var p = persons[i]; // current element
    
    document.body.innerHTML += p.name + "<br>"; 
  }

}



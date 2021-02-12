window.onload = init();

function init() {

  var persons = [
    {name:'Michel', age:51},
    {name:'Henri', age:20},
    {name:'Francois', age:29}
  ];
  
  persons.forEach(function(p, index) {
    document.body.innerHTML += p.name + ", age " + p.age + 
                               ", at index " + index + " in the array<br>"; 
  });

}



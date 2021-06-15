var addStarToTheBody = function(){
    document.body.innerHTML += "*";  
};
 
//this will add one star to the document each 200ms (1/5s)
setInterval(addStarToTheBody, 200);


var addStarToTheBody = function(){
    document.body.innerHTML += "*";
    // calls again itself AFTER 200ms
    setTimeout(addStarToTheBody, 200);
};

// calls the function AFTER 200ms
setTimeout(addStarToTheBody, 200);



function removeSelected() {  
  var list = document.querySelectorAll("#fruits input:checked"); 
  var ul = document.querySelector("#fruits");
  
  list.forEach(function(elm) {
    // elm is an <input type="checkbox">, its parent is a li
    // we want to remove from the <ul> list
    // when we remove the <li>, the <input> will also
    // be removed, as it's a child of the <li>
    var li = elm.parentNode;
    ul.removeChild(li);
  });
}

function reset() {
  var ul = document.querySelector("#fruits");
  // Empty the <ul>
  ul.innerHTML = "";
  
  // Adds each list item to the <ul> using innerHTML += ...
  ul.innerHTML += "<li><input type='checkbox' name='fruit' value='apples'>Apples</li>";

  ul.innerHTML += "<li><input type='checkbox' name='fruit' value='oranges'>Oranges</li>";

    ul.innerHTML += "<li><input type='checkbox' name='fruit' value='bananas'>Bananas</li>";

    ul.innerHTML += "<li><input type='checkbox' name='fruit' value='grapes'>Grapes</li>";
}

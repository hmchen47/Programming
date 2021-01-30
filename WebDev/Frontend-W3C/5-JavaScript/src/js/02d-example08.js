var menu = document.querySelector("#context-menu"); 
var menuIsVisible = false;

/* to attache a context menu to all divs, you can do this:

var divs = document.querySelectorAll(".div");

divs.forEach(function(d) {
    addContextMenu(d);
});
*/

var div1 = document.querySelector("#div1");

addContextMenu(div1);

// Clicking anywhere on the window toggle the menu off
window.addEventListener('click', toggleMenuOff);

function addContextMenu(elem) {
    elem.addEventListener("contextmenu", function(e) {
            //console.log("contextmenu activated");
            e.preventDefault();
            toggleMenuOn();
            positionMenu(e);
    });
}
      
function toggleMenuOn() {
   if(!menuIsVisible) {
       menuIsVisible = true;
        menu.classList.add("context-menu--active");
    }
}

function toggleMenuOff() {
    if(menuIsVisible) {
       menuIsVisible = false;
        menu.classList.remove("context-menu--active");
     }
}


function positionMenu(e) {
     // Mouse position is relative to the element clicked
  
     // We make the coords absolute in the page
     var clickCoordsX = e.pageX;
     var clickCoordsY = e.pageY;
  

     var menuWidth = menu.offsetWidth + 1;
     var menuHeight = menu.offsetHeight + 1;

     var elementWidth = e.target.innerWidth;
     var elementHeight = e.target.innerHeight;

     if ((elementWidth - clickCoordsX) < menuWidth) {
       menu.style.left = elementWidth - menuWidth + "px";
     } else {
       menu.style.left = clickCoordsX + "px";
     }

     if ((elementHeight - clickCoordsY) < menuHeight) {
       menu.style.top = elementHeight - menuHeight + "px";
     } else {
       menu.style.top = clickCoordsY + "px";
     }
   }

// Actions called when a menu item is choosen

function menuItem1() {
  console.log('learn');
  toggleMenuOff();
}

function menuItem2() {
  console.log('clear');
  toggleMenuOff();
}


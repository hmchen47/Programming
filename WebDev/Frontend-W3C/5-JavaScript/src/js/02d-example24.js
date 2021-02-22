window.onload = init;

var menu, menuIsVisible;

function init() {
   menu = document.querySelector("#context-menu"); 
  menuIsVisible = false;
  /* to attach a context menu to all divs, you can do this:
     var divs = document.querySelectorAll(".div");

     divs.forEach(function(d) {
          addContextMenu(d);
     });
  */

  // attache the context menu to the first div
  var div1 = document.querySelector("#div1");
  addContextMenu(div1);

  // Clicking anywhere on the window toggle the menu off
  window.addEventListener('click', toggleMenuOff);
}

function addContextMenu(elem) {
    elem.addEventListener("contextmenu", function(e) {
            //console.log("contextmenu activated");
            e.preventDefault(); // avoids default right click menu
            toggleMenuOn();
            positionMenu(e);
    });
}
      
function toggleMenuOn() {
   if(!menuIsVisible) {
       menuIsVisible = true;
        menu.classList.add("context-menu--active"); // see further in the DOM section of the course
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
     var menuHeight = menu.innerHeight + 1;

     var elementWidth = e.target.offsetWidth;
     var elementHeight = e.target.offsetHeight;

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


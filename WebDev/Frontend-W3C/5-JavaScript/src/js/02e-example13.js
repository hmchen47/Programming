function drag(target, evt) {
    // When dragged, copy into the drag'n'drop clipboard
    // the id of the dragged elem (it's target.id)
		evt.dataTransfer.setData("browser", target.id);
	}

function drop(target, evt) {
    // get the id of the element being dragged
		var id = evt.dataTransfer.getData("browser");
  
		target.appendChild(document.getElementById(id));
      // prevent default behavior
      evt.preventDefault();
}

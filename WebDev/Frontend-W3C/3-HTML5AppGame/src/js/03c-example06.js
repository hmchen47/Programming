function dragStartHandler(event) {
  // allow copy effect on cursor
  event.dataTransfer.effectAllowed = 'copy';
  
  // load and create an image
  var dragIcon = document.createElement('img');
  dragIcon.src = 'http://th03.deviantart.net/fs71/150/i/2011/335/0/6/free_html5_3d_logo_icon__10_icons__by_anonsphere-d4h763w.jpg';
  dragIcon.width = 100;
  
  // set it to the drag cursor
  event.dataTransfer.setDragImage(dragIcon, -10, -10);
  
  // Change css class for visual feedback
  event.target.style.opacity = '0.4';
  event.target.classList.add('dragged');
  
  console.log('dragstart event, target: ' + event.target);
  // Copy in the drag'n'drop clipboard the value of the data* attribute of the target, with a type "Fruits".
    event.dataTransfer.setData("Fruit", event.target.dataset.value);
}

  function dragEndHandler(event) {
    console.log("drag end");
    event.target.style.opacity = '1';
    event.target.classList.remove('dragged');  
}

function dragLeaveHandler(event) {
    console.log("drag leave");
    event.target.classList.remove('draggedOver'); 
}

function dragEnterHandler(event) {
  console.log("Drag enter");
  event.dataTransfer.dropEffect = 'copy';  // See the section on the DataTransfer object.
  event.target.classList.add('draggedOver'); 
}

  function dragOverHandler(event) {
    //console.log("Drag over a droppable zone");
    event.preventDefault(); // Necessary. Allows us to drop.
    
}

function dropHandler(event) {
  console.log('drop event, target: ' + event.target);
  // reset the visual look of the drop zone to default
  event.target.classList.remove('draggedOver'); 
  
  var li = document.createElement('li');
  // get the data from the drag'n'drop clipboard, with a type="Fruit"
  var data = event.dataTransfer.getData("Fruit");

  if (data == 'fruit-apple') {
    li.textContent = 'Apples'; 
  } else if (data == 'fruit-orange') {
    li.textContent = 'Oranges';
  } else if (data == 'fruit-pear') {
    li.textContent = 'Pears';
  } else {
    li.textContent = 'Unknown Fruit';
  }
  // add the dropped data as a child of the list.
  document.querySelector("#droppedFruits").appendChild(li);
}  

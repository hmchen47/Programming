function move(elem) {
  var targetList = document.querySelector('#coolBrowsers');
  targetList.append(elem);
  
  // trick to remove the click listener once
  // the image has been moved into the list
  elem.onclick = null;
}



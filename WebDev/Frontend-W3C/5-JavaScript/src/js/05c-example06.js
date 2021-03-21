function borderCollapse() {
  var table = document.querySelector("table");
  
  table.style.borderCollapse = "collapse";
}

function insertRow() {
  var table = document.querySelector("#myTable");
  
  // without parameters, insert at the end,
  // otherwise parameter = index where the row will be inserted
  var row = table.insertRow();
  
  var cell1 = row.insertCell();
  cell1.innerHTML = "New cell1";
  var cell2 = row.insertCell();
  cell2.innerHTML = "New cell2";
  var cell3 = row.insertCell();
  cell3.innerHTML = "New cell3";
}

function deleteFirstRow() {
  var table = document.querySelector("#myTable");
  table.deleteRow(1); // 0 is the header
}


function insertRow() {
  var table = document.querySelector("#myTable");
  
  // without parameters, insert at the end,
  // otherwise parameter = index where the row will be inserted
  var row = table.insertRow();
  
  row.innerHTML = "<td>New</td><td>New</td><td>New</td>"
}

function deleteFirstRow() {
  var table = document.querySelector("#myTable");
  table.deleteRow(1); // 0 is the header
}



function computeBirthdays() {
  // An array. Each element is the number of times my birthday
  // will occur. For the moment: 0 times on a Monday, 0 times on Friday
  // etc.
  var dayOfTheWeek = [0,0,0,0,0,0,0];

  
  var birthday = document.querySelector("#birthday").value;
  
  // birthday is the value of the input field, 
  // as a string (ex: "1965-4-16")
  // Let's turn it into a Date object
  var birthdayAsDate = new Date(birthday);
  
  // Get the month and year (ex: 16 April)
  var birthdayMonth = birthdayAsDate.getMonth(); // ex: April
  var birthdayDate  = birthdayAsDate.getDate();   // ex: 16
  

  var startYear = document.querySelector("#start").value;
  var endYear = document.querySelector("#end").value;
  
  for (var year = startYear; year <= endYear; year++) {
      var dayOfTheWeekMyBirthDayOccurs = 
          new Date(year, birthdayMonth, birthdayDate).getDay();
  
        console.log('Year : ' + year + " Day of your birthday: " + 
                    getDayName(dayOfTheWeekMyBirthDayOccurs));

      // increment the counter for this day
      dayOfTheWeek[dayOfTheWeekMyBirthDayOccurs]++;
   }

   // add a table to the web page, presenting the results
   displayResults(dayOfTheWeek);

}

function getDayName(dayIndex) {
  var days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
  return days[dayIndex];
}

function displayResults(array) {
  document.querySelector("#results").innerHTML = "<p>Occurences of your Birthday:</p>";
  
  var table = document.createElement("table");
  var firstRow = table.insertRow();
  var secondRow = table.insertRow();
  
  
  array.forEach(function(dayOccurence, index) {
    var dayNameCell = firstRow.insertCell(index);
    dayNameCell.innerHTML = getDayName(index);
    
    var nbCell = secondRow.insertCell(index);
    nbCell.innerHTML = dayOccurence;
    
  });
  
  document.querySelector("#results").appendChild(table);
}


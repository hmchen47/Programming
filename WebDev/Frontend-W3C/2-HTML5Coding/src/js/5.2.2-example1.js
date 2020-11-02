 var geocoder;
      var map;
      var infowindow = new google.maps.InfoWindow();
      var marker;
      function init()
      {
      	geocoder = new google.maps.Geocoder();
      	 
      }

	function checkPasswords() 
	 {

	
 	var password1 = document.getElementById('password1');
 	var password2 = document.getElementById('password2');
 	if (password1.value != password2.value) {
		 password2.setCustomValidity('Passwords do not match');
		 } else {
		 password2.setCustomValidity('');
		 }
 	}
 	function getLocation() {

 		
 		
          if (navigator.geolocation) {

          
            navigator.geolocation.getCurrentPosition(showPosition);
          } else {
         // displayCoords.innerHTML="Geolocation API not supported by your browser.";
       }
     }
     function showPosition(position) {

     	
        var txt ="Latitude: " + position.coords.latitude + 
            "<br />Longitude: " + position.coords.longitude;    
       	showOnGoogleMap(new google.maps.LatLng(position.coords.latitude, position.coords.longitude));
 
    }
     function showOnGoogleMap(latlng) {
 		
 		
        geocoder.geocode({'latLng': latlng}, function(results, status) {
          if (status == google.maps.GeocoderStatus.OK) {
            if (results[1]) {
              
              infowindow.setContent(results[1].formatted_address);
              infowindow.open(map, marker);
              
              // Display address as text in the page
             txt =results[0].formatted_address;
			 document.getElementById('adress').value = txt;
            } else {
              alert('No results found');
            }
          } else {
            alert('Geocoder failed due to: ' + status);
          }
        });
      }    


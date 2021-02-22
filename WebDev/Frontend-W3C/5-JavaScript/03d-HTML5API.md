# Module 3: Playing with HTML5 APIs

## 3.4 Displaying a map with the geolocation API


### 3.4.1 The Geolocation API

This chapter presents the new Geolocation API and illustrates its use with several examples.

The Geolocation HTML5 JavaScript API is implemented by most modern Web browsers, and uses different means to get the current location: GPS, GSM/3G triangulation, Wifi, IP address, etc.

It is possible to prompt the user to activate the GPS (this is what most GPS navigation software does on mobile phones), or ask for a particular mean among those available. It is also possible to track the current position when it changes. This is useful for writing a navigation application or for tracking in real time the position of different participants in the case of an application that involves several persons at the same time (using WebSockets, for example).

[Browser support for the Geolocation API](https://caniuse.com/#feat=geolocation) is excellent, both on mobile and on desktop devices.

#### External resources:

+ The W3C specification: [Geolocation API](https://www.w3.org/TR/geolocation-API/)
+ MDN's Web Docs: [Geolocation API](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API)
+ Browser support tables:
  + on CanIuse: [Geolocation](https://caniuse.com/#feat=geolocation)
  + on MDN: [Geolocation API](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API#Browser_compatibility)


#### Notes for 3.4.1 The Geolocation API

+ Geolocation HTML5 API
  + implemented by most modern Web browser
  + using different means to get the current location, including GPS, GSM/3G triangulation, WiFi, IP address, etc.
  + possible to promot the user to activate the GPS
  + possible to track the current position when it changes, e.g., useful for
    + a navigation application
    + tracking in real time the position of different participants
  + [Interfaces](https://tinyurl.com/pjjj7ayq)
    + [Geolocation](https://tinyurl.com/zeyhput6): containing methods to retrieve the user's current position, watch for changes in their position, and clear a previously-set watch
    + [GeolocationPosition](https://tinyurl.com/w1grzn0k): representing the position of a user
    + [GeolocationCoordinates](https://tinyurl.com/ky6s9uoo): representing the coordinates of a user's position
    + [GeolocationPositionError](https://tinyurl.com/y7pldaqo): returned by an unsuccessful call to one of the methods contained inside Geolocation, inside an error callback, and containing an error code and message
    + [Navigator.geolocation](https://tinyurl.com/2djxdf54): return a Geolocation object instance, from which all other functionality accessed


### 3.4.2 Geolocation and maps

This section presents an example of how to get an interactive map, using [the Leaflet API for OpenStreetMap](https://leafletjs.com/reference-1.6.0.html), and gives links to more resources. Did you know that you can even get an estimation of a physical address from the longitude and latitude, using online Web services?


#### How to get a map centered on your longitude and latitude

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick="window.open('https://tinyurl.com/1eelvuef')"
    src    ="https://tinyurl.com/36dracx2"
    alt    ="Example of HTML5 Geolocation and Leaflet showing a location with OpenStreetMap"
    title  ="Example of HTML5 Geolocation and Leaflet showing a location with OpenStreetMap"
  />
</figure>

This example is just given "as is", as there are so many possibilities for rendering a map with [the Leaflet API for OpenStreetMaps](https://leafletjs.com/reference-1.6.0.html). However, we think having such a basic example might be useful.

[CodePen Demo](https://codepen.io/w3devcampus/pen/LYVgyxE)

[Local Demo](src/03d-example01.html)

Source code extract:

HTML part :

<div><ol>
<li style="margin-bottom: 0px;" value="1">&lt;html&gt;</li>
<li style="margin-bottom: 0px;">&lt;head&gt;</li>
<li style="margin-bottom: 0px;"> &lt;meta charset="utf-8"&gt;</li>
<li style="margin-bottom: 0px;"> &lt;title&gt;OpenStreetMap Example&lt;/title&gt;</li>
<li style="margin-bottom: 0px;"> &lt;link rel="stylesheet" href="https://unpkg.com/leaflet@1.0.3/dist/leaflet.css"&gt;</li>
<li style="margin-bottom: 0px;"> &lt;script src="https://unpkg.com/leaflet@1.0.3/dist/leaflet.js"&gt;&lt;/script&gt; </li>
<li style="margin-bottom: 0px;">&lt;/head&gt;</li>
<li style="margin-bottom: 0px;">&lt;body&gt;</li>
<li style="margin-bottom: 0px;"> &lt;button class="btn" onclick="getLocation(event)"&gt;Click to show your location with OpenStreetMap&lt;/button&gt;</li>
<li style="margin-bottom: 0px;"> &lt;div id="map" class="map"&gt;&lt;/div&gt; </li>
<li style="margin-bottom: 0px;">&lt;/body&gt;</li>
<li style="margin-bottom: 0px;">&lt;/html&gt;</li>
</ol></div>

+ _Lines 5 and 6_ are the required files to use the Leaflet API (this is the official name of the OpenStreetMaps API),
+ _Line 10_ is the `<div>` container that will be used to display the interactive map

JavaScript part:

<div><ol>
<li style="margin-bottom: 0px;" value="1">function getLocation(e) { </li>
<li style="margin-bottom: 0px;"> e.preventDefault();</li>
<li style="margin-bottom: 0px;"> if (!navigator.geolocation) {</li>
<li style="margin-bottom: 0px;"> alert("Browser doesn't support geolocation");</li>
<li style="margin-bottom: 0px;"> } else {</li>
<li style="margin-bottom: 0px;"> navigator.geolocation.getCurrentPosition(success, error);</li>
<li style="margin-bottom: 0px;"> }</li>
<li style="margin-bottom: 0px;">}</li>
<li style="margin-bottom: 0px;"> </li>
<li style="margin-bottom: 0px;">// Get current position successfully</li>
<li style="margin-bottom: 0px;">function success(position) {</li>
<li style="margin-bottom: 0px;"> var map, marker,</li>
<li style="margin-bottom: 0px;"> latitude = position.coords.latitude,</li>
<li style="margin-bottom: 0px;"> longitude = position.coords.longitude;</li>
<li style="margin-bottom: 0px;"> </li>
<li style="margin-bottom: 0px;"> // Instance map using leaflet</li>
<li style="margin-bottom: 0px;"> map = L.map('map').setView([latitude, longitude], 13);</li>
<li style="margin-bottom: 0px;"> </li>
<li style="margin-bottom: 0px;"> // Tile layer using key api at cloudmade.com</li>
<li style="margin-bottom: 0px;"> L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {</li>
<li style="margin-bottom: 0px;"> key: '760506895e284217a7442ce2efe97797',</li>
<li style="margin-bottom: 0px;"> styleId: 103288,</li>
<li style="margin-bottom: 0px;"> maxZoom: 16</li>
<li style="margin-bottom: 0px;"> }).addTo(map);</li>
<li style="margin-bottom: 0px;"> </li>
<li style="margin-bottom: 0px;"> // Marker using leaflet</li>
<li style="margin-bottom: 0px;"> marker = L.marker([latitude, longitude]).addTo(map);</li>
<li style="margin-bottom: 0px;"> </li>
<li style="margin-bottom: 0px;"> // Popup in leaflet</li>
<li style="margin-bottom: 0px;"> marker.bindPopup('&lt;p&gt;Your location&lt;/p&gt;').openPopup();</li>
<li style="margin-bottom: 0px;">}</li>
<li style="margin-bottom: 0px;"> </li>
<li style="margin-bottom: 0px;">// Get current position fail</li>
<li style="margin-bottom: 0px;">function error() {</li>
<li style="margin-bottom: 0px;"> alert('Get current position fail. Please access codepen to get geolocation.');</li>
<li style="margin-bottom: 0px;">}</li>
</ol></div>

+ _Line 6_ uses the [Geolocation API](https://www.w3.org/TR/geolocation-API/) to get the current position, in case of success it calls the success function, passing the location as parameter,
+ _Lines 13 and 14_ show how to get the longitude and latitude properties from the location,
+ The rest is a basic use of the Leaflet API. Notice at _line 17_ that 'map' is the id of the `<div>` from the HTML part of the code.


#### Notes for 3.4.2 Geolocation and maps

+ The Leaflet API for OpenStreetMap
  + [Leaflet API reference](https://leafletjs.com/)
  + example: [centering location on map](src/03d-example01.html)
    + button to trigger map: `<button onclick="getLocation(event)">Click to show your location with OpenStreetMap</button>`
    + container for map: `<div id="map"></div>`
    + get current location: `function getLocation(e) {...}`
      + avoid default behavior: `e.preventDefault();`
      + retrieve the position: `if (!navigator.geolocation) { alert("Browser doesn't support geolocation"); } else { navigator.geolocation.getCurrentPosition(success, error); }`
    + get current position successfully: `function success(position) {...}`
      + global variables for current position: `var latitude = position.coords.latitude, longitude = position.coords.longitude;`
      + map instance using leaflet: `map = L.map('map').setView([latitude, longitude], 13);`
      + tile layer using key api at coludmade.com: `L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { key: '760506895e284217a7442ce2efe97797', styleId: 103288, maxZoom: 16 }).addTo(map);`
      + add marker: `marker = L.marker([latitude, longitude]).addTo(map);`
      + popup in leaflet: `marker.bindPopup('<p>Your location</p>').openPopup();`
    + get error position: `function error() { alert('Get current position fail. Please access codepen to get geolocation.'); }`



### 3.4.3 Reverse geocoding

Different Web services can be used to get an address from longitude and latitude. Most are free of charge, but they will ask you to register an API key and enter your credit card number. If you send too many requests, you will be charged. Such a service is the [Google Reverse Geocoding JavaScript API](https://developers.google.com/maps/documentation/javascript/examples/geocoding-reverse). For those of you who are really interested to know how this API works, please read the Google documentation and tutorials.

There is also an interesting Leaflet plugin (an extension to Leaflet) based on the [Gisgraphy](https://www.gisgraphy.com/) (free open source framework) service, that comes with a [nice demo of reverse geocoding](https://services.gisgraphy.com/static/leaflet/index.html).

Let's see some examples of use.


#### Get address from longitude and latitude

__Example #1: how to get a physical address from the longitude and latitude__

Google reverse geocoding example (screenshot only) :

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/pqnkl3q8')"
    src    ="https://tinyurl.com/bjb4tyry"
    alt    ="Reverse geocoder example"
    title  ="Reverse geocoder example"
  />
</figure>


Source code of this example (in order to run it, you need a Google API key, used at _line 6_).

<div><ol>
<li style="margin-bottom: 0px;" value="1">&lt;!DOCTYPE html&gt;</li>
<li style="margin-bottom: 0px;">&lt;html lang="en"&gt;</li>
<li style="margin-bottom: 0px;"> &lt;head&gt;</li>
<li style="margin-bottom: 0px;">&lt;meta charset="utf-8"&gt;</li>
<li style="margin-bottom: 0px;">&lt;title&gt;Js bin &lt;/title&gt; </li>
<li style="margin-bottom: 0px;"> &lt;script src="https://maps.googleapis.com/maps/api/js?key=PUT_HERE_YOUR_API_KEY&amp;v=3.exp&amp;sensor=false"&gt;&lt;/script&gt; </li>
<li style="margin-bottom: 0px;"> &lt;script&gt;</li>
<li style="margin-bottom: 0px;"> // p elements for displaying lat / long and address</li>
<li style="margin-bottom: 0px;"> var displayCoords, myAddress; </li>
<li style="margin-bottom: 0px;"> </li>
<li style="margin-bottom: 0px;"> // used with the google apis</li>
<li style="margin-bottom: 0px;"> var geocoder;</li>
<li style="margin-bottom: 0px;"> var map;</li>
<li style="margin-bottom: 0px;"> var infowindow = new google.maps.InfoWindow();</li>
<li style="margin-bottom: 0px;"> var marker;</li>
<li style="margin-bottom: 0px;"> </li>
<li style="margin-bottom: 0px;"> // Called when the page is loaded</li>
<li style="margin-bottom: 0px;"> function init() {</li>
<li style="margin-bottom: 0px;"> displayCoords=document.getElementById("msg");</li>
<li style="margin-bottom: 0px;"> myAddress = document.getElementById("address");</li>
<li style="margin-bottom: 0px;"> </li>
<li style="margin-bottom: 0px;"> geocoder = new google.maps.Geocoder();</li>
<li style="margin-bottom: 0px;"> </li>
<li style="margin-bottom: 0px;"> // In order to show something even before a user clicks on the button</li>
<li style="margin-bottom: 0px;"> var latlng = new google.maps.LatLng(34.0144, -6.83);</li>
<li style="margin-bottom: 0px;"> </li>
<li style="margin-bottom: 0px;"> var mapOptions = {</li>
<li style="margin-bottom: 0px;"> zoom: 8,</li>
<li style="margin-bottom: 0px;"> center: latlng,</li>
<li style="margin-bottom: 0px;"> mapTypeId: 'roadmap'</li>
<li style="margin-bottom: 0px;"> }</li>
<li style="margin-bottom: 0px;"> map = new google.maps.Map(document.getElementById('map_canvas'), mapOptions); </li>
<li style="margin-bottom: 0px;"> } // end of init()</li>
<li style="margin-bottom: 0px;"> </li>
<li style="margin-bottom: 0px;"> // Called when the button is clicked</li>
<li style="margin-bottom: 0px;"> function getLocation() {</li>
<li style="margin-bottom: 0px;"> if (navigator.geolocation) {</li>
<li style="margin-bottom: 0px;"> navigator.geolocation.getCurrentPosition(showPosition);</li>
<li style="margin-bottom: 0px;"> } else {</li>
<li style="margin-bottom: 0px;"> displayCoords.innerHTML="Geolocation API not supported by your browser.";</li>
<li style="margin-bottom: 0px;"> }</li>
<li style="margin-bottom: 0px;"> }</li>
<li style="margin-bottom: 0px;"> </li>
<li style="margin-bottom: 0px;"> // Called when a position is available</li>
<li style="margin-bottom: 0px;"> function showPosition(position) {</li>
<li style="margin-bottom: 0px;"> displayCoords.innerHTML="Latitude: " + position.coords.latitude + </li>
<li style="margin-bottom: 0px;"> "&lt;br /&gt;Longitude: " + position.coords.longitude; </li>
<li style="margin-bottom: 0px;"> </li>
<li style="margin-bottom: 0px;"> // Display the map</li>
<li style="margin-bottom: 0px;"> showOnGoogleMap(new google.maps.LatLng(position.coords.latitude, </li>
<li style="margin-bottom: 0px;"> position.coords.longitude));</li>
<li style="margin-bottom: 0px;"> }</li>
<li style="margin-bottom: 0px;"> function showOnGoogleMap(latlng) {</li>
<li style="margin-bottom: 0px;"> // Ask google geocoder for an address once we get a longitude and </li>
<li style="margin-bottom: 0px;"> // a latitude. In fact, the reverse geocoder sends back an array of "guesses"</li>
<li style="margin-bottom: 0px;"> // i.e. not just one address object, but several. Each entry in this array</li>
<li style="margin-bottom: 0px;"> // has several properties such as street, city, etc. We use the "formatted_address"</li>
<li style="margin-bottom: 0px;"> // one here, but it might be interesting to get the detailed properties in other</li>
<li style="margin-bottom: 0px;"> // applications like a form with street, city, zip code etc.</li>
<li style="margin-bottom: 0px;"> geocoder.geocode({'latLng': latlng},reverseGeocoderSuccess);</li>
<li style="margin-bottom: 0px;"> </li>
<li style="margin-bottom: 0px;"> function reverseGeocoderSuccess(results, status) {</li>
<li style="margin-bottom: 0px;"> if (status == google.maps.GeocoderStatus.OK) {</li>
<li style="margin-bottom: 0px;"> if (results[1]) {</li>
<li style="margin-bottom: 0px;"> map.setZoom(11);</li>
<li style="margin-bottom: 0px;"> marker = new google.maps.Marker({</li>
<li style="margin-bottom: 0px;"> position: latlng,</li>
<li style="margin-bottom: 0px;"> map: map</li>
<li style="margin-bottom: 0px;"> });</li>
<li style="margin-bottom: 0px;"> infowindow.setContent(results[1].formatted_address);</li>
<li style="margin-bottom: 0px;"> infowindow.open(map, marker);</li>
<li style="margin-bottom: 0px;"> </li>
<li style="margin-bottom: 0px;"> // Display address as text in the page</li>
<li style="margin-bottom: 0px;"> myAddress.innerHTML="Adress: " + results[0].formatted_address;</li>
<li style="margin-bottom: 0px;"> } else {</li>
<li style="margin-bottom: 0px;"> alert('No surface address found');</li>
<li style="margin-bottom: 0px;"> }</li>
<li style="margin-bottom: 0px;"> } else {</li>
<li style="margin-bottom: 0px;"> alert('Geocoder failed due to: ' + status);</li>
<li style="margin-bottom: 0px;"> }</li>
<li style="margin-bottom: 0px;"> } // end of reverseGeocoderSuccess</li>
<li style="margin-bottom: 0px;"> } // end of showOnGoogleMap</li>
<li style="margin-bottom: 0px;"> &lt;/script&gt;</li>
<li style="margin-bottom: 0px;"> &lt;/head&gt;</li>
<li style="margin-bottom: 0px;"> &lt;body onload="init()"&gt;</li>
<li style="margin-bottom: 0px;"> &lt;title&gt;HTML5 + Geolocalisation + Google Maps API Reverse Geocoding&lt;/title&gt;</li>
<li style="margin-bottom: 0px;"> </li>
<li style="margin-bottom: 0px;"> &lt;p id="msg"&gt;Click the button to get your coordinates:&lt;/p&gt;</li>
<li style="margin-bottom: 0px;"> &lt;p id="address"&gt;&lt;/p&gt;</li>
<li style="margin-bottom: 0px;"> </li>
<li style="margin-bottom: 0px;"> &lt;button onclick="getLocation()"&gt;Where am I ?&lt;/button&gt;</li>
<li style="margin-bottom: 0px;"> &lt;div id="map_canvas" style="width: 500px; height: 300px"&gt;&lt;/div&gt;</li>
<li style="margin-bottom: 0px;"> &lt;/body&gt;</li>
<li style="margin-bottom: 0px;">&lt;/html&gt;</li>
</ol></div>


Gisgraphy (free service) reverse geocoding example (screenshot only, click on it to see [the demo on the Gisgraphy website](https://services.gisgraphy.com/static/leaflet/index.html)):


#### Reverse Geolocation

Important note: these examples below rely on an external [GitHub resource](https://github.com/perliedman/leaflet-control-geocoder). No related questions are asked in this module's exerises or final exam.

Please, pan and zoom on the map and click. The longitude and latitude are computed from your click and a free reverse geocoding service is used to convert to a physical address.

[CodePen Demo](https://codepen.io/w3devcampus/pen/ZEQJQQp)

[Local Demo](src/03d-example02.html)


#### Showing address

__Example #3: shows the address on the map, from your current longitude and latitude__

Click on the Codepen logo on the top right to open the example in Codepen. Due to security reasons, it cannot run embedded in this page.

[CodePen Demo](https://codepen.io/w3devcampus/pen/KKVXaRJ)

[Local Demo](src/03d-example03.html)


#### Geolocation, map, and reverse geocoder

__Example #4: use of geolocation, map and reverse geocoder in a HTML form__

This is just a variation of the previous examples. We embedded the interactive map in a form, and we display the results of the reverse geocoder in a form field. This example might be useful if you want to pre-fill the address of a registration form, depending on the current location of the person who is registering.

Click on the Codepen logo (on the top right) so to run the online example (for security reasons the embedded version cannot run in this page):

[CodePen Demo](https://codepen.io/w3devcampus/pen/MWKEJqM)

[Local Demo](src/03d-example04.html)


#### Notes for 3.4.3 Reverse geocoding

+ Reverse geolocation
  + used to get an address from longitude and latitude
  + Web service free charge but limited requests
    + register required w/ credit card
    + charged once exceeding limitation
    + examples:
      + [Google Reverse Geocoding JavaScript API](https://developers.google.com/maps/documentation/javascript/examples/geocoding-reverse)
      + [Gisgraphy](https://www.gisgraphy.com/): base of Leaflet plugin, free open source framework

+ Example: [get address from longitude and latitude w/ Google service](https://services.gisgraphy.com/static/leaflet/index.html)
  + mouse click event listener: `<button onclick="getLocation()">Where am I ?</button>`
  + map container: `<div id="map_canvas" style="width: 500px; height: 300px"></div>`
  + global variables for Google API: `var geocoder; var map; var infowindow = new google.maps.InfoWindow(); var marker;`
  + global variables for input/outout: `var displayCoords, myAddress;`
  + init after the DOM loaded: `function init() {...}`
    + access elements: `displayCoords=document.getElementById("msg"); myAddress = document.getElementById("address");`
    + get geocoder object: `geocoder = new google.maps.Geocoder();`
    + showing demo info before user click: `var latlng = new google.maps.LatLng(34.0144, -6.83);`
    + map settings: `var mapOptions = { zoom: 8, center: latlng, mapTypeId: 'roadmap' }`
    + get map object: `map = new google.maps.Map(document.getElementById('map_canvas'), mapOptions);`
  + action for mouse click: `function getLocation() {...}`
    + show position on map if `navigator.geolocation` exist: `navigator.geolocation.getCurrentPosition(showPosition);`
    + show err msg: `displayCoords.innerHTML="Geolocation API not supported by your browser.";`
  + display longitude and latitude if position available: `function showPosition(position) {...}`
    + add info: `displayCoords.innerHTML="Latitude: " + position.coords.latitude + "<br />Longitude: " + position.coords.longitude;`
    + display map: `showOnGoogleMap(new google.maps.LatLng(position.coords.latitude, position.coords.longitude));`
  + disply on google map: `function showOnGoogleMap(latlng) {...}`
    + ask google decorder for an address and return an array of "guesses" w/ "formatted_address": `geocoder.geocode({'latLng': latlng},reverseGeocoderSuccess);`
    + callback w/ success: `function reverseGeocoderSuccess(results, status) {...}`
      + if `status == google.maps.GeocoderStatus.OK` and `result[1]` existed, then parameter settings: `map.setZoom(11); marker = new google.maps.Marker({ position: latlng, map: map});`
      + display info w/ `infowindow`: `infowindow.setContent(results[1].formatted_address); infowindow.open(map, marker);`
      + display text message: `myAddress.innerHTML="Address: " + results[0].formatted_address;`
      + result failed: `alert('No surface address found');`
      + geocoder failed: `alert('Geocoder failed due to: ' + status);`

+ Example: [reverse geolocation](src/03d-example02.html)
  + map container: `<div id="map"></div>`
  + global variables: `var map = L.map('map').setView([0, 0], 2); var geocoder = L.Control.Geocoder.nominatim(); var marker;`
  + searching: `if (URLSearchParams && location.search) {...}`
    + variables searching: `var params = new URLSearchParams(location.search); var geocoderString = params.get('geocoder');`
    + both info available: `console.log('Using geocoder', geocoderString); geocoder = L.Control.Geocoder[geocoderString]();`
    + only `geocoderString` available: `console.warn('Unsupported geocoder', geocoderString);`
  + control info: `var control = L.Control.geocoder({ query: 'Moon', placeholder: 'Search here...', geocoder: geocoder }).addTo(map);`
  + timeout setting: `setTimeout(function() { control.setQuery('Earth'); }, 12000);`
  + layer setting: `L.tileLayer('https://{s}.tile.osm.org/{z}/{x}/{y}.png', { attribution: '&copy; <a href="https://osm.org/copyright">OpenStreetMap</a> contributors' }).addTo(map);`
  + mouse click event and processing: `map.on('click', function(e) {...})`
    + get reverse geolocation: `geocoder.reverse(e.latlng, map.options.crs.scale(map.getZoom()), function(results) {...})`
      + `result[0]` & `marker` existed: `marker.setLatLng(r.center).setPopupContent(r.html || r.name).openPopup();`
      + only marker existed: `marker = L.marker(r.center).bindPopup(r.name).addTo(map).openPopup();`

+ Example: [showing address](src/03d-example03.html)
  + map container: `<div id="map"></div>`
  + global variables: `var geocoder = L.Control.Geocoder.nominatim(); var map, marker, latitude, longitude;`
  + get location: `function getLocation() {...}`
    + `navigator.geolocation` exist: `navigator.geolocation.getCurrentPosition(success, error);`
    + warning msg if not existed: `alert("Browser doesn't support geolocation");`
  + current position success: `function success(position) {...}`
    + variables: `latitude = position.coords.latitude; longitude = position.coords.longitude;`
    + instance map w/ leaflet: `map = L.map('map').setView([latitude, longitude], 13);`
    + tile layer using key api at coludmade.com: `L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { key: '760506895e284217a7442ce2efe97797', styleId: 103288, maxZoom: 16 }).addTo(map);`
    + marker using leaflet: `marker = L.marker([latitude, longitude]).addTo(map);`
    + popup marker: `marker.bindPopup('<p></p>').openPopup();`
    + display physical address: `getPhysicalAddress({lat:latitude, lng:longitude});`
  + current position failed: `alert('Get current position fail. Please access codepen to get geolocation.');`
  + get physical address: `function getPhysicalAddress(latlong) {...}` w/ the same function as `map.on('click', function(e) {...}` in "reverse geolocation" example
  + execute the JS code: `getGeolocation();`

+ Example: [geolocation, map and reverse geoencoder in a HTML form](src/03d-example04.html)
  + using `<form>` as container for map as address input
    + map field: `<fieldset><legend>Form example with map and address...</legend> <div id="map" style="width: 500px; height: 300px"></div> </fieldset>`
    + address entry: `<fieldset> <legend>Surface address</legend> <input id="surfaceAddress" size=110 type="text"> </fieldset>`
  + global variables: `var geocoder = L.Control.Geocoder.nominatim(); var map, marker, latitude, longitude;`
  + get location as in "showing address"
  + current position success as in "showing address"
  + current position failed as in "showing address"
  + get physical address as in "showing address"


### 3.4.4 Discussion and projects

Here is the discussion forum for this part of the course. Please either post your comments/observations/questions or share your creations.

#### Suggested topics

+ What features of a Web application do you think could benefit from geolocation?
+ Do you know that you can simulate a position using the dev. tools of some browsers? Try exploring the dev. tools of Google Chrome. Also, there are browser extensions and applications that can help develop interactive maps. Please look for some of them and share your findings in the forum.

  <figure style="margin: 0.5em; text-align: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
      onclick="window.open('https://tinyurl.com/1iua3l5r')"
      src    ="https://tinyurl.com/1plnvtiv"
      alt    ="devtool console geolocation simulation"
      title  ="devtool console geolocation simulation"
    />
  </figure>

+ Can you recommend good tutorials about Google Map and about OpenStreetMap, the two main services that propose maps on the fly?


#### Optional projects

Here are a few project ideas. Your classmates and the team who prepared the course will be glad to try them and offer feedback. Please post URLs in this discussion forum. These projects are optional, meaning that they won't be graded.

+ __Project 1 (easy):__ Add a map showing your location to one of your Web pages. Start with a simple, static map, then try with an interactive map. Reuse the examples from the course.
+ __Project 2 (a bit harder):__ The examples provided in the course used OpenStreetMap, but why don't you try to do the same with GoogleMaps? Some services are free of charge, but they will ask you to get an API key (see [this YouTube tutorial](https://www.youtube.com/watch?v=C3znRXBMYZo) about how to get such a key).





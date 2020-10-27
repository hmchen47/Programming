# Week 6: HTML5 Basic APIs


## 6.4 The Geolocation API


### 6.4.0 Lecture Notes

+ [Geolocation API](#641-introduction)
  + implemented by most modern Web browsers
  + using different means to get the current location: GPS, GSM/3G triangulation, Wifi, IP address, etc.
  + mobile phones:
    + prompt the user to activate the GPS and ask for a particular mean among those available
    + track the current position when it changes
    + useful for writing a navigation application
    + useful for tracking in real time the position of different participants
    + application involving several persons at the same time (using WebSockets, for example)
  + typical usage

    ```js
    navigator.geolocation.getCurrentPosition(showPosition, onError);

    function showPosition(position) {
        console.log("latitude is: " + position.coords.latitude);
        console.log("longitude is: " + position.coords.longitude);
    }

    function onError(err) {
        console.log("Could not get the position");
    }
    ```

  + example: get location
    + check if the Web browser supports the `geolocation` API by testing the variable `navigator.geolocation`:
      + `navigator.geolocation.getCurrentPosition(showPosition)` passing a callback function as a parameter
      + when a current position available, the callback function called asynchronously
      + the input parameter of this callback function = the current position

      ```js
      function getLocation() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(showPosition);
        } else {
            displayCoords.innerHTML="Geolocation API not supported by your browser.";
        }
      }
      ```

    + position objects w/ a `coords` property: the longitude and the latitude

      ```js
      function showPosition(position) {
        displayCoords.innerHTML="Latitude: " + position.coords.latitude +
                               "<br />Longitude: " + position.coords.longitude;
      }
      ```

  + [Geolocation API Specification](https://www.w3.org/TR/geolocation-API/)
  + [Geolocation API - WDN](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API)

+ [coords object properties](#642-the-coords-object-properties)
  + __latitude:__ the latitude of the position
  + __longitude:__ the longitude of the position
  + __altitude:__ the altitude of the position
  + __accuracy:__ the accuracy of the measure of the longitude and latitude (in meters)
  + __altitudeAccuracy:__ the accuracy of the measure of the altitude (in meters)
  + __heading:__ giving the orientation relative to north, in degrees
  + __speed:__ current speed in meters/second

+ [Geolocation error codes](#643-geolocation-error-codes)
  + `navigator.geolocation.getCurrentPosition` method possible to pass a second parameter in case of errror
  + example: error handler
    + get location: `navigator.geolocation.getCurrentPosition(showPosition, errorPosition);`
    + error handling

      ```js 
      function errorPosition(error) {
        var info = "Error during geolocation: ";
        switch(error.code) {
          case error.TIMEOUT:
              info += "Timeout !";
              break;
          case error.PERMISSION_DENIED:
              info += "Permission denied, geolocation could not be obtained...";
              break;
          case error.POSITION_UNAVAILABLE:
              info += "Location could not be obtained though the available means...";
              break;
          case error.UNKNOWN_ERROR:
              info += "Unknown error";
              break;
        }
        displayCoords.innerHTML = info;
      }
      ```

+ [Tracking position](#644-tracking-a-position) 
  + syntax: `watchPosition(onSuccess, onError)`
    + get the callback function only when the current position changes
    + return an `id` to use the `clearWatch(id)` method to stop the current tracking
  + track the current position
  + typical usage:
    + get an id of the current tracking: `var watchPosId = navigator.geolocation.watchPosition(showPosition);`
    + stop the tracking: `navigator.geolocation.clearWatch(watchPosId);`

+ [Properties of the coords object for real time tracking](#options-available-when-using-the-geolocation-api-in-particular-real-time-tracking)
  + __enableHighAccuracy:__ 
    + a boolean (true/false) indicating to the device wish to obtain its most accurate readings
    + using the GPS
    + probably making a difference, depending on your hardware, GPS availability, etc.
  + __maximumAge:__
    + the maximum amount of time (in milliseconds) the position  in the cache
    + appropriate as the device may cache readings to save power and/or bandwidth
  + __timeout:__
    + the maximum time (in milliseconds)
    + prepared to allow the device to try to obtain a Geo location
    + after this timeout, call the `onError` callback

+ [Example: tracking position](#example-of-use)
  + ask to turn GPS on, if available: `navigator.geolocation.getCurrentPosition(onSuccess, onError, {enableHighAccuracy:true});`
  + the position cached for 10 mins useful when in tunnels: `maximumAge = 10 mins` 
  + when the device tries to get a position, if it does not succeed, then go on error immediately: `navigator.geolocation.getCurrentPosition(onSuccess, onError, {maximumAge:600000, timeout:0});`
  + position will never come from the cache (maximumAge: 0), and if after 0.1s the position could not be computed, then go on error: `navigator.geolocation.getCurrentPosition(onSuccess, onError, {maximumAge:0, timeout:100});`
  + ask for GPS, cache for 30s, 27s before going on error: `watchId=navigator.geolocation.watchPosition(onSuccess, onError, {enableHighAccuracy:true, maximumAge:30000, timeout:27000});`

+ [Get a map centered on given longitude and latitude](#645-geolocation-and-maps)
  + rendering a map with the [Leaflet API for OpenStreetMaps](https://leafletjs.com/reference-1.6.0.html)
  + required files to use the Leaflet API :
    + `<link rel="stylesheet" href="https://unpkg.com/leaflet@1.0.3/dist/leaflet.css">`
    + `<script src="https://unpkg.com/leaflet@1.0.3/dist/leaflet.js"></script>`
  + container to display the interactive map: `<div id="map"></div>`
  + using the [Geolocation API](https://www.w3.org/TR/geolocation-API/) to get the current position: `navigator.geolocation.getCurrentPosition(success, error);`
  + successfully get the location: `function success(position) {...}`
    + get the longitude and latitude properties from the location: `latitude = position.coords.latitude, longitude = position.coords.longitude;`
    + instance map using leaflet w/ `id='map'`: `map = L.map('map').setView([latitude, longitude], 13);`
    + tile layer using key API at cloudmade.com

      ```js
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        key: '760506895e284217a7442ce2efe97797',
        styleId: 103288,
        maxZoom: 16
      }).addTo(map);
      ```

    +  marker using leaflet: `marker = L.marker([latitude, longitude]).addTo(map);`
    + popup in leaflet: `marker.bindPopup('<p>Your location</p>').openPopup();`
  + get current position fail: ` alert('Get current position fail. Please access codepen to get geolocation.');`

+ [Reverse Geocoding](#646-reverse-geocoding)
  + Web services:
    + used to get an address from longitude and latitude
    + mostly free of charge, but ask to register an API key and enter your credit card number
    + if too many requests, you will be charged
    + examples:
      + the [Google Reverse Geocoding JavaScript API](https://tinyurl.com/pdlpfjc)
      + Leaflet plugin (an extension to Leaflet) based on the Gisgraphy (free open source framework)
  + example: get address from longitude & latitude
    + access Google API: `<script src="https://maps.googleapis.com/maps/api/js?key=PUT_HERE_YOUR_API_KEY&v=3.exp&sensor=false">`
    + using the google apis: `var infowindow = new google.maps.InfoWindow();`
    + initializing JS after page loaded: `function init() {...}`
      + linking w/ html elements: `displayCoords=document.getElementById("msg"); myAddress = document.getElementById("address");`
      + access Google map: `geocoder = new google.maps.Geocoder();`
      + displaying something before click button: `geocoder = new google.maps.Geocoder();`
      + parameters for Google map: `var mapOptions = { zoom: 8, center: latlng, mapTypeId: 'roadmap' }`
      + get initial map: `map = new google.maps.Map(document.getElementById('map_canvas'), mapOptions);`
    + button clicked: `navigator.geolocation.getCurrentPosition(showPosition);`
    + show position as available: `function showPosition(position) {...}`
      + insert HTML code: `displayCoords.innerHTML="Latitude: " + position.coords.latitude + "<br />Longitude: " + position.coords.longitude;`
      + display map: `showOnGoogleMap(new google.maps.LatLng(position.coords.latitude, position.coords.longitude));`
    + ask google geocoder for an address: `function showOnGoogleMap(latlng) {...}`
      + the reverse geocoder sends back an array of "guesses", i.e. not just one address object, but several
      + each entry in this array has several properties such as street, city, etc.
      + using the "formatted_address" one here
      + probably interesting to get the detailed properties in other applications like a form with street, city, zip code etc.
      + the reverse geocoder: `geocoder.geocode({'latLng': latlng},reverseGeocoderSuccess);`
    + process the map: `function reverseGeocoderSuccess(results, status) {...}`
      + display marker if success: `status == google.maps.GeocoderStatus.OK`

        ```js
        if (results[1]) {
            map.setZoom(11);
            marker = new google.maps.Marker({ position: latlng, map: map });
            infowindow.setContent(results[1].formatted_address);
            infowindow.open(map, marker);
            // Display address as text in the page
            myAddress.innerHTML="Adress: " + results[0].formatted_address; 
        } else {
            alert('No surface address found');
        }
        ```

      + showing warning message: `alert('Geocoder failed due to: ' + status);`


### 6.4.1 Introduction


#### Introduction

This chapter presents the new Geolocation API and illustrates its use with several examples.

The Geolocation HTML5 JavaScript API is implemented by most modern Web browsers, and uses different means to get the current location: GPS, GSM/3G triangulation, Wifi, IP address, etc.

It is possible to prompt the user to activate the GPS (this is what most GPS navigation software does on mobile phones), or ask for a particular mean among those available. It is also possible to track the current position when it changes. This is useful for writing a navigation application or for tracking in real time the position of different participants in the case of an application that involves several persons at the same time (using WebSockets, for example).

[Browser support for the Geolocation API](https://caniuse.com/#feat=geolocation) is excellent, both on mobile and on desktop devices.


#### Typical use

<div><ol>
<li value="1"><strong>navigator.geolocation.getCurrentPosition(showPosition, onError);</strong></li>
<li>&nbsp;</li>
<li>function showPosition(position) {</li>
<li>&nbsp; &nbsp; console.log("latitude is: " + position.coords.latitude); </li>
<li>&nbsp; &nbsp; console.log("longitude is: " + position.coords.longitude);</li>
<li>}</li>
<li>&nbsp;</li>
<li>function onError(err) {</li>
<li>&nbsp; &nbsp; console.log("Could not get the position");</li>
<li>}</li>
</ol></div>

[This online example at JSBin](https://jsbin.com/toyeley/1/edit?html,output) shows how to get the current longitude and latitude and display them in an HTML page. Try it below in your browser: ([Local Example - Location](src/6.4.1-example1.html))

<div>
<p id="msg">Click the button to get your coordinates:</p>
<p><button onclick="getLocation2()">Where am I ?</button></p>
</div>

Note that the first time you execute this example, for privacy reasons, the browser will ask if you agree to share your position with the application.

Source code of this typical example:

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html lang="en"&gt;</li>
<li> &lt;head&gt;</li>
<li>&lt;meta charset="utf-8"&gt;</li>
<li>&lt;title&gt;Basic example of use of the geolocation API&lt;/title&gt;</li>
<li> &lt;/head&gt;</li>
<li>&lt;body&gt;</li>
<li>&lt;p id="msg"&gt;Click the button to get your coordinates:&lt;/p&gt;</li>
<li>&lt;button onclick="getLocation()"&gt;Where am I ?&lt;/button&gt;</li>
<li> </li>
<li>&lt;script&gt;</li>
<li>&nbsp; &nbsp; var displayCoords=document.getElementById("msg");</li>
<li> </li>
<li>&nbsp; &nbsp; function getLocation() {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;if (navigator.geolocation) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <strong>navigator</strong><strong>.geolocation.getCurrentPosition(showPosition);</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;} else {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; displayCoords.innerHTML="Geolocation API not supported by your browser.";</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;}</li>
<li>&nbsp; &nbsp;}</li>
<li> </li>
<li>&nbsp; <strong>&nbsp;function</strong><strong> showPosition(position)</strong> {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;displayCoords.innerHTML="Latitude: " +<strong> position.coords.latitude </strong>+ </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"&lt;br /&gt;Longitude: " +<strong> position.coords.longitude</strong>; </li>
<li>&nbsp; &nbsp;}</li>
<li>&lt;/script&gt;</li>
<li>&lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
</ol></div>


<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick="window.open('https://tinyurl.com/yyr7wu43')"
    src    ="https://tinyurl.com/y6xmjhzm"
    alt    ="geolocation callback illustration"
    title  ="geolocation callback illustration"
  />
</figure>


__Explanations:__

+ _Line 14_ checks if the Web browser supports the `geolocation` API by testing the variable `navigator.geolocation`. If not null, then the `geolocation` API is supported.
+ _Line 15_ calls `navigator.geolocation.getCurrentPosition(showPosition)` passing a callback function as a parameter (in this example we did not specify a callback in case of error). __When a current position is available, the callback function will be called asynchronously, and the input parameter of this callback function will be the current position,__ like in the function `showPosition(position)` of the example.
+ _Line 22_: the `position` objects has a `coords` property that is the object that holds the `longitude` and the `latitude`.


#### External resources:

+ The W3C specification: [Geolocation API](https://www.w3.org/TR/geolocation-API/)
+ MDN's Web Docs: [Geolocation API](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API)
+ Browser support tables:
  + on CanIuse: [Geolocation](https://caniuse.com/#feat=geolocation)
  + on MDN: [Geolocation API](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API#Browser_compatibility)



### 6.4.2 The coords object properties

In the previous example, we used the `coords` property of the position passed as an input parameter to the callback function. This `coords` object has many properties:

<table style="table-layout: auto; border: 5px solid lightGrey; color: black; font-size: 1.0em; font-family: arial,helvetica,sans-serif; width: 45vw;" cellspacing="0" cellpadding="5" border="0" align="center">  
<tbody>
<tr>
<td colspan="2" style="padding: 5px; background-color: #007ff6; color: white; font-size: 1.2em; border: 2px solid lightGrey; text-align: center;">Properties of the coords object</td>
</tr>
<tr>
<td style="text-align: center; background-color: #007ff6; color: white; font-size: 1.2em; border: 2px solid lightGrey;" valign="top"><strong><span style="font-family: 'courier new', courier;">latitude</span></strong></td>
<td style="background-color: white; border: 2px solid lightGrey; color: black;" valign="top">The latitude of the position</td>
</tr>
<tr>
<td style="text-align: center; background-color: #007ff6; color: white; font-size: 1.2em; border: 2px solid lightGrey;" valign="top"><strong><span style="font-family: 'courier new', courier;">longitude</span></strong></td>
<td style="background-color: white; border: 2px solid lightGrey; color: black;" valign="top">The longitude of the position</td>
</tr>
<tr>
<td style="text-align: center; background-color: #007ff6; color: white; font-size: 1.2em; border: 2px solid lightGrey;" valign="top"><strong><span style="font-family: 'courier new', courier;">altitude</span></strong></td>
<td style="background-color: white; border: 2px solid lightGrey; color: black;" valign="top">The altitude of the position</td>
</tr>
<tr>
<td style="text-align: center; background-color: #007ff6; color: white; font-size: 1.2em; border: 2px solid lightGrey;" valign="top"><strong><span style="font-family: 'courier new', courier;">accuracy</span></strong></td>
<td style="background-color: white; border: 2px solid lightGrey; color: black;" valign="top">The accuracy of the measure of the longitude and latitude (in meters)</td>
</tr>
<tr>
<td style="text-align: center; background-color: #007ff6; color: white; font-size: 1.2em; border: 2px solid lightGrey;" valign="top"><strong><span style="font-family: 'courier new', courier;">altitudeAccuracy</span></strong></td>
<td style="background-color: white; border: 2px solid lightGrey; color: black;" valign="top">The accuracy of the measure of the altitude (in meters)</td>
</tr>
<tr>
<td style="text-align: center; background-color: #007ff6; color: white; font-size: 1.2em; border: 2px solid lightGrey;" valign="top"><strong><span style="font-family: 'courier new', courier;">heading</span></strong></td>
<td style="background-color: white; border: 2px solid lightGrey; color: black;" valign="top">gives the orientation relative to north, in degrees</td>
</tr>
<tr>
<td style="text-align: center; background-color: #007ff6; color: white; font-size: 1.2em; border: 2px solid lightGrey;" valign="top"><strong><span style="font-family: 'courier new', courier;">speed</span></strong></td>
<td style="background-color: white; border: 2px solid lightGrey; color: black;" valign="top">current speed in meters/second</td>
</tr>
</tbody>
</table>

Not all these values may be available in all Web browsers. When one of these properties is null, it means that it is not available (often the case of the altitudeAccuracy)


### 6.4.3 Geolocation error codes

In the last example, we used the `navigator.geolocation.getCurrentPosition(showPosition)` with only one callback function (in the case of success), but it is also possible to pass a second parameter that is another callback function called in the case of error.

A slightly different version of the previous example [shows how to properly check against the different possible errors](https://jsbin.com/bafusik/edit?html,output). Try it, then turn your WiFi off or unplug your Ethernet cable (or turn off GPS and 3G/4G on a mobile phone). You should see an error message "_Error during geolocation: Location could not be obtained though the available means_":

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick="window.open('https://tinyurl.com/y64sfgkf')"
    src    ="https://tinyurl.com/y2mlkhsq"
    alt    ="geolocation error"
    title  ="geolocation error"
  />
</figure>


Source code of the example:

<div><ol>
<li value="1"><span>&lt;!DOCTYPE html&gt;</span></li>
<li><span>&lt;html</span><span> </span><span>lang</span><span>=</span><span>"en"</span><span>&gt;</span></li>
<li><span> </span><span>&lt;head&gt;</span></li>
<li><span>&lt;meta</span><span> </span><span>charset</span><span>=</span><span>"utf-8"</span><span>&gt;</span></li>
<li><span>&lt;title&gt;</span><span>Basic example of use of the geolocation API</span><span>&lt;/title&gt;</span></li>
<li><span> </span><span>&lt;/head&gt;</span></li>
<li><span>&lt;body&gt;</span></li>
<li><span>&lt;p</span><span> </span><span>id</span><span>=</span><span>"msg"</span><span>&gt;</span><span>Click the button to get your coordinates:</span><span>&lt;/p&gt;</span></li>
<li><span>&lt;button</span><span> </span><span>onclick</span><span>=</span><span>"</span><span>getLocation</span><span>()</span><span>"</span><span>&gt;</span><span>Where am I ?</span><span>&lt;/button&gt;</span></li>
<li><span> </span></li>
<li><span>&lt;script&gt;</span></li>
<li><span>&nbsp; &nbsp;var</span><span> displayCoords</span><span>=</span><span>document</span><span>.</span><span>getElementById</span><span>(</span><span>"msg"</span><span>);</span></li>
<li><span> </span></li>
<li><span>&nbsp; &nbsp;function</span><span> getLocation</span><span>()</span><span> </span><span>{</span></li>
<li><span>&nbsp; &nbsp; &nbsp;&nbsp;</span><span>if</span><span> </span><span>(</span><span>navigator</span><span>.</span><span>geolocation</span><span>)</span><span> </span><span>{</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<strong>navigator</strong></span><strong><span>.</span><span>geolocation</span><span>.</span><span>getCurrentPosition</span><span>(</span><span>showPosition</span><span>,</span><span style="color: #ff0000;"> errorPosition</span><span>);</span></strong></li>
<li><span>&nbsp; &nbsp; &nbsp; </span><span>}</span><span> </span><span>else</span><span> </span><span>{</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; displayCoords</span><span>.</span><span>innerHTML</span><span>=</span><span>"Geolocation API not supported by your browser."</span><span>;</span></li>
<li><span>&nbsp; &nbsp; &nbsp;&nbsp;</span><span>}</span></li>
<li><span>&nbsp; &nbsp;}</span></li>
<li><span> </span></li>
<li><span> </span></li>
<li><span>&nbsp; &nbsp;function</span><span> showPosition</span><span>(</span><span>position</span><span>)</span><span> </span><span>{</span></li>
<li><span>&nbsp; &nbsp; &nbsp; displayCoords</span><span>.</span><span>innerHTML</span><span>=</span><span>"Latitude: "</span><span> </span><span>+</span><span> position</span><span>.</span><span>coords</span><span>.</span><span>latitude </span><span>+</span><span> </span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span>"&lt;br /&gt;Longitude: "</span><span> </span><span>+</span><span> position</span><span>.</span><span>coords</span><span>.</span><span>longitude</span><span>;</span><span> </span></li>
<li><span>&nbsp; &nbsp;}</span></li>
<li><span> </span></li>
<li><span>&nbsp; <span style="color: #ff0000;">&nbsp;</span></span><span style="color: #ff0000;"><strong><span>function</span></strong></span><strong><span style="color: red;"> errorPosition</span></strong><span style="color: #ff0000;"><strong><span>(</span><span>error</span><span>)</span></strong></span><span> </span><span>{</span><span> </span></li>
<li><span>&nbsp; &nbsp; &nbsp;&nbsp;</span><span>var</span><span> info </span><span>=</span><span> </span><span>"Error during geolocation: "</span><span>;</span></li>
<li><span> </span></li>
<li><span>&nbsp; &nbsp; &nbsp;&nbsp;</span><span>switch</span><span>(</span><span>error</span><span>.</span><span>code</span><span>)</span><span> </span><span>{</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span>case</span><span> error</span><span>.</span><span>TIMEOUT</span><span>:</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; info </span><span>+=</span><span> </span><span>"Timeout !"</span><span>;</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span>break</span><span>;</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span>case</span><span> error</span><span>.</span><span>PERMISSION_DENIED</span><span>:</span><span> </span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; info </span><span>+=</span><span> </span><span>"Permission denied, geolocation could not be obtained..."</span><span>;</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span>break</span><span>;</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span>case</span><span> error</span><span>.</span><span>POSITION_UNAVAILABLE</span><span>:</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; info </span><span>+=</span><span> </span><span>"Location could not be obtained though the available means..."</span><span>;</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span>break</span><span>;</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span>case</span><span> error</span><span>.</span><span>UNKNOWN_ERROR</span><span>:</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; info </span><span>+=</span><span> </span><span>"Unknown error"</span><span>;</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span>break</span><span>;</span></li>
<li><span>&nbsp; &nbsp; &nbsp;&nbsp;</span><span>}</span></li>
<li><span>&nbsp; &nbsp; &nbsp; displayCoords</span><span>.</span><span>innerHTML </span><span>=</span><span> info</span><span>;</span></li>
<li><span>&nbsp; &nbsp;&nbsp;</span><span>}</span></li>
<li><span>&lt;/script&gt;</span></li>
<li><span>&lt;/body&gt;</span></li>
<li><span>&lt;/html&gt;</span></li>
</ol></div>


### 6.4.4 Tracking a position

In order to track the current position, the geolocation API provides a method similar to the `getCurrentPosition(onSuccess, onError)` named `watchPosition(onSuccess, onError)`. 

When `getCurrentPosition` gives a position when called, `watchPosition` does the following:

+ __It gets the callback function only when the current position changes.__ If you stay in the same location, the callback function won't be called regularly.
+ It returns an `id` so that you can use the `clearWatch(id)` method to stop the current tracking.


#### Typical use

<div><ol>
<li value="1"><span>// get an id of the current tracking, the showPosition callback is like the one we saw in earlier examples.</span></li>
<li><span>var</span><span> watchPosId </span><span>=</span><span> navigator</span><span>.</span><span>geolocation</span><span>.</span><span>watchPosition</span><span>(</span><span>showPosition</span><span>);</span></li>
<li><span>...</span></li>
<li><span>// stop the tracking</span></li>
<li><span>navigator</span><span>.</span><span>geolocation</span><span>.</span><span>clearWatch</span><span>(</span><span>watchPosId</span><span>);</span></li>
</ol></div>

As a test, you may just try to change `getCurrentPosition` to `watchPosition` in the previous examples, and try this code using a mobile phone or tablet, walk for 20 meters and see the position changing.


#### Options available when using the geolocation API, in particular real time tracking

Several options are available when using HTML5 geolocation. We can pass a third parameter to the `getCurrentPosition` and `watchPosition` methods, that will hold one or several of the following options:

<table style="table-layout: auto; border: 5px solid lightGrey; color: black; font-size: 1.0em; font-family: arial,helvetica,sans-serif; width: 55vw;" cellspacing="0" cellpadding="5" border="0" align="center">
<tbody>
<tr>
<td style="padding: 5px; background-color: #007ff6; color: white; font-size: 1.2em; border: 2px solid lightGrey; text-align: center;" colspan="2">Properties of the coords object</td>
</tr>
<tr>
<td style="text-align: center; background-color: #007ff6; color: white; font-size: 1.2em; border: 2px solid lightGrey;" valign="top"><strong><span style="font-family: 'courier new', courier;">enableHighAccuracy</span></strong></td>
<td style="background-color: white; border: 2px solid lightGrey; color: black;" valign="top">A boolean (true/false) which indicates to the device that you wish to obtain its most accurate readings. in other words: use the GPS please! (However, this parameter may or may not make a difference, depending on your hardware, GPS availability, etc.)</td>
</tr>
<tr>
<td style="text-align: center; background-color: #007ff6; color: white; font-size: 1.2em; border: 2px solid lightGrey;" valign="top"><strong><span style="font-family: 'courier new', courier;">maximumAge</span></strong></td>
<td style="background-color: white; border: 2px solid lightGrey; color: black;" valign="top">The maximum amount of time (in milliseconds) the position may remain in the cache (this is appropriate as the device may cache readings to save power and/or bandwidth).</td>
</tr>
<tr>
<td style="text-align: center; background-color: #007ff6; color: white; font-size: 1.2em; border: 2px solid lightGrey;" valign="top"><strong><span style="font-family: 'courier new', courier;">timeout</span></strong></td>
<td style="background-color: white; border: 2px solid lightGrey; color: black;" valign="top">The maximum time (in milliseconds) for which you are prepared to allow the device to try to obtain a Geo location. After this timeout value has elapsed, the onError callback is called.</td>
</tr>
</tbody>
</table>


#### Example of use

Source code:

<div><ol>
<li value="1"><span>// Just ask to turn GPS on, if available</span></li>
<li><span>navigator</span><span>.</span><span>geolocation</span><span>.</span><span>getCurrentPosition</span><span>(</span><span>onSuccess</span><span>,</span><span> onError</span><span>,</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;{</span><span>enableHighAccuracy</span><span>:</span><span>true</span><span>});</span></li>
<li><span></span></li>
<li><span>// maximumAge = 10 mins, the position can be cached for 10 mins, </span></li>
<li><span>// useful when in&nbsp;</span><span>tunnels...When the device tries to get </span></li>
<li><span>// a position, if it does not&nbsp;succeed, then go on error</span></li>
<li><span>// immediately</span></li>
<li><span>navigator</span><span>.</span><span>geolocation</span><span>.</span><span>getCurrentPosition</span><span>(</span><span>onSuccess</span><span>,</span><span> onError</span><span>,</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; {</span><span>maximumAge</span><span>:</span><span>600000</span><span>,&nbsp;</span><span>timeout</span><span>:</span><span>0</span><span>});</span></li>
<li><span>// Position will never come from the cache (maximumAge: 0), and </span></li>
<li><span>// if after 0.1s the&nbsp;</span><span>position could not be computed, then go on </span></li>
<li><span>// error</span></li>
<li><span>navigator</span><span>.</span><span>geolocation</span><span>.</span><span>getCurrentPosition</span><span>(</span><span>onSuccess</span><span>,</span><span> onError</span><span>,</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;{</span><span>maximumAge</span><span>:</span><span>0</span><span>,&nbsp;</span><span>timeout</span><span>:</span><span>100</span><span>});</span></li>
<li><span>// Ask for GPS, cache for 30s, 27s before going on error...</span></li>
<li><span>watchId</span><span>=</span><span>navigator</span><span>.</span><span>geolocation</span><span>.</span><span>watchPosition</span><span>(</span><span>onSuccess</span><span>,</span><span> onError</span><span>,</span><span> </span></li>
<li><span>&nbsp; &nbsp; {</span><span>enableHighAccuracy</span><span>:</span><span>true</span><span>,</span><span> maximumAge</span><span>:</span><span>30000</span><span>,</span><span> timeout</span><span>:</span><span>27000</span><span>});</span></li>
</ol></div>

Look for the explanations in the lines of comment.


### 6.4.5 Geolocation and maps

This section presents an example of how to get an interactive map, using [the Leaflet API for OpenStreetMap](https://leafletjs.com/reference-1.6.0.html), and gives links to more resources. Did you know that you can even get an estimation of a physical address from the longitude and latitude, using online Web services?


#### How to get a map centered on your longitude and latitude

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick="window.open('https://tinyurl.com/yyptjsw2')"
    src    ="https://tinyurl.com/y4revzgq"
    alt    ="Leaflet API example 1"
    title  ="Leaflet API example 1"
  />
</figure>


This example is just given "as is", as there are so many possibilities for rendering a map with [the Leaflet API for OpenStreetMaps](https://leafletjs.com/reference-1.6.0.html). However, we think having such a basic example might be useful.

[Codepen](https://tinyurl.com/y2dt8xh3) ([Local Example - Street Map](src/6.4.5-example1.html))

Source code extract:

HTML part :

<div><ol>
<li value="1"><span>&lt;html&gt;</span></li>
<li><span>&lt;head&gt;</span></li>
<li><span>&nbsp; &lt;meta</span><span> </span><span>charset</span><span>=</span><span>"utf-8"</span><span>&gt;</span></li>
<li><span>&nbsp; &lt;title&gt;</span><span>OpenStreetMap Example</span><span>&lt;/title&gt;</span></li>
<li><span>&nbsp; &lt;link</span><span> </span><span>rel</span><span>=</span><span>"stylesheet"</span><span> </span><span>href</span><span>=</span><span>"https://unpkg.com/leaflet@1.0.3/dist/leaflet.css"</span><span>&gt;</span></li>
<li><span>&nbsp; &lt;script</span><span> </span><span>src</span><span>=</span><span>"https://unpkg.com/leaflet@1.0.3/dist/leaflet.js"</span><span>&gt;&lt;/script&gt;</span><span> </span></li>
<li><span>&lt;/head&gt;</span></li>
<li><span>&lt;body&gt;</span></li>
<li><span></span><span>&nbsp; &lt;button</span><span> </span><span>class</span><span>=</span><span>"btn"</span><span> </span><span>onclick</span><span>=</span><span>"</span><span>getLocation</span><span>(</span><span>event</span><span>)</span><span>"</span><span>&gt;</span><span>Click to show your location with OpenStreetMap</span><span>&lt;/button&gt;</span></li>
<li><span></span><span>&nbsp; &lt;div</span><span> </span><span>id</span><span>=</span><span>"map"</span><span> </span><span>class</span><span>=</span><span>"map"</span><span>&gt;&lt;/div&gt;</span><span> </span></li>
<li><span>&lt;/body&gt;</span></li>
<li><span>&lt;/html&gt;</span></li>
</ol></div>

+ _Lines 5_ and _6_ are the required files to use the Leaflet API (this is the official name of the OpenStreetMaps API),
+ _Line 10_ is the `<div>` container that will be used to display the interactive map

JavaScript part :

<div><ol>
<li value="1"><span>function</span><span> getLocation</span><span>(</span><span>e</span><span>)</span><span> </span><span>{</span><span> </span></li>
<li><span>&nbsp; e</span><span>.</span><span>preventDefault</span><span>();</span></li>
<li><span></span><span>&nbsp; if</span><span> </span><span>(!</span><span>navigator</span><span>.</span><span>geolocation</span><span>)</span><span> </span><span>{</span></li>
<li><span>&nbsp; &nbsp; alert</span><span>(</span><span>"Browser doesn't support geolocation"</span><span>);</span></li>
<li><span></span><span>&nbsp; }</span><span> </span><span>else</span><span> </span><span>{</span></li>
<li><span>&nbsp; &nbsp; navigator</span><span>.</span><span>geolocation</span><span>.</span><span>getCurrentPosition</span><span>(</span><span>success</span><span>,</span><span> error</span><span>);</span></li>
<li><span></span><span>&nbsp; }</span></li>
<li><span>}</span></li>
<li><span>&nbsp;</span></li>
<li><span>// Get current position successfully</span></li>
<li><span>function</span><span> success</span><span>(</span><span>position</span><span>)</span><span> </span><span>{</span></li>
<li><span></span><span>&nbsp; var</span><span> map</span><span>,</span><span> marker</span><span>,</span></li>
<li><span>&nbsp; latitude </span><span>=</span><span> position</span><span>.</span><span>coords</span><span>.</span><span>latitude</span><span>,</span></li>
<li><span>&nbsp; longitude </span><span>=</span><span> position</span><span>.</span><span>coords</span><span>.</span><span>longitude</span><span>;</span></li>
<li><span> </span></li>
<li><span></span><span>&nbsp; // Instance map using leaflet</span></li>
<li><span>&nbsp; map </span><span>=</span><span> L</span><span>.</span><span>map</span><span>(</span><span>'map'</span><span>).</span><span>setView</span><span>([</span><span>latitude</span><span>,</span><span> longitude</span><span>],</span><span> </span><span>13</span><span>);</span></li>
<li><span> </span></li>
<li><span></span><span>&nbsp; // Tile layer using key api at cloudmade.com</span></li>
<li><span>&nbsp; L</span><span>.</span><span>tileLayer</span><span>(</span><span>'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'</span><span>,</span><span> </span><span>{</span></li>
<li><span>&nbsp; &nbsp; key</span><span>:</span><span> </span><span>'760506895e284217a7442ce2efe97797'</span><span>,</span></li>
<li><span>&nbsp; &nbsp; styleId</span><span>:</span><span> </span><span>103288</span><span>,</span></li>
<li><span>&nbsp; &nbsp; maxZoom</span><span>:</span><span> </span><span>16</span></li>
<li><span></span><span>&nbsp; }).</span><span>addTo</span><span>(</span><span>map</span><span>);</span></li>
<li><span>&nbsp;</span></li>
<li><span></span><span>&nbsp; // Marker using leaflet</span></li>
<li><span>&nbsp; marker </span><span>=</span><span> L</span><span>.</span><span>marker</span><span>([</span><span>latitude</span><span>,</span><span> longitude</span><span>]).</span><span>addTo</span><span>(</span><span>map</span><span>);</span></li>
<li><span>&nbsp;</span></li>
<li><span></span><span>&nbsp; // Popup in leaflet</span></li>
<li><span>&nbsp; marker</span><span>.</span><span>bindPopup</span><span>(</span><span>'&lt;p&gt;Your location&lt;/p&gt;'</span><span>).</span><span>openPopup</span><span>();</span></li>
<li><span>}</span></li>
<li><span>&nbsp;</span></li>
<li><span>// Get current position fail</span></li>
<li><span>function</span><span> error</span><span>()</span><span> </span><span>{</span></li>
<li><span>&nbsp; alert</span><span>(</span><span>'Get current position fail. Please access codepen to get geolocation.'</span><span>);</span></li>
<li><span>}</span></li>
</ol></div>

+ _Line 6_ uses the [Geolocation API](https://www.w3.org/TR/geolocation-API/) to get the current position, in case of success it calls the success function, passing the location as parameter,
+ _Lines 13_ and _14_ show how to get the longitude and latitude properties from the location,
+ The rest is a basic use of the Leaflet API. Notice at line 17 that 'map' is the id of the `<div>` from the HTML part of the code.


### 6.4.6 Reverse geocoding

Different Web services can be used to get an address from longitude and latitude. Most are free of charge, but they will ask you to register an API key and enter your credit card number. If you send too many requests, you will be charged. Such a service is the [Google Reverse Geocoding JavaScript API](https://developers.google.com/maps/documentation/javascript/examples/geocoding-reverse). For those of you who are really interested to know how this API works, please read the Google documentation and tutorials.

There is also an interesting Leaflet plugin (an extension to Leaflet) based on the Gisgraphy (free open source framework) service, that comes with [a nice demo of reverse geocoding](https://services.gisgraphy.com/static/leaflet/index.html).

Let's see some examples of use.


#### Example #1: how to get a physical address from the longitude and latitude

Google reverse geocoding example (screenshot only) :

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick="window.open('https://tinyurl.com/y4co8klf')"
    src    ="https://tinyurl.com/y53acpuj"
    alt    ="Reverse geocoder example"
    title  ="Reverse geocoder example"
  />
</figure>


Source code of this example (in order to run it,  you need a Google API key, used at line 6).

<div><ol>
<li value="1"><span>&lt;!DOCTYPE html&gt;</span></li>
<li><span>&lt;html</span><span> </span><span>lang</span><span>=</span><span>"en"</span><span>&gt;</span></li>
<li><span> </span><span>&lt;head&gt;</span></li>
<li><span>&lt;meta</span><span> </span><span>charset</span><span>=</span><span>"utf-8"</span><span>&gt;</span></li>
<li><span>&lt;title&gt;Js bin </span><span>&lt;/title&gt;</span><span> </span></li>
<li><span>&nbsp; &nbsp;&nbsp;</span><span>&lt;script</span><span> </span><span>src</span><span>=</span><span>"https://maps.googleapis.com/maps/api/js?key=PUT_HERE_YOUR_API_KEY&amp;v=3.exp&amp;sensor=false"</span><span>&gt;&lt;/script&gt;</span><span> </span></li>
<li><span> </span><span>&lt;script&gt;</span></li>
<li><span> </span><span>// p elements for displaying lat / long and address</span></li>
<li><span> </span><span>var</span><span> displayCoords</span><span>,</span><span> myAddress</span><span>;</span><span> </span></li>
<li><span> </span></li>
<li><span> </span><span>// used with the google apis</span></li>
<li><span> </span><span>var</span><span> geocoder</span><span>;</span></li>
<li><span> </span><span>var</span><span> map</span><span>;</span></li>
<li><span> </span><span>var</span><span> infowindow </span><span>=</span><span> </span><span>new</span><span> google</span><span>.</span><span>maps</span><span>.</span><span>InfoWindow</span><span>();</span></li>
<li><span> </span><span>var</span><span> marker</span><span>;</span></li>
<li><span> </span></li>
<li><span> </span><span>// Called when the page is loaded</span></li>
<li><span> </span><span>function</span><span> init</span><span>()</span><span> </span><span>{</span></li>
<li><span>&nbsp; &nbsp; displayCoords</span><span>=</span><span>document</span><span>.</span><span>getElementById</span><span>(</span><span>"msg"</span><span>);</span></li>
<li><span>&nbsp; &nbsp; myAddress </span><span>=</span><span> document</span><span>.</span><span>getElementById</span><span>(</span><span>"address"</span><span>);</span></li>
<li><span> </span></li>
<li><span>&nbsp; &nbsp; geocoder </span><span>=</span><span> </span><span>new</span><span> google</span><span>.</span><span>maps</span><span>.</span><span>Geocoder</span><span>();</span></li>
<li><span> </span></li>
<li><span>&nbsp; &nbsp;&nbsp;</span><span>// In order to show something even before a user clicks on the button</span></li>
<li><span>&nbsp; &nbsp;&nbsp;</span><span>var</span><span> latlng </span><span>=</span><span> </span><span>new</span><span> google</span><span>.</span><span>maps</span><span>.</span><span>LatLng</span><span>(</span><span>34.0144</span><span>,</span><span> </span><span>-</span><span>6.83</span><span>);</span></li>
<li><span> </span></li>
<li><span>&nbsp; &nbsp;&nbsp;</span><span>var</span><span> mapOptions </span><span>=</span><span> </span><span>{</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp;zoom</span><span>:</span><span> </span><span>8</span><span>,</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp;center</span><span>:</span><span> latlng</span><span>,</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp;mapTypeId</span><span>:</span><span> </span><span>'roadmap'</span></li>
<li><span>&nbsp; &nbsp; </span><span>}</span></li>
<li><span>&nbsp; &nbsp; map </span><span>=</span><span> </span><span>new</span><span> google</span><span>.</span><span>maps</span><span>.</span><span>Map</span><span>(</span><span>document</span><span>.</span><span>getElementById</span><span>(</span><span>'map_canvas'</span><span>),</span><span> mapOptions</span><span>);</span><span> </span></li>
<li><span> </span><span>} // end of init()</span></li>
<li><span> </span></li>
<li><span> </span><span>// Called when the button is clicked</span></li>
<li><span> </span><span>function</span><span> getLocation</span><span>()</span><span> </span><span>{</span></li>
<li><span>&nbsp; &nbsp;&nbsp;</span><span>if</span><span> </span><span>(</span><span>navigator</span><span>.</span><span>geolocation</span><span>)</span><span> </span><span>{</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp;navigator</span><span>.</span><span>geolocation</span><span>.</span><span>getCurrentPosition</span><span>(</span><span>showPosition</span><span>);</span></li>
<li><span>&nbsp; &nbsp;&nbsp;</span><span>}</span><span> </span><span>else</span><span> </span><span>{</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp;displayCoords</span><span>.</span><span>innerHTML</span><span>=</span><span>"Geolocation API not supported by your browser."</span><span>;</span></li>
<li><span>&nbsp; &nbsp;&nbsp;</span><span>}</span></li>
<li><span> </span><span>}</span></li>
<li><span> </span></li>
<li><span> </span><span>// Called when a position is available</span></li>
<li><span> </span><span>function</span><span> showPosition</span><span>(</span><span>position</span><span>)</span><span> </span><span>{</span></li>
<li><span>&nbsp; &nbsp; displayCoords</span><span>.</span><span>innerHTML</span><span>=</span><span>"Latitude: "</span><span> </span><span>+</span><span> position</span><span>.</span><span>coords</span><span>.</span><span>latitude </span><span>+</span><span> </span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; </span><span>"&lt;br /&gt;Longitude: "</span><span> </span><span>+</span><span> position</span><span>.</span><span>coords</span><span>.</span><span>longitude</span><span>;</span><span> </span></li>
<li><span> </span></li>
<li><span>&nbsp; &nbsp;&nbsp;</span><span>// Display the map</span></li>
<li><span>&nbsp; &nbsp; showOnGoogleMap</span><span>(</span><span>new</span><span> google</span><span>.</span><span>maps</span><span>.</span><span>LatLng</span><span>(</span><span>position</span><span>.</span><span>coords</span><span>.</span><span>latitude</span><span>,</span><span>&nbsp; &nbsp; &nbsp; &nbsp;</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;position</span><span>.</span><span>coords</span><span>.</span><span>longitude</span><span>));</span></li>
<li><span>&nbsp;</span><span>}</span></li>
<li><span>&nbsp;</span><span>function</span><span> showOnGoogleMap</span><span>(</span><span>latlng</span><span>)</span><span> </span><span>{</span></li>
<li><span>&nbsp; &nbsp;</span><span>// Ask google geocoder for an address once we get a longitude and </span></li>
<li><span>&nbsp; &nbsp;</span><span>// a latitude. In fact, the reverse geocoder sends back an array of "guesses"</span></li>
<li><span>&nbsp; &nbsp;</span><span>// i.e. not just one address object, but several. Each entry in this array</span></li>
<li><span>&nbsp; &nbsp;</span><span>// has several properties such as street, city, etc. We use the "formatted_address"</span></li>
<li><span>&nbsp; &nbsp;</span><span>// one here, but it might be interesting to get the detailed properties in other</span></li>
<li><span>&nbsp; &nbsp;</span><span>// applications like a form with street, city, zip code etc.</span></li>
<li><span>&nbsp; &nbsp;geocoder</span><span>.</span><span>geocode</span><span>({</span><span>'latLng'</span><span>:</span><span> latlng</span><span>},</span><span>reverseGeocoderSuccess</span><span>);</span></li>
<li><span> </span></li>
<li><span>&nbsp; &nbsp;</span><span>function</span><span> reverseGeocoderSuccess</span><span>(</span><span>results</span><span>,</span><span> status</span><span>)</span><span> </span><span>{</span></li>
<li><span>&nbsp; &nbsp; &nbsp;</span><span>if</span><span> </span><span>(</span><span>status </span><span>==</span><span> google</span><span>.</span><span>maps</span><span>.</span><span>GeocoderStatus</span><span>.</span><span>OK</span><span>)</span><span> </span><span>{</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span>if</span><span> </span><span>(</span><span>results</span><span>[</span><span>1</span><span>])</span><span> </span><span>{</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;map</span><span>.</span><span>setZoom</span><span>(</span><span>11</span><span>);</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;marker </span><span>=</span><span> </span><span>new</span><span> google</span><span>.</span><span>maps</span><span>.</span><span>Marker</span><span>({</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; position</span><span>:</span><span> latlng</span><span>,</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; map</span><span>:</span><span> map</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span>});</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;infowindow</span><span>.</span><span>setContent</span><span>(</span><span>results</span><span>[</span><span>1</span><span>].</span><span>formatted_address</span><span>);</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;infowindow</span><span>.</span><span>open</span><span>(</span><span>map</span><span>,</span><span> marker</span><span>);</span></li>
<li><span> </span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span>// Display address as text in the page</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;myAddress</span><span>.</span><span>innerHTML</span><span>=</span><span>"Adress: "</span><span> </span><span>+</span><span> results</span><span>[</span><span>0</span><span>].</span><span>formatted_address</span><span>;</span>&nbsp;</li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span>}</span><span> </span><span>else</span><span> </span><span>{</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;alert</span><span>(</span><span>'No surface address&nbsp;found'</span><span>);</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span>}</span></li>
<li><span>&nbsp; &nbsp; &nbsp;&nbsp;</span><span>}</span><span> </span><span>else</span><span> </span><span>{</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;alert</span><span>(</span><span>'Geocoder failed due to: '</span><span> </span><span>+</span><span> status</span><span>);</span></li>
<li><span>&nbsp; &nbsp; &nbsp;&nbsp;</span><span>}</span></li>
<li><span>&nbsp; &nbsp;&nbsp;</span><span>}</span><span> </span><span>// end of reverseGeocoderSuccess</span></li>
<li><span> </span><span>}</span><span> </span><span>// end of showOnGoogleMap</span></li>
<li><span> </span><span>&lt;/script&gt;</span></li>
<li><span> </span><span>&lt;/head&gt;</span></li>
<li><span> </span><span>&lt;body</span><span> </span><span>onload</span><span>=</span><span>"</span><span>init</span><span>()</span><span>"</span><span>&gt;</span></li>
<li><span> </span><span>&lt;title&gt;</span><span>HTML5 + Geolocalisation + Google Maps API Reverse Geocoding</span><span>&lt;/title&gt;</span></li>
<li><span> </span></li>
<li><span> </span><span>&lt;p</span><span> </span><span>id</span><span>=</span><span>"msg"</span><span>&gt;</span><span>Click the button to get your coordinates:</span><span>&lt;/p&gt;</span></li>
<li><span> </span><span>&lt;p</span><span> </span><span>id</span><span>=</span><span>"address"</span><span>&gt;&lt;/p&gt;</span></li>
<li><span> </span></li>
<li><span> </span><span>&lt;button</span><span> </span><span>onclick</span><span>=</span><span>"</span><span>getLocation</span><span>()</span><span>"</span><span>&gt;</span><span>Where am I ?</span><span>&lt;/button&gt;</span></li>
<li><span> </span><span>&lt;div</span><span> </span><span>id</span><span>=</span><span>"map_canvas"</span><span> </span><span>style</span><span>=</span><span>"</span><span>width</span><span>:</span><span> </span><span>500px</span><span>;</span><span> height</span><span>:</span><span> </span><span>300px</span><span>"</span><span>&gt;&lt;/div&gt;</span></li>
<li><span> </span><span>&lt;/body&gt;</span></li>
<li><span>&lt;/html&gt;</span></li>
</ol></div>

Gisgraphy (free service) reverse geocoding example (screenshot only, click on it to see [the demo on the Gisgraphy website](https://services.gisgraphy.com/static/leaflet/index.html)):

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
    onclick="window.open('https://tinyurl.com/y4co8klf')"
    src    ="https://tinyurl.com/y52x2yr3"
    alt    ="Gisgraphy leaflet plugin (reverse geocoding)"
    title  ="Gisgraphy leaflet plugin (reverse geocoding)"
  />
</figure>


#### Example #2: reverse geocoding + OpenStreetMap

Important note: these examples below rely on an external [GitHub resource](https://github.com/perliedman/leaflet-control-geocoder). No related questions are asked in this module's exercise or final exam.

Please, pan and zoom on the map and click. The longitude and latitude are computed from your click and a free reverse geocoding service is used to convert to a physical address.

[Remote Example - Codepen](https://tinyurl.com/y26kgvys) ([Local Example - Reverse Geocoding](src/6.4.6-exmapl2.html))


#### Example #3: shows the address on the map, from your current longitude and latitude

Click on the Codepen logo on the top right to open [the example in Codepen](https://codepen.io/w3devcampus/pen/KKVXaRJ). Due to security reasons, it cannot run embedded in this page. ([Local Example - Longtitude & Latitude to Address](src/6.4.6-exmapl3.html))


#### Example #4: use of geolocation, map and reverse geocoder in a HTML form

This is just a variation of the previous examples. We embedded the interactive map in a form, and we display the results of the reverse geocoder in a form field. This example might be useful if you want to pre-fill the address of a registration form, depending on the current location of the person who is registering.

Click on the Codepen logo (on the top right) so to run the [online example](https://codepen.io/w3devcampus/pen/MWKEJqM) (for security reasons the embedded version cannot run in this page). ([Local Example - Geolocation, Map & Reverse Geocoder](src/6.4.6-exmapl4.html))



### 6.4.7 Discussion and projects

Here is the discussion forum for this part of the course. Please either post your comments/observations/questions or share your creations.


#### Suggested topics

+ What features of a Web application do you think could benefit from geolocation?
+ Do you know that you can simulate a position using the dev. tools of some browsers? Try exploring the dev. tools of Google Chrome. Also, there are browser extensions and applications that can help develop interactive maps. Please look for some of them and share your findings in the forum.

  <figure style="margin: 0.5em; text-align: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
      onclick="window.open('https://tinyurl.com/y4n5n22d')"
      src    ="https://tinyurl.com/yyty8o72"
      alt    ="devtool console geolocation simulation"
      title  ="devtool console geolocation simulation"
    />
  </figure>

+ Can you recommend good tutorials about Google Map and about OpenStreetMap, the two main free services that propose maps on the fly?


#### Optional projects

Here are a few project ideas. Your classmates and the team who prepared the course will be glad to try them and offer feedback. Please post URLs in this discussion forum. These projects are optional, meaning that they won't be graded.

+ __Project 1 (easy):__ Add a map showing your location to one of your Web pages. Start with a simple, static map, then try with an interactive map. Reuse the examples from the course.
+ __Project 2 (a bit harder):__ The examples provided in the course used OpenStreetMap, but why don't you try to do the same with GoogleMaps? Some services are free of charge, but will ask you to get an API key (see [this YouTube tutorial](https://www.youtube.com/watch?v=C3znRXBMYZo) about how to get such a key).




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
    + [Geolocation](https://tinyurl.com/zeyhput6): containing methods to retrieve the user's current position, watch for changes in their position, and clear a previousdly-set watch
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;head&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag"> &lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag"> &lt;title&gt;</span><span class="pln">OpenStreetMap Example</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag"> &lt;link</span><span class="pln"> </span><span class="atn">rel</span><span class="pun">=</span><span class="atv">"stylesheet"</span><span class="pln"> </span><span class="atn">href</span><span class="pun">=</span><span class="atv">"https://unpkg.com/leaflet@1.0.3/dist/leaflet.css"</span><span class="tag">&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag"> &lt;script</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://unpkg.com/leaflet@1.0.3/dist/leaflet.js"</span><span class="tag">&gt;&lt;/script&gt;</span><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;/head&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&lt;body&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag"> &lt;button</span><span class="pln"> </span><span class="atn">class</span><span class="pun">=</span><span class="atv">"btn"</span><span class="pln"> </span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">getLocation</span><span class="pun">(</span><span class="pln">event</span><span class="pun">)</span><span class="atv">"</span><span class="tag">&gt;</span><span class="pln">Click to show your location with OpenStreetMap</span><span class="tag">&lt;/button&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag"> &lt;div</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"map"</span><span class="pln"> </span><span class="atn">class</span><span class="pun">=</span><span class="atv">"map"</span><span class="tag">&gt;&lt;/div&gt;</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>

+ _Lines 5 and 6_ are the required files to use the Leaflet API (this is the official name of the OpenStreetMaps API),
+ _Line 10_ is the `<div>` container that will be used to display the interactive map

JavaScript part:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> getLocation</span><span class="pun">(</span><span class="pln">e</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> e</span><span class="pun">.</span><span class="pln">preventDefault</span><span class="pun">();</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd"> if</span><span class="pln"> </span><span class="pun">(!</span><span class="pln">navigator</span><span class="pun">.</span><span class="pln">geolocation</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> alert</span><span class="pun">(</span><span class="str">"Browser doesn't support geolocation"</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun"> }</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> navigator</span><span class="pun">.</span><span class="pln">geolocation</span><span class="pun">.</span><span class="pln">getCurrentPosition</span><span class="pun">(</span><span class="pln">success</span><span class="pun">,</span><span class="pln"> error</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun"> }</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="com">// Get current position successfully</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> success</span><span class="pun">(</span><span class="pln">position</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd"> var</span><span class="pln"> map</span><span class="pun">,</span><span class="pln"> marker</span><span class="pun">,</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> latitude </span><span class="pun">=</span><span class="pln"> position</span><span class="pun">.</span><span class="pln">coords</span><span class="pun">.</span><span class="pln">latitude</span><span class="pun">,</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> longitude </span><span class="pun">=</span><span class="pln"> position</span><span class="pun">.</span><span class="pln">coords</span><span class="pun">.</span><span class="pln">longitude</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="com"> // Instance map using leaflet</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> map </span><span class="pun">=</span><span class="pln"> L</span><span class="pun">.</span><span class="pln">map</span><span class="pun">(</span><span class="str">'map'</span><span class="pun">).</span><span class="pln">setView</span><span class="pun">([</span><span class="pln">latitude</span><span class="pun">,</span><span class="pln"> longitude</span><span class="pun">],</span><span class="pln"> </span><span class="lit">13</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="com"> // Tile layer using key api at cloudmade.com</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> L</span><span class="pun">.</span><span class="pln">tileLayer</span><span class="pun">(</span><span class="str">'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'</span><span class="pun">,</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> key</span><span class="pun">:</span><span class="pln"> </span><span class="str">'760506895e284217a7442ce2efe97797'</span><span class="pun">,</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> styleId</span><span class="pun">:</span><span class="pln"> </span><span class="lit">103288</span><span class="pun">,</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> maxZoom</span><span class="pun">:</span><span class="pln"> </span><span class="lit">16</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun"> }).</span><span class="pln">addTo</span><span class="pun">(</span><span class="pln">map</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="com"> // Marker using leaflet</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> marker </span><span class="pun">=</span><span class="pln"> L</span><span class="pun">.</span><span class="pln">marker</span><span class="pun">([</span><span class="pln">latitude</span><span class="pun">,</span><span class="pln"> longitude</span><span class="pun">]).</span><span class="pln">addTo</span><span class="pun">(</span><span class="pln">map</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="com"> // Popup in leaflet</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> marker</span><span class="pun">.</span><span class="pln">bindPopup</span><span class="pun">(</span><span class="str">'&lt;p&gt;Your location&lt;/p&gt;'</span><span class="pun">).</span><span class="pln">openPopup</span><span class="pun">();</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="com">// Get current position fail</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> error</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> alert</span><span class="pun">(</span><span class="str">'Get current position fail. Please access codepen to get geolocation.'</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

+ _Line 6_ uses the [Geolocation API](https://www.w3.org/TR/geolocation-API/) to get the current position, in case of success it calls the success function, passing the location as parameter,
+ _Lines 13 and 14_ show how to get the longitude and latitude properties from the location,
+ The rest is a basic use of the Leaflet API. Notice at _line 17_ that 'map' is the id of the `<div>` from the HTML part of the code.


#### Notes for 3.4.2 Geolocation and maps

+ The Leaflet API for OpenStreetMap
  + [Leaflet API reference](https://leafletjs.com/)
  + example: [centering location on map](src/03d-example01.html)
    + button to trigger map: `<button class="btn" onclick="getLocation(event)">Click to show your location with OpenStreetMap</button>`
    + container for map: `<div id="map" class="map"></div>`
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

Different Web services can be used to get an address from longitude and latitude. Most are free of charge, but they will ask you to register an API key and enter your credit card number. If you send too many requests, you will be charged.Such a service is the [Google Reverse Geocoding JavaScript API](https://tinyurl.com/pb44te35). For those of you who are really interested to know how this API works, please read the Google documentation and tutorials.

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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;head&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;title&gt;Js bin </span><span class="tag">&lt;/title&gt;</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;script</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://maps.googleapis.com/maps/api/js?key=PUT_HERE_YOUR_API_KEY&amp;v=3.exp&amp;sensor=false"</span><span class="tag">&gt;&lt;/script&gt;</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;script&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// p elements for displaying lat / long and address</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> displayCoords</span><span class="pun">,</span><span class="pln"> myAddress</span><span class="pun">;</span><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// used with the google apis</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> geocoder</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> map</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> infowindow </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> google</span><span class="pun">.</span><span class="pln">maps</span><span class="pun">.</span><span class="typ">InfoWindow</span><span class="pun">();</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> marker</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// Called when the page is loaded</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> init</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> displayCoords</span><span class="pun">=</span><span class="pln">document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">"msg"</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> myAddress </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">"address"</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> geocoder </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> google</span><span class="pun">.</span><span class="pln">maps</span><span class="pun">.</span><span class="typ">Geocoder</span><span class="pun">();</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// In order to show something even before a user clicks on the button</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> latlng </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> google</span><span class="pun">.</span><span class="pln">maps</span><span class="pun">.</span><span class="typ">LatLng</span><span class="pun">(</span><span class="lit">34.0144</span><span class="pun">,</span><span class="pln"> </span><span class="pun">-</span><span class="lit">6.83</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> mapOptions </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> zoom</span><span class="pun">:</span><span class="pln"> </span><span class="lit">8</span><span class="pun">,</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> center</span><span class="pun">:</span><span class="pln"> latlng</span><span class="pun">,</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> mapTypeId</span><span class="pun">:</span><span class="pln"> </span><span class="str">'roadmap'</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> map </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> google</span><span class="pun">.</span><span class="pln">maps</span><span class="pun">.</span><span class="typ">Map</span><span class="pun">(</span><span class="pln">document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'map_canvas'</span><span class="pun">),</span><span class="pln"> mapOptions</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">} // end of init()</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// Called when the button is clicked</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> getLocation</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">navigator</span><span class="pun">.</span><span class="pln">geolocation</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> navigator</span><span class="pun">.</span><span class="pln">geolocation</span><span class="pun">.</span><span class="pln">getCurrentPosition</span><span class="pun">(</span><span class="pln">showPosition</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> displayCoords</span><span class="pun">.</span><span class="pln">innerHTML</span><span class="pun">=</span><span class="str">"Geolocation API not supported by your browser."</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// Called when a position is available</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> showPosition</span><span class="pun">(</span><span class="pln">position</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> displayCoords</span><span class="pun">.</span><span class="pln">innerHTML</span><span class="pun">=</span><span class="str">"Latitude: "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> position</span><span class="pun">.</span><span class="pln">coords</span><span class="pun">.</span><span class="pln">latitude </span><span class="pun">+</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="str">"&lt;br /&gt;Longitude: "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> position</span><span class="pun">.</span><span class="pln">coords</span><span class="pun">.</span><span class="pln">longitude</span><span class="pun">;</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// Display the map</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> showOnGoogleMap</span><span class="pun">(</span><span class="kwd">new</span><span class="pln"> google</span><span class="pun">.</span><span class="pln">maps</span><span class="pun">.</span><span class="typ">LatLng</span><span class="pun">(</span><span class="pln">position</span><span class="pun">.</span><span class="pln">coords</span><span class="pun">.</span><span class="pln">latitude</span><span class="pun">,</span><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> position</span><span class="pun">.</span><span class="pln">coords</span><span class="pun">.</span><span class="pln">longitude</span><span class="pun">));</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> showOnGoogleMap</span><span class="pun">(</span><span class="pln">latlng</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// Ask google geocoder for an address once we get a longitude and </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// a latitude. In fact, the reverse geocoder sends back an array of "guesses"</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// i.e. not just one address object, but several. Each entry in this array</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// has several properties such as street, city, etc. We use the "formatted_address"</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// one here, but it might be interesting to get the detailed properties in other</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// applications like a form with street, city, zip code etc.</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> geocoder</span><span class="pun">.</span><span class="pln">geocode</span><span class="pun">({</span><span class="str">'latLng'</span><span class="pun">:</span><span class="pln"> latlng</span><span class="pun">},</span><span class="pln">reverseGeocoderSuccess</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> reverseGeocoderSuccess</span><span class="pun">(</span><span class="pln">results</span><span class="pun">,</span><span class="pln"> status</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">status </span><span class="pun">==</span><span class="pln"> google</span><span class="pun">.</span><span class="pln">maps</span><span class="pun">.</span><span class="typ">GeocoderStatus</span><span class="pun">.</span><span class="pln">OK</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">results</span><span class="pun">[</span><span class="lit">1</span><span class="pun">])</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> map</span><span class="pun">.</span><span class="pln">setZoom</span><span class="pun">(</span><span class="lit">11</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> marker </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> google</span><span class="pun">.</span><span class="pln">maps</span><span class="pun">.</span><span class="typ">Marker</span><span class="pun">({</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> position</span><span class="pun">:</span><span class="pln"> latlng</span><span class="pun">,</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> map</span><span class="pun">:</span><span class="pln"> map</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">});</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> infowindow</span><span class="pun">.</span><span class="pln">setContent</span><span class="pun">(</span><span class="pln">results</span><span class="pun">[</span><span class="lit">1</span><span class="pun">].</span><span class="pln">formatted_address</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> infowindow</span><span class="pun">.</span><span class="pln">open</span><span class="pun">(</span><span class="pln">map</span><span class="pun">,</span><span class="pln"> marker</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// Display address as text in the page</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> myAddress</span><span class="pun">.</span><span class="pln">innerHTML</span><span class="pun">=</span><span class="str">"Adress: "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> results</span><span class="pun">[</span><span class="lit">0</span><span class="pun">].</span><span class="pln">formatted_address</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> alert</span><span class="pun">(</span><span class="str">'No surface address found'</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> alert</span><span class="pun">(</span><span class="str">'Geocoder failed due to: '</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> status</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span><span class="pln"> </span><span class="com">// end of reverseGeocoderSuccess</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span><span class="pln"> </span><span class="com">// end of showOnGoogleMap</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/script&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/head&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;body</span><span class="pln"> </span><span class="atn">onload</span><span class="pun">=</span><span class="atv">"</span><span class="pln">init</span><span class="pun">()</span><span class="atv">"</span><span class="tag">&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;title&gt;</span><span class="pln">HTML5 + Geolocalisation + Google Maps API Reverse Geocoding</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;p</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"msg"</span><span class="tag">&gt;</span><span class="pln">Click the button to get your coordinates:</span><span class="tag">&lt;/p&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;p</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"address"</span><span class="tag">&gt;&lt;/p&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">getLocation</span><span class="pun">()</span><span class="atv">"</span><span class="tag">&gt;</span><span class="pln">Where am I ?</span><span class="tag">&lt;/button&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;div</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"map_canvas"</span><span class="pln"> </span><span class="atn">style</span><span class="pun">=</span><span class="atv">"</span><span class="pln">width</span><span class="pun">:</span><span class="pln"> </span><span class="lit">500px</span><span class="pun">;</span><span class="pln"> height</span><span class="pun">:</span><span class="pln"> </span><span class="lit">300px</span><span class="atv">"</span><span class="tag">&gt;&lt;/div&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/body&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
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









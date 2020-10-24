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
    + checks if the Web browser supports the `geolocation` API by testing the variable `navigator.geolocation`:
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

    + position objects w/ a `coords` property: the longitude and  the latitude

      ```js
      function showPosition(position) {
        displayCoords.innerHTML="Latitude: " + position.coords.latitude +
                               "<br />Longitude: " + position.coords.longitude;
      }
      ```

  + [Geolocation API Specification](https://www.w3.org/TR/geolocation-API/)
  + [Geolocation API - WDN](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API)

+ [coords object properties](#642-the-coords-object-properties)
  + __latitude:__ The latitude of the position
  + __longitude:__ The longitude of the position
  + __altitude:__ The altitude of the position
  + __accuracy:__ The accuracy of the measure of the longitude and latitude (in meters)
  + __altitudeAccuracy:__ The accuracy of the measure of the altitude (in meters)
  + __heading:__ gives the orientation relative to north, in degrees
  + __speed:__ current speed in meters/second

+ [Geolocation error codes](#643-geolocation-error-codes)
  + `navigator.geolocation.getCurrentPosition` method possible to pass a second parameter in case of errror
  + example:
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
  + __enableHighAccuracy:__ A boolean (true/false) which indicates to the device that you wish to obtain its most accurate readings. in other words: use the GPS please! (However, this parameter may or may not make a difference, depending on your hardware, GPS availability, etc.)
  + __maximumAge:__ The maximum amount of time (in milliseconds) the position may remain in the cache (this is appropriate as the device may cache readings to save power and/or bandwidth).
  + __timeout:__ The maximum time (in milliseconds) for which you are prepared to allow the device to try to obtain a Geo location. After this timeout value has elapsed, the onError callback is called.

+ [Example: tracking position](#example-of-use)
  + ask to turn GPS on, if available: `navigator.geolocation.getCurrentPosition(onSuccess, onError, {enableHighAccuracy:true});`
  + the position can be cached for 10 mins useful when in tunnels: `maximumAge = 10 mins`
  + when the device tries to get a position, if it does not succeed, then go on error immediately: `navigator.geolocation.getCurrentPosition(onSuccess, onError, {maximumAge:600000, timeout:0});`
  + position will never come from the cache (maximumAge: 0), and if after 0.1s the position could not be computed, then go on error: `navigator.geolocation.getCurrentPosition(onSuccess, onError, {maximumAge:0, timeout:100});`
  + ask for GPS, cache for 30s, 27s before going on error: `watchId=navigator.geolocation.watchPosition(onSuccess, onError, {enableHighAccuracy:true, maximumAge:30000, timeout:27000});`






### 6.4.1 Introduction


#### Introduction

This chapter presents the new Geolocation API and illustrates its use with several examples.

The Geolocation HTML5 JavaScript API is implemented by most modern Web browsers, and uses different means to get the current location: GPS, GSM/3G triangulation, Wifi, IP address, etc.

It is possible to prompt the user to activate the GPS (this is what most GPS navigation software does on mobile phones), or ask for a particular mean among those available. It is also possible to track the current position when it changes. This is useful for writing a navigation application or for tracking in real time the position of different participants in the case of an application that involves several persons at the same time (using WebSockets, for example).

[Browser support for the Geolocation API](https://caniuse.com/#feat=geolocation) is excellent, both on mobile and on desktop devices.


#### Typical use

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><strong><span class="pln">navigator</span><span class="pun">.</span><span class="pln">geolocation</span><span class="pun">.</span><span class="pln">getCurrentPosition</span><span class="pun">(</span><span class="pln">showPosition</span><span class="pun">,</span><span class="pln"> onError</span><span class="pun">);</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> showPosition</span><span class="pun">(</span><span class="pln">position</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"latitude is: "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> position</span><span class="pun">.</span><span class="pln">coords</span><span class="pun">.</span><span class="pln">latitude</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"longitude is: "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> position</span><span class="pun">.</span><span class="pln">coords</span><span class="pun">.</span><span class="pln">longitude</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> onError</span><span class="pun">(</span><span class="pln">err</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"Could not get the position"</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

[This online example at JSBin](https://jsbin.com/toyeley/1/edit?html,output) shows how to get the current longitude and latitude and display them in an HTML page. Try it below in your browser: ([Local Example - Location](src/6.4.1-example1.html))

<div class="exampleHTML">
<p id="msg">Click the button to get your coordinates:</p>
<p><button onclick="getLocation2()">Where am I ?</button></p>
</div>

Note that the first time you execute this example, for privacy reasons, the browser will ask if you agree to share your position with the application.

Source code of this typical example:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;head&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&lt;title&gt;</span><span class="pln">Basic example of use of the geolocation API</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/head&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;body&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;p</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"msg"</span><span class="tag">&gt;</span><span class="pln">Click the button to get your coordinates:</span><span class="tag">&lt;/p&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">getLocation</span><span class="pun">()</span><span class="atv">"</span><span class="tag">&gt;</span><span class="pln">Where am I ?</span><span class="tag">&lt;/button&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="tag">&lt;script&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="kwd">&nbsp; &nbsp; var</span><span class="pln"> displayCoords</span><span class="pun">=</span><span class="pln">document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">"msg"</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">&nbsp; &nbsp; function</span><span class="pln"> getLocation</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">navigator</span><span class="pun">.</span><span class="pln">geolocation</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <strong>navigator</strong></span><strong><span class="pun">.</span><span class="pln">geolocation</span><span class="pun">.</span><span class="pln">getCurrentPosition</span><span class="pun">(</span><span class="pln">showPosition</span><span class="pun">);</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; displayCoords</span><span class="pun">.</span><span class="pln">innerHTML</span><span class="pun">=</span><span class="str">"Geolocation API not supported by your browser."</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp;}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="kwd">&nbsp; <strong>&nbsp;function</strong></span><strong><span class="pln"> showPosition</span><span class="pun">(</span><span class="pln">position</span><span class="pun">)</span></strong><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;displayCoords</span><span class="pun">.</span><span class="pln">innerHTML</span><span class="pun">=</span><span class="str">"Latitude: "</span><span class="pln"> </span><span class="pun">+</span><strong><span class="pln"> position</span><span class="pun">.</span><span class="pln">coords</span><span class="pun">.</span><span class="pln">latitude </span></strong><span class="pun">+</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="str">"&lt;br /&gt;Longitude: "</span><span class="pln"> </span><span class="pun">+</span><strong><span class="pln"> position</span><span class="pun">.</span><span class="pln">coords</span><span class="pun">.</span><span class="pln">longitude</span></strong><span class="pun">;</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp;}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;/script&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;head&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&lt;title&gt;</span><span class="pln">Basic example of use of the geolocation API</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/head&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;body&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;p</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"msg"</span><span class="tag">&gt;</span><span class="pln">Click the button to get your coordinates:</span><span class="tag">&lt;/p&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">getLocation</span><span class="pun">()</span><span class="atv">"</span><span class="tag">&gt;</span><span class="pln">Where am I ?</span><span class="tag">&lt;/button&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="tag">&lt;script&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="kwd">&nbsp; &nbsp;var</span><span class="pln"> displayCoords</span><span class="pun">=</span><span class="pln">document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">"msg"</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">&nbsp; &nbsp;function</span><span class="pln"> getLocation</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">navigator</span><span class="pun">.</span><span class="pln">geolocation</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<strong>navigator</strong></span><strong><span class="pun">.</span><span class="pln">geolocation</span><span class="pun">.</span><span class="pln">getCurrentPosition</span><span class="pun">(</span><span class="pln">showPosition</span><span class="pun">,</span><span class="pln" style="color: #ff0000;"> errorPosition</span><span class="pun">);</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; </span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; displayCoords</span><span class="pun">.</span><span class="pln">innerHTML</span><span class="pun">=</span><span class="str">"Geolocation API not supported by your browser."</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp;}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">&nbsp; &nbsp;function</span><span class="pln"> showPosition</span><span class="pun">(</span><span class="pln">position</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; displayCoords</span><span class="pun">.</span><span class="pln">innerHTML</span><span class="pun">=</span><span class="str">"Latitude: "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> position</span><span class="pun">.</span><span class="pln">coords</span><span class="pun">.</span><span class="pln">latitude </span><span class="pun">+</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="str">"&lt;br /&gt;Longitude: "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> position</span><span class="pun">.</span><span class="pln">coords</span><span class="pun">.</span><span class="pln">longitude</span><span class="pun">;</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp;}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; <span style="color: #ff0000;">&nbsp;</span></span><span style="color: #ff0000;"><strong><span class="kwd">function</span></strong></span><strong><span class="pln" style="color: red;"> errorPosition</span></strong><span style="color: #ff0000;"><strong><span class="pun">(</span><span class="pln">error</span><span class="pun">)</span></strong></span><span class="pln"> </span><span class="pun">{</span><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> info </span><span class="pun">=</span><span class="pln"> </span><span class="str">"Error during geolocation: "</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">switch</span><span class="pun">(</span><span class="pln">error</span><span class="pun">.</span><span class="pln">code</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">case</span><span class="pln"> error</span><span class="pun">.</span><span class="pln">TIMEOUT</span><span class="pun">:</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; info </span><span class="pun">+=</span><span class="pln"> </span><span class="str">"Timeout !"</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">break</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">case</span><span class="pln"> error</span><span class="pun">.</span><span class="pln">PERMISSION_DENIED</span><span class="pun">:</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; info </span><span class="pun">+=</span><span class="pln"> </span><span class="str">"Permission denied, geolocation could not be obtained..."</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">break</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">case</span><span class="pln"> error</span><span class="pun">.</span><span class="pln">POSITION_UNAVAILABLE</span><span class="pun">:</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; info </span><span class="pun">+=</span><span class="pln"> </span><span class="str">"Location could not be obtained though the available means..."</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">break</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">case</span><span class="pln"> error</span><span class="pun">.</span><span class="pln">UNKNOWN_ERROR</span><span class="pun">:</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; info </span><span class="pun">+=</span><span class="pln"> </span><span class="str">"Unknown error"</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">break</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; displayCoords</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> info</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;/script&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>


### 6.4.4 Tracking a position

In order to track the current position, the geolocation API provides a method similar to the `getCurrentPosition(onSuccess, onError)` named `watchPosition(onSuccess, onError)`. 

When `getCurrentPosition` gives a position when called, `watchPosition` does the following:

+ __It gets the callback function only when the current position changes.__ If you stay in the same location, the callback function won't be called regularly.
+ It returns an `id` so that you can use the `clearWatch(id)` method to stop the current tracking.


#### Typical use

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com">// get an id of the current tracking, the showPosition callback is like the one we saw in earlier examples.</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> watchPosId </span><span class="pun">=</span><span class="pln"> navigator</span><span class="pun">.</span><span class="pln">geolocation</span><span class="pun">.</span><span class="pln">watchPosition</span><span class="pun">(</span><span class="pln">showPosition</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">...</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="com">// stop the tracking</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">navigator</span><span class="pun">.</span><span class="pln">geolocation</span><span class="pun">.</span><span class="pln">clearWatch</span><span class="pun">(</span><span class="pln">watchPosId</span><span class="pun">);</span></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com">// Just ask to turn GPS on, if available</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">navigator</span><span class="pun">.</span><span class="pln">geolocation</span><span class="pun">.</span><span class="pln">getCurrentPosition</span><span class="pun">(</span><span class="pln">onSuccess</span><span class="pun">,</span><span class="pln"> onError</span><span class="pun">,</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;{</span><span class="pln">enableHighAccuracy</span><span class="pun">:</span><span class="kwd">true</span><span class="pun">});</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="com"></span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="com">// maximumAge = 10 mins, the position can be cached for 10 mins, </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="com">// useful when in&nbsp;</span><span class="com">tunnels...When the device tries to get </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="com">// a position, if it does not&nbsp;succeed, then go on error</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="com">// immediately</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">navigator</span><span class="pun">.</span><span class="pln">geolocation</span><span class="pun">.</span><span class="pln">getCurrentPosition</span><span class="pun">(</span><span class="pln">onSuccess</span><span class="pun">,</span><span class="pln"> onError</span><span class="pun">,</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; {</span><span class="pln">maximumAge</span><span class="pun">:</span><span class="lit">600000</span><span class="pun">,&nbsp;</span><span class="pln">timeout</span><span class="pun">:</span><span class="lit">0</span><span class="pun">});</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="com">// Position will never come from the cache (maximumAge: 0), and </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="com">// if after 0.1s the&nbsp;</span><span class="com">position could not be computed, then go on </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="com">// error</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">navigator</span><span class="pun">.</span><span class="pln">geolocation</span><span class="pun">.</span><span class="pln">getCurrentPosition</span><span class="pun">(</span><span class="pln">onSuccess</span><span class="pun">,</span><span class="pln"> onError</span><span class="pun">,</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;{</span><span class="pln">maximumAge</span><span class="pun">:</span><span class="lit">0</span><span class="pun">,&nbsp;</span><span class="pln">timeout</span><span class="pun">:</span><span class="lit">100</span><span class="pun">});</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="com">// Ask for GPS, cache for 30s, 27s before going on error...</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">watchId</span><span class="pun">=</span><span class="pln">navigator</span><span class="pun">.</span><span class="pln">geolocation</span><span class="pun">.</span><span class="pln">watchPosition</span><span class="pun">(</span><span class="pln">onSuccess</span><span class="pun">,</span><span class="pln"> onError</span><span class="pun">,</span><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; {</span><span class="pln">enableHighAccuracy</span><span class="pun">:</span><span class="kwd">true</span><span class="pun">,</span><span class="pln"> maximumAge</span><span class="pun">:</span><span class="lit">30000</span><span class="pun">,</span><span class="pln"> timeout</span><span class="pun">:</span><span class="lit">27000</span><span class="pun">});</span></li>
</ol></div>

Look for the explanations in the lines of comment.







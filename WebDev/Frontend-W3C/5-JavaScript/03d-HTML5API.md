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





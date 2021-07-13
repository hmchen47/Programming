# Module 3: HTML5 file upload and download section


## 3.7 Conclusion on client-side persistence

The two W3Cx courses, [HTML5 Coding Essentials and Best Practices](https://www.edx.org/course/html5-coding-essentials-and-best-practices) and this one (HTML5 Apps and Games), have covered a lot of material, and you may have trouble identifying which of the different techniques you have learned best suit your needs.

To sum up:

+ __If you need to work with transactions__ (in the database sense: protect data against concurrent access, etc.), or do some searches on a large amount of data, if you need indexes, etc., then use IndexedDB
+ __If you need a way to store simple strings or JSON objects, then use localStorage/sessionStorage.__ Example: store HTML form content as you type, store a game's hi-scores, preferences of an application, etc.
+ __If you need to manipulate files (read or download/upload), then use the File API and XHR2.__
+ If you need to manipulate a file system, there is a FileSystem and a FileWriter API which are very poorly supported and will certainly be replaced in HTML 5.1. We decided not to discuss these in the course because they lack agreement within the community and browser vendors.
If you need an SQL database client-side: No! Forget this idea, please! There was once a WebSQL API, but it disappeared rapidly.
Note that the above points may be used in any combination: you may have a Web app that uses localStorage and IndexedDB to cache its resources so that it can run in offline mode.

### External resources

+ You might be interested by [the Cache API](https://developers.google.com/web/fundamentals/instant-and-offline/web-storage/cache-api) to make your application data available offline (in other terms: making your Web page or your Web app. available offline). 
+ Read also [this article](https://web.dev/storage-for-the-web/) that covers all different options for storing data in the browser and gives another look at what has been presented in this chapter of the course.






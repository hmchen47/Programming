# HTML - Multimedia


## Image and Multimedia

+ [Image and multimedia](https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Image_and_multimedia)

  + HTML supports various multimedia resources such as images, audio, and video.

  <table style="font-family: arial,helvetica,sans-serif; margin: auto; width: 55vw" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
  <thead>
    <tr style="border-bottom: double black;">
    <th style="background-color: #3d64ff; color: #ffffff; width: 5%">Element</th>
    <th style="background-color: #3d64ff; color: #ffffff; width: 50%">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
    <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/area" title="The HTML <area> element defines a hot-spot region on an image, and optionally associates it with a hypertext link. This element is used only within a <map> element."><code>&lt;area&gt;</code></a></td>
    <td>The <strong>HTML <code>&lt;area&gt;</code> element</strong> defines a hot-spot region on an image, and optionally associates it with a <a class="glossaryLink" href="/en-US/docs/Glossary/Hyperlink" title="hypertext link: Hyperlinks connect webpages or data items to one another. In HTML, <a> elements define hyperlinks from a spot on a webpage (like a text string or image) to another spot on some other webpage (or even on the same page).">hypertext link</a>. This element is used only within a <a href="/en-US/docs/Web/HTML/Element/map" title="The HTML <map> element is used with <area> elements to define an image map (a clickable link area)."><code>&lt;map&gt;</code></a> element.</td>
    </tr>
    <tr>
    <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/audio" title="The HTML <audio> element is used to embed sound content in documents. It may contain one or more audio sources, represented using the src attribute or the <source> element:&nbsp;the browser will choose the most suitable one. It can also be the destination for streamed media, using a MediaStream."><code>&lt;audio&gt;</code></a></td>
    <td>The <strong>HTML <code>&lt;audio&gt;</code> element</strong> is used to embed sound content in documents. It may contain one or more audio sources, represented using the <code>src</code> attribute or the <a href="/en-US/docs/Web/HTML/Element/source" title="The HTML <source> element specifies multiple media resources for the <picture>, the <audio> element, or the <video> element."><code>&lt;source&gt;</code></a> element:&nbsp;the browser will choose the most suitable one. It can also be the destination for streamed media, using a <a href="/en-US/docs/Web/API/MediaStream" title="The MediaStream interface represents a stream of media content. A stream consists of several tracks such as&nbsp;video or audio tracks. Each track is specified as an instance of MediaStreamTrack."><code>MediaStream</code></a>.</td>
    </tr>
    <tr>
    <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/img" title="The HTML <img> element embeds an image into the document. It is a replaced element."><code>&lt;img&gt;</code></a></td>
    <td>The <strong>HTML <code>&lt;img&gt;</code> element</strong> embeds an image into the document. It is a <a href="/en-US/docs/Web/CSS/Replaced_element">replaced element</a>.</td>
    </tr>
    <tr>
    <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/map" title="The HTML <map> element is used with <area> elements to define an image map (a clickable link area)."><code>&lt;map&gt;</code></a></td>
    <td>The <strong>HTML <code>&lt;map&gt;</code> element</strong> is used with <a href="/en-US/docs/Web/HTML/Element/area" title="The HTML <area> element defines a hot-spot region on an image, and optionally associates it with a hypertext link. This element is used only within a <map> element."><code>&lt;area&gt;</code></a> elements to define an image map (a clickable link area).</td>
    </tr>
    <tr>
    <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/track" title="The HTML <track> element is used as a child of the media elements <audio> and <video>. It lets you specify timed text tracks (or time-based data), for example to automatically handle subtitles. The tracks are formatted in WebVTT format (.vtt files) — Web Video Text Tracks or&nbsp;Timed Text Markup Language (TTML)."><code>&lt;track&gt;</code></a></td>
    <td>The <strong>HTML <code>&lt;track&gt;</code> element</strong> is used as a child of the media elements <a href="/en-US/docs/Web/HTML/Element/audio" title="The HTML <audio> element is used to embed sound content in documents. It may contain one or more audio sources, represented using the src attribute or the <source> element:&nbsp;the browser will choose the most suitable one. It can also be the destination for streamed media, using a MediaStream."><code>&lt;audio&gt;</code></a> and <a href="/en-US/docs/Web/HTML/Element/video" title="The HTML Video element (<video>) embeds a media player which supports video playback into the document."><code>&lt;video&gt;</code></a>. It lets you specify timed text tracks (or time-based data), for example to automatically handle subtitles. The tracks are formatted in <a href="/en-US/docs/Web/API/Web_Video_Text_Tracks_Format">WebVTT format</a> (<code>.vtt</code> files) — Web Video Text Tracks or&nbsp;<a class="external external-icon" href="https://w3c.github.io/ttml2/index.html" rel="noopener">Timed Text Markup Language (TTML).</a></td>
    </tr>
    <tr>
    <td style="vertical-align: top;"><a href="/en-US/docs/Web/HTML/Element/video" title="The HTML Video element (<video>) embeds a media player which supports video playback into the document."><code>&lt;video&gt;</code></a></td>
    <td>The <strong>HTML Video element</strong> (<strong><code>&lt;video&gt;</code></strong>) embeds a media player which supports video playback into the document.</td>
    </tr>
  </tbody>
  </table>



## Image Element

### Characteristics of Image Element

+ [Concerns when using the `src` attribute](../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#image-src-attribute):
  + no space in image path.
  + image path matches the capitalization of the actual path
  + use Unix (/) path name separator instead of Windows () style
  + ensure the image resides in the right location or the user is going to get a broken link
  + relative path best practice: always keep the images at the same level, or one level down
  + absolute paths: not recommended

+ [alt attribute](../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#attribute-alt)
  + provide a short description of what the image is about
  + convey information about the image or its function in the page
  + important attribute:
    + the text alternative to the image for users who are unable to see the image, instead using assistive technology like screen readers that rely on the alt text
    + screen readers will typically announce that there is an image and read out the contents of the alt attribute
    + alternate text displayed if image not displayed if
      + the path in your source attribute is wrong
      + slow internet connection
      + image relocated or renamed
    + Search engines rely on the alt attribute to find out what the image is about.
    + tell mobile users what the image is about if images turn off

+ [reasons using images](../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#purpose-of-the-image):
  + represent a concept, illustration or just a photograph that provide information
  + background for a button or link
  + display a quote or message in the form of text in an image
  + decorative images

+ Images used for decoration or presentation purposes should have an empty value for alt. `<img alt="">`

+ The alt attribute is meant to be an alternate source of information while the title attribute should provide additional information about the image.

+ The ['ismap' & 'usemap'](../WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#the-ismap-and-usemap-attributes) attributes
  + the picture is an image with clickable areas
  + e.g., a world map where different countries on the map can be clicked and navigates to another page like the country's wikipedia page
  + 'ismap' attribute
    + a boolean attribute
    + create an image with the image source file and indicate a server-side image-map
    + if click on a part of your image, navigate to the link indicated
    + require to create a map file with these details and then add the location of this map file using the anchor element
    + the href attribute points to the location of the map file
    + used within the anchor element
  + 'usemap' attribute
    + like ismap but more widely used
    + client-side image-maps
    + NOT of type boolean but the name of the map with a '#' character preceding it
    + use the `<area>` element as a child of `<map>` element to specify the coordinates and the page it should navigate to
    + `<map>`: define a client-side image map
    + `<area>`:
      + define the areas clicked and naviated page
      + shape of the area, coordinates of the area, and URL of the pag to redirect
      + 'shape' attribute values: circle, rect, poly, and default
      + [MND Specification](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/area)
  + cgi file:
    + target areas within the image in terms of coordinates
    + clicks on a part of the image, then calculate the exact 'x' and 'y' coordinates of the image that was clicked
    + the browser will consult with the map file on the server (specified in the anchor tag) after clicking, by sending these mouse click coordinates to the server
    + based on the coordination, return the target web page
  + client-side image-maps vs. Client-side image-maps
    + Server-side image-maps:
      + use separate map files that have to be downloade
      + depend on the server for translating the request
      + depend on the server for translating the request
    + Client-side image-maps
      + reside within an HTML document
      + the browser takes care of the translation (translating mouse coordinates clicked to corresponding Web pages)



### List of Attributes for Image Element

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=100%>
  <caption style="font-size: 1.5em;"><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#the-img-tag">Attributes of &lt;img&gt; tag</a></caption>
<thead>
  <tr>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="10%">Attribute</td>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="40%">Description</td>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="30%">Usage</td>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="10%">Link</td>
  </tr>
  <tr>
    <td>src</td>
    <td>
      <p><span style="font-family: arial,helvetica,sans-serif;">Where to fetch the image from (must have)</span></p>
      <p><span style="font-family: arial,helvetica,sans-serif;">Values:</span></p>
      <ul>
        <li><span style="font-family: arial,helvetica,sans-serif;">Path to an image file within your Web site</span></li>
        <li><span style="font-family: arial,helvetica,sans-serif;">Path to an image file that resides elsewhere on the Web</span></li>
      </ul>
    </td>
    <td>
      <p><span style="font-family: arial,helvetica,sans-serif;">&lt;img <span style="color: $ff6000; font-eright: bold;">src</span>="example.png" alt="Example Tutorial Image"&gt;</span></p>
    </td>
    <td>
      <p><a href="../WebDev/Frontend-W3C/1.HTML5CSS/02.Attributes.md#image-src-attribute">Source18</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#the-img-tag">src19</a></p>
    </td>
  </tr>
</thead>
<tbody>
  <tr>
    <td>alt</td>
    <td>
      <p><span style="font-family: arial,helvetica,sans-serif;">Provide a short description of what the image is about (must have)<br/>offer meaning to the image and suggests the purpose of the image content</span></p>
    </td>
    <td><span style="font-family: arial,helvetica,sans-serif;">&lt;img src="image/example.png" <span style="color: $ff6000; font-eright: bold;">alt</span>="Add a short text description of the image here"&gt;</span></td>
    <td>
      <p><a href="../WebDev/Frontend-W3C/1.HTML5CSS/02.Attributes.md#the-alt-attribute">Alt Text</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#attribute-alt">alt</a></p>
    </td>
  </tr>
  <tr>
    <td>title</td>
    <td>
      <p><span style="font-family: arial,helvetica,sans-serif;">A global attribute to provide the title of the image</span></p>
    </td>
    <td><span style="font-family: arial,helvetica,sans-serif;">&lt;img src="image/example.png" alt="Add a short text description of the image here" <span style="color: $ff6000; font-eright: bold;">title</span>="Add a title of the image"&gt;</span></td>
    <td>
      <p><a href="../WebDev/Frontend-W3C/1.HTML5CSS/02.Attributes.md#the-title-attribute">Ttitle</a>, <a href="../WebDev/Frontend-W3C/1.HTML5CSS/02.Attributes.md#global-attribute-title-">Global Ttitle</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#the-title-attribute">title</a></p>
    </td>
  </tr>
  <tr>
    <td>height <br/><br/> width</td>
    <td>
      <p><span style="font-family: arial,helvetica,sans-serif;">Resize the image in pixels without using an external editor</span></p>
    </td>
    <td><span style="font-family: arial,helvetica,sans-serif;">&lt;img src="image/example.png" alt="Add a short text description of the image here" <span style="color: $ff6000; font-eright: bold;">height</span>="hhh"&gt;</span><br/><br/><span style="font-family: arial,helvetica,sans-serif;">&lt;img src="image/example.png" alt="Add a short text description of the image here" <span style="color: $ff6000; font-eright: bold;">width</span>="www"&gt;</span><br/><br/><span style="font-family: arial,helvetica,sans-serif;">&lt;img src="image/example.png" alt="Add a short text description of the image here" <span style="color: $ff6000; font-eright: bold;">width</span>="www" <span style="color: $ff6000; font-eright: bold;">height</span>="hhh"&gt;</span></td>
    <td>
      <p><a href="../WebDev/Frontend-W3C/1.HTML5CSS/02.Attributes.md#the-height-width-attributes">Size</a>, <a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/02-Attributes.md#the-height-width-attributes">width&height</a></p>
    </td>
  </tr>
  <tr>
    <td>ismap</td>
    <td>
      <p><span style="font-family: arial,helvetica,sans-serif;">Specifies an image as a server-side image-map</span></p>
    </td>
    <td><span style="font-family: arial,helvetica,sans-serif;">&lt;img src="images/logo.png" alt="ismap tutorial" <span style="color: $ff6000; font-eright: bold;">ismap</span>&gt;</span></td>
    <td>
      <p><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#the-ismap-attribute">ismap</a>, <a href="https://www.w3schools.com/tags/att_img_ismap.asp">W3S</a></p>
    </td>
  </tr>
  <tr>
    <td>usemap</td>
    <td>
      <p><span style="font-family: arial,helvetica,sans-serif;">Specifies an image as a client-side image-map</span></p>
    </td>
    <td><span style="font-family: arial,helvetica,sans-serif;">&lt;img src="navigator.jpg" alt="Pages in this Web site" <span style="color: $ff6000; font-eright: bold;">usemap</span>="#navigatormap"&gt;</span></td>
    <td>
      <p><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#the-usemap-attribute">usemap</a>, <a href="https://www.w3schools.com/tags/att_img_usemap.asp">W3S</a></p>
    </td>
  </tr>
</tbody>
</table>


### Attributes of the 'map' tag

<table style="font-family: arial,helvetica,sans-serif; margin: auto;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=90%>
  <caption style="font-size: 1.5em;"><a href="https://www.w3schools.com/tags/tag_map.asp">Attributes of &lt;map&gt; tag</a></caption>
  <tbody><tr>
    <th style="background-color: #3d64ff; color: #ffffff; width:10%;">Attribute</th>
    <th style="background-color: #3d64ff; color: #ffffff; width:20%;">Value</th>
    <th style="background-color: #3d64ff; color: #ffffff; width:60%;">Description</th>
  </tr>
  <tr>
    <td><a href="https://www.w3schools.com/att_map_name.asp">name</a></td>
    <td><i>mapname</i></td>
    <td>Required. Specifies the name of an image-map</td>
  </tr>
</tbody></table>


### Attributes of the 'area' tag

<table style="font-family: arial,helvetica,sans-serif; margin: auto;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=90%>
  <caption style="font-size: 1.5em;"><a href="https://www.w3schools.com/tags/tag_area.asp">Attributes of &lt;area&gt; tag</a></caption>
  <thead><tr>
    <th style="background-color: #3d64ff; color: #ffffff; width:10%;">Attribute</th>
    <th style="background-color: #3d64ff; color: #ffffff; width:20%;">Value</th>
    <th style="background-color: #3d64ff; color: #ffffff; width:60%;">Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td><a href="att_area_alt.asp">alt</a></td>
    <td><i>text</i></td>
    <td>Specifies an alternate text for the area. Required if the href attribute is present</td>
  </tr>
  <tr>
    <td><a href="att_area_coords.asp">coords</a></td>
    <td><i>coordinates</i></td>
    <td>Specifies the coordinates of the area</td>
  </tr>
  <tr>
    <td><a href="att_area_download.asp">download</a></td>
    <td><i>filename</i></td>
    <td>Specifies that the target will be downloaded when a user clicks on the hyperlink</td>
  </tr>
  <tr>
    <td><a href="att_area_href.asp">href</a></td>
    <td><i>URL</i></td>
    <td>Specifies the hyperlink target for the area</td>
  </tr>
  <tr>
    <td><a href="att_area_hreflang.asp">hreflang</a></td>
    <td><i>language_code</i></td>
    <td>Specifies the language of the target URL</td>
  </tr>
  <tr>
    <td><a href="att_area_media.asp">media</a></td>
    <td><i>media query</i></td>
    <td>Specifies what media/device the target URL is optimized for</td>
  </tr>
  <tr>
    <td><a href="att_area_nohref.asp" class="notsupported">nohref</a></td>
    <td><i>value</i></td>
    <td><span class="deprecated">Not supported in HTML5.</span><br>Specifies that an area has no associated link</td>
  </tr>
  <tr>
    <td><a href="att_area_rel.asp">rel</a></td>
    <td>alternate, author, bookmark<br>help, license, next<br>nofollow, noreferrer, prefetch<br>prev, search, tag</td>
    <td>Specifies the relationship between the current document and the target URL</td>
      </tr>
  <tr>
    <td><a href="att_area_shape.asp">shape</a></td>
    <td>default, rect<br>circle, poly</td>
    <td>Specifies the shape of the area</td>
  </tr>
  <tr>
    <td><a href="att_area_target.asp">target</a></td>
    <td>_blank, _parent<br>_self, _top<br>
 <em>framename</em></td>
    <td>Specifies where to open the target URL</td>
  </tr>
  <tr>
    <td><a href="att_area_type.asp">type</a></td>
    <td><i>media_type</i></td>
    <td>Specifies the media type of the target URL</td>
    </tr>
</tbody></table>


## Audio Element

### Characteristics of Audio Elements

+ [&lt;audio&gt; tag](../WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#audio-tag)
  + embed audio in web page
  + Any text within the &lt;audio&gt; tags will be displayed if the browser does not support the audio element. 
  + should add such a message to provide better user experience

+ [File format](../WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#audio-file-formats)
  + using common audio file formats for browser compatibility
  + Browser Compatibility [lists](https://developer.mozilla.org/en-US/docs/Web/HTML/Supported_media_formats)
  + types of audio formats
    + uncompressed (eg: WAV)
    + lossless compressed (eg: MPEG-4, WMA Lossless)
    + lossy compressed (eg: Opus, MPC, AAC, WMA Lossy)
  + parts of audio format
    + Ogg:
      + a digital container format
      + a specification that describes how different elements of data and metadata work in an audio file
      + no information on how the data is compressed
    + Opus
      + a lossy audio coding format
      + the encoding or decoding mechanism for that stream of audio

+ [&lt;source&gt; element](../WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#source-element-for-multiple-source-files)
  + the same purpose as the src attribute in an audio element
  + used to specify source files for the audio and video elements
  + able to specify multiple source files
  + trying try the source files in sequence if the browser not supported the previous format file



### Attributes of the audio Tag

<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
  <caption style="font-size: 1.5em;"><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#audio-tag">Attributes of &lt;audio&gt; tag</a></caption>
<thead>
  <tr>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="15%">Attribute</td>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="40%">Description</td>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="30%">Usage</td>
  </tr>
  <tr>
    <td>src</td>
    <td>
      <p><span style="font-family: arial,helvetica,sans-serif;">Used to specify the URL of the audio file to embed.</span></p>
      <p><span style="font-family: arial,helvetica,sans-serif;">Values:</span></p>
      <ul>
        <li><span style="font-family: arial,helvetica,sans-serif;">absolute URL (file residing somewhere on the Web)</span></li>
        <li><span style="font-family: arial,helvetica,sans-serif;">relative URL (within your Web site)</span></li>
      </ul>
    </td>
    <td>
      <p><span style="font-family: arial,helvetica,sans-serif;">&lt;audio src="sounds/flute.mp3"&gt;&lt;/audio&gt;</span></p>
    </td>
  </tr>
</thead>
<tbody>
  <tr>
    <td>controls</td>
    <td>
      <p><span style="font-family: arial,helvetica,sans-serif;">Boolean attribute when specified provides controls for the user like play, pause, seek bar and volume</span></p>
      <p><img alt="Controls from HTML5 audio" src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/327f2b7346ed0f5b804d41e3d49dd8ea/asset-v1:W3Cx+HTML5.0x+2T2018+type@asset+block/audio-controls.PNG" type="saveimage" target="[object Object]" isimmediatepropagationstopped="function t(){return!1}" ispropagationstopped="function t(){return!1}" isdefaultprevented="function t(){return!1}" stopimmediatepropagation="function (){r.isImmediatePropagationStopped=n}" stoppropagation="function (){r.isPropagationStopped=n}" preventdefault="function (){r.isDefaultPrevented=n}" width="263" height="26"></p>
    </td>
    <td><span style="font-family: arial,helvetica,sans-serif;">&lt;audio src="sounds/flute.mp3" controls&gt;&lt;/audio&gt;</span></td>
  </tr>
  <tr>
    <td>loop</td>
    <td>
      <p><span style="font-family: arial,helvetica,sans-serif;">Boolean attribute when specified loops media content</span></p>
    </td>
    <td><span style="font-family: arial,helvetica,sans-serif;">&lt;audio src="sounds/flute.mp3" controls loop&gt;&lt;/audio&gt;</span></td>
  </tr>
  <tr>
    <td>muted</td>
    <td>
      <p><span style="font-family: arial,helvetica,sans-serif;">Boolean attribute when specified mutes media when playback begins</span></p>
    </td>
    <td><span style="font-family: arial,helvetica,sans-serif;">&lt;audio src="sounds/flute.mp3" controls muted&gt;&lt;/audio&gt;</span></td>
  </tr>
  <tr>
<td>preload</td>
<td>
<p><span style="font-family: arial,helvetica,sans-serif;">Allows author to communicate to the browser which settings will work best - audio should not be preloaded (none), only audio metadata is fetched (metadata), audio file can be downloaded when page loads (auto)</span><br><span style="font-family: arial,helvetica,sans-serif;">values: none, metadata, auto</span></p>
</td>
<td><span style="font-family: arial,helvetica,sans-serif;">&lt;audio src="sounds/flute.mp3" controls preload="auto"&gt;&lt;/audio&gt;</span></td>
</tr>
<tr>
<td>autoplay</td>
<td>
<p><span style="font-family: arial,helvetica,sans-serif;">Boolean attribute when specified will automatically begin playing the source file as soon as it can without waiting for the entire audio file to finish downloading</span></p>
<p></p>
</td>
<td><span style="font-family: arial,helvetica,sans-serif;">&lt;audio src="sounds/flute.mp3" controls autoplay&gt;&lt;/audio&gt;</span><audio autoplay="autoplay"></audio></td>
</tr>
</tbody>
</table>


### Attributes of the source Tag


<table style="font-family: arial,helvetica,sans-serif;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
  <caption style="font-size: 1.5em;"><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#audio-tag">Attributes of &lt;table&gt; tag</a></caption>
<tbody>
  <tr>
    <th style="text-align: left; background-color: #3d64ff; color: #ffffff;" width="15%">Attribute</td>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="40%">Description</td>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="30%">Usage</td>
  </tr>
  <tr>
    <td>src</td>
    <td><span style="font-family: arial,helvetica,sans-serif;">Specifies the URL of the media file</span></td>
    <td><span style="font-family: arial,helvetica,sans-serif;">&lt;source src="sounds/flute.mp3"&gt;</span></td>
  </tr>
  <tr>
    <td>type</td>
    <td>
      <p><span style="font-family: arial,helvetica,sans-serif;">Specifies the internet media type, also known as the MIME type for the audio resource. A media type is an identifier for file formats and format contents transmitted over the internet like text and audio files.</span></p>
      <p><span style="font-family: arial,helvetica,sans-serif;">It consists of a type and a sub-type. Eg: "audio/mpeg" - <strong>audio</strong> is the type and <strong>mpeg</strong> is the subtype. It can also take optional parameters that can be specified after a semicolon - "audio/ogg; codecs=opus" means the audio is in the ogg format and uses the opus codec. If the browser supports the Ogg format but not the Opus codec, the audio file will not load.</span></p>
      <p><span style="font-family: arial,helvetica,sans-serif;">If the type attribute is not specified, the media type is retrieved from the server.</span></p>
    </td>
    <td><span style="font-family: arial,helvetica,sans-serif;">&lt;source src="sounds/flute.mp3" type="audio/mpeg"&gt;</span></td>
  </tr>
</tbody>
</table>


## Video Element

### Characteristics of the video elements

+ The [&lt;video&gt;](../WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#video-element) tag
  + embed video in web page
  + specify the location of your video file using the src attribute or source element (for multiple source files)
  + Any text within the &lt;video&gt; tags will be displayed if the browser does not support the video element.

+ The ['poster'](../WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#poster-attribute) attribute in &lt;video&gt; tag
  + used to specify what picture shown before the video starts playing
  + by default, simply the first frame of the video
  + used to specify a different image, including a particular frame of the video or a real movie poster

+ [File formats](../WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#video-file-formats)
  + use common video file formats for browser compatibility ensuring the highest probability that your video file will pla
  + Browser Compatibility [lists](https://developer.mozilla.org/en-US/docs/Web/HTML/Supported_media_formats)
  + types of video formats
    + uncompressed
    + lossless compressed: [list](https://en.wikipedia.org/wiki/List_of_codecs#Lossless_video_compression)
    + lossy compressed: [list](https://en.wikipedia.org/wiki/List_of_codecs#Lossy_compression_2)
      + select a range of compression rates
      + the bigger the loss in quality and smaller the file size
  + Most videos go through some form of compression to reduce redundancy in video files.
  + three parts of H.264 and MP3 in MP4
    + H.264: a video compression standard
    + MP3: an audio coding format that uses lossy compression for sound in the video
    + MP4: a digital container format, similar to Ogg in audio format; storing audio and video data rather than code the information

+ [source tag](../WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#source-element-for-multiple-source-files)
  + used to specify multiple source files for the video element
  + self-closing element
  + trying video files in sequence if the browser doesn't support the previous file format
  
+ [Track tag](../WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#track-element-for-captions-and-subtitles)
  + used to add timed text like subtitles, captions or any text you would like to display to the user when the video is playing
  + types of timed text
    + Web Video Text Tracks (WebVTT) files: 
      + the standard to include subtitles or captions
      + [creation and format](https://w3c.github.io/webvtt/)
  + [Caption vs Subtitle](https://www.alsintl.com/blog/subtitles-captions-difference/)
    + Captions
      + for the deaf or people who have difficulty hearing
      + including sound effects and other significant audio like music and lyrics and is usually in the same language as the audio
    + Subtitles: translate the language (for those who do not understand the language being spoken in the video)
  + able to add multiple &lt;track&gt; tags in video element to add multiple subtitle/caption tracks
  + self-closing elemnt


### Attributes of the video Tag

<table style="font-family: arial,helvetica,sans-serif; max-width: 100%;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
  <caption style="font-size: 1.5em;"><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#video-element">Content Attributes of &lt;video&gt; tag</a></caption>
  <thead>
  <tr>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="15%">Attribute</td>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;"  width="40%">Description</td>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;" width="35%">Usage</td>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td>src</td>
    <td>specifies the URL or location of the media file</td>
    <td width="40%">&lt;video&nbsp;src="multimedia/running.mp4"&gt;&lt;/video&gt;</td>
  </tr>
  <tr>
    <td>autoplay</td>
    <td>Boolean attribute when specified will automatically begin playing source file as soon as it can without waiting for the entire video&nbsp;file to finish downloading. Note: Some versions of chrome support autostart instead of autoplay</td>
    <td width="40%">
      <p>&lt;video&nbsp;src="multimedia/running.mp4"&nbsp;autoplay&gt;&lt;/video&gt;</p>
    </td>
  </tr>
  <tr>
    <td>controls</td>
    <td>
      <p>Boolean attribute when specified provides controls for the user like play, pause, seek bar and volume</p>
      <p><img alt="Image of HTML5 video controls" src="https://prod-edxapp.edx-cdn.org/assets/courseware/v1/b30f1164c96da183a2c339b152ebe472/asset-v1:W3Cx+HTML5.0x+2T2018+type@asset+block/video-controls.PNG" type="saveimage" target="[object Object]" isimmediatepropagationstopped="function t(){return!1}" ispropagationstopped="function t(){return!1}" isdefaultprevented="function t(){return!1}" stopimmediatepropagation="function (){r.isImmediatePropagationStopped=n}" stoppropagation="function (){r.isPropagationStopped=n}" preventdefault="function (){r.isDefaultPrevented=n}" width="232" height="26"></p>
    </td>
    <td>
      <p>&lt;video&nbsp;src="multimedia/running.mp4"&nbsp;controls&gt;&lt;/video&gt;</p>
    </td>
  </tr>
  <tr>
    <td>loop</td>
    <td>Boolean attribute when specified loops media content</td>
    <td>
      <p>&lt;video&nbsp;src="multimedia/running.mp4"&nbsp;controls&nbsp;loop&gt;&lt;/video&gt;</p>
    </td>
  </tr>
  <tr>
    <td>muted</td>
    <td>Boolean attribute when specified mutes media when playback begins</td>
    <td>
      <p>&lt;video&nbsp;src="multimedia/running.mp4"&nbsp;controls&nbsp;muted&gt;&lt;/video&gt;</p>
    </td>
  </tr>
  <tr>
    <td>preload</td>
    <td>Allows author to communicate to the browser which settings will work best - video&nbsp;should not be preloaded (none), only video&nbsp;metadata is fetched (metadata), video&nbsp;file can be downloaded (auto)<br>values: none, metadata, auto</td>
    <td>
      <p>&lt;video&gt; src="multimedia/running.mp4"&nbsp;controls&nbsp;preload="auto"&gt;&lt;/video&gt;</p>
    </td>
  </tr>
  <tr>
    <td>poster</td>
    <td>Specifies the URL of the frame you want to display as&nbsp;the video cover until the user starts or seeks the video. By default, the first frame is considered the poster frame. &nbsp;The poster can also be an arbitrary image, not necessarily in any frame of the video.</td>
    <td>
      <p>&lt;video&nbsp;src="multimedia/running.mp4"&nbsp;poster="/images/video-screenshot.png" controls&gt;</p>
    </td>
  </tr>
  <tr>
    <td>height, width</td>
    <td>height and width of the video's play area in pixels. Always set height and width for a video so the browser can allocate the specified space for it when it loads the page.&nbsp;</td>
    <td>
      <p>&lt;video&nbsp;src="multimedia/running.mp4"&nbsp;controls&nbsp;width="320" height="240"&gt;&lt;/video&gt;</p>
    </td>
  </tr>
</tbody>
</table>


### Attributes of the source Element

<table style="font-family: arial,helvetica,sans-serif; max-width: 100%;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center">
  <caption style="font-size: 1.5em;"><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#source-element-for-multiple-source-files-1">Attributes of &lt;source&gt; tag</a></caption>
  <thead>
  <tr>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; min-width: 5em;">Attribute</td>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff;">Description</td>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; min-width: 13em;">Usage</td>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td>src</td>
    <td>Specifies the URL or location of the media file</td>
    <td>&lt;source src="multimedia/small.mp4"&gt;&lt;/source&gt;</td>
  </tr>
  <tr>
    <td>type</td>
    <td>
      <p>Specifies the internet media type, also known as the MIME type for the audio/video resource. A media type is an identifier for file formats and format contents transmitted over the internet like text and audio files.</p>
      <p>It consists of a type and a sub-type. Eg: "video/mp4" - <b>video</b>&nbsp;is the type and <strong>mp4</strong>&nbsp;is the subtype. It can also take optional parameters that can be specified after a semicolon - "video/mp4; codecs="avc1.42E01E, mp4a.40.2"" means the video&nbsp;is in the mp4 format and uses the codecs -&nbsp;avc1.42E01E, mp4a.40.2. If the browser supports the mp4&nbsp;format but none of the&nbsp;avc1.42E01E, mp4a.40.2&nbsp;codecs, the video file will not load.</p>
      <p>If the type attribute is not specified, the media type is retrieved from the server.</p>
    </td>
    <td>&lt;source src="multimedia/small.mp4" type="video/mp4"&gt;&lt;/source&gt;</td>
  </tr>
</tbody>
</table>


### Attributes of the track Element


<table style="font-family: arial,helvetica,sans-serif; margin: auto;" table-layout="auto" cellspacing="0" cellpadding="5" border="1" align="center" width=100%>
  <caption style="font-size: 1.5em;"><a href="https://www.w3schools.com/tags/tag_track.asp">Attributes of &lt;track&gt; tag</a></caption>
  <tbody><tr>
    <th style="background-color: #3d64ff; color: #ffffff; width:10%;">Attribute</th>
    <th style="background-color: #3d64ff; color: #ffffff; width:20%;">Value</th>
    <th style="background-color: #3d64ff; color: #ffffff; width:60%;">Description</th>
  </tr>
    <tr>
    <td><a href="https://www.w3schools.com/tags/att_track_default.asp">default</a></td>
    <td>default</td>
    <td>
      <p>Specifies that the track is to be enabled if the user's preferences do not indicate that another track would be more appropriate</p>
      <p>It is a boolean attribute. If you have multiple tracks for the same video file, you can specify which one is the default using this attribute. It can be used on one track element in a video. If you only have one track element, default should still be added to deliver the video with captions turned on in most browsers.</p>
      <p><a href="../WebDev/Frontend-W3C/1-HTML5CSSFund/05-MoreHTMLCSS.md#track-element-for-captions-and-subtitles">Usage</a><br/>
      &lt;video src="multimedia/small.mp4" controls&gt; <br/>
      &nbsp; &lt;track src="captions/small-en.vtt" label="english" default&gt;<br/>
      &nbsp; &lt;track src="captions/small-fr.vtt" label="French"&gt;<br/>
      &lt;/video&gt;</p>
    </td>
  </tr>
  <tr>
    <td><a href="https://www.w3schools.com/tags/att_track_kind.asp">kind</a></td>
    <td>captions<br>chapters<br>descriptions<br>metadata<br>subtitles</td>
    <td>Specifies the kind of text track</td>
  </tr>
  <tr>
    <td><a href="https://www.w3schools.com/tags/att_track_label.asp">label</a></td>
    <td><em>text</em></td>
    <td>Specifies the title of the text track</td>
  </tr>
  <tr>
    <td><a href="https://www.w3schools.com/tags/att_track_src.asp">src</a></td>
    <td><em>URL</em></td>
    <td>Required. Specifies the URL of the track file</td>
  </tr>
  <tr>
    <td><a href="https://www.w3schools.com/tags/att_track_srclang.asp">srclang</a></td>
    <td><i>language_code</i></td>
    <td>Specifies the language of the track text data (required if kind="subtitles")</td>
  </tr>
</tbody></table>



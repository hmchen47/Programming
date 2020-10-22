# Week 6: HTML5 Basic APIs


## 6.3 The File API





### 6.3.1 Introduction

The objective of this chapter is to provide an overview of the File API.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y2xpgmdq')"
    src    ="https://tinyurl.com/y6k8n294"
    alt    ="sound sample editor serverless"
    title  ="sound sample editor serverless"
  />
</figure>


Before HTML5, file management was limited to multipart forms and to Ajax for sending/requesting files to/from a remote Web server.

Possible actions were limited, both for the developer and the user. However, HTML5 now comes with an API called "File"  that holds features for accessing file metadata (name, size, type) from client-side JavaScript. The API also has methods for reading file contents directly in the browser. This is particularly interesting for displaying preview of images before uploading them, or - and this is much more interesting - for developing Web applications that work with local files without the need for a server.

Imagine a multimedia player that accesses (in read-only) your file system, reads your audio and video files, etc., such as the [Remo Music player](https://tinyurl.com/ya9fuqb2) below, or an application that edits the audio content of local mp3 files, for example, the [HYA-WAVE sound editor](https://wav.hya.io/#/fx) (screenshot above).

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/y2xpgmdq" ismap target="_blank">
    <img style="margin: 0.1em;" height=200
      src  ="https://tinyurl.com/y5m6fw8g"
      alt  ="audio player that plays local files"
      title="audio player that plays local files"
    >
    <img style="margin: 0.1em;" height=200
      src  ="https://tinyurl.com/y3n3q6et"
      alt  ="polarr photo editor uses the File API"
      title="polarr photo editor uses the File API"
    >
  </a>
</div>


#### External resources

+ From W3C's specification: [File API](https://www.w3.org/TR/FileAPI/)
+ An article from Web.dev: [Read files in JavaScript](https://web.dev/read-files/)
+ MDN's Web Docs: [Using files from web applications](https://developer.mozilla.org/en-US/docs/Web/API/File/Using_files_from_web_applications)







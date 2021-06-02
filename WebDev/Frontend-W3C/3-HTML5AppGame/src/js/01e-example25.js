var bufferLoader;
var ctx;

var listOfSoundSamplesURLs = [
 'http://mainline.i3s.unice.fr/mooc/shoot1.mp3', 
 'http://mainline.i3s.unice.fr/mooc/shoot2.mp3'
];

window.onload = function init() {
  // To make it work even on browsers like Safari, that still
  // do not recognize the non prefixed version of AudioContext
var audioContext = window.AudioContext || window.webkitAudioContext;

 ctx = new audioContext();
  
 loadAllSoundSamples();
};

function playSampleNormal(buffer){
    var bufferSource = ctx.createBufferSource();
    bufferSource.buffer = buffer;
    bufferSource.connect(ctx.destination);
    bufferSource.start();
}


function onSamplesDecoded(buffers){
  console.log("all samples loaded and decoded");
  shot1Normal.disabled=false;
  shot2Normal.disabled=false;
  
    shot1Normal.onclick = function(evt) {
        playSampleNormal(buffers[0]);
    };
  
    shot2Normal.onclick = function(evt) {
        playSampleNormal(buffers[1]);
    };
}

function loadAllSoundSamples() {
  // onSamplesDecoded will be called when all samples 
  // have been loaded and decoded, and the decoded sample will
  // be its only parameter (see function above)
    bufferLoader = new BufferLoader(
        ctx,
        listOfSoundSamplesURLs,
        onSamplesDecoded
    );
  
  // start loading and decoding the files
    bufferLoader.load();              
}

// You do not have to understand in details the next lines of code...
// just use them!

/* ############################
    BUFFER LOADER for loading multiple files asyncrhonously. The callback functions is called when all
    files have been loaded and decoded 
 ############################## */
function BufferLoader(context, urlList, callback) {
    this.context = context;
    this.urlList = urlList;
    this.callback = callback;
    this.bufferList = [];
    this.loadCount = 0;
}

BufferLoader.prototype.loadBuffer = function(url, index) {
    // Load buffer asynchronously
    console.log('file : ' + url + "loading and decoding");

    var request = new XMLHttpRequest();
    request.open("GET", url, true);

    request.responseType = "arraybuffer";

    var loader = this;

    request.onload = function() {

        // Asynchronously decode the audio file data in request.response
        loader.context.decodeAudioData(
                request.response,
                function(buffer) {
                        console.log("Loaded and decoded track " + (loader.loadCount+1) + 
                        "/" +  loader.urlList.length + "...");

                    if (!buffer) {
                        alert('error decoding file data: ' + url);
                        return;
                    }
                    loader.bufferList[index] = buffer;

                    //console.log("In bufferLoader.onload bufferList size is " + loader.bufferList.length + " index =" + index);
                    if (++loader.loadCount == loader.urlList.length)
                       // call the callback and pass it the decoded buffers, we've finihed
                      loader.callback(loader.bufferList);
                },
                function(error) {
                    console.error('decodeAudioData error', error);
                }
        );
    };

    request.onprogress = function(e) {
         if(e.total !== 0) {
            var percent = (e.loaded * 100) / e.total;

            console.log("loaded " + percent  + " % of file " + index);
         }
    };
    
    request.onerror = function() {
        alert('BufferLoader: XHR error');
    };

    request.send();
};

BufferLoader.prototype.load = function() {
    console.log("Loading " + this.urlList.length + "track(s)... please wait...");
    for (var i = 0; i < this.urlList.length; ++i)
        this.loadBuffer(this.urlList[i], i);
};


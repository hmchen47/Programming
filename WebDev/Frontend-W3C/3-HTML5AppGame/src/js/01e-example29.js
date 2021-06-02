var bufferLoader;
var ctx;

var canvas;
var canvasContext;
var gradient;
var analyser, analyserLeft, analyserRight;
var width, height;

var dataArray, bufferLength;
var dataArrayLeft, dataArrayRight;

var listOfSoundSamplesURLs = [
 'https://mainline.i3s.unice.fr/mooc/shoot1.mp3', 
 'https://mainline.i3s.unice.fr/mooc/shoot2.mp3'
];

window.onload = function init() {
  // To make it work even on browsers like Safari, that still
  // do not recognize the non prefixed version of AudioContext
var audioContext = window.AudioContext || window.webkitAudioContext;

 ctx = new audioContext();
  
  loadAllSoundSamples();
  createStaticNodes();
  
    canvas = document.querySelector("#myCanvas");
  width = canvas.width;
  height = canvas.height;
  canvasContext = canvas.getContext('2d');
  
  // create a vertical gradient of the height of the canvas
  gradient = canvasContext.createLinearGradient(0,0,0, height);
  gradient.addColorStop(1,'#000000');
  gradient.addColorStop(0.75,'#ff0000');
  gradient.addColorStop(0.25,'#ffff00');
  gradient.addColorStop(0,'#ffffff');
  
  requestAnimationFrame(visualize);

};

function visualize() {
  
  clearCanvas();
  
  drawVolumeMeters();
  drawWaveform();

  // call again the visualize function at 60 frames/s
  requestAnimationFrame(visualize);
  
}

function drawWaveform() {
  canvasContext.save();
  // Get the analyser data
  analyser.getByteTimeDomainData(dataArray);

  canvasContext.lineWidth = 2;
  canvasContext.strokeStyle = 'lightBlue';

  // all the waveform is in one single path, first let's
  // clear any previous path that could be in the buffer
  canvasContext.beginPath();
  
  var sliceWidth = width / bufferLength;
  var x = 0;
  
      // values go from 0 to 256 and the canvas heigt is 100. Let's rescale
      // before drawing. This is the scale factor
      heightScale = height/128;

  for(var i = 0; i < bufferLength; i++) {
     // dataArray[i] between 0 and 255
     var v = dataArray[i] / 255;
     var y = v * height;
    
     if(i === 0) {
        canvasContext.moveTo(x, y);
     } else {
        canvasContext.lineTo(x, y);
     }

     x += sliceWidth;
  }

  canvasContext.lineTo(canvas.width, canvas.height/2);
  
  // draw the path at once
  canvasContext.stroke();    
  canvasContext.restore();
}

function clearCanvas() {
   canvasContext.save();
  
   // clear the canvas
   // like this: canvasContext.clearRect(0, 0, width, height);
  
   // Or use rgba fill to give a slight blur effect
  canvasContext.fillStyle = 'rgba(0, 0, 0, 0.5)';
  canvasContext.fillRect(0, 0, width, height);
  
  canvasContext.restore();
}


function drawVolumeMeters() {
  canvasContext.save();
  
  // set the fill style to a nice gradient
  canvasContext.fillStyle=gradient;
  
  // left channel
  analyserLeft.getByteFrequencyData(dataArrayLeft);
  var averageLeft = getAverageVolume(dataArrayLeft);
  
  // draw the vertical meter for left channel
  canvasContext.fillRect(0,height-averageLeft,25,height);
  
  // right channel
  analyserRight.getByteFrequencyData(dataArrayRight);
  var averageRight = getAverageVolume(dataArrayRight);
  
  // draw the vertical meter for left channel
  canvasContext.fillRect(26,height-averageRight,25,height);

  
  canvasContext.restore();
}

function getAverageVolume(array) {
        var values = 0;
        var average;
 
        var length = array.length;
 
        // get all the frequency amplitudes
        for (var i = 0; i < length; i++) {
            values += array[i];
        }
 
        average = values / length;
        return average;
    }



function createStaticNodes() {
  // these nodes can be used multiple times
     stereoPanner = ctx.createStereoPanner();
  // Create an analyser node
  analyser = ctx.createAnalyser();
  
  // Try changing for lower values: 512, 256, 128, 64...
  analyser.fftSize = 1024;
  bufferLength = analyser.frequencyBinCount;
  dataArray = new Uint8Array(bufferLength);

    // two analysers for the stereo volume meters
  analyserLeft = ctx.createAnalyser();
  analyserLeft.fftSize = 256;
  bufferLengthLeft = analyserLeft.frequencyBinCount;
  dataArrayLeft = new Uint8Array(bufferLengthLeft);
  
  analyserRight = ctx.createAnalyser();
  analyserRight.fftSize = 256;
  bufferLengthRight = analyserRight.frequencyBinCount;
  dataArrayRight = new Uint8Array(bufferLengthRight);

  splitter = ctx.createChannelSplitter();

}
function makeSource(buffer) {
   // build graph source -> gain -> compressor -> speakers
   var source = ctx.createBufferSource();
   var compressor = ctx.createDynamicsCompressor();
   var gain = ctx.createGain();
   gain.gain.value = 0.2 + Math.random();
   source.buffer = buffer;
   source.connect(gain);
   gain.connect(compressor);
  
  
    // connect the source node to a stereo pannel
  compressor.connect(stereoPanner);
  
  
  
  // connect the stereo pannel to the analyser
  stereoPanner.connect(analyser);
  // and teh analyser to the destination
  analyser.connect(ctx.destination);
  
  // This is new, we add another route from the stereoPanner node
  
 
  // connect the source to the analyser and the splitter
  stereoPanner.connect(splitter);
 
  // connect one of the outputs from the splitter to
  // the analyser
  splitter.connect(analyserLeft,0,0);
  splitter.connect(analyserRight,1,0);
  
   return source;
}

function playSampleRepeated(buffer, rounds, interval, random, random2) {
  if (typeof random == 'undefined') {
    random = 0;
  }
   if (typeof random2 == 'undefined') {
    random2 = 0;
  }
 


    var time = ctx.currentTime;
  // Make multiple sources using the same buffer and play in quick succession.
  for (var i = 0; i < rounds; i++) {
    var source = makeSource(buffer);
    source.playbackRate.value = 1 + Math.random() * random2;
    source.start(time + i * interval + Math.random() * random);
  }
}
  function playSampleNormal(buffer){
    var source = makeSource(buffer);
    source.start();
}
function onSamplesDecoded(buffers){
  console.log("all samples loaded and decoded");
  
    shot1Normal.onclick = function(evt) {
        playSampleNormal(buffers[0]);
    };
  
    shot2Normal.onclick = function(evt) {
        playSampleNormal(buffers[1]);
    };
      shot1Repeated.onclick = function(evt) {
        playSampleRepeated(buffers[0], 3, 0.1);
    };
  
    shot2Repeated.onclick = function(evt) {
        playSampleRepeated(buffers[1], 10, 0.2);
    };
  
    shot1RepeatedIntervalRandom.onclick = function(evt) {
        playSampleRepeated(buffers[0], 10, 0.08, 0.05);
    };
  
    shot2RepeatedPitchAndIntervalRandom.onclick = function(evt) {
        playSampleRepeated(buffers[1], 10, 0.08, 1, 1);
    };

}

function loadAllSoundSamples() {
  
    bufferLoader = new BufferLoader(
            ctx,      
            listOfSoundSamplesURLs,   // urls of all sound samples to load
            onSamplesDecoded          // called when all samples have been loaded and decoded
            );
  
    bufferLoader.load();              // start loading. Will call onSamplesDecoded once all files loaded and decoded
}

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

            console.log("loaded " + percent  + " % of song " + index);
         }
    };
    
    request.onerror = function() {
        alert('BufferLoader: XHR error');
    };

    request.send();
};
//noprotect
BufferLoader.prototype.load = function() {
    console.log("Loading " + this.urlList.length + "track(s)... please wait...");
    for (var i = 0; i < this.urlList.length; ++i)
        this.loadBuffer(this.urlList[i], i);
};



var ctx = window.AudioContext || window.webkitAudioContext;
var audioContext = new ctx();

/* BiquadFilterNode */



var biquadExample = document.querySelector('#biquadExample');
    biquadExample.onplay = (e) => {audioContext.resume();}

var biquadFilterFrequencySlider = document.querySelector('#biquadFilterFrequencySlider');
var biquadFilterDetuneSlider = document.querySelector('#biquadFilterDetuneSlider');
var biquadFilterQSlider = document.querySelector('#biquadFilterQSlider');
var biquadFilterTypeSelector = document.querySelector('#biquadFilterTypeSelector');

var biquadExampleMediaElementSource = audioContext.createMediaElementSource(biquadExample);

var filterNode = audioContext.createBiquadFilter();

biquadExampleMediaElementSource.connect(filterNode);

filterNode.connect(audioContext.destination);

biquadFilterFrequencySlider.oninput = function(evt){
    filterNode.frequency.value = parseFloat(evt.target.value);
};

biquadFilterDetuneSlider.oninput = function(evt){
    filterNode.detune.value = parseFloat(evt.target.value);
};

biquadFilterQSlider.oninput = function(evt){
    filterNode.Q.value = parseFloat(evt.target.value);
};


biquadFilterTypeSelector.onchange = function(evt){
    filterNode.type = evt.target.value;
};

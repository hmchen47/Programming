//=================== AddKeys.js ====================//

var notes = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"];
var note = 0;
var octave = 1;

for(var i=13;i<=49;i++)
{
   var thisNote = notes[note];
   var className = (thisNote.length > 1) ? 'black' : 'white';

   var el = "<div id='" + thisNote + octave + "' class='" + className + "' onmousedown='start("+i+",this);' onmouseup='stop(this);'><p>" + thisNote + "</p></div>";

   if(className == "white")
   {
      document.getElementById("pianoKeys").innerHTML += el;
   }
   else
   {
      //console.log(thisNote.substring(0,1) + octave);
      document.getElementById(thisNote.substring(0,1) + octave).innerHTML += el;
   }

   if(thisNote == "B")
   {
      octave ++;
   }

   if(i%12 == 0)
   {
      note = 0;
   }
   else
   {
      note++;
   }
}

//=============== Context.js ==================//
var context = new (window.AudioContext || window.webkitAudioContext || window.mozAudioContext || window.oAudioContext || window.msAudioContext)();

function getContext()
{
   return context;
}


//================= Oscillator.js ================//

function Oscillator()
{
   this.context = getContext();
   this.instance = context.createOscillator();
   this.gainNode = context.createGain();
   this.freq = 440;
   this.gain = 100;
   this.waveForm = "sine";
   this.octave = 0;
   this.fineTune = 0;

   //Methods
   this.createOscillator = function(freq, gain)
   {
      this.instance = this.context.createOscillator();
      this.instance.connect(this.gainNode);
      this.gainNode.connect(context.destination);
      this.instance.type = this.waveForm;
   };

   this.setFreq = function(freq)
   {
      this.freq = freq;
      this.instance.frequency.value = freq;
   };

   this.setGain = function(gain)
   {
      this.gain = gain;
      this.gainNode.gain.value = gain / 100 / 12;
   };

   this.setWaveForm = function(waveForm)
   {
      this.waveForm = waveForm;
   };

   this.setOctave = function(octave)
   {
      this.octave = octave;
   };

   this.setFineTune = function(fineTune)
   {
      this.fineTune = fineTune;
   };

}

//================ Tones.js ================//

var context = getContext();

var playing = false;

var osc = new Oscillator();
var osc2 = new Oscillator();

osc.setGain(document.getElementById("osc1Gain").value);
osc2.setGain(document.getElementById("osc2Gain").value);

osc.setWaveForm(document.querySelector('input[name="osc1Led"]:checked').getAttribute("data-waveform"));
osc2.setWaveForm(document.querySelector('input[name="osc2Led"]:checked').getAttribute("data-waveform"));

osc.setOctave(document.querySelector('input[name="osc1OctLed"]:checked').getAttribute("data-position") - 1);
osc2.setOctave(document.querySelector('input[name="osc2OctLed"]:checked').getAttribute("data-position") - 1);

console.log(osc.octave);

function toneGen(oscillator, noteKey)
{
   var freq = calculateFrequency(noteKey + (oscillator.octave * 12));

   freq = calculateFineTune(oscillator.fineTune, freq);

   oscillator.createOscillator();
   oscillator.setFreq(freq);
   oscillator.instance.start(0);
}


function start(noteKey,e) {
   console.log(e.id);

   e.className = e.className + " keyDown";
   event.cancelBubble = true;

   if(e.id.substring(1,1) == "#")
   {
      document.getElementById(e.id.substring(0,1) + e.id.substring(2,1)).className = "white";
   }

   if(!playing) {
      playing = true;

      toneGen(osc,noteKey);
      toneGen(osc2,noteKey);
   }
}

function stop(e)
{
   e.className = e.className.substring(0,5) == "white" ? "white" : "black";

   playing = false;
   //setVolume(0);


   osc.instance.stop();
   osc.gainNode.disconnect();
   osc2.instance.stop();
   osc2.gainNode.disconnect();

}

function calculateFrequency(noteKey)
{
   var concertPitch = 440;
   var A4Key = 49;
   var a = Math.pow(2,(1/12));
   return Math.pow(a,(noteKey - A4Key)) * concertPitch;
}


function calculateFineTune(fineTune, freq)
{
   var pos, positive;
   if(-fineTune>0)
   {
      pos = -fineTune; //Is made positive
      positive = false;

   }
   else
   {
      pos = fineTune; //Already Positive
      positive = true;
   }

   var percentage = freq * (pos/100);
   freq = positive ? freq + percentage : freq - percentage;

   //console.log(fineTune + " " +  freq + "hz before | " + (parseFloat(freq) + parseInt(fineTune)) + "hz after");
   return freq;
}


document.addEventListener('DOMContentLoaded', function ()
{
   document.getElementById("osc1Gain").addEventListener("change", setGain);
   document.getElementById("osc2Gain").addEventListener("change", setGain);

   document.getElementById("osc1FineTune").addEventListener("change", setFineTune);
   document.getElementById("osc2FineTune").addEventListener("change", setFineTune);

   window.addEventListener("keydown",handleKeyPress,false);
   window.addEventListener("keyup",handleKeyPress,false);
});


function handleKeyPress(e)
{
   var keyCode = e.which;
   var id = null;
   //console.log(e, keyCode, e.which);

   switch(keyCode)
   {

      case 90:    id = "A1";     break;
      case 83:    id = "A#1";    break;
      case 88:    id = "B1";     break;
      case 67:    id = "C2";     break;
      case 70:    id = "C#2";    break;
      case 86:    id = "D2";     break;
      case 71:    id = "D#2";    break;
      case 66:    id = "E2";     break;
      case 78:    id = "F2";     break;
      case 74:    id = "F#2";    break;
      case 77:    id = "G2";     break;
      case 75:    id = "G#2";    break;
      case 188:   id = "A2";     break;

      case 81:    id = "A2";     break;
      case 50:    id = "A#2";    break;
      case 87:    id = "B2";     break;
      case 69:    id = "C3";     break;
      case 52:    id = "C#3";    break;
      case 82:    id = "D3";     break;
      case 53:    id = "D#3";    break;
      case 84:    id = "E3";     break;
      case 89:    id = "F3";     break;
      case 55:    id = "F#3";    break;
      case 85:    id = "G3";     break;
      case 56:    id = "G#3";    break;
      case 73:   id = "A3";     break;

      default:
   }

   var el = document.getElementById(id);

   if(id != null)
   {
      if(e.type == "keydown")
      {
         el.onmousedown();
         el.className = el.className.substring(0,5) + " keyDown";
      }
      else
      {
         el.onmouseup();
         el.className = el.className.substring(0,5);
      }
   }


}




//--------------------------Getters And Setters--------------------------//



function setGain(e)
{
   var oscillator = this.getAttribute("data-osc");

   switch(oscillator)
   {
      case "1":
         osc.setGain(this.value);
         break;
      case "2":
         osc2.setGain(this.value);
         break;
      default:
   }
}

function setFineTune(e)
{
   var oscillator = this.getAttribute("data-osc");

   switch(oscillator)
   {
      case "1":
         osc.setFineTune(this.value);
         console.log(osc.fineTune);
         break;
      case "2":
         osc2.setFineTune(this.value);
         break;
      default:
   }
}

function setOctave(e)
{
   var oscillator = e.getAttribute("data-osc");
   var position = parseInt(document.querySelector('input[name="osc' + oscillator + 'OctLed"]:checked').getAttribute("data-position"));
   var newPosition = position < 2 ? (position + 1) : 0;
   newPosition = e.id.substring(0,7) == "osc" + oscillator + "Oct" ?  position : newPosition;

   var octaves = [-1,0,+1];

   switch(oscillator)
   {
      case "1":
         osc.setOctave(newPosition - 1);
         console.log("osc1 " + osc.octave);
         break;
      case "2":
         osc2.setOctave(newPosition - 1);
         console.log("osc2 " + osc2.octave);
         break;
      default:
   }

   id = "osc" + oscillator + "OctLed" + newPosition;

   document.getElementById(id).checked = true;
}



function setWaveForm(e)
{
   var oscillator = e.getAttribute("data-osc");
   var position = parseInt(document.querySelector('input[name="osc' + oscillator + 'Led"]:checked').getAttribute("data-position"));


   var newPosition = position < 3 ? (position + 1) : 0;
   newPosition = (e.id.substring(0,7) == "osc" + oscillator + "Led") ?  position : newPosition;

   var waves = ["sine","square","sawtooth","triangle"];


   switch(oscillator)
   {
      case "1":
         osc.setWaveForm(waves[newPosition]);
         console.log("osc1 " + osc.waveForm);
         break;
      case "2":
         osc2.setWaveForm(waves[newPosition]);
         console.log("osc2 " + osc2.waveForm);
         break;
      default:
   }

   id = "osc" + oscillator + "Led" + newPosition;

   document.getElementById(id).checked = true;

}

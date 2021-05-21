// Transcript.js
function loadTranscript(lang) {
  var url = "https://mainline.i3s.unice.fr/mooc/" + 'elephants-dream-subtitles-' + lang + '.vtt';
      
	loadTranscriptFile(url);
}

function loadTranscriptFile(webvttFileUrl) {
	var reqTrans = new XMLHttpRequest();
  
	reqTrans.open('GET', webvttFileUrl);
  
	reqTrans.onload = function(e) {
		
			var pattern = /^([0-9]+)$/;
			var patternTimecode = /^([0-9]{2}:[0-9]{2}:[0-9]{2}[,.]{1}[0-9]{3}) --\> ([0-9]{2}:[0-9]{2}:[0-9]{2}[,.]{1}[0-9]{3})(.*)$/;
			
			var content = this.response; // content of the webVTT file
      
			var lines = content.split(/\r?\n/);
			var transcript = '';
			for (i = 0; i < lines.length; i++) {
                var identifier = pattern.exec(lines[i]);
				if (identifier) {
					i++;
					var timecode = patternTimecode.exec(lines[i]);
					if (timecode && i < lines.length) {
						i++;
						var text = lines[i];
						i++;
						while (lines[i] !== '' && i < lines.length) {
							text = text + '\n' + lines[i];
							i++;
						}
						var transText = '';
						var voices = getVoices(text);
						if (voices.length > 0) {
							for (var j = 0; j < voices.length; j++) {
								transText += voices[j].voice + ': ' + removeHTML(voices[j].text) + '<br />';
							}
						}
						else transText = removeHTML(text) + '<br />';
						transcript += transText;
					}
	    		}
			
			var oTrans = document.getElementById('transcript');
			oTrans.innerHTML = transcript;
		}
	};
	reqTrans.send();
}

function getVoices(speech) {
	var voices = [];
	var pos = speech.indexOf('<v');
  
	while (pos != -1) {
		endVoice = speech.indexOf('>');
		var voice = speech.substring(pos + 2, endVoice).trim();
		var endSpeech = speech.indexOf('</v>');
		var text = speech.substring(endVoice + 1, endSpeech);
		voices.push({
			'voice': voice,
			'text': text
		});
		speech = speech.substring(endSpeech + 4);
		pos = speech.indexOf('<v');
	}
	return voices;
}

function removeHTML(text) {
	var div = document.createElement('div');
	div.innerHTML = text;
	return div.textContent || div.innerText || '';
}
// 


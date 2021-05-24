// This demo is based on code at http://dev.w3.org/html5/spec/media-elements.html#text-track-api

window.onload = function() {

    var audio = new   Audio("https://mainline.i3s.unice.fr/mooc/animalSounds.mp3");

        audio.addEventListener("loadedmetadata", function() {
        var track = audio.addTextTrack("metadata", "sprite track", "en");
        track.mode = "hidden";

        // for browsers that do not implement the getCueById() method
        if (typeof track.getCueById !== "function") {
                track.getCueById = function(id) {
                    var cues = track.cues;
                    for (var i = 0; i != track.cues.length; ++i) {
                        if (cues[i].id === id) {
                            return cues[i];
                        }
                    }
                };
            }

            var sounds = [{
                id: "purr",
                startTime: 0.200,
                endTime: 1.800
            }, {
                id: "meow",
                startTime: 2.300,
                endTime: 3.300
            }, {
                id: "bark",
                startTime: 3.900,
                endTime: 4.300
            }, {
                id: "baa",
                startTime: 5.000,
                endTime: 5.800
            }, {
                id: "moo",
                startTime: 6.500,
                endTime: 8.200
            }, {
                id: "bleat",
                startTime: 8.500,
                endTime: 9.400
            }, {
                id: "woof",
                startTime: 9.900,
                endTime: 10.400
            }, {
                id: "cluck",
                startTime: 11.100,
                endTime: 13.400
            }, {
                id: "mew",
                startTime: 13.800,
                endTime: 15.600
            }];

            for (var i = 0; i !== sounds.length; ++i) {
                var sound = sounds[i];
                var cue = new VTTCue(sound.startTime, sound.endTime, sound.id); // change in spec
                cue.id = sound.id;
                track.addCue(cue);
                document.querySelector("#soundButtons").innerHTML += "<button class='playSound' id=" + sound.id + ">" + sound.id + "</button>";
            }

            var endTime;
            audio.addEventListener("timeupdate", function(event) {
                if (event.target.currentTime > endTime)
                    event.target.pause();
            });

            function playSound(id) {
                var cue = track.getCueById(id);
                audio.currentTime = cue.startTime;
                endTime = cue.endTime;
                audio.play();
            }

            var buttons = document.querySelectorAll("button.playSound");
          
          for(i = 0; i < buttons.length; i++) {
            buttons[i].addEventListener("click", function(e) {
              playSound(this.id);
              
            });
          }
           

        });
    };

    function addListenerToButton(i) {
  
}


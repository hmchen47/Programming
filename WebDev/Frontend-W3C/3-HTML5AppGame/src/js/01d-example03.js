let speedX = 3,speedY=4,asideH, canvas, ctx, width, height, size = 50, x = y = 100;
let x1 = y1 = 0;
let audio, track, cues, endTime, sounds;
let ids = ['purr', 'meow', 'bark', 'baa', 'moo', 'bleat', 'woof', 'cluck', 'mew'];
let squareColors = ['blue', 'green', 'red','pink', 'magenta','cyan', 'khaki','indigo','yellow'];
var idIncr = 0;
window.onload = function () {
    canvas = document.querySelector("#myCanvas");
    ctx = canvas.getContext('2d');

    width = canvas.width;
    height = canvas.height;
  
  asideH = height;
  var aside = document.querySelector("#aside");
  aside.style.height = asideH;

    audio = new Audio("https://mainline.i3s.unice.fr/mooc/animalSounds.mp3");

    audio.addEventListener('loadedmetadata', function () {
        track = audio.addTextTrack('metadata', 'animal sounds', 'en');
        track.mode = 'hidden';

        if (typeof track.getCueById !== 'function') {
            track.getCueById = function (id) {
                cues = track.cues;
                for (var i = 0; i != track.cues.length; ++i) {
                    if (cues[i].id == id) {
                        return cues[i];
                    }
                }
            };
        }

         sounds = [{
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
            var cue = new VTTCue(sound.startTime, sound.endTime, sound.id);
            cue.id = sound.id;
            track.addCue(cue);
        }


        audio.addEventListener('timeupdate', function (event) {
            if (event.target.currentTime > endTime)
                event.target.pause();
        });

        
            requestAnimationFrame(animate);
    });
}

function animate() {
  // clear canvas
    ctx.clearRect(0, 0, width, height);
  
  // save and translate context 
    ctx.save();
    ctx.translate(0, 0);
  
  
    ctx.strokeStyle = 'indigo';
    ctx.fillStyle = squareColors[idIncr];
    ctx.lineWidth = 5;

    ctx.fillRect(x, y, size, size);
    ctx.strokeRect(x, y, size, size);


    x += speedX;
    y += speedY;


    if (x + size > width || x < 0) {
        playSound(ids[idIncr]);
       

        speedX *= -1;
    } 
  if (y < 0 || y + size > height) {
        speedY *= -1;
        playSound(ids[idIncr])


    }

    ctx.restore();

    requestAnimationFrame(animate);
}

function playSound(id) {
   
    var cue = track.getCueById(id);
    audio.currentTime = cue.startTime;
    endTime = cue.endTime;
    audio.play();

    if (idIncr < ids.length)
        idIncr += 1;

    if (idIncr === ids.length)
        idIncr = 0;
   
}


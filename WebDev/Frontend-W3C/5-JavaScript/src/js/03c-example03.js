window.onload = init;

let vid;

function init() {
	console.log("Page loaded, DOM is ready!"); 
	
	vid = document.querySelector("#myPlayer");
	
	vid.ontimeupdate = displayTimeWhileVideoIsPlaying;
}

function playVideo() {
	vid.play();
}

function pauseVideo() {
	vid.pause();
}

function rewindVideo() {
	vid.currentTime = 0;
}

function displayTimeWhileVideoIsPlaying(evt) {
	console.log(vid.currentTime);
	if(vid.currentTime > 5)
		vid.pause();
	
}


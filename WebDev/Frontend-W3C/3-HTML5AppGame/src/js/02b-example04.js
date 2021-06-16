var GF = function(){

    var mainLoop = function(){
        //main function, called each frame
        document.body.innerHTML = Math.random();
      
        // call the animation loop every 1/60th of second
        requestAnimationFrame(mainLoop);
    };

    var start = function(){
        requestAnimationFrame(mainLoop);
    };

    //our GameFramework returns a public API visible from outside its scope
    return {
        start: start
    };
};

var game = new GF();
game.start();


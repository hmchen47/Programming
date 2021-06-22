var canvas, ctx, width, height;
var tableauDeBalles = [];

function init() {
  canvas = document.querySelector("#myCanvas");
  ctx = canvas.getContext('2d');
  width = canvas.width;
  height = canvas.height;
  
  creeDesBalles(2);
 
  anime();
}
                                
function creeDesBalles(nombreDeBalles) {
  for(var i=0; i < nombreDeBalles; i++) {
    
    // On cree une balle
    var balle =  new Ball(width*Math.random(),
                          height*Math.random(),
                          (1*Math.random())-0.5,
                          (1*Math.random())-0.5,  
                          120);
    
    // On la rajoute au tableau
    tableauDeBalles[i] = balle;
  }
}                                

function anime() {
    // On efface l'Ã©cran
    ctx.clearRect(0, 0, canvas.width, canvas.height);
   //ctx.fillStyle = "rgba(0, 240, 240, 0.2)";
  //ctx.fillRect (0, 0, width, height);
  //ctx.fillStyle='black';
  
    // Pour chaque balle dans le tableau
    for(var i=0; i < tableauDeBalles.length; i++) {
      var balle = tableauDeBalles[i];
      
      // 1) On dÃ©place la balle 
      balle.deplaceToi();   
  
      // 2) On regarde si la balle touche un mur
      testeCollisionAvecMurs(balle);
  
      // 3) On dessine la balle
      balle.dessineToi();
  }
  
  testeCollisionsEntreBalles();
  
    // On demande une nouvelle frame d'animation
     window.requestAnimationFrame(anime);
}
 
function testeCollisionAvecMurs(ball) {
    if (ball.x < ball.rayon) {
        ball.x = ball.rayon;
        ball.vx *= -1;
    } 
    if (ball.x > width - (ball.rayon)) {
        ball.x = width - (ball.rayon);
        ball.vx *= -1;
    }     
    if (ball.y < ball.rayon) {
        ball.y = ball.rayon;
        ball.vy *= -1;
    }     
    if (ball.y > height - (ball.rayon)) {
        ball.y = height - (ball.rayon);
        ball.vy *= -1;
    }
}

function testeCollisionsEntreBalles() {  
  var balles = tableauDeBalles;
  
  for (var i = 0; i < tableauDeBalles.length; i++) {
        for (var j = i + 1; j < tableauDeBalles.length; j++) {
            var dx = balles[j].x - balles[i].x;
            var dy = balles[j].y - balles[i].y;

            // Pour le debug / la compréhension
            drawVecteurs(i, j);
          
            var dist = Math.sqrt(dx * dx + dy * dy);
            if (dist < (balles[j].rayon + balles[i].rayon)) {
              // Calcul de v1, v2 et n
              var v1x = balles[i].vx, v1y = balles[i].vy;
              var v2x = balles[j].vx, v2y = balles[j].vy;
              
              var nx = dx / dist;
              var ny = dy / dist; 

              
              
              
              
                // collision
              
                // Normale au plan de collision / axe séparateur
                var normaleX = dx / dist;
                var normaleY = dy / dist; 
              
                // Milieu de l'axe reliant les deux balles
                var milieuX = (balles[i].x + balles[j].x) / 2;
                var milieuY = (balles[i].y + balles[j].y) / 2;

              
                // On fait reculer les deux balles en collision le
                // long de l'axe reliant les deux centres
                // pour qu'elles reviennent pile au point de contact
                balles[i].x = milieuX - normaleX * balles[i].rayon;
                balles[i].y = milieuY - normaleY * balles[i].rayon;
                balles[j].x = milieuX + normaleX * balles[j].rayon;
                balles[j].y = milieuY + normaleY * balles[j].rayon; 
              
              
                var dVector = (balles[i].vx - balles[j].vx) * normaleX;
                dVector += (balles[i].vy - balles[j].vy) * normaleY;
                var dvx = dVector * normaleX;
                var dvy = dVector * normaleY;
              
                balles[i].vx -= dvx;
                balles[i].vy -= dvy;
                balles[j].vx += dvx;
                balles[j].vy += dvy;
            }
        }
    }
}

function drawVecteurs(i, j) {
  var balles = tableauDeBalles;
  // Milieu de l'axe reliant les deux balles
  var milieuX = (balles[i].x + balles[j].x) / 2;
  var milieuY = (balles[i].y + balles[j].y) / 2;

  // On dessine l'axe et le milieu
  ctx.beginPath();
  ctx.moveTo(balles[i].x, balles[i].y);
  ctx.lineTo(balles[j].x, balles[j].y);
  ctx.stroke();
  ctx.beginPath();
  ctx.arc(balles[i].x, balles[i].y, 3, 0, Math.PI*2, false);
  ctx.fill();
  ctx.beginPath();
  ctx.arc(balles[j].x, balles[j].y, 3, 0, Math.PI*2, false);
  ctx.fill();
  // point milieu
  ctx.beginPath();
  ctx.arc(milieuX, milieuY, 3, 0, Math.PI*2, false);
  ctx.fill();
  // le dx et le dy
  ctx.beginPath();
  ctx.moveTo(balles[i].x, balles[i].y);
  ctx.lineTo(balles[j].x, balles[i].y);
  ctx.lineTo(balles[j].x, balles[j].y);
  ctx.stroke();  
  
  // Dessine le plan de collision / axe séparateur 
  drawPlanCollision(balles[i], balles[j]);
  
  // Dessine les vecteurs vitesse des balles
drawVecteurVitesse(balles[i], 3, 100, 'blue');
  drawVecteurVitesse(balles[j], 3, 100, 'green');
} 

function drawPlanCollision(balle1, balle2) {
  // calcul du vecteur normé reliant les balles
  var x1 = balle1.x, y1 = balle1.y;
  var x2 = balle2.x, y2 = balle2.y;
  var vx = x2-x1, vy = y2-y1;
  
  var norme = Math.sqrt(vx*vx + vy*vy);
  vx /= norme; vy /= norme;
  
  var milieuX = (balle1.x + balle2.x) / 2;
  var milieuY = (balle1.y + balle2.y) / 2;
  
  // vecteur orthogonal à (vx, vy) = vecteur (-vy, vx) 
  ctx.beginPath();
  ctx.moveTo(milieuX+vy*100, milieuY-vx*100);
  ctx.lineTo(milieuX-vy*100, milieuY+vx*100);
  ctx.stroke();
}

function drawVecteurVitesse(balle, epaisseur, longueurEnPixels, color) {
  var x = balle.x;
  var y = balle.y;
  
  var vx = balle.vx;
  var vy = balle.vy;
  
  var norme = Math.sqrt(vx * vx + vy * vy);
  var vxNorm = vx / norme;
  var vyNorm = vy / norme;
  
  drawArrow(ctx, x, y, x+vxNorm*longueurEnPixels, y+vyNorm*longueurEnPixels,epaisseur, color);
}

function Ball(x, y, vx, vy, diametre) {
  this.x = x;
  this.y = y;
  this.vx = vx;
  this.vy = vy;
  this.rayon = diametre/2;
  
  this.dessineToi = function() {
    ctx.beginPath();
      ctx.arc(this.x, this.y, this.rayon, 0, 2*Math.PI);
      ctx.stroke();
  };
  
  this.deplaceToi = function() {
    
    this.x += this.vx;
    this.y += this.vy;
  };
  
}

// Borrowed and adapted from : http://stackoverflow.com/questions/808826/draw-arrow-on-canvas-tag
function drawArrow(ctx, fromx, fromy, tox, toy, arrowWidth, color){
  //variables to be used when creating the arrow
  var headlen = 10;
  var angle = Math.atan2(toy-fromy,tox-fromx);

  ctx.save();
  ctx.strokeStyle = color;

  //starting path of the arrow from the start square to the end square and drawing the stroke
  ctx.beginPath();
  ctx.moveTo(fromx, fromy);
  ctx.lineTo(tox, toy);
  ctx.lineWidth = arrowWidth;
  ctx.stroke();

  //starting a new path from the head of the arrow to one of the sides of the point
  ctx.beginPath();
  ctx.moveTo(tox, toy);
  ctx.lineTo(tox-headlen*Math.cos(angle-Math.PI/7),toy-headlen*Math.sin(angle-Math.PI/7));

  //path from the side point of the arrow, to the other side point
  ctx.lineTo(tox-headlen*Math.cos(angle+Math.PI/7),toy-headlen*Math.sin(angle+Math.PI/7));

  //path from the side point back to the tip of the arrow, and then again to the opposite side point
  ctx.lineTo(tox, toy);
  ctx.lineTo(tox-headlen*Math.cos(angle-Math.PI/7),toy-headlen*Math.sin(angle-Math.PI/7));

  //draws the paths created above
  ctx.stroke();
  ctx.restore();
}


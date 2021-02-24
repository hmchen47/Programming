class Point {
  constructor(x, y) {
    this.x = x;
    this.y = y;
    // static property
    Point.nbPointsCreated++;
  }

  // static method
  static distance(a, b) {
    const dx = a.x - b.x;
    const dy = a.y - b.y;

    return Math.sqrt(dx*dx + dy*dy);
  }
}
// static property
Point.nbPointsCreated=0;

// We create 3 points
const p1 = new Point(5, 5);
const p2 = new Point(10, 10);
const p3 = new Point(12, 27);

document.body.innerHTML += "<p>Distance between points (5, 5) and (10, 10) is " + 
                     Point.distance(p1, p2) + "</p>";
document.body.innerHTML += "Number of Points created is " + Point.nbPointsCreated;


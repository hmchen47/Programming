functionPlot({
  target: '#myFunction',
  data: [{
    fn: 'sin(x)', 
    color: 'red'
 },
 {
    fn: 'cos(x)', 
    color: 'blue'
 }],
  grid: true,
  yAxis: {domain: [-1, 1]},
  xAxis: {domain: [0, 2*Math.PI]}
});

